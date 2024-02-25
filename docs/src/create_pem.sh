openssl req -x509 -newkey rsa:4096 -sha256 -days 1000 -nodes \
	-keyout server_first_key.pem -out server_first_cert.pem
