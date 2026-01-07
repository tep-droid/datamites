import streamlit as st
import subprocess
import sys

from textPreprocessing.text_preprocessing_resume import *
from textPreprocessing.jd_preprcosseing import *
from rule_based_scoring.skill_matching import *

# Import the UI module
# import app_ui

from sample import *

st.set_page_config(layout="wide")

st.title("Resume Score Predictor")
st.write("Hello User")

# =========================
# TOP SECTION (Resume | JD)
# =========================
left_col, right_col = st.columns(2)

# -------- LEFT: Resume Upload --------
with left_col:
    st.subheader("📄 Resume")

    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

    if uploaded_file is not None:
        st.success("📄 Resume uploaded successfully")

        content = uploaded_file.read().decode("utf-8")
        st.text_area(
            "Original Resume Text",
            content,
            height=200
        )

        # Resume preprocessing
        cleaned_text = clean_data(content)
        tokens = tokenize_data(cleaned_text)
        filtered_tokens = rem_stopwords(tokens)
        lemmatized_tokens = lemma(filtered_tokens)
        normalised_words = normalisation(lemmatized_tokens)

# -------- RIGHT: Job Description --------
with right_col:
    st.subheader("📝 Job Description")

    jd_text = st.text_area(
        "Enter Job Description",
        placeholder="Enter JD here...",
        height=200
    )

    if jd_text:
        st.success("✅ Job Description received")

        jd_cleaned_text = jd_clean_data(jd_text)
        jd_tokens = jd_tokenize_data(jd_cleaned_text)
        jd_filtered_tokens = jd_rem_stopwords(jd_tokens)
        jd_lemmatized_tokens = jd_lemma(jd_filtered_tokens)
        jd_normalised_skills = jd_normalisation(jd_lemmatized_tokens)

# Ready status
# if jd_text and uploaded_file is not None:
#     st.success("🚀 Ready to calculate score")
# calculate_btn = st.button("📊 Calculate Scores")

st.markdown("---")

# =========================
# BOTTOM SECTION (Scores)
# =========================
bottom_left, bottom_right = st.columns(2)

# -------- LEFT: Rule-based Score --------
with bottom_left:
    rule_btn = st.button("📊 Calculate Rule-Based Score")

    if rule_btn and jd_text and uploaded_file is not None:
        st.success("🚀 Calculating Rule-Based Score...")

        # Create JD skill dictionary with weights
        jd_skill_dict = {skill: 5 for skill in jd_normalised_skills}
        resume_skill = normalised_words

        # Calculate score and pros/cons
        score, score_percentage = resume_score(normalised_words, jd_normalised_skills)
        pros, cons = pros_cons(resume_skill, jd_skill_dict)

        # Display nicely
        st.subheader("📊 Rule-Based Scoring")
        st.metric("Skills Matched", score)
        st.progress(int(score_percentage))
        st.write(f"**Match Percentage:** {score_percentage:.2f}%")
        st.write("### Pros")
        st.write(pros)
        st.write("### Cons")
        st.write(cons)

# -------- RIGHT: ML Prediction --------
# initial code

with bottom_right:
    st.subheader("🤖 ML Prediction")

    # ---------- ML Prediction Button ----------
    ml_btn = st.button("📊 Calculate ML Score")

    if ml_btn and jd_text and uploaded_file is not None:
        st.info("Running ML prediction...")

        # Call prediction.py
        result = subprocess.run(
            [
                sys.executable,
                "prediction.py",
                str(normalised_words),
                str(jd_normalised_skills),
                content
            ],
            capture_output=True,
            text=True
        )

        # Parse and display ML prediction nicely
        if result.returncode == 0:
            # Extract prediction line
            output_lines = result.stdout.splitlines()
            pred_line = [line for line in output_lines if "prediction:" in line]
            if pred_line:
                raw_pred = pred_line[0].split("prediction:")[-1].strip()
                try:
                    pred_score = float(raw_pred.strip("[]"))
                except:
                    pred_score = None

                if pred_score is not None:
                    st.metric("ML Predicted Score", f"{pred_score:.2f}%")
            else:
                # fallback: show full stdout if parsing fails
                st.text(result.stdout)
        else:
            st.error("ML Prediction failed")
            st.text(result.stderr)



# trying to add skills matched, pros cons, etc
# with bottom_right:
#     st.subheader("🤖 ML Prediction + Rule-Based Details")
#
#     # ---------- ML Prediction Button ----------
#     ml_btn = st.button("📊 Calculate ML Score ▶")
#
#     if ml_btn and jd_text and uploaded_file is not None:
#         st.info("Fetching predictions from prediction.py...")
#
#         # Call prediction.py with user inputs
#         result = subprocess.run(
#             [
#                 sys.executable,
#                 "prediction.py",
#                 str(normalised_words),
#                 str(jd_normalised_skills),
#                 content
#             ],
#             capture_output=True,
#             text=True
#         )
#
#         if result.returncode == 0:
#             # Parse stdout line by line
#             output_dict = {}
#             for line in result.stdout.splitlines():
#                 if ":" in line:
#                     key, val = line.split(":", 1)
#                     output_dict[key.strip()] = val.strip()
#
#             # -----------------------------
#             # Display Rule-Based + ML nicely
#             # -----------------------------
#             st.metric("Skills Matched", output_dict.get("matched_skills", 0))
#
#             # Progress bar expects 0.0–1.0, so divide by 100
#             match_percentage = float(output_dict.get("match_percentage", 0))
#             st.progress(match_percentage / 100)
#             st.write(f"**Match Percentage:** {match_percentage:.2f}%")
#
#             st.write("### Pros")
#             st.write(output_dict.get("pros", ""))
#
#             st.write("### Cons")
#             st.write(output_dict.get("cons", ""))
#
#             st.metric("ML Predicted Score", f"{output_dict.get('prediction', 0)}%")
#
#         else:
#             st.error("Prediction failed")
#             st.text(result.stderr)

