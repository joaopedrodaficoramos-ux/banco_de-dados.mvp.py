# banco_de-dados.mvp.py
 Projeto de Análise de Dados - E-commerce 

Repositório estruturado para o processo seletivo de *Analista de Dados Pleno* na Nava, contendo o pipeline completo de dados: automação e análises exploratórias em Python, tratamento de dados, modelagem, medidas DAX e dashboard interativo no Power BI.

---

## 📋 Visão Geral do Projeto
Este projeto simula um cenário real de e-commerce, unificando bases de clientes, produtos e vendas para responder a perguntas estratégicas de negócio, analisar tendências e entregar indicadores executivos de faturamento e desempenho.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
* *Python (Pandas, Matplotlib/Seaborn):* Limpeza, tratamento, consolidação automatizada (ETL) e geração de gráficos analíticos exploratórios iniciais via código (projeto.py e graficos.py).
* *Power BI Desktop:* Modelagem de dados, criação de medidas DAX avançadas e design do painel interativo final.
* *GitHub:* Versionamento de código e documentação do portfólio.

---

## 📈 Análise Exploratória e Gráficos em Python
Antes de estruturar o painel final, todo o processo de ingestão e os primeiros cruzamentos gráficos foram programados e validados diretamente em scripts Python:
* *projeto.py*: Pipeline de ETL que consolida as planilhas brutas em uma única base tratada (Base_Consolidada_ETL).
* *graficos.py*: Scripts dedicados à geração de visualizações analíticas em código para validação rápida das tendências de vendas.

---

## 📊 Dashboard Interativo (Power BI)
O painel executivo foi desenvolvido no Power BI para acompanhar os principais indicadores de desempenho (KPIs) da operação com base na tabela consolidada:

![Dashboard do Power BI](dashboard_nava.png)

### Principais Indicadores Desenvolvidos (Medidas DAX):
* *Faturamento Total:* SUM(Base_Consolidada_ETL[faturamento_total])
* *Média de Faturamento por Venda:* AVERAGE(Base_Consolidada_ETL[faturamento_total])
* *Filtros Dinâmicos:* Segmentação interativa por status de pagamento (Concluído, Pendente, Cancelado).

---

## 📂 Estrutura do Repositório
* projeto.py — Script principal em Python responsável pela consolidação e ETL.
* graficos.py — Script com a construção dos gráficos analíticos em Python.
* Base_Dados_Nava_Ecommerce.xlsx — Base de dados consolidada.
* dashboard_nava.png — Captura de tela do Dashboard executivo em Power BI.

<img width="1862" height="950" alt="Captura de tela 2026-09-21 174639" src="https://github.com/user-attachments/assets/73af7ebd-0bc1-4907-89f1-71c474f79445" />


