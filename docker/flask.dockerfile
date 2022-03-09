FROM python:3.9.10-bullseye

LABEL maintainer="SylvanBrocard sylvan.brocard@gmail.com"

WORKDIR /app

COPY . /app

RUN pip install /app/dist/sentiments-0.1.0-py3-none-any.whl

ENTRYPOINT [ "python" ]

CMD [ "sentiments/app.py" ]