# 📊 Análise de Tendências no Mercado de Trabalho em TI

## 🎯 Objetivo
Este projeto tem como objetivo analisar os dados da pesquisa anual da **Stack Overflow Developer Survey 2024** para identificar tendências no mercado de tecnologia da informação. As análises buscam compreender padrões relacionados a linguagens utilizadas, níveis educacionais, salários, perfis profissionais e distribuição geográfica.

## 🗂️ Dados Utilizados
- **Fonte**: [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024) (via Kaggle)
- **Formato**: CSV
- **Atributos analisados**:
  - País (`Country`)
  - Tipo de desenvolvedor (`DevType`)
  - Linguagens utilizadas (`LanguageHaveWorkedWith`)
  - Nível educacional (`EdLevel`)
  - Situação de emprego (`Employment`)
  - Faixa salarial (`ConvertedCompYearly`)

## 🧰 Tecnologias Utilizadas
- Python
- Streamlit
- Pandas
- Seaborn
- Matplotlib

## 🔎 Funcionalidades e Análises
A aplicação oferece um painel interativo com as seguintes seções:

- **Introdução** — Visão geral do projeto
- **Distribuição de Cargos** — Análise dos tipos de cargos mais frequentes
- **Distribuição Salarial** — Histograma com KDE dos salários anuais (USD)
- **Salário Mediano por País (Top 15)** — Comparação entre países
- **Nível Educacional Mais Comum** — Gráfico dos 10 níveis mais comuns
- **Linguagens Mais Usadas** — Top 10 linguagens com maior ocorrência
- **Tipos de Desenvolvedor Mais Frequentes** — Categorias profissionais em destaque
- **Top Países com Mais Desenvolvedores** — Ranking por volume de participantes
- **Dados do País Selecionado** — Tabela detalhada por país e cargo

### 🔄 Filtros Interativos
- **País(es)**: permite escolher múltiplos países
- **Tipo de cargo(s)**: permite filtrar os desenvolvedores por perfil profissional

> Obs: Dados do país **Gabon** foram removidos devido a inconsistência estatística.

## 💡 Principais Insights 
- JavaScript e Python e lideram entre as linguagens utilizadas.
- Os maiores salários estão em países como **EUA*
- A maioria dos desenvolvedores possui **ensino superior completo**.
- Perfis mais comuns: **Full Stack Developer**, **Backend Developer** e **DevOps**.

---

## 🧪 Como Executar
1. Clone este repositório:
   ```bash
   git clone (https://github.com/VinnySou/pi3-analise-tendencias-ti)
   ```
2. Baixe a base CSV:
   ```
   https://drive.google.com/file/d/1lgdCGA5OuPDsoq8QLoL1Yt7w4KfYSX1W/view?usp=drive_link
   ```
   Altere o caminho da base na linha 19 do código AnaliseMercado.py
   ```py
   @st.cache_data
   def carregar_dados():
    url = r"C:\\Users\\souza\\Downloads\\DATASET\\survey_results_public.csv"
    return pd.read_csv(url)
    ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```bash
   streamlit run streamlit_app.py
   ```

---

## 🎥 Vídeo (Entrega 3)
Video da analise:
[![YouTube](https://img.shields.io/badge/Ver%20no-YouTube-red)](https://www.youtube.com/watch?v=D6ZA5yCWhEQ)
```
https://www.youtube.com/watch?v=D6ZA5yCWhEQ
```
---

## 👥 Integrantes

**Turma 4HC2 – Ciência da Computação**
- Arthur Coutinho Chagas  
- Jairo Cavalcanti  
- Juliana Seith  
- Ryan Oliveira  
- Vinícius Silva  

**Integrantes de outra turma (5HC1):**
- Pedro Henrique Neves  
- Enzo Sampaio  

> Projeto Integrador III — Ciência da Computação — FAESA – 2025
