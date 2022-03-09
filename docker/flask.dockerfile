FROM python:3.9.10-bullseye

LABEL maintainer="SylvanBrocard sylvan.brocard@gmail.com"

WORKDIR /app

COPY  dist/sentiments-0.1.0-py3-none-any.whl /app

RUN pip install sentiments-0.1.0-py3-none-any.whl

EXPOSE 8000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]