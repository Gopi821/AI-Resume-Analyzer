from utils.pdf_reader import extract_text
from utils.skill_extractor import extract_skills
from utils.matcher import calculate_similarity

resume_text = extract_text(
    "data/resumes/Gopi Data_Science Resume.pdf"
)

with open(
    "data/jobs/ai_engineer.txt",
    "r",
    encoding="utf-8"
) as file:
    job_text = file.read()

score = calculate_similarity(
    resume_text,
    job_text
)

resume_skills = extract_skills(
    resume_text
)

job_skills = extract_skills(
    job_text
)

missing_skills = list(
    set(job_skills) -
    set(resume_skills)
)

print("Match Score:", score, "%")
print("Resume Skills:", resume_skills)
print("Job Skills:", job_skills)
print("Missing Skills:", missing_skills)