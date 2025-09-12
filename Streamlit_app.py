import streamlit as st
import os

PASTA = r'C:\DADOS\ATENDIMENTO'
USUARIO = 'amanda'
SENHA = 'senha123'

st.set_page_config(page_title="Arquivos Disponíveis", layout="centered")

# Autenticação simples
st.title("🔐 Login")
usuario = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

if usuario == USUARIO and senha == SENHA:
    st.success("Login bem-sucedido!")

    st.title("📁 Arquivos disponíveis")
    arquivos = os.listdir(PASTA)

    for arquivo in arquivos:
        caminho = os.path.join(PASTA, arquivo)
        with open(caminho, "rb") as f:
            st.download_button(label=f"📥 Baixar {arquivo}", data=f, file_name=arquivo)
else:
    st.warning("Digite usuário e senha para acessar os arquivos.")
