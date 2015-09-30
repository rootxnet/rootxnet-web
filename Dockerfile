RUN echo 00001  # increment to invalidate docker cache

# Set the base image to use to Ubuntu
FROM ubuntu:14.04
MAINTAINER Michal Lech "rootx@rootxnet.com"

ENV APP_SRCDIR=web
ENV APP_HOMEDIR=/opt/rootxnet-web

RUN apt-get -qq update
RUN apt-get install -y python-dev python-setuptools
RUN apt-get install -y g++ # required for pyzmq
RUN easy_install pip
RUN pip install --upgrade pip setuptools wheel virtualenv

COPY $APP_SRCDIR $APP_HOMEDIR/web
WORKDIR $APP_HOMEDIR
RUN virtualenv --no-site-packages .env
COPY ./requirements.txt ./
RUN . ./.env/bin/activate && pip install --upgrade -r requirements.txt
WORKDIR $APP_HOMEDIR/web
RUN . ../.env/bin/activate && python nano.py build_ipynb

EXPOSE 8000

COPY ./docker-entrypoint.sh ./
RUN chmod u+x ./docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
