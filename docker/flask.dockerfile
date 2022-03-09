FROM python:3.9.10-alpine

LABEL maintainer="SylvanBrocard sylvan.brocard@gmail.com"

WORKDIR /app

RUN pip install Flask

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]