FROM python:3.12-alpine3.18

COPY Pipfile ./
COPY LinkCat /LinkCat
WORKDIR /LinkCat
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev


RUN python -m pip install --upgrade pip

RUN pip install pipenv && pipenv lock && pipenv install --dev --system --deploy
