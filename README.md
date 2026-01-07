RESUME SCORE PREDICTOR – README CONTENT
==================================

Resume Score Predictor is a web-based and API-powered tool designed to evaluate resumes against job descriptions using a combination of rule-based scoring and machine learning.

Built with Streamlit, FastAPI, and Scikit-Learn, this project applies natural language preprocessing, skill matching, and ML predictions to help recruiters and candidates assess resume–JD fit.

----------------------------------
FEATURES
----------------------------------

1. Rule-Based Scoring
- Counts skills matched between resume and JD
- Calculates match percentage
- Displays pros (skills present) and cons (missing skills)

2. ML-Based Prediction
- Uses a trained Random Forest Regressor
- Predicts resume score using:
  - Number of matched skills
  - Number of missing skills
  - Certification score
  - Years of experience
  - Study/education score
  - Total JD skills
- Supports:
  - Local prediction via Streamlit
  - API prediction via FastAPI endpoint

3. Text Preprocessing
- Cleans text using regex
- Tokenization, stopword removal, lemmatization
- Skill normalization (e.g., js → JavaScript)

----------------------------------
PROJECT STRUCTURE
----------------------------------

ML/
  my_model.pkl                 Trained Random Forest model

rule_based_scoring/
  other_skill_score.py         Certification, experience, study scoring
  skill_matching.py            Rule-based scoring and pros/cons

textPreprocessing/
  text_preprocessing_resume.py Resume preprocessing
  jd_preprcosseing.py          JD preprocessing

sample/
  backend_resume.txt           Sample resume

synthetic_resume_data.csv      Dataset for ML training
prediction.py                  Local ML inference script
predictions_api.py             FastAPI backend
app.py                          Streamlit frontend
requirements.txt               Dependencies
README.md                       Documentation

----------------------------------
INSTALLATION
----------------------------------

1. Clone repository
git clone <your-repo-url>
cd <repo-folder>

2. Create virtual environment
python -m venv venv
source venv/bin/activate   (Linux/macOS)
venv\Scripts\activate      (Windows)

3. Install dependencies
pip install -r requirements.txt

----------------------------------
USAGE
----------------------------------

STREAMLIT APP
streamlit run app.py

- Upload resume (.txt)
- Paste Job Description
- Calculate rule-based score
- Calculate ML score locally or via API

FASTAPI
uvicorn predictions_api:app --reload

POST /predict

Request:
{
  "resume_skills": ["Python", "SQL", "Docker"],
  "jd_skills": ["Python", "SQL", "AWS", "Docker"],
  "resume_text": "3+ years experience in Python and SQL"
}

Response:
{
  "matched_skills": 3,
  "match_percentage": 75.0,
  "pros": "Candidate has skills: Python, SQL, Docker",
  "cons": "Missing skills: AWS",
  "ml_prediction": 43.5
}

----------------------------------
FUTURE IMPROVEMENTS
----------------------------------

- PDF resume support
- Semantic skill matching using embeddings
- Batch resume scoring
- Cloud deployment
