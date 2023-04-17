# Custom docker image for fastapi
FROM python:3.9 as build-image

ARG PIP_TRUSTED_HOST
ARG PIP_EXTRA_INDEX_URL
ARG PROJECT_NAME=fromzero2ai

# Possible db libraries
RUN apt update
RUN apt-get install -y \
    gcc \
    curl \
    libmariadb-dev \
    libpq-dev

WORKDIR /${PROJECT_NAME}

# RUN python3 -m pip install --upgrade pip
# Virtual env configuration
ENV VIRTUAL_ENV=./venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install poetry==1.3.1

COPY ${PROJECT_NAME}/ /${PROJECT_NAME}/${PROJECT_NAME}/
COPY poetry.lock pyproject.toml launch.sh /${PROJECT_NAME}/

RUN chmod -R 777 /${PROJECT_NAME}/launch.sh

# RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --without-urls
# RUN pip install -r requirements.txt  --target /${PROJECT_NAME}/deps

# Install project
RUN poetry config virtualenvs.create false \
&& poetry config virtualenvs.in-project false \
&& poetry install 

FROM python:3.9

ARG CONTAINER_PORT=8090
ARG PROJECT_NAME=fromzero2ai
ENV CONTAINER_PORT=${CONTAINER_PORT}
WORKDIR /${PROJECT_NAME}

# Copy in the build image dependencies
COPY --from=build-image /${PROJECT_NAME} /${PROJECT_NAME}

EXPOSE ${CONTAINER_PORT}

RUN groupadd --gid 1300 agent && useradd -m --gid agent --uid 1300 agent
USER agent
# Virtual env configuration
ENV VIRTUAL_ENV=./venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENTRYPOINT ["./launch.sh"]
