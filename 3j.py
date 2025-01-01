import json
import numpy as np

# Load your saved 3D question embeddings and questions
question_embeddings = np.load('question_embeddings.npy')  # Assuming you've already reduced them to 3D
with open('qa_data.json', 'r') as f:
    qa_data = json.load(f)

# Extract questions
questions = [item['Q'] for item in qa_data]

# Save both embeddings and questions to a JSON file
data = {
    "embeddings": question_embeddings.tolist(),  # Convert embeddings to list format for JSON
    "questions": questions
}

# Write the data to a JSON file for use in Three.js
with open('question_embeddings_data.json', 'w') as outfile:
    json.dump(data, outfile)

print("Data exported to question_embeddings_data.json")
