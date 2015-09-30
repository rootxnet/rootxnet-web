# Set the base image to use to UbuntuM
FROM ubuntu:14.04

# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV DOCKYARD_SRC=hello_django
# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/srv
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=/srv/hello_django

# Copy application source code to SRCDIR
COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ

#RUN apt-get update && apt-get -y upgrade
#RUN apt-get install -y python python-pip

WORKDIR $DOCKYARD_SRVHOME
COPY ./docker-entrypoint.sh ./
ENTRYPOINT ["./docker-entrypoint.sh"]
