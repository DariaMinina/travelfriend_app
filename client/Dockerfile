# syntax=docker.io/docker/dockerfile:1.7-labs

FROM node:14

WORKDIR /app

COPY --exclude=*node_modules* . /app
RUN npm install
RUN npm install -g serve

RUN npm run build

EXPOSE 5015

CMD ["serve", "-s", "dist"]
