import streamlit as st
from textPreprocessing.text_preprocessing_resume import *
from textPreprocessing.jd_preprcosseing import *
st.title("Resume Score Predictor")
st.write("Hello User")

#text area
jd_text = st.text_area("Enter your message", placeholder="Enter JD here...",
    height=150)

if jd_text:
    st.success("✅ Job Description received")

    jd_cleaned_text = jd_clean_data(jd_text)
    jd_tokens = jd_tokenize_data(jd_cleaned_text)
    jd_filtered_tokens = jd_rem_stopwords(jd_tokens)
    jd_lemmatized_tokens = jd_lemma(jd_filtered_tokens)
    jd_normalised_skills = jd_normalisation(jd_lemmatized_tokens)


# uploading text file
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    st.success("📄 Resume uploaded successfully")

    content = uploaded_file.read().decode("utf-8")
    st.write("### Original Resume Text")
    st.text(content)

    #resume preprocessing function calls
    cleaned_text = clean_data(content)
    tokens = tokenize_data(cleaned_text)
    filtered_tokens = rem_stopwords(tokens)
    lemmatized_tokens = lemma(filtered_tokens)

    # print("Tokens after cleaning & stopwords removal & lemmatization:")
    # print(lemmatized_tokens)

    normalised_words = normalisation(lemmatized_tokens)


if jd_text and uploaded_file is not None:
    st.success("🚀 Ready to calculate score")

# scoring
from rule_based_scoring.skill_matching import *

# Create JD skill dictionary with weights (for scoring)
if jd_text and uploaded_file is not None:
    jd_skill_dict = {skill: 5 for skill in jd_normalised_skills}
    resume_skill = normalised_words

    score = match_skills(resume_skill, jd_skill_dict)
    percentage = normalized_score(resume_skill, jd_skill_dict)
    pros, cons = pros_cons(resume_skill, jd_skill_dict)

    st.write(f"### Candidate Score: {score}")
    st.write(f"### Normalized Score: {percentage:.2f}%")
    st.write("### Pros & Cons")
    st.write(pros)
    st.write(cons)