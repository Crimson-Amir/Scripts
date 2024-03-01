import os
import subprocess

print(os.system('apt install certbot -y'))

server_addres = input('Enter Your Domain: ')

print(os.system(f'certbot certonly --standalone --agree-tos --register-unsafely-without-email -d {server_addres}'))

print(os.system('apt install nginx -y'))

ok_json = '{"success": true}'

site_available = """
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name {server_domain} www.{server_domain};

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl default_server;
    listen [::]:443 ssl default_server;

    server_name {server_domain} www.{server_domain};

    ssl_certificate /etc/letsencrypt/live/{server_domain}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/{server_domain}/privkey.pem;

    location / {
        index ok.json;
        alias /var/www/html/;
    }
}
""".replace('{server_domain}', server_addres)


try:
    with open('/var/www/html/ok.json', 'w') as file:
        file.write(ok_json)

    with open('/etc/nginx/sites-available/simple_json', 'w') as file:
        file.write(site_available)

except Exception as e:
    print(f"* Error In Writhing Files: {e}")
    exit(1)
    
print(os.system('rm /etc/nginx/sites-available/default'))
print(os.system('rm /etc/nginx/sites-enabled/default'))

print(os.system('ln -s /etc/nginx/sites-available/simple_json /etc/nginx/sites-enabled/'))
print(os.system('systemctl restart nginx'))

subprocess.run("bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh)")
