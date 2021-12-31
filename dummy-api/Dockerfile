FROM python:3.10.1-alpine

RUN apk add curl

RUN pip install --no-cache-dir Flask

RUN mkdir /app
WORKDIR /app

COPY * .

EXPOSE 105

CMD [ "python", "./app.py" ]
