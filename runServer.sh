#!/usr/bin/env bash

. .venv/bin/activate; gunicorn -p server.pid -w 4 -b 0.0.0.0:5000 --limit-request-line 0 --reload --access-logfile - yee:app
