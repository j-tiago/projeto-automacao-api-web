# Desafio de Automação QA (API e Web)

Este projeto contém a automação de testes para a API do Swagger Petstore e testes End-to-End (E2E) Web para o site SauceDemo.

## Tecnologias Utilizadas
* Python 3
* Pytest (Framework de testes)
* Selenium WebDriver + Page Objects (Automação Web)
* Requests (Automação de API)
* GitHub Actions (Pipeline de CI)

## Como Instalar e Rodar Localmente

1. Clone o repositório:
   `git clone <seu-link-do-github>`
2. Crie e ative um ambiente virtual:
   `python -m venv venv`
   *(Windows)*: `.\venv\Scripts\activate`
   *(Linux/Mac)*: `source venv/bin/activate`
3. Instale as dependências:
   `pip install -r requirements.txt`

## Executando os Testes
* Para rodar todos os testes: `pytest -v`
* Para rodar apenas API: `pytest tests/api/ -v`
* Para rodar apenas Web: `pytest tests/web/ -v`