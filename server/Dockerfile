FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . server

ENV SECRET_KEY=your_secret_key_here
ENV DATABASE_URL="postgresql+psycopg2://root:root@localhost:5432/travel_app"
ENV SERVER_NAME=127.0.0.1:5015
ENV UPLOAD_FOLDER=uploads
ENV MAX_CONTENT_LENGTH=16777216

EXPOSE 5015

CMD [ "python", "server/run.py" ]
