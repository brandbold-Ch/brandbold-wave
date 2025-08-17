FROM python:3.11-alpine3.21

ENV PYTHONUNBUFFERED=1

WORKDIR /flask

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

#CMD ["gunicorn", "-w", "4", "main:app", "-b", "0.0.0.0:5000", "--timeout", "7200"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]
