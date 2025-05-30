# Lembre360 - Painel de Compromissos dos Clientes

O Lembre360 é uma solução digital desenvolvida para organizar e monitorar compromissos fiscais e financeiros dos clientes. Ele oferece uma visão clara dos prazos importantes, ajudando a evitar esquecimentos, multas e retrabalho.

## Funcionalidades

- Filtro interativo por status do compromisso e cliente.
- Alerta visual para compromissos próximos do vencimento.
- Painel com resumo gráfico da distribuição de compromissos por status.
- Upload do arquivo Excel pelo cliente para carregar os dados.
- Exportação dos dados filtrados para Excel.
- Atualização automática dos dados a partir do arquivo enviado.

## Tecnologias Utilizadas

- Python 3.x  
- Pandas  
- Streamlit  
- Plotly Express  
- OpenPyXL (para ler Excel)

## Como usar

1. Clone este repositório:  
   ```bash
   git clone https://github.com/vanessa-programacao/lembre360.git
Navegue até a pasta do projeto:

bash
Copiar
Editar
cd lembrete_360
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute o aplicativo:

bash
Copiar
Editar
streamlit run LEMBRETE_360.py
Na interface do app, o cliente deve carregar seu arquivo Excel (.xlsx) contendo os compromissos.

Estrutura do arquivo Excel
O arquivo Excel deve conter, no mínimo, as seguintes colunas:

Cliente	Descrição	Data	Valor	Status
Nome A	Exemplo	2025-06-10	1000	Pendente
Nome B	Exemplo	2025-07-15	2000	Em andamento
Nome C	Exemplo	2025-05-20	500	Concluído

O campo Data deve estar no formato de data (AAAA-MM-DD).

O campo Status deve conter um dos valores:

Pendente

Em andamento

Concluído

Após o upload, o sistema automaticamente:

Gera alertas para compromissos próximos do vencimento.

Mostra gráfico interativo da distribuição por status.

Permite exportar os dados filtrados para Excel.

Estrutura do projeto
bash
Copiar
Editar
/LEMBRETE_360
├── LEMBRETE_360.py
├── iniciar_lembrete360.bat
├── requirements.txt
├── README.md
└── /modelo (opcional)
    └── exemplo_compromissos.xlsx
Contato
Desenvolvido por Vanessa — Ciência de Dados & Soluções Digitais