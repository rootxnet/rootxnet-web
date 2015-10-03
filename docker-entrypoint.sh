#!/bin/bash


source $APP_HOMEDIR/.env/bin/activate

if [[ $RUN_TESTS ]]; then
    cd $APP_HOMEDIR
    tox
else
    # Prepare log files and start outputting logs to stdout
    mkdir $APP_HOMEDIR/logs/
    touch $APP_HOMEDIR/logs/gunicorn.log
    touch $APP_HOMEDIR/logs/access.log
    tail -n 0 -f $APP_HOMEDIR/logs/*.log &

    # Start Gunicorn processes
    echo Starting Gunicorn.
    cd $APP_HOMEDIR/web
    exec gunicorn nano:application \
        --name nano \
        --bind 0.0.0.0:8000 \
        --workers 3 \
        --log-level=info \
        --log-file=$APP_HOMEDIR/logs/gunicorn.log \
        --access-logfile=$APP_HOMEDIR/logs/access.log \
        "$@"
fi