# pdf_finetune
pdf Q/A
PDF Reader App
Overview
This PDF Reader App is designed to process PDF files and enable users to query the content using natural language questions. Built with Streamlit, the app leverages OpenAI's embeddings, LangChain, and FAISS for efficient document searching and question answering.

Features
PDF Processing: Upload and process PDF files to extract text content.
Question Answering: Ask questions and get answers based on the content of the uploaded PDF.
Installation
To run this app, you need to install the necessary Python libraries. Use the following command to install the dependencies:

bash
Copy code
pip install streamlit PyPDF2 langchain faiss-cpu openai
Setting Up
Before starting the app, you must set up your OpenAI API key. Replace the placeholder with your actual API key in the environment variable:

python
Copy code
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"
Running the App
To run the app, navigate to the directory containing the app script and run the following command:

bash
Copy code
streamlit run app.py
Usage
Upload a PDF: Use the file uploader to select and upload a PDF file.
Ask a Question: After processing, enter a question related to the PDF content in the provided text input.
Get an Answer: Click the "Get Answer" button to retrieve information from the PDF based on your question.
Limitations
The app currently supports PDF files up to 10 MB in size.
Processing time may vary depending on the length and complexity of the PDF.
Acknowledgements
This app utilizes several open-source libraries and APIs, including Streamlit, PyPDF2, LangChain, FAISS, and OpenAI.
