import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


question_embeddings = np.load('question_embeddings.npy')
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def find_similar_question(user_question):
  
    user_question_embedding = model.encode([user_question])

    
    similarities = cosine_similarity(user_question_embedding, question_embeddings)

   
    for idx, score in enumerate(similarities[0]):
        print(f"Question {idx + 1}: Similarity Score = {score}")


user_input = "is the money you make back from business a factor when using predictive analytics??"
find_similar_question(user_input)
