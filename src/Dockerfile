FROM python:3.8-slim as base

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

FROM base as production
ENTRYPOINT ["uvicorn",  "main:app", "--host", "0.0.0.0", "--port", "8080"]