import re

def certification_score(resume_text):
    resume_text = resume_text.lower()
    return len(re.findall(r'certified|certifications?', resume_text))

file_path = "/Users/pando-thomas/PycharmProjects/datamites/PractiseProject1/sample/backend_resume.txt"
with open(file_path, "r", encoding="utf-8") as file:
    resume_text = file.read()

print(certification_score(resume_text))

def exp_mapping(resume_text):
    years = re.findall((r'(\d+)\+?\s*year?'),resume_text,flags=re.IGNORECASE) #pattern mapping,string,flags
    years = [int(x) for x in years]   # changing string values to integer
    return sum(years)
print(exp_mapping(resume_text))

def study_score(resume_text):
    bachelors = [ 'B.Sc', 'B.Tech', 'B.E', 'BCA', 'B.A']
    masters = [ 'M.Sc', 'M.Tech', 'M.E', 'MCA', 'M.B.A']

    stu_score = 0
    if any(x in resume_text for x in bachelors):
        stu_score = 1
    if any(x in resume_text for x in masters):
        stu_score = 2

    return stu_score
print(study_score(resume_text))






