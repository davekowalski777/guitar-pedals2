#!/bin/bash

# Create a Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput
