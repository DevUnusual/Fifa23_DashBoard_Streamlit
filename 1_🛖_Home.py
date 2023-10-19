import streamlit as st
import pandas as pd
import webbrowser as wb
from datetime import datetime

if "data" not in st.session_state:
  df = pd.read_csv("database\CLEAN_FIFA23_official_data.csv", index_col=0)
  df = df[df["Contract Valid Until"] >= datetime.now().year]
  df = df[df["Value(£)"] > 0]
  df = df.sort_values(by="Overall", ascending=False)
  st.session_state["df_fifa"] = df


st.markdown("# BEM VINDO A UMA DASHBOARD DE ANALISE DE DADOS DO FIFA23.")
st.markdown("""
            Bem-vindo à Dashboard de Análise de Dados do FIFA 23!

Aqui, você está no controle total do jogo. Nossa plataforma foi projetada para fornecer a você uma visão abrangente e inteligente do mundo do FIFA 23. Seja você um jogador dedicado, um técnico virtual ou apenas um apaixonado pelo esporte, esta dashboard é a sua porta de entrada para a experiência de jogo mais avançada.
            """)
st.sidebar.markdown("Feito por [DevUnusual](https://github.com/DevUnusual)")