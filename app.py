print("Headline Generator Project")
import streamlit as st
from transformers import pipeline

# Load summarization model
st.title("📰 Headline Generator")
st.subheader("Generate headlines from article content")

article = st.text_area("Paste your article or news content here:")

if st.button("Generate Headline"):
    with st.spinner("Generating..."):
        summarizer = pipeline("summarization")
        result = summarizer(article, max_length=15, min_length=5, do_sample=False)
        st.success("Headline:")
        st.write(result[0]['summary_text'])


