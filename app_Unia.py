import streamlit as st
from transformers import pipeline

st.title("🤖 Pergunte algo sobre os documentos")

# Carrega o modelo gratuito da Hugging Face
@st.cache_resource
def carregar_modelo():
    return pipeline("text-generation", model="gpt2")

modelo = carregar_modelo()

pergunta = st.text_input("Digite sua pergunta")
if pergunta:
    resposta = modelo(pergunta, max_new_tokens=100)[0]["generated_text"]
    st.markdown(f"**Resposta:** {resposta}")
