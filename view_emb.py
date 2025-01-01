# import json
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA
# from mpl_toolkits.mplot3d import Axes3D

# # Load the saved JSON file with questions and answers
# with open('qa_data.json', 'r') as f:
#     qa_data = json.load(f)

# # Extract all questions from the Q&A data
# questions = [item['Q'] for item in qa_data]

# # Load the saved question embeddings
# question_embeddings = np.load('question_embeddings.npy')

# # Use PCA to reduce embeddings to 3 dimensions for visualization
# pca = PCA(n_components=3)
# reduced_embeddings = pca.fit_transform(question_embeddings)

# # Create a 3D scatter plot with a red background
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d', facecolor='red')  # Red background

# # Plot the embeddings as scatter points with color mapping and customized markers
# colors = np.arange(len(reduced_embeddings))  # Color by question index
# sc = ax.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], reduced_embeddings[:, 2], 
#                 s=100, c=colors, cmap='viridis', marker='o', alpha=0.8)

# # Add a color bar to map the color to the question index
# cbar = plt.colorbar(sc)
# cbar.set_label('Question Index')

# # Annotate points with question indices (optional)
# for i in range(len(reduced_embeddings)):
#     ax.text(reduced_embeddings[i, 0], reduced_embeddings[i, 1], reduced_embeddings[i, 2], 
#             f'{i + 1}', fontsize=10, color='white')  # White text for better contrast on red background

# # Function to display the question on click
# def on_pick(event):
#     ind = event.ind[0]  # Get the index of the clicked point
#     question = questions[ind]
#     print(f"Question: {question}")  # Print the question in the console

# # Connect the pick event to the plot
# fig.canvas.mpl_connect('pick_event', on_pick)

# # Enable clickability for the scatter plot points
# sc.set_picker(True)

# # Customize the plot further (axis labels, title, etc.)
# ax.set_xlabel('PCA 1', fontsize=12)
# ax.set_ylabel('PCA 2', fontsize=12)
# ax.set_zlabel('PCA 3', fontsize=12)
# plt.title("3D Visualization of Question Embeddings", fontsize=16, color='white')

# # Rotate the view for a better angle
# ax.view_init(elev=20, azim=45)  # Adjust the elevation and azimuth for the view angle

# # Save the plot as an image file (e.g., PNG)
# plt.savefig('3d_question_embeddings.png', format='png', dpi=300)  # Save with 300 DPI for high-quality image

# # Display the plot
# plt.show()


# import json
# import numpy as np
# import plotly.graph_objs as go
# from sklearn.decomposition import PCA

# # Load the saved JSON file with questions and answers
# with open('qa_data.json', 'r') as f:
#     qa_data = json.load(f)

# # Extract all questions from the Q&A data
# questions = [item['Q'] for item in qa_data]

# # Load the saved question embeddings
# question_embeddings = np.load('question_embeddings.npy')

# # Use PCA to reduce embeddings to 3 dimensions for visualization
# pca = PCA(n_components=3)
# reduced_embeddings = pca.fit_transform(question_embeddings)

# # Create a 3D scatter plot in Plotly
# trace = go.Scatter3d(
#     x=reduced_embeddings[:, 0],
#     y=reduced_embeddings[:, 1],
#     z=reduced_embeddings[:, 2],
#     mode='markers',
#     marker=dict(
#         size=8,
#         color=np.arange(len(reduced_embeddings)),  # Color by question index
#         colorscale='Viridis',
#         opacity=0.8
#     ),
#     text=questions  # This is the hover text (shows the question when you hover over the point)
# )

# layout = go.Layout(
#     scene=dict(
#         xaxis_title='PCA 1',
#         yaxis_title='PCA 2',
#         zaxis_title='PCA 3',
#         bgcolor='rgb(0, 0, 0)'  # Red background
#     ),
#     title='3D Visualization of Question Embeddings',
# )

# # Create the figure
# fig = go.Figure(data=[trace], layout=layout)

# # Save the interactive plot as an HTML file
# fig.write_html('interactive_3d_plot.html')

# # Display the plot in the browser (optional, for testing)
# fig.show()


import json
import numpy as np
import plotly.graph_objs as go
from sklearn.decomposition import PCA

# Load your JSON data (questions and answers)
with open('json_embeddings.json', 'r') as f:
    qa_data = json.load(f)

# Extract all questions
questions = [item['question'] for item in qa_data]

# Load the embeddings
question_embeddings = np.load('question_embeddings.npy')

# Use PCA to reduce embeddings to 3 dimensions for 3D visualization
pca = PCA(n_components=3)
reduced_embeddings = pca.fit_transform(question_embeddings)

# Create a 3D scatter plot using Plotly
trace = go.Scatter3d(
    x=reduced_embeddings[:, 0],
    y=reduced_embeddings[:, 1],
    z=reduced_embeddings[:, 2],
    mode='markers',
    marker=dict(
        size=10,
        color=np.arange(len(reduced_embeddings)),  # Color by index
        colorscale='Electric',  # More modern color scale
        opacity=0.9,
        symbol='circle'
    ),
    text=questions,  # Hover text
    hoverinfo='text'  # Display hover info as the question text
)

# Custom layout with modern aesthetics
layout = go.Layout(
    scene=dict(
        xaxis=dict(title='PCA 1', backgroundcolor='rgb(230, 230, 230)', gridcolor='white', showbackground=True),
        yaxis=dict(title='PCA 2', backgroundcolor='rgb(230, 230, 230)', gridcolor='white', showbackground=True),
        zaxis=dict(title='PCA 3', backgroundcolor='rgb(230, 230, 230)', gridcolor='white', showbackground=True),
    ),
    title='Modern 3D Visualization of Question Embeddings',
    template='plotly_dark'  # Modern dark theme for a sleek look
)

# Create the figure and display it
fig = go.Figure(data=[trace], layout=layout)
fig.show()
