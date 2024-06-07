FROM python:3.10.11-alpine
LABEL Author="munchan2808@gmail.com"
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "run:app"]