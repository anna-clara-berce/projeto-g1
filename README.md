# ☔ Monitoramento de Chuvas e Deslizamentos no Estado do Rio de Janeiro

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-222222?style=for-the-badge&logo=github)

Projeto de análise exploratória de dados pluviométricos e mapeamento de riscos geoambientais no Estado do Rio de Janeiro, desenvolvido para a **Avaliação G1** da disciplina de Linguagem de Programação.

---

## 🔗 Links Rápidos de Acesso

* 🌐 **Página Web de Apresentação (GitHub Pages):** [Acessar Apresentação](https://anna-clara-berce.github.io/projeto-g1/)
* 📊 **Dashboard Interativo (Streamlit Cloud):** [Acessar Dashboard](https://anna-clara-berce.streamlit.app/)
* 💻 **Repositório do Código (GitHub):** [Acessar Repositório](https://github.com/anna-clara-berce/projeto-g1)

---

## 📌 Sobre o Projeto

O Estado do Rio de Janeiro sofre constantemente com eventos climáticos extremos. Este projeto analisa a relação entre precipitação, acúmulo de chuvas e ocorrências de deslizamentos em áreas de encosta.

### Funcionalidades do Dashboard:
- 🔍 **Filtros Dinâmicos:** Seleção de municípios e períodos.
- 📈 **KPIs em Tempo Real:** Total de registros, precipitação média (mm) e contagem de ocorrências de risco elevado.
- 📊 **Gráficos Interativos:** Séries temporais de pluviometria e distribuição estatística via Plotly e Seaborn.
- 🌐 **Consumo de API Meteorológica:** Previsão em tempo real utilizando a API pública Open-Meteo.
- 🗄️ **Persistência em Banco de Dados:** Mapeamento e exportação dos dados limpos via SQLAlchemy em banco SQLite.

---

## 📁 Estrutura do Repositório

```text
projeto-g1/
│
├── app.py                  # Código do Dashboard em Streamlit
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação completa
├── index.html              # Página Web de Apresentação (GitHub Pages)
├── dados/                  # Base de dados (simulacao_chuvas_deslizamentos_rj.csv)
├── database/               # Banco de dados SQLite (chuvas_rj.db)
├── notebooks/              # Jupyter Notebook com a análise exploratória (.ipynb)
└── imagens/                # Capturas de tela e gráficos do projeto
