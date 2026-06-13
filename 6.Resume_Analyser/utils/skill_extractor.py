SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "docker",
    "aws",
    "fastapi",
    "pandas",
    "numpy"
]

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills