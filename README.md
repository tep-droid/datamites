# SENIOR MENTOR GUIDE: RESUME SCORING WEB APPLICATION

This document is a step-by-step mentoring roadmap for a complete beginner building their first end-to-end project.

---

## PHASE 0 — Environment & Mindset

**Goal:** Set up a stable development environment and correct learning mindset.

**Build:**

* Install Python 3.10+
* Create virtual environment
* Install Streamlit
* Run a basic Streamlit app

**Checklist:**

* Python installed
* Virtual environment created
* Streamlit runs successfully

**Common mistakes:**

* Skipping virtual environments
* Installing random libraries
* Rushing ahead

---

## PHASE 1 — Frontend Basics (Streamlit)

**Goal:** Understand user interaction.

**Build:**

* Resume upload button
* Job description text area
* Submit button
* Placeholder output

**Checklist:**

* `st.file_uploader`
* `st.text_area`
* `st.button`
* Conditional rendering

**Mistakes:**

* Mixing UI and logic
* Over-designing UI

---

## PHASE 2 — Resume Upload & Input Handling

**Goal:** Handle and validate inputs.

**Build:**

* Extract resume text
* Validate inputs
* Show extracted text for debugging

**Mistakes:**

* Assuming clean PDFs
* Hiding errors

---

## PHASE 3 — NLP Core Logic

**Goal:** Convert raw text into clean tokens.

**Build:**

* Cleaning
* Tokenization
* Stopword removal
* Lemmatization
* Skill normalization

**Mistakes:**

* Over-cleaning
* Blind library usage

---

## PHASE 4 — Rule-Based Scoring

**Goal:** Learn logic before ML.

**Build:**

* Keyword extraction
* Skill matching
* Score calculation
* Pros & cons generation

---

## PHASE 5 — Dataset Creation

**Goal:** Understand importance of data.

**Build:**

* 100+ labeled samples
* Resume text
* Job description text
* Score labels

**Mistakes:**

* Small datasets
* Inconsistent labels

---

## PHASE 6 — Machine Learning Training

**Goal:** Build first ML pipeline.

**Build:**

* TF-IDF vectorizer
* Regression model
* Evaluation metrics
* Save model

---

## PHASE 7 — Applying ML to New Resumes

**Goal:** Inference-only prediction.

**Build:**

* Load model
* Predict score

**Mistakes:**

* Retraining during inference

---

## PHASE 8 — Displaying Results

**Goal:** Make results understandable.

**Build:**

* Score display
* Visual indicators
* Pros & cons
* Explanation

---

## PHASE 9 — Code Transparency (Optional)

**Goal:** Explain logic clearly.

---

## PHASE 10 — Final Polish

**Goal:** Think like an engineer.

**Build:**

* Folder structure
* README
* Limitations
* Future improvements

---

## FINAL ADVICE

* Build slowly
* Never skip phases
* Confusion means learning
* Understanding > shortcuts
