import streamlit as st
from prompt_engineering import apply_technique
from models import get_model_response, MODELS
from utils import load_techniques, load_prompts
import os

# Load data for ethical techniques and prompts
techniques = load_techniques()
prompts_data = load_prompts()

# Sidebar for user input
st.sidebar.title("🧠 Ethics in AI Tool")

# API Key validation
if os.getenv("OPENAI_API_KEY"):
    st.sidebar.success("✅ API key already provided!")
else:
    st.sidebar.error("❌ API key not provided. Please set your OpenAI API key.")

# Model selection
selected_model = st.sidebar.selectbox("Select Model", list(MODELS.keys()))
selected_model_engine = MODELS[selected_model]

# Model parameter sliders
st.sidebar.subheader("Model Parameters")
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, step=0.01)
top_p = st.sidebar.slider("Top-P (Nucleus Sampling)", 0.0, 1.0, 1.0, step=0.01)
max_tokens = st.sidebar.slider("Max Length", 10, 500, 150, step=10)

# Ethical topic selection
selected_department = st.sidebar.selectbox("Select Ethical Topic", list(prompts_data.keys()))
selected_prompt = st.sidebar.selectbox("Select Scenario", prompts_data[selected_department])

# Technique selection
selected_technique = st.sidebar.selectbox("Select Technique", list(techniques.keys()))
technique_description = techniques[selected_technique]["description"]

# Output format and tone selection
output_format = st.sidebar.selectbox("Select Output Format", ["Text", "JSON", "Bullet Points"])
tone = st.sidebar.selectbox("Select Tone", ["Formal", "Casual", "Technical"])

# Advanced Settings
with st.sidebar.expander("Advanced Settings"):
    role = st.selectbox("Assign Role", ["No Role", "Technical Specialist", "Editor", "Marketing Manager", "Technical Trainer", "Product Owner"])
    use_thinking_step = st.slider("Include Thinking Step", 0, 1, 0, step=1)
    avoid_hallucinations = st.slider("Avoid Hallucinations", 0, 1, 0, step=1)

# Main content section
st.title("Ethics in AI Tool")

# Prompt and Technique Information
st.subheader("Selected Prompt")
user_prompt = st.text_area("Edit the ethical scenario or prompt below:", value=selected_prompt)
st.subheader("Technique Description")
st.info(technique_description)

# Apply the technique to the prompt
transformed_prompt, transformation_explanation = apply_technique(user_prompt, selected_technique)

# Adjust the transformed prompt based on output format and tone
formatted_prompt = f"{transformed_prompt}\n\nFormat the output in {output_format} format with a {tone} tone."

if role != "No Role":
    formatted_prompt += f"\n\nRole: {role}."
if use_thinking_step == 1:
    formatted_prompt += "\n\n### Thinking Step\nExplain step-by-step reasoning."
if avoid_hallucinations == 1:
    formatted_prompt += "\n\nIf you don't know, state 'I don't know.'"

st.subheader("Transformed Prompt")
st.info(formatted_prompt)

# Display transformation explanation
detailed_explanation = f"""
Transformation applied using the **{selected_technique}** technique:
- **Output Format**: {output_format}
- **Tone**: {tone}
- **Temperature**: {temperature}
- **Top-P**: {top_p}
- **Max Tokens**: {max_tokens}
- **Role**: {role}
- **Thinking Step**: {"Enabled" if use_thinking_step == 1 else "Disabled"}
- **Avoid Hallucinations**: {"Enabled" if avoid_hallucinations == 1 else "Disabled"}
"""
st.subheader("Transformation Explanation")
st.info(detailed_explanation)

# Button to get model response
if st.button("Generate Response"):
    with st.spinner("Generating response..."):
        response = get_model_response(
            selected_model_engine,
            formatted_prompt,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens
        )
    if response:
        st.subheader("Model Response")
        st.write(response)
    else:
        st.error("The response could not be generated. Try again later or select another model.")
