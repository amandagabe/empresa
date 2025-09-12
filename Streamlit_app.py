import streamlit as st
import os
from docx import Document

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
    for arquivo in arquivos:
        caminho = os.path.join(PASTA, arquivo)
        st.write(f"📄 {arquivo}")

        if arquivo.endswith(".docx"):
            doc = Document(caminho)
            texto = "\n".join([p.text for p in doc.paragraphs])
            st.text_area(f"Conteúdo de {arquivo}", texto, height=300)

