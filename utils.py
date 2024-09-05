def generate_prompt(template, department):
    if department == "Customer Services":
        return f"{template} regarding the availability of a product."
    elif department == "Marketing":
        return f"{template} for promoting a new product launch."
    elif department == "Development":
        return f"{template} to help debug a Python script."

