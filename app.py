import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Configuração da página
st.set_page_config(page_title="Análise de Veículos", layout="wide")

# Função para carregar os dados com cache


@st.cache_data
def load_data(path):
    return pd.read_csv(path)


def main():
    # Cabeçalho e introdução
    st.title("Análise Exploratória de Dados de Veículos")
    st.header("Visualização de Dados e Gráficos Interativos")

    # Definir o caminho absoluto para o arquivo CSV, relativo ao local de app.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'vehicles.csv')

    # Tenta ler o arquivo e exibe mensagem de erro se não conseguir
    try:
        car_data = load_data(data_path)
    except Exception as e:
        st.error(f"Erro ao ler o arquivo CSV: {e}")
        return

    # Exibe as primeiras linhas do dataset
    st.write("Visualizando as primeiras linhas do dataset:")
    st.dataframe(car_data.head())

    # Botão para criar um histograma de 'odometer'
    hist_button = st.button("Criar Histograma")
    if hist_button:
        st.write(
            "Criando um histograma para o conjunto de dados de anúncios de vendas de carros.")
        if 'odometer' in car_data.columns:
            fig_hist = px.histogram(
                car_data,
                x="odometer",
                nbins=50,
                title="Distribuição da Quilometragem (odometer)",
                labels={"odometer": "Quilometragem"}
            )
            st.plotly_chart(fig_hist, use_container_width=True)
        else:
            st.warning("A coluna 'odometer' não foi encontrada no dataset.")

    # Botão para criar um gráfico de dispersão relacionando 'odometer' e 'price'
    scatter_button = st.button("Criar Gráfico de Dispersão")
    if scatter_button:
        st.write("Criando um gráfico de dispersão relacionando 'odometer' e 'price'.")
        if 'odometer' in car_data.columns and 'price' in car_data.columns:
            fig_scatter = px.scatter(
                car_data,
                x="odometer",
                y="price",
                title="Relação entre Quilometragem e Preço",
                labels={"odometer": "Quilometragem", "price": "Preço"}
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
        else:
            st.warning(
                "As colunas 'odometer' e/ou 'price' não foram encontradas no dataset.")


if __name__ == '__main__':
    main()
