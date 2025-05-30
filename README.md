# Lembre360 - Painel de Compromissos dos Clientes

Lembre360 é uma aplicação para organizar e monitorar compromissos fiscais e financeiros dos clientes, facilitando o acompanhamento de prazos e status.

## Funcionalidades

- Upload do arquivo Excel (.xlsx) ou CSV com os compromissos.
- Filtragem por status e cliente.
- Alertas para compromissos próximos do vencimento.
- Gráfico interativo da distribuição dos compromissos por status.
- Exportação dos dados filtrados para CSV.
- Aplicação hospedada online para acesso fácil via navegador.

## Tecnologias Utilizadas

- Python 3.x  
- Pandas  
- Streamlit  
- Plotly Express  
- OpenPyXL  

## Acesse o app online

Você pode acessar o Lembre360 diretamente no navegador, sem precisar instalar nada:

[👉 https://lembre360-78pbyhnf2hz5iiwj2kj3kz.streamlit.app/](https://lembre360-78pbyhnf2hz5iiwj2kj3kz.streamlit.app/)

## Como usar localmente

1. Clone o repositório:  
   `git clone https://github.com/vanessa-programacao/lembre360.git`

2. Entre na pasta do projeto:  
   `cd Lembrete_360`

3. Instale as dependências:  
   `pip install -r requirements.txt`

4. Rode o app:  
   `streamlit run LEMBRETE_360.py`

5. No app, faça upload do arquivo Excel ou CSV contendo os compromissos.

## Estrutura do arquivo Excel/CSV

O arquivo deve conter as seguintes colunas:

| Cliente   | Descrição                 | Data       | Valor | Status       |
|-----------|---------------------------|------------|-------|--------------|
| Empresa A | Descrição do compromisso   | 2025-06-10 | 1500  | Pendente     |
| Empresa B | Outro compromisso          | 2025-07-01 | 2000  | Em andamento |
| Empresa C | Compromisso finalizado     | 2025-05-20 | 500   | Concluído    |

- **Data** no formato AAAA-MM-DD.  
- **Status** deve ser um dos: Pendente, Em andamento, Concluído.

## Contato

Desenvolvido por Vanessa — Ciência de Dados & Soluções Digitais  
GitHub: https://github.com/vanessa-programacao

## Licença

Projeto open source sob licença MIT.
