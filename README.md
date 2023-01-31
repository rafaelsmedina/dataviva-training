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
## Organização das Pastas

As pastas no projeto foram organizadas da seguinte maneira:

**app**: toda a implementação de código do site
**app** -> **modules**: arquivos .py auxiliares
**app** -> **templates**: todos os layouts/templates do site em html + python

## Desenvolvedores

Este projeto foi realizado por João Vitor Otoni, Kayque Siqueira, Marcos Pantuza, Rubens Castro e Samuel Santos como projeto inicial de
nivelamento do time de desenvolvimento de 2023 do site "Dataviva".