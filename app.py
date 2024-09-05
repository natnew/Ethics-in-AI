import streamlit as st
import openai
from utils import generate_ethics_prompt

# API Key Validation
api_key = st.secrets.get("openai", {}).get("api_key")
if not api_key:
    st.error("Missing OpenAI API key. Please set it in Streamlit Secrets.")
    st.stop()
else:
    openai.api_key = api_key

# Streamlit page configuration
st.set_page_config(
    page_title="Ethics in AI",
    page_icon="🤖",
    layout="wide"
)

# Sidebar configuration
st.sidebar.title("🧠 Ethics in AI Tool")
st.sidebar.subheader("Explore ethical concerns in AI systems")

# Model options and corresponding engines
MODELS = {
    "gpt-4": "gpt-4",
    "gpt-4-turbo": "gpt-4-turbo",
    "gpt-3.5-turbo": "gpt-3.5-turbo"
}

# Model selection from sidebar
selected_model = st.sidebar.selectbox("Select Model", list(MODELS.keys()))
selected_model_engine = MODELS[selected_model]

# Customizable parameters in the sidebar
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
top_p = st.sidebar.slider("Top-P (Nucleus Sampling)", 0.0, 1.0, 0.9)
max_tokens = st.sidebar.slider("Max Tokens", 50, 500, 200)

# Predefined ethical topics for prompt generation
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

# Display description based on the selected ethical issue
st.write("#### Ethics in AI Description")
if ethical_issue == "Bias and Fairness":
    st.write("Bias and fairness concerns arise when AI systems disproportionately impact certain groups or individuals.")
elif ethical_issue == "Data Privacy":
    st.write("Data privacy involves ensuring that AI systems handle sensitive user information securely.")
elif ethical_issue == "Accountability":
    st.write("Accountability concerns arise when AI systems make harmful or incorrect decisions.")
elif ethical_issue == "Transparency":
    st.write("Transparency is crucial to make AI algorithms explainable and understandable by stakeholders.")
elif ethical_issue == "Ethical AI Development":
    st.write("Ethical AI development involves integrating fairness, accountability, and transparency throughout the AI lifecycle.")

# Button to generate response from GPT model
if st.button("Generate Response"):
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model=selected_model_engine,
                messages=[
                    {"role": "system", "content": "You are an AI ethics assistant."},
                    {"role": "user", "content": prompt_text}
                ],
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p
            )
            ethics_response = response['choices'][0]['message']['content']
            st.write("### Generated Response")
            st.write(ethics_response)
        except openai.error.OpenAIError as e:
            st.error(f"An error occurred: {str(e)}")

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
