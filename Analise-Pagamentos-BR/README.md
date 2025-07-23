# Análise do Ecossistema de Pagamentos no Brasil: A Relação entre PIX e TED

## 📖 Visão Geral do Projeto

Este projeto realiza uma análise exploratória de dados abertos do Banco Central do Brasil para investigar as transformações no cenário de pagamentos após a introdução do PIX. O foco principal é entender a dinâmica entre o PIX e os métodos tradicionais, especialmente o TED, e identificar as tendências e implicações futuras para o mercado.

---

## 🎯 Principais Objetivos e Perguntas

O estudo foi guiado pelas seguintes questões:

* Qual o real impacto do crescimento acelerado do PIX sobre os métodos de pagamento já consolidados?
* PIX e TED atuam como concorrentes diretos, um substituindo o outro, ou são ferramentas complementares?
* Como está distribuída a participação de mercado (em valor) entre os principais métodos de pagamento?
* Quais são as implicações destas tendências para consumidores, empresas e o mercado financeiro?

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Bibliotecas de Análise:** Pandas, NumPy
* **Bibliotecas de Visualização:** Matplotlib, Seaborn
* **Ambiente:** Jupyter Notebook

---

## 🔬 Análises e Principais Insights

### 1. O Crescimento do PIX e a Resiliência do TED

A análise mostra um crescimento exponencial do PIX desde o seu lançamento em 2020, impulsionado por suas vantagens claras:
* **Instantaneidade 24/7**
* **Custo zero** para o usuário final
* **Facilidade de uso** através de chaves simples

Apesar disso, o TED não foi substituído. A sua resiliência pode ser atribuída a fatores como:
* **Hábito e confiança** em um método consolidado.
* **Preferência para transações de alto valor**, por segurança ou políticas institucionais.
* **Integração com sistemas legados** em muitas empresas.

### 2. Correlação Positiva: Complementaridade, não Concorrência

A análise estatística revelou uma forte correlação positiva entre o volume de transações de PIX e TED.

![Gráfico de Correlação entre PIX e TED](https://raw.githubusercontent.com/sfer26/BOOTCAMP_SOULCODE_AN-DADOS/main/Analise-Pagamentos-BR/images/correlacao_totalPIX-TED.png)

> **A análise de correlação demonstrou, com alta significância estatística (r=0,81, p≈0,0000), que PIX e TED atuam como ferramentas complementares. Em vez de se canibalizarem, ambos os métodos crescem em paralelo, sugerindo que um aumento geral na atividade econômica impulsiona todo o ecossistema de pagamentos.**

Este é o insight mais poderoso do projeto: o PIX expandiu o mercado em vez de simplesmente tomar o lugar do TED.

### 3. Participação de Mercado: Um Cenário em Transição

Ao analisar a participação de cada método no valor total transacionado no último período disponível, observou-se que:
* O **TED ainda é o líder incontestável em volume financeiro**, sendo o preferido para grandes movimentações.
* O **PIX, embora com um ticket médio menor, ganha terreno rapidamente** e já domina em número de transações do dia a dia.

---

## 📈 Conclusões e Implicações Futuras

Os dados indicam um mercado em clara transição. A tendência é que o PIX se consolide como o principal método de pagamento para a maioria dos casos de uso, enquanto o TED manterá sua relevância para nichos específicos, como transações de alto valor.

* **Para Consumidores:** A tendência é de mais praticidade, agilidade e economia.
* **Para Empresas:** Fica o alerta sobre a necessidade de se adaptar e oferecer opções de pagamento modernas.
* **Para o Mercado Financeiro:** A competição entre os métodos continuará a impulsionar a inovação e a busca por soluções mais eficientes.
