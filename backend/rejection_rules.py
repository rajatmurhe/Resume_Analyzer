def analyze_rejection(skills, experience_mentions):
    reasons = []
    suggestions = []

    if len(skills) < 3:
        reasons.append("Insufficient technical skill coverage")
        suggestions.append("Add or highlight more technical skills")

    if not experience_mentions:
        reasons.append("No explicit experience duration mentioned")
        suggestions.append("Mention experience in years or months")

    if "python" not in skills:
        reasons.append("Python not detected (high demand skill)")
        suggestions.append("Consider learning and adding Python projects")

    return reasons, suggestions
