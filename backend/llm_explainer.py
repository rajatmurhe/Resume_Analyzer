def generate_llm_explanation(skills, rejection_reasons, bias_flags):
    explanation = ""

    # Opening summary
    explanation += "Based on the resume analysis, here is a detailed hiring insight:\n\n"

    # Skills summary
    if skills:
        explanation += f"The candidate demonstrates skills in {', '.join(skills)}. "
    else:
        explanation += "The resume does not clearly highlight technical skills. "

    # Rejection reasoning
    if rejection_reasons:
        explanation += "\n\nHowever, the resume may face rejection due to the following reasons:\n"
        for reason in rejection_reasons:
            explanation += f"- {reason}\n"
    else:
        explanation += "\n\nNo strong rejection signals were detected. "

    # Bias awareness
    if bias_flags:
        explanation += "\nPotential bias risks identified:\n"
        for bias in bias_flags:
            explanation += f"- {bias}\n"

        explanation += (
            "\nSome of these issues may be related to automated filtering systems "
            "rather than the candidate’s true capability."
        )

    # Suggestions
    explanation += (
        "\n\nRecommended next steps:\n"
        "- Strengthen high-demand technical skills\n"
        "- Clearly mention experience duration\n"
        "- Optimize resume keywords for ATS systems\n"
    )

    return explanation
