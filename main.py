import streamlit as st
from cohere import Client
import os
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

# Initialize Cohere
api_key = os.getenv("COHERE_API_KEY")
if not api_key:
    raise "API key not found. Please set the COHERE_API_KEY environment variable."

client = Client(api_key=api_key)

# Streamlit UI
st.title("Disease Prediction from Symptoms")
st.write("Enter your symptoms to get a possible disease prediction.")

# User input
symptoms = st.text_area("Enter your symptoms (comma-separated):")

if st.button("Predict"):
    if symptoms:
        response = client.chat(
            message=f"Symptoms: {symptoms}",
            model="command-r-08-2024",
            preamble=(
                "You are a highly knowledgeable virtual medical assistant with expertise in diagnosing potential medical conditions based on symptoms. "
                "Your task is to analyze the provided symptoms and suggest a list of possible medical conditions that could be associated with them. "
                "It is crucial to emphasize that these are only potential conditions and not definitive diagnoses. Always recommend consulting a healthcare professional "
                "for an accurate diagnosis and treatment plan.\n\n"
                "Consider the following symptoms and provide a list of possible conditions. Ensure that your suggestions are relevant and based on common medical knowledge. "
                "Avoid suggesting conditions that are extremely rare or unrelated to the symptoms provided.\n\n"
                "Output Format:\n"
                "* Possible Conditions:\n"
                "  * Condition 1\n"
                "  * Condition 2\n"
                "  * ...\n\n"
                "IMPORTANT: This information is for educational purposes only and should not be used as a substitute for professional medical advice. "
                "Encourage users to seek advice from qualified healthcare providers. Provide Answer in Concise way, No more than 2-3 Lines."
            ),
            max_tokens=1024,
        )
        prediction = response.text.strip()
        st.success(prediction)
    else:
        st.warning("Please enter some symptoms.")


