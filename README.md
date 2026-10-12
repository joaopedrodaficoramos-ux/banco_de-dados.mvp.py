# Análise de vendas com Python e Power BI

Projeto de portfólio para acompanhar vendas, faturamento e lucro por categoria e período. A análise parte de uma base Excel já consolidada, aplica validações e gera indicadores e gráficos com Pandas e Matplotlib. O repositório também inclui um dashboard em Power BI.

## Executar (Python 3.10+)
Na raiz:
```bash
python -m pip install -r requirements.txt
python "banco_de dados.mvp.py/projeto.py"
python "banco_de dados.mvp.py/graficos.py"
```
Os caminhos são relativos ao arquivo do script. Os gráficos são salvos em `outputs/` sem exigir uma janela gráfica.

## Regras e qualidade dos dados
- A base possui uma linha por venda (`id_venda`); IDs ausentes ou duplicados geram erro.
- Faturamento, lucro, ticket médio e compras por cliente consideram apenas `Concluído`.
- Ticket médio = faturamento concluído / vendas concluídas distintas.
- Quantidade total de registros e distribuição por status consideram a base inteira.
- Datas, status e valores numéricos são validados antes dos cálculos.
- O script analisa a aba `Base_Consolidada_ETL`; não realiza a consolidação de fontes brutas.

## Arquivos
- `banco_de dados.mvp.py/Base_Dados_Nava_Ecommerce.xlsx`: base de entrada.
- `banco_de dados.mvp.py/projeto.py`: validação e indicadores.
- `banco_de dados.mvp.py/graficos.py`: faturamento por categoria e lucro mensal.
- `banco_de dados.mvp.py/dashbord_nava_ecommerce.pbix`: dashboard existente.
- `medidas_dax.dax`: medidas propostas com regras alinhadas aos scripts Python.

## Power BI
Abra o PBIX no Power BI Desktop e ajuste o caminho da fonte Excel para o arquivo local. A captura abaixo corresponde ao painel original:

<img width="1862" height="950" alt="Dashboard de vendas original" src="https://github.com/user-attachments/assets/73af7ebd-0bc1-4907-89f1-71c474f79445" />

As novas medidas estão em `medidas_dax.dax` para aplicação manual, uma por vez, na tabela `Base_Consolidada_ETL`. Use-as nos cartões e visuais financeiros e confira os totais com `projeto.py`. O PBIX original permanece sem atualização automatizada; a captura não comprova os novos cálculos.

## Limitações e interpretação
Projeto de estudo, sem comprovação de resultados em operação real. Os scripts trabalham com dados já consolidados e não demonstram um ETL completo. A consistência entre filtros, medidas e visuais deve ser verificada no Power BI após aplicar as medidas propostas.

## Resultados reproduzidos na base de estudo
- 576 de 1.000 vendas estão concluídas (57,6%).
- As concluídas somam R$ 1.384.988,00 de faturamento e R$ 472.938,00 de lucro registrado; ticket médio de R$ 2.404,49.
- Informática lidera o faturamento concluído, com R$ 627.679,00.
- 211 vendas estão pendentes e 213 canceladas. Acompanhar essas duas situações separadamente evita confundir carteira com vendas concluídas; a base não informa os motivos de cancelamento.
