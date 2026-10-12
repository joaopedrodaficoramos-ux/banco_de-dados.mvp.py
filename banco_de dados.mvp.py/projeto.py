"""Análise de uma base já consolidada; métricas financeiras de vendas concluídas."""
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parent
BASE = ROOT / 'Base_Dados_Nava_Ecommerce.xlsx'
def carregar_base():
    df = pd.read_excel(BASE, sheet_name='Base_Consolidada_ETL')
    required = {'id_venda', 'id_cliente', 'data_venda', 'status_pagamento', 'categoria', 'faturamento_total', 'lucro'}
    if not required.issubset(df.columns):
        raise ValueError('Colunas obrigatórias ausentes na base')
    if df['id_venda'].isna().any() or df['id_venda'].duplicated().any():
        raise ValueError('Esta análise espera uma linha por id_venda')
    if df['status_pagamento'].isna().any() or not df['status_pagamento'].isin(['Concluído', 'Pendente', 'Cancelado']).all():
        raise ValueError('Status de pagamento inválido')
    for col in ('faturamento_total', 'lucro'):
        df[col] = pd.to_numeric(df[col], errors='raise')
        if df[col].isna().any() or df[col].isin([float('inf'), float('-inf')]).any():
            raise ValueError(f'Valores inválidos em {col}')
    df['data_venda'] = pd.to_datetime(df['data_venda'], errors='raise')
    if df['data_venda'].isna().any():
        raise ValueError('Data de venda ausente')
    return df
def indicadores(df):
    paid = df.loc[df['status_pagamento'] == 'Concluído'].copy()
    total = float(paid['faturamento_total'].sum())
    vendas = int(paid['id_venda'].nunique())
    clientes = int(paid['id_cliente'].nunique())
    return {
        'registros_total_base': len(df), 'vendas_concluidas': vendas,
        'clientes_com_vendas_concluidas': clientes,
        'faturamento_concluido': round(total, 2),
        'lucro_vendas_concluidas': round(float(paid['lucro'].sum()), 2),
        'ticket_medio_concluido': round(total / vendas, 2) if vendas else None,
        'compras_por_cliente': round(vendas / clientes, 2) if clientes else None
    }
def analisar():
    df = carregar_base()
    print(pd.Series(indicadores(df)).to_string())
    print('\nDistribuição de registros por status:')
    print(df['status_pagamento'].value_counts().to_string())
    paid = df.loc[df['status_pagamento'] == 'Concluído']
    print('\nFaturamento de vendas concluídas por categoria:')
    print(paid.groupby('categoria')['faturamento_total'].sum().sort_values(ascending=False).to_string())
if __name__ == '__main__':
    analisar()
