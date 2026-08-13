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

```bash
pip install -r requirements.txt
