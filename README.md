# Projeto de API utilizando FASTAPI e MongoDB

## Configuração do Projeto

### MongoDB

Os dados utilizados no projeto são de uma base sample disponibilizada pelo próprio MongoDB
(https://www.mongodb.com/pt-br/docs/atlas/sample-data/sample-restaurants/).
Estes dados foram carregados em um servidor [Atlas](https://www.mongodb.com/pt-br/atlas), que serão consumidos pela API.

### Arquivo .env

Crie um arquivo _.env_ contendo as seguintes informações:
ATLAS_URI=<URL disponibilizada para conexão com o MongoDB Atlas>

## Docker

No arquivo _Dockerfile_ são instaladas as bibliotecas [FastAPI](https://pypi.org/project/fastapi/), [pymongo](https://pypi.org/project/pymongo/) e [python-dotenv](https://pypi.org/project/python-dotenv/) 

## Criação de Imagem

```bash
docker buildx build -t rest-img .
```
## Execução de Container
```bash
docker run -p 0.0.0.0:8000:8000 --name rest-container rest-img 
```

A API deve subir no endereço https://127.0.0.1:8000/

A Documentação da API (swagger) estará disponível em https://127.0.0.1/docs/