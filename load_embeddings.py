import numpy as np
import json
import time  

embeddings = np.load('question_embeddings.npy').tolist()

# Generate a timestamp and filename

file_name = f"embeddings.json"  

# Save embeddings to JSON
with open(file_name, "w") as file:
    json.dump(embeddings, file)  
