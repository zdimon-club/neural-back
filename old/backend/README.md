# Deploy

     sudo apt-get install python3 python-dev python3-dev \
     build-essential libssl-dev libffi-dev \
     libxml2-dev libxslt1-dev zlib1g-dev \
     python-pip

    sudo apt install python-pydot python-pydot-ng graphviz libpq-dev

## Install requirements

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

## Run dev Angular server on 4201 port

    ./bin/npminstall
    ./bin/ngrun

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


# Links

[Test site](http://dating-test.webmonstr.com)

[Swagger](http://ng-dating-test.webmonstr.com/swagger)

[Django](http://ng-dating-test.webmonstr.com/admin/doc)

[Sphinx](http://doc-dating-test.webmonstr.com/)
