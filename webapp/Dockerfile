FROM python:2-alpine
ADD . /
RUN apk update && apk add --virtual build-dependencies \
        build-base \
        gcc \
        mariadb-dev \
        mariadb-connector-c-dev && \
        pip install -r requirements.txt  
CMD ["flask","run","--host=0.0.0.0"]