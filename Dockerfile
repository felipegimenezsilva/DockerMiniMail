FROM python:alpine3.16
WORKDIR /app
COPY app.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3","app.py"]
