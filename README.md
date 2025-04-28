# Calculadora Kappa
> Túlio Gois

Esta aplicação permite medir a concordância entre dois ou mais anotadores através do cálculo de Kappa. O índice é calculado utilizando Cohen's Kappa para dois anotadores e Fleiss' Kappa para mais de dois anotadores.
O [Kappa](https://pt.wikipedia.org/wiki/Concordância_entre_avaliadores#Estatísticas_Kappa) é uma das formas de medir concordância ou confiabilidade, corrigindo as classificações que podem ser iguais por acaso.
Os cálculos de concordância utilizados na aplicação são realizados através das funções [`kappa()`](https://www.nltk.org/api/nltk.metrics.agreement.html#nltk.metrics.agreement.AnnotationTask.kappa) e [`multi_kappa()`](https://www.nltk.org/api/nltk.metrics.agreement.html#nltk.metrics.agreement.AnnotationTask.multi_kappa) da biblioteca [NLTK](https://www.nltk.org/).

## Estrutura do repositório
### 📁 .streamlit
Arquivo de configuração do Streamlit.

### 📁 imgs
Logo utilizada na aplicação.

### `kappa.py`
Implementação do cálculo de Kappa.

### `main.py`
Código principal da aplicação em Streamlit.

### `requirements.txt`
Dependências do projeto.

