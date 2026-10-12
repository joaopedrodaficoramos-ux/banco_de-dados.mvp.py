from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from projeto import carregar_base
ROOT = Path(__file__).resolve().parent
def gerar_graficos():
    df = carregar_base()
    paid = df.loc[df['status_pagamento'] == 'Concluído'].copy()
    output = ROOT.parent / 'outputs'
    output.mkdir(exist_ok=True)
    categoria = paid.groupby('categoria')['faturamento_total'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(categoria.index, categoria.values)
    ax.set(xlabel='Categoria', ylabel='Faturamento (R$)', title='Faturamento por categoria - vendas concluídas')
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    fig.savefig(output / 'faturamento_categoria.png', dpi=150)
    plt.close(fig)
    lucro = paid.groupby(paid['data_venda'].dt.to_period('M'))['lucro'].sum().sort_index()
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(lucro.index.astype(str), lucro.values, marker='o')
    ax.set(xlabel='Mês/Ano', ylabel='Lucro (R$)', title='Evolução do lucro - vendas concluídas')
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    fig.savefig(output / 'lucro_mensal.png', dpi=150)
    plt.close(fig)
    print(f'Gráficos salvos em {output}')
if __name__ == '__main__':
    gerar_graficos()
