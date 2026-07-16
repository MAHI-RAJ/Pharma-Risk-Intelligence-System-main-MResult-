import streamlit as st
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=st.secrets["GROQ_API_KEY"]
)

def generate_answer(query, context):

    prompt = f"""
You are a pharmaceutical risk intelligence assistant.

Answer ONLY from the provided context.

If the information is not available,
say:

"I could not find sufficient information in the uploaded documents."

Context:
{context}

Question:
{query}

Provide a clear concise answer.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content