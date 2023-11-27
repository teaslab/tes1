FROM python:3.9-slim

WORKDIR /app/bot

COPY ./bot .

RUN pip install -r requirements.txt

CMD ["python", "-u", "main.py"]