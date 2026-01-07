# rule_based_scoring/skill_matching.py

def resume_score(resume_skills, jd_skills):
    # Count how many JD skills are found in the resume
    matched_skills = []
    for skill in jd_skills:
        if skill in resume_skills:
            matched_skills.append(skill)

    score = len(matched_skills)  # raw score = number of matched skills
    total_jd_skills = len(jd_skills)  # total JD skills
            # Calculate percentage of JD skills matched
    if total_jd_skills > 0:
        score_percentage = (score / total_jd_skills) * 100
    else:
        score_percentage = 0

    print("Matched skills:", matched_skills)
    print("Total JD skills:", total_jd_skills)

    return score, score_percentage


def pros_cons(resume_skills, jd_skill_dict):
    pros = f"Candidate has skills: {', '.join(resume_skills)}"

    missing = [
        skill for skill in jd_skill_dict
        if skill.lower() not in [s.lower() for s in resume_skills]
    ]

    cons = (
        f"Missing skills: {', '.join(missing)}"
        if missing else "No missing skills"
    )

    return pros, cons
