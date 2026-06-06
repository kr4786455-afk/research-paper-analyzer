import streamlit as st
import PyPDF2
from collections import Counter
import string

st.title("Research Paper Analyzer")

uploaded_file = st.file_uploader("Upload a research paper PDF", type=["pdf"])

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text

def get_word_count(text):
    words = text.split()
    return len(words)

def get_summary(text, sentence_count=5):
    sentences = text.replace("\n", " ").split(".")
    summary = sentences[:sentence_count]
    return ". ".join(summary) + "."

def get_keywords(text, top_n=10):
    words = text.lower().split()

    clean_words = []
    for word in words:
        word = word.strip(string.punctuation)
        if len(word) > 3:
            clean_words.append(word)

    return Counter(clean_words).most_common(top_n)

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Text Preview")
    st.write(text[:1000])

    st.subheader("Word Count")
    st.write(get_word_count(text))

    st.subheader("Simple Summary")
    st.write(get_summary(text))

    st.subheader("Top Keywords")
    keywords = get_keywords(text)

    for word, count in keywords:
        st.write(f"{word}: {count}")