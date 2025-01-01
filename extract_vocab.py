from transformers import AutoTokenizer

# Load the tokenizer from the Sentence-BERT model
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/paraphrase-MiniLM-L6-v2")

# Save the vocabulary to a file (vocab.txt)
with open("model_vocab.txt", "w") as vocab_file:
    for token, index in sorted(tokenizer.vocab.items(), key=lambda x: x[1]):  # Sort by token index
        vocab_file.write(f"{token}\n")

print("vocab.txt file has been generated successfully.")
