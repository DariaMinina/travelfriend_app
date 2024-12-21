# syntax=docker.io/docker/dockerfile:1.7-labs

FROM ubuntu:latest

WORKDIR /app

RUN apt-get update
RUN apt install -y npm

COPY --exclude=*node_modules* . /app

RUN npm install
RUN npm install -g serve

ENV VITE_SERVER_CONNECT_STRING="http://127.0.0.1:5015"

EXPOSE 5015

CMD npm run build && serve -s dist
