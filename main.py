import streamlit as st
import pandas as pd
from kappa import *

st.set_page_config(
    page_title="Calculadora Kappa",
    page_icon="🤝",
    layout="wide"
)

st.title("Calculadora Kappa")
st.markdown("> Cálculo de concordância usando Kappa")
st.markdown("Essa aplicação permite medir a concordância entre dois ou mais anotadores através do cálculo de Kappa. O índice é calculado utilizando Cohen's Kappa para dois anotadores e Fleiss' Kappa para mais de dois anotadores. Mais detalhes da implementação estão na aba **Saiba mais**.")

tab1, tab2 = st.tabs(["Calculadora", "Saiba mais"])

with tab1:
    st.markdown("""
        ### Cálculo de concordância
        ##### 1. Carregue um arquivo *csv* ou *xlsx* com os dados anotados
    """)

    arquivo = st.file_uploader(
        label="Upload de arquivo",
        type=["csv", "xlsx"],
        help="Carregue um arquivo *csv* ou *xlsx* com os dados anotados."
    )
    
    if arquivo is not None:
        if arquivo.name.endswith(".csv"):
            df = pd.read_csv(arquivo)
        elif arquivo.name.endswith(".xlsx"):
            df = pd.read_excel(arquivo)

        st.dataframe(df, use_container_width=True)

        st.markdown("##### 2. Selecione as colunas contendo as anotações")

        colunas = st.multiselect(
            label="Selecione as colunas",
            options=df.columns.tolist(),
            help="Selecione as colunas que contêm os dados anotados pelos anotadores."
        )

        if len(colunas) >= 2:
            if st.button(
                label="Calcular Kappa",
                help="Clique para calcular o Kappa usando os dados selecionados."
            ):
                with st.container(border=True):
                    st.markdown("### Resultado")
                    st.markdown(f"Concordância entre: `{colunas}`")
                    st.code(
                        body=f"""{"Cohen's" if len(colunas) == 2 else "Fleiss'"} Kappa = {calcular_kappa(df, colunas):.4f}"""
                    )
        
        else:
            st.button(
                label="Calcular Kappa",
                help="Clique para calcular o Kappa usando os dados selecionados.",
                disabled=True
            )
            st.warning("Selecione pelo menos duas colunas para calcular o Kappa.")

    else:
        st.markdown("##### 2. Selecione as colunas contendo as anotações")
        st.warning("Carregue um arquivo para continuar")
        colunas = st.multiselect(
            label="Selecione as colunas",
            help="Selecione as colunas que contêm os dados anotados pelos anotadores.",
            options=[],
            disabled=True
        )
        st.button(
                label="Calcular Kappa",
                help="Clique para calcular o Kappa usando os dados selecionados.",
                disabled=True
        )
            
with tab2:
    st.markdown(
        """
        ### Saiba mais
        O [Kappa](https://pt.wikipedia.org/wiki/Concordância_entre_avaliadores#Estatísticas_Kappa) é uma das formas de medir concordância ou confiabilidade, corrigindo as classificações que podem ser iguais por acaso.   
        Os cálculos de concordância utilizados nessa aplicação são realizados através das funções [`kappa()`](https://www.nltk.org/api/nltk.metrics.agreement.html#nltk.metrics.agreement.AnnotationTask.kappa) e [`multi_kappa()`](https://www.nltk.org/api/nltk.metrics.agreement.html#nltk.metrics.agreement.AnnotationTask.multi_kappa) da biblioteca [NLTK](https://www.nltk.org/).
        """
    )

st.divider()
colunas = st.columns([3, 0.6])
colunas[0].image('imgs/lamid.png', width=130)
colunas[1].caption("Desenvolvido por Túlio Gois", unsafe_allow_html=True)
