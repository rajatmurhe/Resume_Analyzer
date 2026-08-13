import re

def detect_bias(resume_text, skills_detected):
    bias_flags = []
    bias_insights = []

    text = resume_text.lower()

    # ---------- CGPA Detection ----------
    cgpa_match = re.search(r"(cgpa|gpa)\s*[:\-]?\s*(\d\.\d+|\d+)", text)

    if cgpa_match:
        cgpa_value = float(cgpa_match.group(2))

        if cgpa_value < 7.0:
            bias_flags.append("Low CGPA bias risk")
            bias_insights.append(
                "Candidate may be filtered due to CGPA, despite having relevant skills"
            )
    else:
        bias_flags.append("CGPA not mentioned")
        bias_insights.append(
            "Resume may be auto-rejected due to missing CGPA field"
        )

    # ---------- Keyword Over-filtering ----------
    if len(skills_detected) <= 2:
        bias_flags.append("Keyword over-filtering risk")
        bias_insights.append(
            "Candidate skills may not match ATS keyword thresholds"
        )

    return bias_flags, bias_insights
