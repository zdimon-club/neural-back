# Install virtualenv and requirements.

    virtualenv -p python3 venv
    . ./venv/bin/activate
    pip install -r requirements.txt

## Run server

    cd back
    ./manage.py runserver 8001