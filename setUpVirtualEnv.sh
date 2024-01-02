#!/bin/bash

mkdir testEnv
cd testEnv

python3 -m venv .venv
. .venv/bin/activate


python3 -m pip install requests
pip install pytest
pip install pytest-steps
pip install jsonschema
