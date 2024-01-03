#!/bin/bash

mkdir testEnv
cd testEnv

python3 -m venv .venv

# source to activate the virtual env works only in the shell where this script is executed, then the shell is closed at the end
. .venv/bin/activate


python3 -m pip install requests
pip install pytest
pip install pytest-steps
pip install jsonschema
