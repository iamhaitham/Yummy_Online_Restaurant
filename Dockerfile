# syntax=docker/dockerfile:1
FROM ubuntu:latest
EXPOSE 8000
EXPOSE 80
WORKDIR .
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN git clone https://github.com/MohammedBayatena/Python_Project.git
WORKDIR /Python_Project
RUN cd ./yummy_proj/
RUN pip install -r requirements.txt 
WORKDIR /Python_Project/yummy_proj/

