FROM python:3.8.12-slim

WORKDIR /app

COPY ["requirements.txt", "requirements.txt"]

RUN pip install -r requirements.txt

COPY ["predict.py", "model_C=0.5.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]