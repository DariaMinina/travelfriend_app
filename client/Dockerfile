FROM ubuntu:latest

WORKDIR /app

RUN apt-get update
RUN apt install -y npm
RUN apt install -y xsel

COPY . /app
RUN npm install
RUN npm install -g serve

RUN npm run build

EXPOSE 5015

CMD ["serve", "-s", "dist"]
#CMD ["npm", "run", "dev"]
