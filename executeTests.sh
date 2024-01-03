cp test_PetStoreEndpoints.py testEnv/
cd testEnv

# source to activate the virtual env works only in the shell where this script is executed, then the shell is closed at the end
source .venv/bin/activate
python -m pytest 
