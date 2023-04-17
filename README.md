# fromzero2ai-website
website for fromzero2ai




## Local dockerfile build
```docker build -t engine .```

## Local launch
```bash
docker run --env-file .env -it -p 9000:8080 engine

docker composer build
docker composer up

> http://0.0.0.0:9000/fromzero2ai/documentation
> http://0.0.0.0:8501/

```




## .env example content
```bash

API_NAME=DemoAPI
RESPONSE_TIMEOUT=60
API_ROOT_URL=/fromzero2ai
API_SWAGGER_TITLE=fromzero2ai

```