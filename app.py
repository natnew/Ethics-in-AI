import streamlit as st
from src.models import get_model_response, MODELS

# Streamlit page configuration
st.set_page_config(
    page_title="Ethics in AI",
    page_icon="🤖",
    layout="wide"
)

# Sidebar configuration
st.sidebar.title("🧠 Ethics in AI Tool")
st.sidebar.subheader("Explore ethical concerns in AI systems")

# Model selection from sidebar
selected_model = st.sidebar.selectbox("Select Model", list(MODELS.keys()))

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
prompt_text = st.text_area("Edit the ethical scenario or prompt below:", f"Let's discuss {ethical_issue} in AI development.")

# Button to generate response from GPT model
if st.button("Generate Response"):
    with st.spinner("Thinking..."):
        response = get_model_response(
            model=MODELS[selected_model], 
            prompt=prompt_text, 
            temperature=temperature, 
            top_p=top_p, 
            max_tokens=max_tokens
        )
        if response:
            st.write("### Generated Response")
            st.write(response)

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
