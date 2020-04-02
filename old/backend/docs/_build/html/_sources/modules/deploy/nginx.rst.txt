Nginx settings
===============


.. code::

    server {

            client_max_body_size 50m;
            server_name ng-dating-test.webmonstr.com;

            location / {
                    #add_header "Access-Control-Allow-Origin *';
                    proxy_set_header        Host $host;
                    proxy_set_header        X-Real-IP $remote_addr;
                    proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
                    proxy_set_header   X-Forwarded-Host $server_name;
                    proxy_set_header   X-Forwarded-Protocol $scheme;
                    proxy_pass http://localhost:8000;
            }



        listen 443 ssl; # managed by Certbot
        ssl_certificate /etc/letsencrypt/live/ng-dating-test.webmonstr.com/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/ng-dating-test.webmonstr.com/privkey.pem; # managed by Certbot
        include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

    }



