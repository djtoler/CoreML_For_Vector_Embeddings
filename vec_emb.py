import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Load your original JSON data
qa_data = [
  {
    "Q": "What distinguishes data-driven businesses from traditional data-producing ones?",
    "A": "Data-driven businesses leverage real-time or near-real-time data analysis to make informed decisions that directly impact their operations and customer experiences, while traditional businesses relied on periodic batch analysis for strategic planning.",
    "E": "For example, a hotel booking app using real-time data to inform customers about room demand to accelerate booking decisions, as opposed to analyzing booking patterns at the end of the month.",
    "S": [
      "Data-Driven Business",
      "Real-time Analytics",
      "Business Strategy"
    ]
  },
  {
    "Q": "Can you explain the concept of a data pipeline in the context of modern businesses?",
    "A": "A data pipeline represents the entire data journey within a business, starting from various data producers (users, devices, applications), flowing through the organization's systems for storage and processing, and ultimately reaching data consumers (applications, BI tools, AI/ML platforms).",
    "E": "Imagine a flight-tracking application collecting data from users, airlines, and weather services, processing it to provide real-time flight status and predictions, and sharing this information with other travel applications.",
    "S": [
      "Data Pipeline",
      "Data Producers",
      "Data Consumers"
    ]
  },
  {
    "Q": "How does the increasing use of predictive analytics affect the way businesses view data?",
    "A": "Predictive analytics elevates data from a mere byproduct of business operations to a valuable asset. Understanding, analyzing, and acting upon data in near real-time becomes crucial for gaining a competitive edge.",
    "E": "An e-commerce business using predictive analytics to analyze customer data and recommend products in real-time, directly influencing sales and customer satisfaction.",
    "S": [
      "Predictive Analytics",
      "Data as an Asset",
      "Business Strategy"
    ]
  },
  {
    "Q": "What are some practical challenges businesses face when transitioning to a data-driven approach with predictive analytics?",
    "A": "Challenges include shifting organizational mindset to recognize data's value, ensuring data accessibility and usability, establishing efficient data pipelines, and addressing skill gaps in data science and analytics.",
    "E": "A company might need to invest in training programs for employees to understand data analysis or hire data scientists to build and deploy predictive models.",
    "S": [
      "Predictive Analytics Implementation",
      "Organizational Challenges",
      "Data Literacy"
    ]
  },
  {
    "Q": "Why is it important to have a clear business case and ROI analysis before implementing predictive analytics?",
    "A": "Predictive analytics initiatives require time, resources, and organizational change. Demonstrating a positive ROI and aligning the initiative with specific business pain points ensures support, resources, and long-term success.",
    "E": "For instance, a logistics company investing in predictive analytics to optimize inventory management should quantify potential cost savings and efficiency improvements to justify the investment.",
    "S": [
      "Predictive Analytics Implementation",
      "Business Case",
      "ROI Analysis"
    ]
  },
  {
    "Q": "How do streaming platforms like Netflix utilize data analytics and trend analysis?",
    "A": "Streaming platforms analyze vast amounts of user activity data to understand content consumption patterns across demographics. These insights drive recommendations, content acquisition decisions, and marketing campaigns.",
    "E": "Netflix's recommendation engine suggesting shows based on your watch history and preferences is a prime example of how streaming services utilize data analytics.",
    "S": [
      "Data Analytics",
      "Trend Analysis",
      "Streaming Platforms",
      "Recommendation Engines"
    ]
  },
  {
    "Q": "What are some techniques used in descriptive analytics to understand trends in historical and current data?",
    "A": "Descriptive analytics employs techniques like data aggregation, drilling down into details, creating data slices for specific periods, and dicing data to form smaller, focused datasets.",
    "E": "Analyzing Netflix usage data to identify the most-watched series in a specific month is an example of creating a data slice for trend analysis.",
    "S": [
      "Descriptive Analytics",
      "Data Analysis Techniques",
      "Trend Analysis"
    ]
  },
  {
    "Q": "Explain the difference between correlation and causation in the context of diagnostic analytics.",
    "A": "Correlation signifies a relationship between variables where they change together, while causation implies that one variable directly influences the change in the other.",
    "E": "Rainy weather and feeling down might show a correlation, but it's the lack of sunlight affecting serotonin levels that causes mood changes, not the rain itself.",
    "S": [
      "Diagnostic Analytics",
      "Correlation",
      "Causation"
    ]
  },
  {
    "Q": "What is the key difference between supervised and unsupervised learning in machine learning?",
    "A": "Supervised learning utilizes labeled data to train algorithms, while unsupervised learning relies on algorithms to identify patterns and relationships in unlabeled data.",
    "E": "Training an algorithm with labeled data of benign and malignant tumors to predict tumor type is supervised learning. Clustering customers based on purchasing behavior without pre-defined labels is unsupervised learning.",
    "S": [
      "Machine Learning",
      "Supervised Learning",
      "Unsupervised Learning"
    ]
  },
  {
    "Q": "How does predictive analytics contribute to the knowledge acquisition process of businesses?",
    "A": "Predictive analytics transforms raw data into actionable knowledge by identifying patterns, making predictions about future trends, and informing data-driven decisions.",
    "E": "A hospitality chain using historical data and predictive analytics to forecast customer demand, enabling them to optimize staffing levels based on predicted occupancy.",
    "S": [
      "Predictive Analytics",
      "Knowledge Acquisition",
      "Data-Driven Decisions"
    ]
  },
  {
    "Q": "What are some key benefits of using Python for predictive analytics and machine learning?",
    "A": "Python's simple syntax, extensive libraries for data processing and visualization, and strong community support make it an ideal language for developing and deploying predictive models.",
    "E": "Libraries like TensorFlow, scikit-learn, and pandas provide powerful tools for building, training, and evaluating machine learning models in Python.",
    "S": [
      "Python",
      "Predictive Analytics",
      "Machine Learning"
    ]
  },
  {
    "Q": "What is TensorFlow, and how does it facilitate the development of machine learning applications?",
    "A": "TensorFlow is an open-source library for numerical computation, particularly well-suited for developing and deploying machine learning models. It offers a flexible framework, comprehensive tools, and broad community support.",
    "E": "Data scientists use TensorFlow to create, train, and deploy machine learning models for various applications like image recognition, natural language processing, and predictive analytics.",
    "S": [
      "TensorFlow",
      "Machine Learning",
      "Open-Source Libraries"
    ]
  },
  {
    "Q": "Describe how AWS SageMaker empowers users in their machine learning journey.",
    "A": "AWS SageMaker is a fully managed service that simplifies the entire machine learning lifecycle. It provides tools for building, training, and deploying ML models, supporting both built-in algorithms and custom code.",
    "E": "A data scientist can use SageMaker to build a recommendation engine using their own algorithms and deploy it for real-time predictions within their application.",
    "S": [
      "AWS SageMaker",
      "Machine Learning",
      "Cloud Computing"
    ]
  },
  {
    "Q": "What are the key features and advantages of using Google's BigQuery for data warehousing and analytics?",
    "A": "BigQuery is a fully managed data warehouse service with built-in machine learning and business intelligence capabilities. Its scalability, performance, and integration with other GCP services make it suitable for handling large datasets and complex analytical tasks.",
    "E": "Businesses can use BigQuery ML to build and deploy predictive models directly within BigQuery, leveraging its processing power and seamless data integration.",
    "S": [
      "BigQuery",
      "Data Warehousing",
      "Cloud Computing"
    ]
  },
  {
    "Q": "How can businesses benefit from using Amazon Forecast for demand forecasting?",
    "A": "Amazon Forecast allows businesses to leverage their historical time series data to generate accurate demand forecasts. Its fully managed nature simplifies the process, requiring minimal machine learning expertise.",
    "E": "A retail company can utilize Amazon Forecast to predict future product demand, optimize inventory levels, and minimize storage costs while ensuring product availability.",
    "S": [
      "Amazon Forecast",
      "Demand Forecasting",
      "Cloud Computing"
    ]
  }
]

# Initialize the SentenceTransformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # or any other preferred model

# Extract all questions from the Q&A data
questions = [item['Q'] for item in qa_data]

# Generate vector embeddings for all the questions
question_embeddings = model.encode(questions)

# Save embeddings and the original Q&A data for later use
np.save('question_embeddings.npy', question_embeddings)

with open('qa_data.json', 'w') as f:
    json.dump(qa_data, f)

print("Embeddings and Q&A data saved.")
