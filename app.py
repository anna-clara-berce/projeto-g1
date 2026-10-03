import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(page_title="Monitor de Chuvas e Deslizamentos - RJ", layout="wide")

st.title(" Monitoramento de Chuvas e Deslizamentos no Estado do Rio de Janeiro")
st.markdown("Análise exploratória de dados pluviométricos e mapeamento de riscos climáticos no RJ.")

@st.cache_data
def carregar_dados():
    return pd.read_csv('dados/simulacao_chuvas_deslizamentos_rj.csv')

df = carregar_dados()

# Sidebar - Filtros Interativos
st.sidebar.title("Filtros de Análise")
if 'Municipio' in df.columns:
    municipios = st.sidebar.multiselect(
        "Selecione os Municípios",
        options=df['Municipio'].unique(),
        default=df['Municipio'].unique()
    )
    df_filtrado = df[df['Municipio'].isin(municipios)]
else:
    df_filtrado = df

# Abas / Seções Organizadoras
tab1, tab2, tab3 = st.tabs(["KPIs & Gráficos", "Clima em Tempo Real (API)", "Dados Detalhados"])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Registros", len(df_filtrado))
    if 'Precipitacao_mm' in df.columns:
        col2.metric("Média de Precipitação (mm)", f"{df_filtrado['Precipitacao_mm'].mean():.1f} mm")
    if 'Risco_Deslizamento' in df.columns:
        col3.metric("Ocorrências / Risco Alto", int(df_filtrado['Risco_Deslizamento'].sum()))

    # Gráfico com Plotly
    if 'Data' in df.columns and 'Precipitacao_mm' in df.columns:
        fig = px.line(df_filtrado, x='Data', y='Precipitacao_mm', title="Série Temporal de Precipitação")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Consumo de API Externa (Previsão do Tempo Exemplo)")
    # Consumo de API para dados meteorológicos reais
    try:
        res = requests.get("https://api.open-meteo.com/v1/forecast?latitude=-22.9068&longitude=-43.1729&current_weather=true").json()
        temp = res['current_weather']['temperature']
        st.info(f"Temperatura atual na Capital (Rio de Janeiro): {temp} °C")
    except Exception as e:
        st.warning("Não foi possível carregar a API externa no momento.")

with tab3:
    st.dataframe(df_filtrado)
    st.download_button("Baixar Dados Filtrados (CSV)", df_filtrado.to_csv(index=False), "chuvas_rj_filtrado.csv")

st.markdown("---")
st.caption("Conclusão Executiva: Os dados apontam maior risco nos meses de verão, exigindo atenção para planos de contingência.")
