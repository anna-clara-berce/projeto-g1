import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from sqlalchemy import create_engine

st.set_page_config(page_title="Chuvas & Deslizamentos RJ", layout="wide")

# Título e Descrição
st.title("☔ Monitoramento de Chuvas e Deslizamentos - RJ")
st.markdown("Análise de precipitação pluviométrica e mapeamento de riscos para o Estado do Rio de Janeiro.")

# Carregamento de dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv('dados/simulacao_chuvas_deslizamentos_rj.csv')
    return df

df = carregar_dados()

# Persistência com SQLAlchemy (Salva dados no banco SQLite local)
engine = create_engine('sqlite:///database/chuvas_rj.db')
df.to_sql('ocorrencias', con=engine, if_exists='replace', index=False)

# Sidebar / Filtros
st.sidebar.header("🔍 Filtros de Consulta")
colunas = df.columns.tolist()

# Filtro dinâmico se existir coluna de município/região
if 'Municipio' in df.columns:
    muni_sel = st.sidebar.multiselect("Municípios", options=df['Municipio'].unique(), default=df['Municipio'].unique())
    df_filtrado = df[df['Municipio'].isin(muni_sel)]
else:
    df_filtrado = df

# Abas Organizadoras
tab1, tab2, tab3 = st.tabs(["📌 KPIs & Gráficos", "🌐 Clima em Tempo Real (API)", "📄 Tabela & Download"])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Ocorrências", len(df_filtrado))
    if 'Precipitacao_mm' in df_filtrado.columns:
        col2.metric("Precipitação Média", f"{df_filtrado['Precipitacao_mm'].mean():.1f} mm")
    if 'Risco_Deslizamento' in df_filtrado.columns:
        col3.metric("Alto Risco", int(df_filtrado['Risco_Deslizamento'].sum()))

    st.markdown("---")
    
    # Gráfico com Plotly
    if 'Precipitacao_mm' in df_filtrado.columns:
        fig = px.histogram(df_filtrado, x='Precipitacao_mm', title="Distribuição de Precipitação (mm)", color_discrete_sequence=['#1e3d59'])
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("🌐 Previsão Meteorológica Atual na Capital (API Open-Meteo)")
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=-22.9068&longitude=-43.1729&current_weather=true"
        res = requests.get(url).json()
        temp = res['current_weather']['temperature']
        vento = res['current_weather']['windspeed']
        st.info(f"🌡️ **Temperatura Atual:** {temp} °C | 💨 **Velocidade do Vento:** {vento} km/h")
    except Exception as e:
        st.error("Erro ao carregar os dados da API.")

with tab3:
    st.dataframe(df_filtrado)
    st.download_button("Baixar Dados Filtrados (CSV)", df_filtrado.to_csv(index=False), "dados_chuvas_rj.csv")

st.markdown("---")
st.caption("Conclusão Executiva: O acúmulo continuado de precipitação correlaciona-se diretamente com o aumento do risco geoambiental.")
