import pickle

from rule_based_scoring import other_skill_score,skill_matching


# Load the model
with open('./ML/my_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Placeholders just to satisfy IDE
resume_skills = ['Python', 'SQL']   # Example skills
jd_skills = ['Python', 'SQL', 'Excel']  # Example JD skills
jd_skill_dict = len(jd_skills)  # total number of JD skills
resume_text = "Sample resume text with certifications and experience."  # placeholder

new_dict = {}

score, score_percentage = skill_matching.resume_score(resume_skills, jd_skills)

new_dict['num_matched_skills'] = score
new_dict['num_missing_skills'] = jd_skill_dict - score
new_dict['certification_score'] = other_skill_score.certification_score(resume_text)
new_dict['exp_years'] = other_skill_score.exp_mapping(resume_text)
new_dict['study_score'] = other_skill_score.study_score(resume_text)
new_dict['total_jd_skills'] = jd_skill_dict
#new_dict['score_percentage'] = score_percentage

print("Dictionary: ",new_dict)

import pandas as pd
new_row = pd.DataFrame([new_dict])
print(new_row)
print(new_row.columns)

# Before prediction

# FEATURE_ORDER = [
#     'num_matched_skills',
#     'num_missing_skills',
#     'certification_score',
#     'exp_years',
#     'study_score',
#     'total_jd_skills'
# ]

# new_row = new_row[FEATURE_ORDER] -> the machine does not see names it sees columns as [ 5, 2, 1, 4, 2, 6 ]

# here printing row.columns to check order but follow the above

prediction = loaded_model.predict(new_row)
print("prediction: ", prediction)

if prediction < 0:
    prediction = 0
elif prediction > 0:
    prediction = 100
else:
    prediction
