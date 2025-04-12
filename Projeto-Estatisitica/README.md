# 📊 Análise de Turnover: Identificando Padrões de Rotatividade com Data Science

## 🎓 Contexto do Projeto

Este trabalho foi desenvolvido como parte do **Bootcamp de Analista de Dados** da [SoulCode Academy](https://www.soulcodeacademy.org/), com o objetivo de aplicar técnicas estatísticas em um cenário real de People Analytics.

## 🤝 Equipe de Desenvolvimento

[![Analista de Dados](https://img.shields.io/badge/Clarice_Matos-Analista_de_Dados-2ea44f?logo=github)](https://www.linkedin.com/in/claricematos/)
[![Analista de Dados](https://img.shields.io/badge/Flavia_Reis-Analista_de_Dados-2ea44f?logo=python)](https://github.com/flaviare1s/)  
[![Analista de Dados](https://img.shields.io/badge/Maria_Eduarda-Analista_de_Dados-3178c6?logo=pandas)](https://github.com/)
[![Analista de Dados](https://img.shields.io/badge/Mariana_Angeli-Analista_de_Dados-ffd43b?logo=powerbi)](https://github.com/)  
[![Analista de Dados](https://img.shields.io/badge/Michelle_Pacheco-Analista_de_Dados-9c59b6?logo=r)](https://www.linkedin.com/in/michelle-pacheco-509366351/)
[![Analista de Dados](https://img.shields.io/badge/Mylena_Tuponi-Analista_de_Dados-4d96ff?logo=sqlite)](https://www.linkedin.com/in/mylenatuponi/)  
[![Analista de Dados](https://img.shields.io/badge/Stella_Fernandes-Analista_de_Dados-e67e22?logo=tableau)](https://github.com/sfer26/)

### 👨‍🏫 Orientação Acadêmica
[![Professor](https://img.shields.io/badge/Prof._Stefane_Bressani-Mentor-8e44ad?logo=graduation-cap)](https://www.linkedin.com/in/stefane-bressani-germano/)

*Equipe formada durante o Bootcamp SoulCode Academy - Turma D13 20224*


## 🔍 Visão Geral do Projeto
Este projeto aplica técnicas estatísticas e de análise exploratória para investigar os fatores determinantes do turnover em uma organização. Através de uma abordagem data-driven, identificamos padrões comportamentais e operacionais que contribuem para a rotatividade de funcionários, oferecendo insights acionáveis para a retenção de talentos.

**Tecnologias Utilizadas**:
- Python 3.10
- Pandas (Análise de Dados)
- NumPy (Cálculos Estatísticos)
- Matplotlib/Seaborn (Visualização)
- Jupyter Notebook (Ambiente de Análise)

## 🎯 Objetivos Principais
1. Identificar correlações entre variáveis organizacionais e turnover
2. Construir perfis de risco de desligamento
3. Quantificar o impacto de políticas de RH nos índices de retenção
4. Propor recomendações baseadas em evidências estatísticas

## 📈 Insights Chave

### 🚨 Padrão Crítico: Efeito Pós-Promoção
```python
sns.kdeplot(df[df['Demissão'] == 'Não']['Anos desde a última promoção']
```

![Distribuição Pós-Promoção](Projeto-Estatisitica\images\anos-desde-ultima-promo-ajustado.png)

**Descobertas Notáveis**:
- 📌 **Pico Imediato**: 100+ demissões no ano seguinte à promoção
  - Possíveis causas: 
    - Expectativas não alinhadas
    - Preparação inadequada para novas responsabilidades
    - Síndrome do impostor em novos cargos

- 📉 **Queda Acelerada**: Redução de 60% nas demissões nos primeiros 5 anos pós-promoção
  - Indica período crítico de adaptação

- 🔍 **Padrão Bimodal**:
  - Pico principal em 1-2 anos (ciclo regular de promoções)
  - Segundo pico em 7 anos (estagnação de carreira)
    - Funcionários estáveis permanecem sem progressão
    - Risco crescente de desligamento após 5+ anos sem promoção

**Implicações para RH**:
1. Necessidade de programas de onboarding para cargos recém-promovidos
2. Revisão dos critérios e processos de promoção
3. Criação de planos de desenvolvimento para funcionários em plateau

## 🏗️ Estrutura do Projeto

```
/Projeto-Estatistica/
├── /data/             #dados csv
├── /docs/             #análise completa da persona e insights
├── /images/           # Todas as visualizações exportadas
├── estatistica.ipynb  # Jupyter - Notebook principal -com insights e análise completa
├── README.md          # Documentação principal
├── requirements.txt   # Dependências
```

## 💡 Aprendizados para Análise de Dados

Este projeto demonstra o **poder da análise estatística aplicada a RH**:
1. **Identificação de padrões não óbvios**: A análise quantitativa revelou relações não perceptíveis em abordagens qualitativas
2. **Priorização de iniciativas**: Os dados indicam onde intervenções terão maior impacto
3. **Mensuração de risco**: Modelagem estatística permite prever grupos vulneráveis
4. **Tomada de decisão baseada em evidências**: Redução de viés na gestão de pessoas

## 🛠️ Como Reproduzir

```bash
# 1. Configurar ambiente
pip install -r requirements.txt

# 2. Executar análise
jupyter notebook notebooks/analise_estatistica.ipynb
```

## 📌 Recomendações Estratégicas

1. **Programa de Transição de Cargos**:
   - Mentoria para recém-promovidos
   - Expectativas claras para novos cargos

2. **Revisão do Ciclo de Promoções**:
   - Avaliar critérios atuais
   - Implementar progressão gradual

3. **Monitoramento de Risco**:
   - Sistema de alerta para funcionários em plateau
   - Pesquisas de satisfação pós-promoção

4. **Planos de Desenvolvimento Individual**:
   - Rotas alternativas de crescimento
   - Atribuições desafiadoras para evitar estagnação

Este projeto exemplifica como a análise de dados transforma informações brutas em estratégias organizacionais eficazes, destacando o valor do data science na gestão moderna de pessoas.