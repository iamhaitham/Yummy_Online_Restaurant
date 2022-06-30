# syntax=docker/dockerfile:1
FROM python:3.9.13-bullseye
EXPOSE 8000
EXPOSE 80
WORKDIR .
RUN apt-get update
RUN apt-get install -y python3.9
RUN apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN apt-get install -y git
RUN git clone https://github.com/MohammedBayatena/Python_Project.git
WORKDIR /Python_Project
RUN cd ./yummy_proj/
RUN pip install -r requirements.txt 
WORKDIR /Python_Project/yummy_proj/

