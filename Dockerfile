FROM python:3

RUN apt-get update -y && \
  apt-get install -y python3-pip python-dev

WORKDIR /app

RUN pip install tk
RUN pip install Pillow

COPY . .

CMD ["python", "./app.py"]