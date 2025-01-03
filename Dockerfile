FROM python:3.12

WORKDIR /app

RUN pip install --no-cache-dir -U python-dotenv
RUN pip install --no-cache-dir -U Misskey.py

COPY meow.py .

STOPSIGNAL SIGKILL

ENTRYPOINT ["python", "meow.py"]
