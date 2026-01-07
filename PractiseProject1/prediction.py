import pickle

from rule_based_scoring import other_skill_score,skill_matching


# Load the model
with open('./ML/my_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Placeholders just to satisfy IDE
# resume_skills = ['Python', 'SQL']   # Example skills
# jd_skills = ['Python', 'SQL', 'Excel']  # Example JD skills
# jd_skill_dict = len(jd_skills)  # total number of JD skills
# resume_text = "Sample resume text with certifications and experience."  # placeholder

# getting values from user
# chatgpt
import sys
import ast

resume_skills = ast.literal_eval(sys.argv[1])
jd_skills = ast.literal_eval(sys.argv[2])
resume_text = sys.argv[3]
jd_skill_dict = len(jd_skills)




new_dict = {}

score, score_percentage = skill_matching.resume_score(resume_skills, jd_skills)

new_dict['num_matched_skills'] = score
new_dict['num_missing_skills'] = jd_skill_dict - score
new_dict['certification_score'] = other_skill_score.certification_score(resume_text)
new_dict['exp_years'] = other_skill_score.exp_mapping(resume_text)
new_dict['study_score'] = other_skill_score.study_score(resume_text)
new_dict['total_jd_skills'] = jd_skill_dict
#new_dict['score_percentage'] = score_percentage

# print("Dictionary: ",new_dict)

import pandas as pd
new_row = pd.DataFrame([new_dict])
 # print(new_row)
# print(new_row.columns)

# Before prediction

FEATURE_ORDER = [
    'num_matched_skills',
    'num_missing_skills',
    'certification_score',
    'exp_years',
    'study_score',
    'total_jd_skills'
]

new_row = new_row[FEATURE_ORDER] # -> the machine does not see names it sees columns as [ 5, 2, 1, 4, 2, 6 ]

# here printing row.columns to check order but follow the above

prediction = loaded_model.predict(new_row)
# print("prediction: ", prediction)
# Convert prediction array to scalar
pred_score = float(prediction[0])

# Clamp values if you want 0–100
if pred_score < 0:
    pred_score = 0
elif pred_score > 100:
    pred_score = 100

# Now pred_score is a clean float
print("prediction:", pred_score)


# trying to print on screen, no problem to comment off
# At the end of prediction.py, after calculating everything

# Rule-Based details
print("matched_skills:", new_dict['num_matched_skills'])
print("match_percentage:", round(score_percentage, 2))
pros, cons = skill_matching.pros_cons(resume_skills, jd_skills)
print("pros:", pros)
print("cons:", cons)

# ML Prediction
print("prediction:", round(pred_score, 2))
