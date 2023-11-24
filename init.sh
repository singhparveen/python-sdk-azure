#!/usr/bin/env bash
set -xe
rm -rf venv # clean start

# prod dependencies
python3 -m venv venv
source ./venv/bin/activate
pip install pylint autopep8 # dev dependencies
pip install --upgrade pip
pip install -r requirements.txt
