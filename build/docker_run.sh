#!/bin/bash
set -eo pipefail

NAME="ldap-auth"

docker run -d \
  -v /smartops/etc:/var/www/etc \
  -v /smartops/data:/var/www/data \
  -p "8093:8080/tcp" \
  --pids-limit 100 \
  --memory 512m \
  --cpu-shares 512 \
  --security-opt=no-new-privileges \
  --restart=unless-stopped \
  --name="$NAME"-server \
  "$NAME"-server

# Add local CA for Vault
cd /smartops/easy-rsa/easyrsa3/pki/ || exit
tar -cf - ca.crt --mode u=+rwx,g=+rx-w,o=-rw+x --owner 1000 --group root | docker cp - "$NAME"-server:/usr/local/share/ca-certificates/

# Add specific client CA chain
cd /etc/pki/ca-trust/source/anchors/ || exit
tar -cf - autorite_chain.pem --mode u=+rwx,g=+rx-w,o=-rw+x --owner 1000 --group root | docker cp - "$NAME"-server:/usr/local/share/ca-certificates/
docker exec -u 0 "$NAME"-server mv /usr/local/share/ca-certificates/autorite_chain.pem /usr/local/share/ca-certificates/autorite_chain.crt

# Update CA
docker exec -u 0 "$NAME"-server update-ca-certificates