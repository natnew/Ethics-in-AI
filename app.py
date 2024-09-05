import streamlit as st
import openai
from utils import generate_ethics_prompt

# Set up the OpenAI API key from the Streamlit Cloud's secrets management
openai.api_key = st.secrets["openai"]["api_key"]

# Streamlit Page Configuration
st.set_page_config(
    page_title="Ethics in AI",
    page_icon="🤖",
    layout="wide"
)

# Sidebar configuration
st.sidebar.title("🧠 Ethics in AI Tool")
st.sidebar.subheader("Explore ethical concerns in AI systems")

# Model parameters from sidebar
model = st.sidebar.selectbox("Select Model", ["GPT-4", "GPT-3.5"])
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
top_p = st.sidebar.slider("Top-P (Nucleus Sampling)", 0.0, 1.0, 0.9)
max_tokens = st.sidebar.slider("Max Tokens", 10, 500, 200)

# Predefined ethical topics for prompt engineering
ethical_issue = st.sidebar.selectbox(
    "Select Ethical Issue", 
    ["Bias and Fairness", "Data Privacy", "Accountability", "Transparency", "Ethical AI Development"]
)

# Main content layout
st.title("Ethics in AI Tool")
st.write("### Overview")
st.write("This app helps users explore and understand the ethical considerations involved in AI development and deployment. It provides interactive prompts to generate insights on various ethical topics using AI models.")

st.write("#### Selected Ethical Topic")
prompt_text = st.text_area("Edit the ethical scenario or prompt below:", generate_ethics_prompt(ethical_issue))

st.write("#### Ethics in AI Description")
st.write(f"Topic Selected: {ethical_issue}")
if ethical_issue == "Bias and Fairness":
    st.write("Bias and fairness concerns arise when AI systems disproportionately impact certain groups or individuals.")
elif ethical_issue == "Data Privacy":
    st.write("Data privacy involves ensuring that AI systems handle sensitive user information securely.")
# Add more descriptions as necessary for each topic

# Button to generate response from GPT model
if st.button("Generate Response"):
    with st.spinner("Thinking..."):
        response = openai.Completion.create(
            model=model,
            prompt=prompt_text,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p
        )
        ethics_response = response['choices'][0]['text']
        st.write("### Generated Response")
        st.write(ethics_response)

# External link to your prompt engineering app
st.markdown("### Related Tool")
st.write("Want to learn more about prompt engineering techniques?")
st.markdown("[Explore the Prompt Engineering Tool](https://prompt-engineering-agvnm69ahlwpyqpqrws4nd.streamlit.app)")

# Additional Resources
st.write("### Additional Resources")
st.write("""
- [AI Ethics Guidelines](https://example.com/ethics)
- [AI Bias Mitigation Techniques](https://example.com/bias-mitigation)
- [Responsible AI Development Practices](https://example.com/responsible-ai)
""")
