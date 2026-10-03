import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(
    page_title="Monitor de Chuvas e Deslizamentos RJ",
    page_icon="☔",
    layout="wide"
)

st.title("☔ Monitoramento de Chuvas e Deslizamentos - RJ")
st.subheader("Avaliação G1 — Análise e Visualização de Dados")

# 3. Leitura de dados otimizada com cache (@st.cache_data)
@st.cache_data
def carregar_dados():
    return pd.read_csv("dados/simulacao_chuvas_deslizamentos_rj.csv")

df = carregar_dados()

# Identificação do Projeto na Barra Lateral (Sidebar)
st.sidebar.markdown("---")
st.sidebar.subheader("📌 Informações do Projeto")
st.sidebar.write("**Disciplina:** Linguagem de Programação — Análise e Visualização de Dados com Python")
st.sidebar.write("**Professor:** Alexandre Neves Louzada")
st.sidebar.write("**Aluna:** Anna Clara Berce")
st.sidebar.markdown("---")

# 5. Organização em Abas (Tabs)
tab1, tab2, tab3 = st.tabs(["KPIs & Gráficos", "API Meteorológica", "Tabela de Dados"])

# --- ABA 1: KPIs e Gráficos ---
with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total de Registros", value=len(df_filtrado))
    if 'Precipitacao_mm' in df_filtrado.columns:
        col2.metric(label="Precipitação Média", value=f"{df_filtrado['Precipitacao_mm'].mean():.1f} mm")
    if 'Risco_Deslizamento' in df_filtrado.columns:
        col3.metric(label="Alto Risco", value=int(df_filtrado['Risco_Deslizamento'].sum()))

    st.markdown("---")
    
    # Gráfico interativo com Plotly
    if 'Precipitacao_mm' in df_filtrado.columns:
        fig = px.histogram(df_filtrado, x='Precipitacao_mm', title="Distribuição do Volume de Chuva (mm)", color_discrete_sequence=['#1e3d59'])
        st.plotly_chart(fig, use_container_width=True)

# --- ABA 2: Consumo de API Externa ---
with tab2:
    st.subheader("Temperatura Atual na Capital (Open-Meteo API)")
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=-22.9068&longitude=-43.1729&current_weather=true"
        res = requests.get(url).json()
        temp = res['current_weather']['temperature']
        st.info(f"**Temperatura no Rio de Janeiro:** {temp} °C")
    except Exception:
        st.error("Não foi possível carregar os dados da API.")

# --- ABA 3: Tabela e Download ---
with tab3:
    st.dataframe(df_filtrado)
    st.download_button(
        label="Baixar Dados Filtrados (CSV)",
        data=df_filtrado.to_csv(index=False),
        file_name="chuvas_rj_filtrado.csv",
        mime="text/csv"
    )

st.markdown("---")
st.caption("Conclusão Executiva: O acúmulo de chuva acima de 80 mm correlaciona-se com aumento no risco geoambiental.")
