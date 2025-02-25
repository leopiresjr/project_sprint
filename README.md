# project_sprint
Análise Exploratória de Dados de Veículos
Descrição do Projeto
Este projeto consiste em um aplicativo web interativo desenvolvido com Streamlit, destinado a facilitar a análise exploratória de um conjunto de dados de veículos. O aplicativo permite aos usuários visualizar e interagir com os dados de anúncios de vendas de carros, proporcionando insights importantes sobre variáveis como quilometragem (odometer) e preço.

Funcionalidades
Visualização Inicial dos Dados:
Exibe as primeiras linhas do dataset para que o usuário possa ter uma visão geral dos dados.

Histograma Interativo:
Ao clicar em um botão, o aplicativo gera um histograma interativo da variável 'odometer', permitindo a análise da distribuição da quilometragem dos veículos.

Gráfico de Dispersão:
Um segundo botão permite a criação de um gráfico de dispersão que relaciona a quilometragem com o preço, facilitando a identificação de possíveis correlações entre essas variáveis.

Validações e Alertas:
O aplicativo realiza checagens para garantir que as colunas necessárias existem no dataset, exibindo mensagens de alerta caso alguma informação esteja faltando.

Como Usar
Instalação:

Clone o repositório.
Instale as dependências necessárias (consulte o arquivo requirements.txt).
Execução:

No terminal, navegue até o diretório do projeto.
Execute o aplicativo com o comando:
bash
Copiar
streamlit run app.py
Interação:

Utilize os botões disponíveis na interface para gerar os gráficos interativos e explorar os dados.
Tecnologias Utilizadas
Python
Pandas
Plotly Express
Streamlit
