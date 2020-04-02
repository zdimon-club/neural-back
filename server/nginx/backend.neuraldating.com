server {

        client_max_body_size 50m;
        server_name backend.neuraldating.com;

        location / {
                #add_header "Access-Control-Allow-Origin *';
                proxy_set_header        Host $host;
                proxy_set_header        X-Real-IP $remote_addr;
                proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header   X-Forwarded-Host $server_name;
                proxy_set_header   X-Forwarded-Protocol $scheme;
                proxy_pass http://localhost:8085;
        }


}