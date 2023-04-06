# fromzero2ai-website
website for fromzero2ai

http://127.0.0.1:9000/fromzero2ai/documentation


## Local dockerfile build
```docker build -t engine .```

## Local launch
```bash
docker run --env-file .env -it -p 9000:8080 engine

>http://0.0.0.0:9000/fromzero2ai/documentation
```


## .env example content
```bash

API_NAME=DemoAPI
RESPONSE_TIMEOUT=60
API_ROOT_URL=/fromzero2ai

```