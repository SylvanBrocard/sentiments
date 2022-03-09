FROM python:3.9.10-bullseye

LABEL maintainer="SylvanBrocard sylvan.brocard@gmail.com"

WORKDIR /app

RUN pip install poetry

COPY . /app

RUN cd /app \
    && poetry config virtualenvs.create false \
    && poetry install

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]