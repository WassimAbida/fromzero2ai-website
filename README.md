# fromzero2ai-website

This repository provides three main components :

 - Math Engine: folder for your research source code 

 - API Engine: Folder containing source code for the API for HTTP calls on available endpoints

 - APP Engine: Folder containing source code for Streamlit App, designed for demonstrations


## A set of environment variables are needed for the API
Check api.env example content

```bash
API_NAME=DemoAPI
RESPONSE_TIMEOUT=60
API_ROOT_URL=/fromzero2ai
API_SWAGGER_TITLE=fromzero2ai
```


## Development using Docker
We are using docker compose to manage available ressources
```bash
docker compose build
docker compose up
```

API is accessible using this url [http://0.0.0.0:9000/fromzero2ai/documentation](http://0.0.0.0:9000/fromzero2ai/documentation)

Streamlit Application is accessible using [http://0.0.0.0:8501/](http://0.0.0.0:8501/)


## Using API through curl

```bash
--> Using Parameters layer
curl -X 'POST' \
  'http://0.0.0.0:9000/fromzero2ai/addition?a=44&b=33' \
  -H 'accept: application/json'

--> Using Pydantic layer
curl -X 'POST' \
  'http://0.0.0.0:9000/fromzero2ai/multiplication' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "a": 5,
  "b": 6
}'

--> Expected output 
{"result": 30}
```
