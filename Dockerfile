FROM python:3.10.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /code

WORKDIR /code

RUN pip install -r /code/requirements.txt

ENTRYPOINT ["sh","./entrypoint.sh"]
