FROM python:3.11

WORKDIR /app

COPY pyproject.toml poetry.lock /

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . .

EXPOSE 5000

CMD ["python", "app.py", "prod"]

