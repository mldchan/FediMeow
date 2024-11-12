FROM python:3.12

WORKDIR /app

RUN pip install -U python-dotenv
RUN pip install -U Misskey.py

COPY meow.py .

ENTRYPOINT ["python", "meow.py"]
