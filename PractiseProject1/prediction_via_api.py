from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pickle
import pandas as pd
from rule_based_scoring import other_skill_score, skill_matching

# Load model once at startup
with open('./ML/my_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

app = FastAPI(title="Resume Scorer API")

# Request body model
class ResumeRequest(BaseModel):
    resume_skills: List[str]
    jd_skills: List[str]
    resume_text: str

@app.post("/predict")
def predict(req: ResumeRequest):
    resume_skills = req.resume_skills
    jd_skills = req.jd_skills
    resume_text = req.resume_text
    jd_skill_dict_len = len(jd_skills)

    # Rule-Based features
    score, score_percentage = skill_matching.resume_score(resume_skills, jd_skills)
    pros, cons = skill_matching.pros_cons(resume_skills, jd_skills)

    # Features for ML
    new_dict = {
        'num_matched_skills': score,
        'num_missing_skills': jd_skill_dict_len - score,
        'certification_score': other_skill_score.certification_score(resume_text),
        'exp_years': other_skill_score.exp_mapping(resume_text),
        'study_score': other_skill_score.study_score(resume_text),
        'total_jd_skills': jd_skill_dict_len
    }

    df = pd.DataFrame([new_dict])
    FEATURE_ORDER = [
        'num_matched_skills',
        'num_missing_skills',
        'certification_score',
        'exp_years',
        'study_score',
        'total_jd_skills'
    ]
    df = df[FEATURE_ORDER]

    prediction = loaded_model.predict(df)
    pred_score = float(prediction[0])
    pred_score = max(0, min(100, pred_score))  # clamp 0-100

    return {
        "matched_skills": score,
        "match_percentage": round(score_percentage, 2),
        "pros": pros,
        "cons": cons,
        "ml_prediction": round(pred_score, 2)
    }
