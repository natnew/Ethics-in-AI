import streamlit as st
import openai
import os
from utils import generate_prompt

# Set your OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Page Configurations
st.set_page_config(
    page_title="Interactive Prompt Engineering Tool",
    page_icon="🤖",
    layout="wide"
)

# Sidebar - Parameters and settings
st.sidebar.title("🤖 Prompt Engineering Tool")
st.sidebar.subheader("This tool is designed to explore and learn prompt engineering using models like GPT-4.")

model = st.sidebar.selectbox("Select Model", ["GPT-4", "GPT-3.5"])
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
top_p = st.sidebar.slider("Top-P (Nucleus Sampling)", 0.0, 1.0, 0.9)
max_tokens = st.sidebar.slider("Max Tokens", 10, 500, 200)

department = st.sidebar.selectbox("Select Department", ["Customer Services", "Marketing", "Development"])
prompt_template = st.sidebar.selectbox("Select Prompt", [
    "Draft a response to a customer inquiry",
    "Generate marketing copy",
    "Help with code debugging"
])

technique = st.sidebar.selectbox("Select Technique", ["Zero-Shot Prompting", "Few-Shot Prompting"])
tone = st.sidebar.selectbox("Select Tone", ["Formal", "Casual", "Neutral"])

# Main Layout
st.title("Interactive Prompt Engineering")
st.write("### Overview")
st.write("This is a simple interactive tool to test and learn about prompt engineering techniques with different GPT models.")

st.write("#### Selected Prompt")
prompt_text = st.text_area("Edit your prompt below:", generate_prompt(prompt_template, department))

st.write("#### Technique Description")
st.write(f"Technique Selected: {technique}")
if technique == "Zero-Shot Prompting":
    st.write("Zero-shot prompting involves providing no examples to the model and expecting it to complete the task.")
elif technique == "Few-Shot Prompting":
    st.write("Few-shot prompting involves providing a few examples to guide the model's completion.")

# Call GPT API and generate response
if st.button("Generate Prompt"):
    with st.spinner("Generating response..."):
        response = openai.Completion.create(
            model=model,
            prompt=prompt_text,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p
        )
        transformed_prompt = response['choices'][0]['text']
        st.write("### Transformed Prompt")
        st.write(transformed_prompt)

# Additional Resources section
st.write("### Additional Resources")
st.write("""
- [AI Ethics Guidelines](https://example.com/ethics)
- [Best Practices for AI Development](https://example.com/best-practices)
""")

