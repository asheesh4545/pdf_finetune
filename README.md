# PDF Reader App

## Overview

This PDF Reader App is designed to process PDF files and enable users to query the content using natural language questions. Built with Streamlit, the app leverages OpenAI's embeddings, LangChain, and FAISS for efficient document searching and question answering.

## Features

- **PDF Processing**: Upload and process PDF files to extract text content.
- **Question Answering**: Ask questions and get answers based on the content of the uploaded PDF.

## Installation

To run this app, you need to install the necessary Python libraries. Use the following command to install the dependencies:

```bash
pip install streamlit PyPDF2 langchain faiss-cpu openai
