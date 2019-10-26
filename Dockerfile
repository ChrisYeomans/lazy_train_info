FROM ubuntu:16.04

MAINTAINER Chris Yeomans "chrisj.yeomans@gmail.com"

RUN apt update -y \
    && apt upgrade -y \
    && apt-get install -y python-pip python-dev

# For Caching 
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

# docker run --network="host" lti