#!/bin/bash

gunicorn --workers=4 --bind 0.0.0.0:"$PORT" app:app
