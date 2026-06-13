# 🤖 AI Resume Analyzer & Job Match Engine

## 📌 Overview

AI Resume Analyzer & Job Match Engine is an NLP-powered application that analyzes resumes and compares them with job descriptions to determine how well a candidate matches a specific role.

The system extracts skills from resumes, calculates a match score using AI embeddings, and identifies missing skills required for the target job.

---

## ✨ Features

* 📄 Resume PDF Parsing
* 🧠 Automatic Skill Extraction
* 🎯 Resume-Job Matching
* 📊 AI-Based Match Score
* 🔍 Missing Skills Detection
* 🎨 Interactive Streamlit Interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* PyPDF2
* Sentence Transformers
* Scikit-Learn
* NLP (Natural Language Processing)

---

## 📂 Project Structure

```text
resume-analyzer/
│
├── app.py
├── requirements.txt
│
├── data/
│   ├── resumes/
│   └── jobs/
│
├── utils/
│   ├── pdf_reader.py
│   ├── skill_extractor.py
│   └── matcher.py
│
└── models/
```

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer-and-Job-Match-Engine.git
```

### Navigate to Project

```bash
cd AI-Resume-Analyzer-and-Job-Match-Engine
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Upload a Resume PDF
2. Paste a Job Description
3. Extract skills from both documents
4. Generate embeddings using Sentence Transformers
5. Calculate similarity score
6. Display Match Score and Missing Skills

---

## 📊 Example Output

* Match Score: 85%
* Resume Skills: Python, SQL, Machine Learning
* Missing Skills: Docker, AWS, FastAPI

---

## 🎯 Future Improvements

* Resume Improvement Suggestions
* Multi-Resume Ranking
* Job Recommendation System
* LLM-Based Feedback
* Cloud Deployment

------
