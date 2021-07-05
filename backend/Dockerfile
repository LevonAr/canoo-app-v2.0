FROM python:3.7.4

WORKDIR /app
ENV SECRET_KEY vmalnbaioqbga@#$%$^#@
ENV DB_URL mongodb://admin:cBhbNKEtze0hmMfriEJS@mongodb_container:27017/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]