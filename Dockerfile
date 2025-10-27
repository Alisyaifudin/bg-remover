FROM python:3.13-slim

# Install ONLY the required library
RUN apt-get update && apt-get install -y libexpat1 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY static ./static/
COPY templates ./templates/
COPY .u2net /root/.u2net
COPY main.py .

EXPOSE 1234

CMD ["uwsgi", "--http", "0.0.0.0:1234", "--master", "-p", "4", "-w", "main:app"]