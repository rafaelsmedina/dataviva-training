# Projeto dataviva - Microblogging

Neste repositório será criado um pequeno projeto, utilizando Python, Flask e Javascript de um website de microblogging. 

Este projeto será baseado no [tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) criado por Miguel Grinberg e será realizado em conjunto pelos bolsistas do projeto Dataviva, 2023.

## Como rodar o site:

Primeiramente, para rodar o site, caso você não queira instalar os requisitos diretamente em sua máquina, existe a possibilidade de utilizar
um ambiente virtual ("venv") que possibilita a execução desses. Para utilizá-lo, deve-se aplicar os seguintes passos:

1.  Inicialmente, deve-se clonar este repositório

    <pre><code>git clone https://github.com/rafaelsmedina/dataviva-training.git</code></pre>
2.  Definindo a utilização do ambiente virtual e coloca seu nome como "venv"

    <pre><code>python -m venv venv</code></pre>
3.  Ativando o venv na sua máquina

    <pre><code>venv\Scripts\activate</code></pre>
    <pre><code>source venv/bin/activate</code></pre>
4.  Instalando todos os requisitos/extensões utilizadas para rodar a aplicação

    <pre><code>pip install -r requirements.txt</code></pre>
5.  Rodando o código fonte para possibilitar a visualização do site

    <pre><code>flask run</code></pre>

6.  (Passo contingente) Se algum erro ocorrer em relação ao arquivo do banco de dados (app.db), efetue os seguintes passos:
    1 - Exclua o arquivo app.db
    2 - Exclua a pasta migrations (se ela existir)
    3 - Abra o terminal e digite os seguintes comandos e depois tente rodar o projeto novamente:

    <pre><code>flask db init</code></pre>
    <pre><code>flask db migrate</code></pre>
    <pre><code>flask db upgrade</code></pre>

## Organização das Pastas

As pastas no projeto foram organizadas da seguinte maneira:

**app**: toda a implementação de código do site
**app** -> **modules**: arquivos .py auxiliares
**app** -> **templates**: todos os layouts/templates do site em html + python

Dentro da pasta app, temos 4 arquivos e duas pastas chamadas "modules" e "templates". Dentre esses 4 arquivos, temos o __init__.py, que é responsável por realizar toda a parte de configuração e inicialização do site, o app.db, que é onde estão os dados dinâmicos necessários para o funcionamento da aplicação, o arquivo config.py, que contém as variáveis globais do projeto além de algumas configurações para as bibliotecas utilizadas, e, por último, o arquivo routes.py, que é o responsável por conter todas as rotas do nosso site e conectá-las
aos seus respectivos layouts.

Dentro da pasta "modules", nós temos 4 arquivos que são responsáveis por conter as funções, formulários e classes para o correto funcionamento de todo o fluxo
da aplicação. Já na pasta templates, temos diretórios que armazenam os respectivos arquivos HTML de cada página e componente do site.

## Desenvolvedores

Este projeto foi realizado por João Vitor Otoni, Kayque Siqueira, Marcos Pantuza, Rubens Castro e Samuel Santos como projeto inicial de
nivelamento do time de desenvolvimento de 2023 do site "Dataviva".