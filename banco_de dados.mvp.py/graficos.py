import pandas as pd
import matplotlib.pyplot as plt

chamados = pd.read_excel(
    'Base_Dados_Nava_Ecommerce.xlsx',
    sheet_name='Base_Consolidada_ETL'
)

chamados['data_venda'] = pd.to_datetime(
    chamados['data_venda']
)

# Gráfico 1 - Faturamento por categoria

faturamento_categoria = (
    chamados.groupby('categoria')['faturamento_total']
    .sum()
    .sort_values(ascending=False)
)

plt.bar(
    faturamento_categoria.index,
    faturamento_categoria.values
)

plt.xlabel('Categoria')
plt.ylabel('Faturamento')
plt.title('Faturamento por Categoria')
plt.xticks(rotation=45)
plt.show()


# Gráfico 2 - Evolução do lucro

lucro_mes = (
    chamados.groupby(
        chamados['data_venda'].dt.to_period('M')
    )['lucro']
    .sum()
)

plt.plot(
    lucro_mes.index.astype(str),
    lucro_mes.values,
    marker='o'
)

plt.xlabel('Mês/Ano')
plt.ylabel('Lucro')
plt.title('Evolução do Lucro ao Longo do Tempo')
plt.xticks(rotation=45)
plt.show()