FROM python:3.7-slim-buster

WORKDIR /app

COPY .env ./

RUN pip3 install pymongo python-dotenv

COPY ./src/ .

CMD [ "python3", "index.py"]