import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Lembre360 - Painel Completo de Compromissos")

# Upload do arquivo Excel
arquivo = st.file_uploader("Envie seu arquivo Excel com os compromissos:", type=["xlsx"])

if arquivo is not None:
    try:
        df = pd.read_excel(arquivo, parse_dates=['Data'])

        # Validação das colunas obrigatórias
        colunas_obrigatorias = ['Cliente', 'Descrição', 'Data', 'Valor', 'Status']
        colunas_faltando = [col for col in colunas_obrigatorias if col not in df.columns]

        if colunas_faltando:
            st.error(f"As seguintes colunas estão faltando no arquivo: {', '.join(colunas_faltando)}")
        else:
            # Filtros
            dias_alerta = st.slider("Dias para alerta de vencimento:", 1, 30, 3)

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

            # Filtrar por data
            hoje = pd.Timestamp.today()
            limite = hoje + pd.Timedelta(days=dias_alerta)
            df_vencendo = df_filtrado[
                (df_filtrado['Data'] >= hoje) & (df_filtrado['Data'] <= limite)
            ]

            st.subheader(f"Compromissos pendentes até {limite.date()} (próximos {dias_alerta} dias)")

            if df_vencendo.empty:
                st.success("Nenhum compromisso pendente próximo do vencimento.")
            else:
                for idx, row in df_vencendo.iterrows():
                    cor = ""
                    if row['Status'].lower() == 'pendente':
                        cor = "PENDENTE"
                    elif row['Status'].lower() == 'em andamento':
                        cor = "EM ANDAMENTO"
                    elif row['Status'].lower() == 'concluído':
                        cor = "CONCLUÍDO"

                    st.write(
                        f"{cor} | {row['Cliente']} | {row['Descrição']} | Data: {row['Data'].date()} | Valor: R${row['Valor']} | Status: {row['Status']}"
                    )

            st.write(f"Total de compromissos pendentes próximos do vencimento: {df_vencendo.shape[0]}")

            # Gráfico
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

            # Tabela
            st.subheader("Todos os compromissos filtrados")
            st.dataframe(df_filtrado)

            # Exportar
            @st.cache_data
            def convert_df(df):
                from io import BytesIO
                output = BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False)
                return output.getvalue()

            excel_export = convert_df(df_filtrado)

            st.download_button(
                label="Exportar Excel filtrado",
                data=excel_export,
                file_name='compromissos_filtrados.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )

            st.write("Os dados são processados conforme o Excel enviado.")

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")

else:
    st.info("Por favor, envie um arquivo Excel para iniciar a análise.")