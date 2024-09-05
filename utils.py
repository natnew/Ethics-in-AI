def generate_ethics_prompt(issue):
    if issue == "Bias and Fairness":
        return "Discuss how AI systems can introduce bias and the steps to mitigate fairness issues."
    elif issue == "Data Privacy":
        return "Explain how AI systems handle sensitive user data and the ethical implications of privacy breaches."
    elif issue == "Accountability":
        return "Explore the issue of accountability when AI systems make incorrect or harmful decisions."
    elif issue == "Transparency":
        return "Discuss the importance of transparency in AI algorithms and the challenges of creating explainable AI systems."
    elif issue == "Ethical AI Development":
        return "Outline the key principles for ethical AI development, including bias mitigation, transparency, and accountability."
    return "Describe an ethical scenario in AI development."

