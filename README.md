# AI Hiring Rejection Analyzer

An AI-powered resume analysis platform that simulates ATS-style screening, detects skills and potential rejection factors, identifies hiring bias indicators, and generates explainable hiring insights using NLP and LLMs.

## Features

- PDF resume upload
- Resume text extraction
- NLP-based skill detection
- ATS-style rejection analysis
- Hiring bias detection
- LLM-powered explanations
- MongoDB data persistence
- Analytics dashboard
- FastAPI REST API

## Tech Stack

- Python
- FastAPI
- spaCy
- OpenAI API
- MongoDB
- Docker
- JavaScript
- HTML
- CSS
- pdfplumber

## Project Structure

Resume_Analyzer/
│
├── backend/
│   ├── __init__.py
│   ├── bias_detection.py
│   ├── db.py
│   ├── llm_explainer.py
│   ├── main.py
│   ├── rejection_rules.py
│   └── skills.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .gitignore
├── README.md
└── requirements.txt

## Running Locally

### Install dependencies

1. Clone the Repository
git clone https://github.com/rajatmurhe/Resume_Analyzer.git
cd Resume_Analyzer

3. Create Virtual Environment
python3 -m venv venv

Activate it:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Install spaCy Model
python -m spacy download en_core_web_sm

5. Start MongoDB
Make sure Docker Desktop is running.

docker run -d --name mongo-hiring -p 27017:27017 mongo:6

If the container already exists:

docker start mongo-hiring

Check MongoDB:
docker ps

6. Configure Environment Variables

Create a local .env file containing:
OPENAI_API_KEY=YOUR_API_KEY

Replace YOUR_API_KEY with your own API key.



7. Start the Backend

From the project root:
python -m uvicorn backend.main:app --reload

Backend:
http://127.0.0.1:8000

8. Test Backend

Open:
http://127.0.0.1:8000

FastAPI documentation:
http://127.0.0.1:8000/docs

Main endpoint:
POST /analyze-resume

9. Start Frontend
Open another Terminal:
cd frontend
python3 -m http.server 5500

Open:
http://127.0.0.1:5500

Dashboard
The dashboard provides:

Total resumes analyzed
Detected skills
Potential rejection factors
Bias indicators
Resume analysis results
LLM-generated explanations
Hiring insights
Security


This project is intended as an AI-assisted hiring analysis system and should not be used as the sole decision-maker for real hiring decisions.

AI-generated results should be reviewed by qualified human recruiters.

Future Improvements
Resume-to-job-description matching
Candidate ranking
Advanced ATS scoring
Explainable AI using SHAP/LIME
Authentication and authorization
Recruiter accounts
Job description analysis
Cloud deployment
CI/CD pipeline
Advanced fairness evaluation
Model performance monitoring

Author
Rajat Murhe

License
This project is developed for educational, research, and portfolio purposes.
