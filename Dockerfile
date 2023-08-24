FROM python:3.11.4-slim-bullseye
LABEL authors="gulyaeve"

WORKDIR /src

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["python", "main.py"]