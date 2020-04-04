# Install virtualenv and requirements.

    ng add @nguniversal/express-engine --clientProject front


    sudo apt-get install libpq-dev ffmpeg

    sudo ln -s /usr/bin/ffprobe /usr/local/bin

# Neular Dating

# Deploy OS requirements

## locale

    sudo apt-get install language-pack-en-base

     sudo apt-get install python3 python-dev python3-dev \
     build-essential libssl-dev libffi-dev \
     libxml2-dev libxslt1-dev zlib1g-dev \
     python-pip python-pydot python-pydot-ng graphviz \
     libpq-dev virtualenv ffmpeg npm uwsgi

## Angular builder

    sudo npm install -g @angular/cli

## Node js

    sudo npm install -g n
    sudo n stable

## After clone install nmp and python requirements

    ./bin/install

## Nodejs

    

### For celery purge command

    apt install python-celery-common

## Install database

    sudo apt install postgresql

## Change password, create database

    sudo -u postgres psql
    \password postgres
    ALTER USER postgres PASSWORD '<new_password>';
    create database dating;
    \q

### Create the access from external IP
    
    nano /etc/postgresql/10/main/postgresql.conf

    listen_addresses = '*'  

## Install python requirements

    sudo pip install virtualenv
    virtualenv -p python3 venv
    . ./venv/bin/activate
    pip install -r requirements.txt

# Important!!

Rename /backend/_local.py -> /backend/local.py

Import Test  data

    ./bin/seeddb

## Generate admin interface

    ./bin/gen

## Install js requirements.

    ./bin/npminstall

# Angular commands

## Run angular dev frontend server on 4200 port whith the access to local API server

    ./bin/ngrunfront

## Run angular dev admin server on 4201 port whith the access to local API server

    ./bin/ngrunadmin

## Run angular dev frontend server on 4200 port whith the remote access to the test API server

    ./bin/ngrunfrontr

## Run angular dev admin server on 4201 port whith the remote access to the test API server

    ./bin/ngrunadminr

## Update ssl keys

Copy 

    /etc/letsencrypt/live/archive/ng-dating-test.webmonstr.com/privkey<last number>.pem -> privkey1.pem
    /etc/letsencrypt/live/archive/ng-dating-test.webmonstr.com/fullchain<last number>.pem -> cert1.pem

     - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/neuraldating.com/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/neuraldating.com/privkey.pem
   Your cert will expire on 2020-04-30. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"


# Angular frontend

# Documentation

    npm run docserve

# Linting

    ng lint

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. 



## Fix ng watching on Ubuntu

    sudo sysctl fs.inotify.max_user_watches=524288
    sudo sysctl -p --system


# Links

[Test site](http://neuraldating.com)

[Swagger](http://ng-dating-test.webmonstr.com/swagger)

[Django](http://ng-dating-test.webmonstr.com/admin/doc)

[Sphinx](http://doc-dating-test.webmonstr.com/)

