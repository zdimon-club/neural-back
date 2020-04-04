upstream front-app {
    server localhost:4000;
}


server {
    
    server_name n.webmonstr.com
    

    client_max_body_size 20M;

    location / {
        try_files $uri @proxy_to_app;
    }

    

    location @proxy_to_ws {
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_redirect off;

        proxy_pass   http://app;
    }

    location @proxy_to_app {
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Url-Scheme $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;

        proxy_pass   http://front-app;
    }

}


#
#server {
#	listen 80;
#	listen [::]:80;
#
#	server_name example.com;
#
#	root /var/www/example.com;
#	index index.html;
#
#	location / {
#		try_files $uri $uri/ =404;
#	}
#}
