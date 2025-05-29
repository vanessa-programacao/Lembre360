# Lembre360 - Painel de Compromissos dos Clientes

O Lembre360 é uma solução digital desenvolvida para organizar e monitorar compromissos fiscais e financeiros dos clientes. Ele oferece uma visão clara dos prazos importantes, ajudando a evitar esquecimentos, multas e retrabalho.

## Funcionalidades

- Filtro interativo por status do compromisso e cliente.
- Alerta visual para compromissos próximos do vencimento.
- Painel com resumo gráfico da distribuição de compromissos por status.
- Exportação dos dados filtrados para CSV.
- Atualização automática dos dados a partir de um arquivo CSV.

## Tecnologias Utilizadas

- Python 3.x  
- Pandas  
- Streamlit  
- Plotly Express

## Como usar

1. Clone este repositório:  
   `git clone https://github.com/vanessa-programacao/lembre360.git`

2. Navegue até a pasta do projeto:  
   `cd lembrete_360`

3. Instale as dependências:  
   `pip install pandas streamlit plotly`

4. Coloque seu arquivo `compromissos_com_clientes.csv` na pasta do projeto, ou altere o caminho no script conforme necessário.

5. Execute o aplicativo:  
   `streamlit run seu_arquivo.py`  
   *(substitua `seu_arquivo.py` pelo nome do seu script Python)*

## Estrutura do arquivo CSV

O arquivo CSV deve conter, no mínimo, as seguintes colunas:

- `Cliente` — Nome do cliente  
- `Descrição` — Descrição do compromisso  
- `Data` — Data do compromisso (formato AAAA-MM-DD)  
- `Valor` — Valor financeiro relacionado  
- `Status` — Status atual do compromisso (Ex: Pendente, Em Andamento, Concluído)

## Contato

Desenvolvido por Vanessa — Ciência de Dados & Soluções Digitais  
[GitHub](https://github.com/vanessa-programacao)

## Licença

Projeto de código aberto. Licença MIT.
