virtualenv -p python3 venv;
. venv/scripts/activate;
pip3 install -r requirements.txt;
pre-commit install;