import numpy as np
import json
import time  # Ensure to import the time module

# Load embeddings (e.g., from a numpy file)
embeddings = np.load('question_embeddings.npy').tolist()

# Generate a timestamp and filename

file_name = f"embeddings.json"  # Improved file naming with underscore for readability

# Save embeddings to JSON
with open(file_name, "w") as file:
    json.dump(embeddings, file)  # Corrected to use the correct file handle 'file' instead of 'f'
