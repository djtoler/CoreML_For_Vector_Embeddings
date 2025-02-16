import json
import numpy as np
from sentence_transformers import SentenceTransformer

qa_data = [
{
    "question": "What are the two file extensions commonly used for HTML files?",
    "answer": "The two common file extensions for HTML files are .html and .htm."
  },
  {
    "question": "How do you create a paragraph in HTML?",
    "answer": "You use the `<p>` tag to create a paragraph. You need an opening `<p>` tag and a closing `</p>` tag to enclose the text of the paragraph."
  },
  {
    "question": "What is the purpose of the `<!DOCTYPE>` declaration in an HTML file?",
    "answer": "The `<!DOCTYPE>` declaration tells the browser which version of HTML the document adheres to. It's essential for proper rendering and validation."
  },
  {
    "question": "What are the three essential tags that must be included in every HTML page?",
    "answer": "Every HTML page requires the `<html>`, `<head>`, and `<body>` tags."
  },
  {
    "question": "What does the `<title>` tag do?",
    "answer": "The `<title>` tag defines the title of the web page. This title appears in the browser tab and search engine results."
  },
  {
    "question": "Why is it important to use consistent file naming conventions in HTML?",
    "answer": "Consistent file naming is important because some web servers are case-sensitive. Using uppercase or lowercase consistently prevents broken links and other issues."
  },
  {
    "question": "What is the purpose of character entities in HTML?",
    "answer": "Character entities are used to represent special characters that cannot be typed directly on a keyboard. They ensure consistency across different systems and browsers."
  },
  {
    "question": "How do you create a comment in an HTML file?",
    "answer": "Comments start with `<!--` and end with `-->`.  Anything between these symbols will be ignored by the browser."
  },
  {
    "question": "What is the primary purpose of cascading style sheets (CSS)?",
    "answer": "CSS separates the presentation (styling) of a web page from its content (HTML). This makes websites more accessible, maintainable, and search engine friendly."
  },
  {
    "question": "What are the three types of CSS styles?",
    "answer": "The three types of CSS styles are inline styles, internal styles, and external styles."
  },
  {
    "question": "Explain the difference between inline styles and internal styles in CSS.",
    "answer": "Inline styles are directly embedded within the HTML tag they affect, while internal styles are defined within the `<style>` tag in the `<head>` section of the HTML document."
  },
  {
    "question": "What is the benefit of using external style sheets for CSS?",
    "answer": "External style sheets allow you to separate CSS rules into a separate file. This makes it easier to manage styles across multiple pages, improves code organization, and promotes reusability."
  },
  {
    "question": "What tag is used to create a large header using HTML?",
    "answer": "The `<h1>` tag is used to create a large header in HTML."
  },
  {
    "question": "Which HTML tag is used to create a hyperlink?",
    "answer": "The `<a>` tag is used to create a hyperlink in HTML."
  },
  {
    "question": "What tag is used to create a paragraph in HTML?",
    "answer": "The `<p>` tag is used to create a paragraph in HTML."
  }
]

model = SentenceTransformer("Paraphrase-MiniLM-L6-v2")

questions = [item['question'] for item in qa_data]

question_embeddings = model.encode(questions)

data = {
    "embeddings": question_embeddings.tolist(),
    "questions": questions
}

with open("qa_data_with_embeddings2.json", "w") as f:
    json.dump(data, f)

print("Saved embeddings and Questins to json file")