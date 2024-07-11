#!/bin/bash

cd src

echo Setting up migrations
alembic upgrade head

echo Starting the server
fastapi run main.py
