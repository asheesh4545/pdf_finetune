import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os

from dotenv import dotenv_values
env_vars = dotenv_values(".env")


#os.environ["OPENAI_API_KEY"] = env_vars['OPENAI_API_KEY']

#We set the env varaibles on streamlit settings and then retrive it using the st.secrets command
#os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]


def process_pdf(file_path):
    reader = PdfReader(file_path)
    raw_text = ''
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=800,
        chunk_overlap=50,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_text)

    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(texts, embeddings)

    return docsearch

def main():
    st.title("PDF Reader App")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file is not None:
        if uploaded_file.size > 10 * 1024 * 1024:  # Limit file size to 10 MB
            st.error("File size exceeds the limit (10 MB). Please upload a smaller PDF.")
            return
        
        with st.spinner("Processing PDF..."):
            docsearch = process_pdf(uploaded_file)

        st.subheader("Ask a question about the PDF:")
        question = st.text_input("Question")

        if st.button("Get Answer"):
            chain = load_qa_chain(OpenAI(), chain_type="stuff")
            docs = docsearch.similarity_search(question)
            response = chain.run(input_documents=docs, question=question)
            st.write("Answer:", response)

if __name__ == "__main__":
    main()
