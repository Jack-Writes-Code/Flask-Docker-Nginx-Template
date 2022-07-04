# Flask-Docker-Template

<br>
<h3>Template for Flask deployed through docker using gunicorn.</h3>
<br>

Edit /app/Dockerfile and uncomment the development option if deploying as a dev.

Default port is 8080 for this project, you can change this in the docker-compose.yml file, the app/Dockerfile, app/main.py & app/wsgi.py

Run using 'docker-compose up -d' in terminal.

<br>
<h3>To deploy using Ubuntu</h3>
<br>

Serving with nginx forward the port in /etc/nginx/sites-available/your_project_name:


```
server {
        listen 80;
        listen [::]:80;
        server_name yourdomain.com;

    location / {
        proxy_pass         "http://0.0.0.0:8080";
        proxy_redirect     off;

        proxy_set_header   Host                 $host;
        proxy_set_header   X-Real-IP            $remote_addr;
        proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto    $scheme;
    }
}
```

<br>

Mirror the file from sites-available

```
sudo ln -s /etc/nginx/sites-available/your/project/name /etc/nginx/sites-enabled
```




<br>

Then run the certbot to add SSL to your domain:
```
https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx
```
