FROM python:3.9.2-buster

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
# pip installs
COPY ./app/backend/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN pip install fasttext

RUN pip install mecab-python3

RUN pip install unidic-lite

WORKDIR ./app


# FastAPIの起動
CMD ["python3.9", "/app/main.py"]
