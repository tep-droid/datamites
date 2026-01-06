# rule_based_scoring/skill_matching.py

def match_skills(resume_skills, jd_skill_dict):
    return sum(jd_skill_dict.get(skill, 0) for skill in resume_skills)


def normalized_score(resume_skills, jd_skill_dict):
    max_score = sum(jd_skill_dict.values())
    score = match_skills(resume_skills, jd_skill_dict)
    return (score / max_score * 100) if max_score else 0


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
