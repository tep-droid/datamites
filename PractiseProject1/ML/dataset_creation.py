import pandas as pd
import numpy as np

np.random.seed(42)  # reproducible

num_samples = 200

# Simulate features
total_jd_skills = np.random.randint(5, 21, num_samples)
num_matched_skills = np.random.randint(0, total_jd_skills + 1)
num_missing_skills = total_jd_skills - num_matched_skills
certification_score = np.random.randint(0, 6, num_samples)
exp_years = np.random.randint(0, 16, num_samples)
study_score = np.random.choice([0, 1, 2], num_samples)  # 0=no degree, 1=bachelor, 2=master
resume_score_raw = num_matched_skills

# Target: score_percentage with some noise
score_percentage = (num_matched_skills / total_jd_skills) * 100
score_percentage = score_percentage + np.random.normal(0, 5, num_samples)  # add noise
score_percentage = np.clip(score_percentage, 0, 100)  # keep 0-100

# Create DataFrame
df = pd.DataFrame({
    'num_matched_skills': num_matched_skills,
    'num_missing_skills': num_missing_skills,
    'certification_score': certification_score,
    'exp_years': exp_years,
    'study_score': study_score,
    'total_jd_skills': total_jd_skills,
    'resume_score_raw': resume_score_raw,
    'score_percentage': score_percentage
})

# Save to CSV
df.to_csv("synthetic_resume_data.csv", index=False)

print("Synthetic dataset created with 200 samples")
print(df.head())
