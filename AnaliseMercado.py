import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Estilo dos gráficos
sns.set(style="whitegrid")

# Configuração da página
st.set_page_config(page_title="Análise do Mercado de Trabalho em TI", layout="wide")

# Cabeçalho
st.title("Análise do Mercado de Trabalho em TI")
st.markdown("Baseado na pesquisa Stack Overflow Developer Survey 2024.")

# Carregamento de dados com cache
@st.cache_data
def carregar_dados():
    url = r"C:\\Users\\souza\\Downloads\\DATASET\\survey_results_public.csv"
    return pd.read_csv(url)

df = carregar_dados()

# Limpeza dos dados
colunas_interesse = ['Employment', 'Country', 'EdLevel', 'DevType',
                     'LanguageHaveWorkedWith', 'ConvertedCompYearly']
df_clean = df[colunas_interesse].dropna()

# Remover o país "Gabon"
df_clean = df_clean[df_clean["Country"] != "Gabon"]

# Menu lateral
st.sidebar.title("🔍 Navegação")
opcao = st.sidebar.radio("Selecione uma seção:", [
    " Introdução",
    "Distribuição de Cargos",
    "Distribuição Salarial",
    "Salário Mediano por País (Top 15)",
    "Nível Educacional Mais Comum",
    "Linguagens Mais Usadas",
    "Tipos de Desenvolvedor Mais Frequentes",
    "Top Países com Mais Desenvolvedores",
    "Dados do País Selecionado"
])

# Filtros
st.sidebar.markdown("---")
pais = st.sidebar.multiselect("Filtrar País(es):", df_clean["Country"].unique())
cargo = st.sidebar.multiselect("Filtrar Cargo(s):", df_clean["DevType"].dropna().unique())

df_filtrado = df_clean.copy()
if pais:
    df_filtrado = df_filtrado[df_filtrado["Country"].isin(pais)]
if cargo:
    df_filtrado = df_filtrado[df_filtrado["DevType"].str.contains('|'.join(cargo))]

# Seções
if opcao == "Introdução":
    st.header("Bem-vindo!")
    st.markdown("""
    Painel para analisar os dados da pesquisa anual do Stack Overflow e permitem analisar tendências como:

    - Linguagens de programação mais usadas
    - Tipos de cargos mais comuns
    - Níveis de escolaridade
    - Distribuição geográfica dos devs
    - Salários comparativos

    ---
    **Como usar:**
    - Navegue entre os gráficos usando o menu à esquerda
    - Aplique filtros para personalizar as análises
 
    ####  Fonte: Stack Overflow Developer Survey 2024
    """)

elif opcao == "Distribuição de Cargos":
    st.subheader("Distribuição de Cargos")

    if not df_filtrado.empty:
        cargos = df_filtrado['DevType'].dropna().str.split(';')
        flat_cargos = [c.strip() for sublist in cargos for c in sublist]
        if flat_cargos:
            cargo_counts = pd.Series(flat_cargos).value_counts().head(10)
            fig, ax = plt.subplots(figsize=(12,6))
            sns.barplot(x=cargo_counts.values, y=cargo_counts.index, palette="Set2", ax=ax)
            ax.set_title("Top 10 Cargos Mais Comuns", fontsize=18, weight="bold")
            ax.set_xlabel("Número de Desenvolvedores", fontsize=14)
            ax.set_ylabel("Cargo", fontsize=14)
            ax.grid(axis='x', linestyle='--', alpha=0.7)
            for i, v in enumerate(cargo_counts.values):
                ax.text(v + 1, i, str(v), color='black', va='center', fontsize=12)
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.info("Nenhum dado de cargo encontrado após aplicar os filtros.")
    else:
        st.warning("Nenhum dado disponível para o(s) filtro(s) selecionado(s).")

elif opcao == "Distribuição Salarial":
    st.subheader("Distribuição Salarial (USD)")

    if not df_filtrado.empty and df_filtrado["ConvertedCompYearly"].notna().any():
        fig, ax = plt.subplots(figsize=(12,6))
        sns.histplot(df_filtrado["ConvertedCompYearly"], bins=40, kde=True, color='teal', ax=ax)
        ax.set_xlabel("Salário Anual (USD)", fontsize=14)
        ax.set_ylabel("Número de Desenvolvedores", fontsize=14)
        ax.set_title("Distribuição Salarial com KDE", fontsize=18, weight='bold')
        ax.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.warning("Sem dados salariais para o(s) filtro(s) atual(is).")

elif opcao == "Salário Mediano por País (Top 15)":
    st.subheader("Salário Anual Mediano por País (Top 15)")

    if not df_filtrado.empty:
        salario_pais = df_filtrado.groupby("Country")["ConvertedCompYearly"].median().sort_values(ascending=False).head(15)

        fig, ax = plt.subplots(figsize=(14,7))
        sns.barplot(x=salario_pais.values, y=salario_pais.index, palette="viridis", ax=ax)

        ax.set_xlabel("Salário Mediano (USD)", fontsize=14)
        ax.set_ylabel("País", fontsize=14)
        ax.set_title("Salário Mediano por País - Top 15", fontsize=20, weight="bold")
        ax.grid(axis='x', linestyle='--', alpha=0.7)

        for i, v in enumerate(salario_pais.values):
            ax.text(v + max(salario_pais.values)*0.01, i, f"${v:,.0f}", color='black', va='center', fontsize=12)

        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.warning("Sem dados para calcular o salário mediano com os filtros aplicados.")

elif opcao == "Nível Educacional Mais Comum":
    st.subheader("Níveis de Educação Mais Comuns")

    edu_counts = df_filtrado['EdLevel'].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(14,7))
    sns.barplot(x=edu_counts.values, y=edu_counts.index, palette="coolwarm", ax=ax)

    ax.set_xlabel("Número de Desenvolvedores", fontsize=14)
    ax.set_ylabel("Nível de Educação", fontsize=14)
    ax.set_title("Top 10 Níveis Educacionais", fontsize=18, weight='bold')
    ax.grid(axis='x', linestyle='--', alpha=0.7)

    for i, v in enumerate(edu_counts.values):
        ax.text(v + max(edu_counts.values)*0.01, i, str(v), color='black', va='center', fontsize=12)

    plt.tight_layout()
    st.pyplot(fig)

elif opcao == "Linguagens Mais Usadas":
    st.subheader("Linguagens de Programação Mais Usadas")

    langs = df_filtrado['LanguageHaveWorkedWith'].dropna().str.split(';')
    flat_langs = [lang.strip() for sublist in langs for lang in sublist]
    lang_counts = pd.Series(flat_langs).value_counts().head(10)

    fig, ax = plt.subplots(figsize=(14,7))
    sns.barplot(x=lang_counts.values, y=lang_counts.index, palette="Blues_d", ax=ax)

    ax.set_title("Top 10 Linguagens Mais Usadas", fontsize=18, weight='bold')
    ax.set_xlabel("Número de Desenvolvedores", fontsize=14)
    ax.set_ylabel("Linguagem", fontsize=14)
    ax.grid(axis='x', linestyle='--', alpha=0.7)

    for i, v in enumerate(lang_counts.values):
        ax.text(v + max(lang_counts.values)*0.01, i, str(v), color='black', va='center', fontsize=12)

    plt.tight_layout()
    st.pyplot(fig)

elif opcao == "Tipos de Desenvolvedor Mais Frequentes":
    st.subheader("Tipos de Desenvolvedor Mais Frequentes")

    devs = df_filtrado["DevType"].dropna().str.split(';')
    flat_devs = [d.strip() for sublist in devs for d in sublist]
    dev_counts = pd.Series(flat_devs).value_counts().head(10)

    fig, ax = plt.subplots(figsize=(14,7))
    sns.barplot(x=dev_counts.values, y=dev_counts.index, palette="Set1", ax=ax)

    ax.set_xlabel("Número de Desenvolvedores", fontsize=14)
    ax.set_ylabel("Tipo de Desenvolvedor", fontsize=14)
    ax.set_title("Top 10 Tipos de Desenvolvedor", fontsize=18, weight='bold')
    ax.grid(axis='x', linestyle='--', alpha=0.7)

    for i, v in enumerate(dev_counts.values):
        ax.text(v + max(dev_counts.values)*0.01, i, str(v), color='black', va='center', fontsize=12)

    plt.tight_layout()
    st.pyplot(fig)

elif opcao == "Top Países com Mais Desenvolvedores":
    st.subheader("Top 15 Países com Mais Desenvolvedores")

    pais_counts = df_filtrado['Country'].value_counts().head(15)

    fig, ax = plt.subplots(figsize=(14,7))
    sns.barplot(x=pais_counts.index, y=pais_counts.values, palette="mako", ax=ax)

    ax.set_ylabel('Número de Desenvolvedores', fontsize=14)
    ax.set_xlabel('País', fontsize=14)
    ax.set_title('Top 15 Países com Mais Desenvolvedores', fontsize=18, weight='bold')
    plt.xticks(rotation=45, ha='right')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    for i, v in enumerate(pais_counts.values):
        ax.text(i, v + max(pais_counts.values)*0.01, str(v), color='black', ha='center', fontsize=12)

    plt.tight_layout()
    st.pyplot(fig)

elif opcao == "Dados do País Selecionado":
    st.subheader("Dados Detalhados do País Selecionado")

    if df_filtrado.empty:
        st.warning("Nenhum dado disponível para o país selecionado.")
    else:
        st.markdown("Exibindo os dados com base no filtro lateral de país.")
        st.dataframe(
            df_filtrado[[
                "Country", "Employment", "EdLevel", "DevType",
                "LanguageHaveWorkedWith", "ConvertedCompYearly"
            ]].sort_values(by="ConvertedCompYearly", ascending=False).reset_index(drop=True),
            use_container_width=True
        )

# Rodapé
st.markdown("---")
st.markdown("Fonte: [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024)")
