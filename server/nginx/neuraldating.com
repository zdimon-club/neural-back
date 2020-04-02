server {

	root /home/webmaster/dating-build/dist/front/;

	index index.html index.htm index.nginx-debian.html;
	server_name neuraldating.com;

	location / {
		
		try_files $uri $uri/ /index.html;
	}


}