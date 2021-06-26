FROM python:3.8.5

COPY . /HomeCam

WORKDIR /HomeCam

RUN pip3 install -r requirements.txt

CMD gunicorn -c gunicorn.conf.py app:app --preload