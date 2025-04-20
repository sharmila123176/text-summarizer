# app.py

import streamlit as st
from transformers import pipeline

# Load summarization pipeline
@st.cache_resource
def load_model():
    return pipeline("summarization")

summarizer = load_model()

st.title("📝 Automated Text Summarization using NLP")
st.write("Upload a text file or enter/paste text to generate a summary.")

# Option 1: File Upload
uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])
input_text = ""

if uploaded_file:
    input_text = uploaded_file.read().decode("utf-8")
else:
    input_text = st.text_area("Or paste your text here", height=300)

if st.button("Summarize"):
    if not input_text.strip():
        st.warning("Please enter or upload some text.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(input_text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
            st.subheader("📌 Summary")
            st.success(summary)
