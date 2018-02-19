# Set the base image to use to Ubuntu
FROM alpine:3.7
MAINTAINER Michal Lech "rootx@rootxnet.com"

ENV APP_SRCDIR=web
ENV APP_HOMEDIR=/opt/rootxnet-web

COPY $APP_SRCDIR $APP_HOMEDIR/web
WORKDIR $APP_HOMEDIR
COPY ["./requirements.txt", "./setup.py", "./tox.ini", "./"]

# g++ required for pyzmq
RUN apk update && \
    apk add python3-dev && \
    apk add g++ && \
    pip3 install --upgrade -r requirements.txt && \
    apk del g++ && \
    rm -rf /var/cache/apk/*

WORKDIR $APP_HOMEDIR/web
RUN python3 nano.py build_ipynb

EXPOSE 8000

COPY ./docker-entrypoint.sh ./
RUN chmod u+x ./docker-entrypoint.sh
ENTRYPOINT ["sh", "./docker-entrypoint.sh"]

