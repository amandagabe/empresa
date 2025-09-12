import streamlit as st
import os
from docx import Document
from transformers import pipeline

# Carrega o modelo leve compatível com Streamlit Cloud
@st.cache_resource
def carregar_agente():
    return pipeline("text-generation", model="sshleifer/tiny-gpt2")

agente = carregar_agente()

PASTA = "ATENDIMENTO"

st.title("🔐 Login")
usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

USUARIO = "amanda"
SENHA = "senha123"

if usuario == USUARIO and senha == SENHA:
    st.success("Login bem-sucedido!")
    st.title("📂 Arquivos disponíveis")

    arquivos = os.listdir(PASTA)
    conteudo_total = ""

    for arquivo in arquivos:
        caminho = os.path.join(PASTA, arquivo)
        st.write(f"📄 {arquivo}")

        if arquivo.endswith(".docx"):
            doc = Document(caminho)
            texto = "\n".join([p.text for p in doc.paragraphs])
            st.text_area(f"Conteúdo de {arquivo}", texto, height=300)
            conteudo_total += f"\n\nConteúdo de {arquivo}:\n{texto}"

    st.markdown("---")
    st.subheader("🤖 Pergunte algo sobre os documentos")

    pergunta = st.text_input("Digite sua pergunta")
    if pergunta:
        prompt = f"""Você é um assistente que responde com base nos documentos abaixo.
Documentos:
{conteudo_total}

Pergunta: {pergunta}
Resposta:"""

        resposta = agente(prompt, max_new_tokens=100)[0]["generated_text"]
        st.markdown(f"**Resposta:** {resposta.split('Resposta:')[-1].strip()}")

