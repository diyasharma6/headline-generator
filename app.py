import streamlit as st
from transformers import pipeline

# ✅ Load and cache model
@st.cache_resource
def load_model():
    return pipeline("summarization",model="sshleifer/distilbart-cnn-12-6")

summarizer = load_model()

def main():
    st.title("📰 Headline Generator")
    st.subheader("Generate headlines from article content")

    article = st.text_area("Paste your article or news content here:")

    if st.button("Generate Headline"):
        if article.strip() == "":
            st.warning("Please enter some content to summarize.")
        else:
            with st.spinner("Generating..."):
                result = summarizer(article, max_length=15, min_length=5, do_sample=False)
                st.success("Headline:")
                st.write(result[0]['summary_text'])

# ✅ Run the main function correctly
if __name__ == "__main__":
    main()
