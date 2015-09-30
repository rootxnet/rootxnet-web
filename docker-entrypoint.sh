#!/bin/bash

# Prepare log files and start outputting logs to stdout
mkdir $APP_HOMEDIR/logs/
touch $APP_HOMEDIR/logs/gunicorn.log
touch $APP_HOMEDIR/logs/access.log
tail -n 0 -f $APP_HOMEDIR/logs/*.log &

source $APP_HOMEDIR/.env/bin/activate
# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn nano:application \
    --name nano \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    --log-file=$APP_HOMEDIR/logs/gunicorn.log \
    --access-logfile=$APP_HOMEDIR/logs/access.log \
    "$@"