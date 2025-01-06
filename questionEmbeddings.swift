import SwiftUI
import Foundation
import CoreML
import NaturalLanguage

// Tokenizer for the Sentence-BERT model
class SentenceBERTTokenizer {
    private var vocab: [String: Int] = [:]

    init(vocabFile: String) {
        loadVocab(from: vocabFile)
    }

    // Load the vocabulary file and map tokens to their IDs
    private func loadVocab(from file: String) {
        if let path = Bundle.main.path(forResource: file, ofType: "txt") {
            do {
                let vocabString = try String(contentsOfFile: path)
                let vocabArray = vocabString.split(separator: "\n")
                for (index, word) in vocabArray.enumerated() {
                    vocab[String(word)] = index
                }
                print("Loaded vocab with \(vocab.count) tokens")
            } catch {
                print("Error loading vocab: \(error)")
            }
        } else {
            print("Failed to find vocab file.")
        }
    }

    // Tokenize the input text to match the AutoTokenizer from Python
    func tokenize(_ text: String) -> [Int] {
        print("Tokenizing input text: \(text)")
        let tokens = text.split(separator: " ")
        var tokenIds: [Int] = []
        
        // Add CLS token at the start
        if let clsTokenId = vocab["[CLS]"] {
            tokenIds.append(clsTokenId)
        }

        for token in tokens {
            if let tokenId = vocab[String(token)] {
                tokenIds.append(tokenId)
            } else {
                // Use [UNK] for unknown tokens
                tokenIds.append(vocab["[UNK]"] ?? 0)
                print("Unknown token encountered: \(token)")
            }
        }

        // Add SEP token at the end
        if let sepTokenId = vocab["[SEP]"] {
            tokenIds.append(sepTokenId)
        }

        print("Tokenized input to IDs: \(tokenIds)")
        return tokenIds
    }
}

// View model for handling embeddings
class EmbeddingViewModel: ObservableObject {
    @Published var userInput: String = ""
    @Published var mostSimilarQuestion: String = ""
    @Published var mostSimilarAnswer: String = ""
    
    private var embeddings: [QuestionEmbedding] = []
    private var answer: [String] = []  // Add answer array

    init() {
        loadEmbeddings()
        inspectModelInputOutput()
    }

    func inspectModelInputOutput() {
        guard let model = loadCompiledModel() else {
            print("Failed to load the model.")
            return
        }
        
        print("Inspecting model input/output features...")
        
        for input in model.modelDescription.inputDescriptionsByName {
            print("Input name: \(input.key), type: \(input.value)")
        }
        
        for output in model.modelDescription.outputDescriptionsByName {
            print("Output name: \(output.key), type: \(output.value)")
        }
    }

    func loadEmbeddings() {
        if let jsonFileURL = Bundle.main.url(forResource: "embeddings", withExtension: "json") {
            do {
                let data = try Data(contentsOf: jsonFileURL)
                let decoder = JSONDecoder()
                let embeddingData = try decoder.decode(EmbeddingData.self, from: data)
                
                embeddings = zip(embeddingData.questions, embeddingData.embeddings).map { QuestionEmbedding(question: $0, embedding: $1) }
                answer = embeddingData.answer
                
                print("Loaded \(embeddings.count) embeddings and \(answer.count) answer")
            } catch {
                print("Error loading embeddings: \(error)")
            }
        } else {
            print("Failed to locate embeddings.json.")
        }
    }
    
    func findMostSimilarQuestion() {
        print("User input: \(userInput)")
        guard let userInputEmbedding = generateUserInputEmbedding(for: userInput) else {
            mostSimilarQuestion = "Failed to generate embedding for input."
            mostSimilarAnswer = ""
            print("Failed to generate embedding for input.")
            return
        }

        var bestMatch: (index: Int, question: String, similarity: Double)? = nil

        for (index, embedding) in embeddings.enumerated() {
            let similarity = cosineSimilarity(userInputEmbedding, embedding.embedding)
            if bestMatch == nil || similarity > bestMatch!.similarity {
                bestMatch = (index, embedding.question, similarity)
            }
        }

        if let bestMatch = bestMatch {
            mostSimilarQuestion = "Most similar question: \(bestMatch.question) (Index: \(bestMatch.index))"
            mostSimilarAnswer = "Answer: \(answer[bestMatch.index])"
            print("Most similar question: \(bestMatch.question) at index \(bestMatch.index)")
            print("Matching answer: \(answer[bestMatch.index])")
        } else {
            mostSimilarQuestion = "No similar question found."
            mostSimilarAnswer = ""
            print("No similar question found.")
        }
    }

    // Cosine similarity calculation
    func cosineSimilarity(_ vecA: [Double], _ vecB: [Double]) -> Double {
        let dotProduct = zip(vecA, vecB).map(*).reduce(0, +)
        let magnitudeA = sqrt(vecA.map { $0 * $0 }.reduce(0, +))
        let magnitudeB = sqrt(vecB.map { $0 * $0 }.reduce(0, +))
        return dotProduct / (magnitudeA * magnitudeB)
    }

    // Generate embeddings using CoreML model
    func generateUserInputEmbedding(for text: String) -> [Double]? {
        guard let model = loadCompiledModel() else {
            print("Failed to load the model.")
            return nil
        }

        // Tokenize the user's input using the Sentence-BERT tokenizer
        let tokenizer = SentenceBERTTokenizer(vocabFile: "model_vocab") // Ensure 'vocab.txt' is added to your bundle
        var inputIds = tokenizer.tokenize(text)

        // Ensure inputIds are exactly 13 tokens long (pad or truncate as needed)
        if inputIds.count > 13 {
            inputIds = Array(inputIds.prefix(13))  // Truncate to 13 tokens
        } else {
            inputIds.append(contentsOf: Array(repeating: 0, count: 13 - inputIds.count))  // Pad with 0s
        }

        print("Tokenized input to IDs (padded or truncated to 13): \(inputIds)")

        // Convert inputIds to MLMultiArray of type Float32
        let inputShape = [1, 13]  // Shape of the input (batch size 1, sequence length 13)
        
        guard let inputIdsMultiArray = try? MLMultiArray(shape: [1, 13], dataType: .float32) else {
            print("Failed to create MLMultiArray for input_ids")
            return nil
        }

        for (index, token) in inputIds.enumerated() {
            inputIdsMultiArray[index] = NSNumber(value: Float32(token))
        }

        print("Converted input_ids to MLMultiArray: \(inputIdsMultiArray)")

        // Prepare input as a dictionary for CoreML model
        let input = ["input_ids": inputIdsMultiArray]

        do {
            // Run the prediction
            let predictionOutput = try model.prediction(from: MLDictionaryFeatureProvider(dictionary: input))
            
            // Extract embedding from prediction output
            if let embeddingArray = predictionOutput.featureValue(for: "var_509")?.multiArrayValue {
                var embedding = [Double]()
                for i in 0..<embeddingArray.count {
                    embedding.append(embeddingArray[i].doubleValue)
                }
                print("Generated embedding: \(embedding)")
                return embedding
            } else {
                print("Failed to retrieve embedding from model output.")
            }
        } catch {
            print("Prediction error: \(error)")
        }

        return nil
    }

    // Load the compiled CoreML model
    func loadCompiledModel() -> MLModel? {
        if let modelURL = Bundle.main.url(forResource: "SentenceEmbeddingModel", withExtension: "mlmodelc") {
            do {
                let model = try MLModel(contentsOf: modelURL)
                print("Model loaded successfully.")
                return model
            } catch {
                print("Error loading model: \(error)")
            }
        } else {
            print("Failed to find SentenceEmbeddingModel.mlmodelc in bundle.")
        }
        return nil
    }
}

// Define structures for embedding data
struct QuestionEmbedding: Codable {
    let question: String
    let embedding: [Double]
}

struct EmbeddingData: Codable {
    let embeddings: [[Double]]
    let questions: [String]
    let answer: [String]  // Add answer array here
}

struct QuestionEmbeddingView: View {
    @StateObject private var viewModel = EmbeddingViewModel()
    @State private var showPopover = false

    func wrappedText(_ text: String, every: Int) -> String {
        return text.split(separator: " ")
            .enumerated()
            .map { $0.offset % every == every - 1 ? $0.element + "\n" : $0.element + " " }
            .joined()
    }

    var body: some View {
        ZStack {
            Image("bg")
                .resizable()
                .scaledToFill()
                .frame(maxWidth: .infinity, maxHeight: .infinity)
                .ignoresSafeArea()

            VStack {
                Text("RAG Example")
                    .font(.custom("Futurism", size: 40))
                    .fontWeight(.bold)
                    .foregroundColor(.white)

                HStack {
                    TextField("Enter your question", text: $viewModel.userInput)
                        .padding()
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                        .foregroundColor(.red)
                        .frame(width: 350)
                }
                .frame(maxWidth: .infinity, alignment: .center)

                Button("Find Most Similar Question") {
                    viewModel.findMostSimilarQuestion()
                    showPopover = true
                }
                .padding()
                .foregroundColor(.white)
                .background(Color.black)
                .cornerRadius(10)
            }
            .padding(.top, 150)
            .padding(.horizontal, 20)

            if showPopover && !viewModel.mostSimilarQuestion.isEmpty && !viewModel.mostSimilarAnswer.isEmpty {
                GeometryReader { geometry in
                    VStack {
                        Spacer()
                        
                        VStack(spacing: 20) {
                            Text("Question")
                                .font(.title2)
                                .fontWeight(.bold)
                                .foregroundColor(.white)

                            Text(wrappedText(viewModel.mostSimilarQuestion, every: 6))
                                .font(.body)
                                .foregroundColor(.white)
                                .multilineTextAlignment(.leading)
                                .fixedSize(horizontal: false, vertical: true)
                                .frame(maxWidth: geometry.size.width * 0.8)
                                .padding(.horizontal)

                            Text("Answer")
                                .font(.title2)
                                .fontWeight(.bold)
                                .foregroundColor(.white)

                            Text(wrappedText(viewModel.mostSimilarAnswer, every: 6))
                                .font(.body)
                                .foregroundColor(.white)
                                .multilineTextAlignment(.leading)
                                .fixedSize(horizontal: false, vertical: true)
                                .frame(maxWidth: geometry.size.width * 0.8)
                                .padding(.horizontal)

                            Button("Close") {
                                showPopover = false
                            }
                            .padding()
                            .foregroundColor(.white)
                            .background(Color.red)
                            .cornerRadius(10)
                        }
                        .padding(20)
                        .background(Color.black.opacity(0.9))
                        .cornerRadius(20)
                        .frame(width: geometry.size.width * 0.9)
                        .padding(.horizontal, geometry.size.width * 0.05)

                        Spacer()
                    }
                    .transition(.move(edge: .bottom))
                    .animation(.easeInOut, value: showPopover)
                }
            }
        }
    }
}




// SwiftUI Preview
struct QuestionEmbeddingView_Previews: PreviewProvider {
    static var previews: some View {
        QuestionEmbeddingView()
    }
}

