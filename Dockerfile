FROM python:3

RUN apt-get update -y && \
  apt-get install -y python3-pip python-dev

WORKDIR /app

RUN pip install 
RUN pip install requests

COPY . .

CMD ["python", "./app.py"]