#!/bin/sh


if [[ $RUN_TESTS ]]; then
    apk update
    apk add g++
    cd $APP_HOMEDIR
    tox
else
    # Start Gunicorn processes
    echo Starting Gunicorn.
    cd $APP_HOMEDIR/web
    exec gunicorn nano:application \
        --name nano \
        --bind 0.0.0.0:8000 \
        --workers 3 \
        --log-level=info \
        --log-file=- \
        --access-logfile=- \
        "$@"
fi