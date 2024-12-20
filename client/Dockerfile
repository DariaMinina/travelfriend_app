# syntax=docker.io/docker/dockerfile:1.7-labs

FROM node:14

WORKDIR /app

COPY --exclude=*node_modules* . /app
RUN npm install
RUN npm install -g serve

ENV VITE_SERVER_CONNECT_STRING="http://127.0.0.1:5015"

RUN npm run build

EXPOSE 5015

CMD ["serve", "-s", "dist"]
