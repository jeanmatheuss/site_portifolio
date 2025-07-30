import streamlit as st
import pandas as pd
import datetime

#@st.cache_data(ttl="1day")

st.set_page_config(page_title="Portifólio", page_icon="📚")

st.markdown(
    """
# Bem vindo ao meu Portifólio

## Aqui você encontrará quem sou eu, meus projetos e objetivos.

"""
)

#tab_python, tab_sql, tab_pbi = st.tabs(["Python", "SQL", "Power BI"])


# Bloco python
with st.container(border=True):
    st.write("Python")
    python = st.expander("Python")
    


# Bloco SQL
sql = st.expander("SQL")
sql.container(border=True)
sql.write("[Projeto 1](https://github.com/jeanmatheuss/jean-EBAC-SQL/blob/main/SQL_analise_credito.ipynb)")

# Bloco PBI
pbi = st.expander("Power BI")
pbi.container(border=True)

# Próximo passo: Organizar os conteúdos por abas, add sidebar, criar páginas extras para cada conteúdo.

# teste pra saber do commit