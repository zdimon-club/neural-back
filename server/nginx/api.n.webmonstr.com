server {
    
    server_name n.api.webmonstr.com
    

    client_max_body_size 20M;

    location / {
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Url-Scheme $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_pass   http://localhost:8881;
    }


}

