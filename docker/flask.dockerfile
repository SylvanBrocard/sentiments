FROM python:3.9.10-bullseye

LABEL maintainer="SylvanBrocard sylvan.brocard@gmail.com"

WORKDIR /app

COPY . /app

RUN cd /app \
    && pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]