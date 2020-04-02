server {

	root /home/webmaster/dating-build/dist/admin/;

	index index.html index.htm index.nginx-debian.html;
	server_name admin.neuraldating.com;

	location / {
		
		try_files $uri $uri/ /index.html;
	}


}