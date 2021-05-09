FROM python:3.8.0-alpine

WORKDIR /usr/src/gateway

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/gateway

CMD ["python", "src/app.py"]

