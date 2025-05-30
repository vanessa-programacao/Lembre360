import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Lembre360 - Painel Completo de Compromissos")

# Upload do arquivo
uploaded_file = st.file_uploader("Faça upload do arquivo de compromissos (CSV ou Excel)", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Escolhe automaticamente CSV ou Excel
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file, parse_dates=['Data'])
    else:
        df = pd.read_excel(uploaded_file, parse_dates=['Data'])

    st.success("✅ Arquivo carregado com sucesso!")

    # Filtro de dias para alerta
    dias_alerta = st.slider("Dias para alerta de vencimento:", 1, 30, 3)

    # Filtros adicionais
    status_selecionado = st.multiselect(
        "Filtrar por Status:",
        options=df['Status'].unique(),
        default=list(df['Status'].unique())
    )

    cliente_selecionado = st.multiselect(
        "Filtrar por Cliente:",
        options=df['Cliente'].unique(),
        default=list(df['Cliente'].unique())
    )

    # Aplicar filtros
    df_filtrado = df[
        (df['Status'].isin(status_selecionado)) &
        (df['Cliente'].isin(cliente_selecionado))
    ]

    # Filtrar por data de vencimento próxima
    hoje = pd.Timestamp.today()
    limite = hoje + pd.Timedelta(days=dias_alerta)
    df_vencendo = df_filtrado[
        (df_filtrado['Data'] >= hoje) & (df_filtrado['Data'] <= limite)
    ]

    st.subheader(f"Compromissos pendentes até {limite.date()} (próximos {dias_alerta} dias)")

    if df_vencendo.empty:
        st.success("Nenhum compromisso pendente próximo do vencimento!")
    else:
        for idx, row in df_vencendo.iterrows():
            st.write(
                f"{row['Cliente']} | {row['Descrição']} | {row['Data'].date()} | R${row['Valor']} | Status: {row['Status']}"
            )

    st.write(f"**Total de compromissos pendentes próximos do vencimento:** {df_vencendo.shape[0]}")

    # Gráfico de barras por Status
    st.subheader("Distribuição de compromissos por Status")
    grafico = df_filtrado['Status'].value_counts().reset_index()
    grafico.columns = ['Status', 'Quantidade']

    fig = px.bar(
        grafico,
        x='Status',
        y='Quantidade',
        color='Status',
        text='Quantidade',
        title='Quantidade de Compromissos por Status'
    )

    st.plotly_chart(fig)

    # Tabela completa
    st.subheader("Todos os compromissos filtrados")
    st.dataframe(df_filtrado)

    # Botão de exportação
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv_export = convert_df(df_filtrado)

    st.download_button(
        label="Exportar CSV filtrado",
        data=csv_export,
        file_name='compromissos_filtrados.csv',
        mime='text/csv'
    )
else:
    st.info("Por favor, envie um arquivo CSV ou Excel para continuar.")
