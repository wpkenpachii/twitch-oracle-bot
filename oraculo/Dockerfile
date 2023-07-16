FROM python:3.10.6

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "--app", "main", "run", "--host=0.0.0.0", "--debug"]