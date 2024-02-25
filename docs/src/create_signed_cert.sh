# create CA key and cert simultaneously
openssl req -x509 -newkey RSA -nodes -keyout CA.key -days 10 -out CA.pem -reqexts \
	v3_ca -subj "/C=CA/ST=ON/L=Toronto/O=Third Bit/OU=x509"

# create server key and cert
openssl req -new -newkey RSA -nodes -keyout server.key -out server.csr -batch \
	-reqexts v3_req -subj "/CN=localhost"

# sign server CSR with CA key
openssl x509 -req -days 10 -in server.csr -CAkey CA.key -CA CA.pem -CAcreateserial \
	-out server.pem -extfile extfile.txt
echo "certificates created"
