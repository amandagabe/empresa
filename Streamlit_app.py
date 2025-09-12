import os
import streamlit as st

PASTA = "ATENDIMENTO"

st.set_page_config(page_title="Arquivos Disponíveis", layout="centered")

st.title("🔐 Login")
usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

USUARIO = 'amanda'
SENHA = 'senha123'

if usuario == USUARIO and senha == SENHA:
    st.success("Login bem-sucedido!")
    st.title("📂 Arquivos disponíveis")

    arquivos = os.listdir(PASTA)
    for arquivo in arquivos:
        st.write(f"- {arquivo}")

