FROM python:3.7.9-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update \
    && apk add libxml2 postgresql-dev linux-headers libevent-dev g++ gcc jpeg-dev zlib-dev libxslt-dev gcc python3-dev musl-dev libressl-dev musl-dev libffi-dev

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt --no-binary :all:
COPY . /code/

ENTRYPOINT ["/code/entrypoint.sh"]


