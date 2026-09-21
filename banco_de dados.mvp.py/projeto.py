import pandas as pd

chamados = pd.read_excel(
    'Base_Dados_Nava_Ecommerce.xlsx',
    sheet_name='Base_Consolidada_ETL'
)
total_shape = chamados.shape    
info_status = chamados['status_pagamento'].info()
total_lucro = chamados['lucro'].sum()
total_faturamento = chamados['faturamento_total'].sum()
total_vendas = chamados['id_venda'].nunique()
total_clientes = chamados['id_cliente'].nunique()
Geral_status = chamados[chamados['status_pagamento'] == 'Concluído']
media_compras = total_vendas / total_clientes
print("Total de vendas pagas:", Geral_status['id_venda'].nunique())
print("Lucro total:", total_lucro)
print("Faturamento total:", total_faturamento)
print("Total de vendas:", total_vendas)
print("Total de clientes:", total_clientes)
print("Média de compras por cliente:", media_compras)
print("Informações sobre o status dos pagamentos:",info_status)
print("Forma do DataFrame:", total_shape)
print(chamados.head())
print(chamados.info())
print(chamados.describe())

#converter datas 
chamados['data_venda'] = pd.to_datetime(chamados['data_venda'])
chamados['data_cadastro'] = pd.to_datetime(chamados['data_cadastro'])
chamados_agrupados = (
    chamados.groupby('categoria')['faturamento_total']
    .sum()
    .sort_values(ascending=False)
)
print("Faturamento total por categoria:",chamados_agrupados)



