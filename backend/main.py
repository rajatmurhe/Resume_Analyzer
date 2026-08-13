# -------------------- STANDARD LIBRARIES --------------------
from collections import Counter

# -------------------- THIRD-PARTY LIBRARIES -----------------
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import spacy

# -------------------- PROJECT IMPORTS -----------------------
from backend.skills import SKILLS
from backend.rejection_rules import analyze_rejection
from backend.bias_detection import detect_bias
from backend.llm_explainer import generate_llm_explanation
from backend.db import analysis_collection

# -------------------- APP SETUP -----------------------------
app = FastAPI(title="AI Hiring Rejection Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

nlp = spacy.load("en_core_web_sm")

# -------------------- ROUTES --------------------------------

@app.get("/")
def root():
    return {"message": "AI Hiring Rejection Analyzer backend is live"}


@app.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):
    try:
        text = ""

        # 1️⃣ Extract text from PDF safely
        with pdfplumber.open(file.file) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted

        if not text.strip():
            return {
                "error": "No readable text found in PDF. Please upload a text-based resume."
            }

        # 2️⃣ NLP processing
        doc = nlp(text.lower())

        # 3️⃣ Skill detection
        found_skills = set()
        for skill in SKILLS:
            if skill in text.lower():
                found_skills.add(skill)

        # 4️⃣ Bias detection
        bias_flags, bias_insights = detect_bias(
            text,
            list(found_skills)
        )

        # 5️⃣ Experience detection
        experience_years = []
        for token in doc:
            if token.like_num and token.i + 1 < len(doc):
                if "year" in doc[token.i + 1].text:
                    experience_years.append(token.text)

        # 6️⃣ Rejection analysis
        reasons, suggestions = analyze_rejection(
            list(found_skills),
            experience_years
        )

        # 7️⃣ LLM explanation (SAFE)
        try:
            llm_explanation = generate_llm_explanation(
                list(found_skills),
                reasons,
                bias_flags
            )
        except Exception as llm_error:
            llm_explanation = (
                "LLM explanation unavailable. "
                "Rule-based analysis was completed successfully."
            )

        # 8️⃣ Store in MongoDB
        analysis_collection.insert_one({
            "skills": list(found_skills),
            "reasons": reasons,
            "bias_flags": bias_flags,
            "llm_explanation": llm_explanation,
            "resume_length": len(text)
        })

        # 9️⃣ Return response
        return {
            "skills_detected": list(found_skills),
            "experience_mentions": experience_years,
            "likely_rejection_reasons": reasons,
            "improvement_suggestions": suggestions,
            "bias_flags": bias_flags,
            "bias_insights": bias_insights,
            "llm_explanation": llm_explanation,
            "resume_length": len(text)
        }

    except Exception as e:
        return {
            "error": f"Resume analysis failed: {str(e)}"
        }


@app.get("/dashboard")
def dashboard():
    logs = list(analysis_collection.find())

    rejection_counter = Counter()
    skill_counter = Counter()
    bias_counter = Counter()

    for log in logs:
        for reason in log.get("reasons", []):
            rejection_counter[reason] += 1

        for skill in log.get("skills", []):
            skill_counter[skill] += 1

        for bias in log.get("bias_flags", []):
            bias_counter[bias] += 1

    return {
        "total_resumes_analyzed": len(logs),
        "top_rejection_reasons": rejection_counter.most_common(5),
        "top_detected_skills": skill_counter.most_common(5),
        "bias_trends": bias_counter.most_common(5)
    }

@app.get("/explanations")
def get_explanations():
    logs = list(
        analysis_collection.find(
            {},
            {"_id": 0, "llm_explanation": 1}
        )
    )

    return {
        "explanations": [
            log["llm_explanation"]
            for log in logs
            if "llm_explanation" in log
        ]
    }
