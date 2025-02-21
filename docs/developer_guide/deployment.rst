.. _developer_guide_deployment:

================
Deployment Guide
================

This guide provides instructions for deploying the JudaicaLink projects in a production environment, including **Django-based applications, Solr, Redis, Apache Jena Fuseki, and Nginx** .

System Requirements
===================

Ensure your system meets the following requirements:

* **OS:**  Ubuntu 22.04 LTS (recommended)
* **Python:**  3.8+
* **Docker & Docker Compose:**  Latest version
* **Nginx:**  Latest version
* **PostgreSQL:*  14+
* **Solr:**  9+
* **Redis:**  6+
* **Apache Jena Fuseki:**  4.5+

Setting Up the Server
=====================

Update the system
_________________
::

    sudo apt update && sudo apt upgrade -y
    sudo apt install -y git curl wget unzip build-essential

Create a new user for deployment
_________________________________

::

    sudo adduser deploy
    sudo usermod -aG sudo deploy
    su - deploy

Setting Up PostgreSQL
=====================

1. Install PostgreSQL
_____________________

::

    sudo apt install -y postgresql postgresql-contrib

2. Create a database and user
_____________________________

::

    sudo -u postgres psql
    CREATE DATABASE judaicalink;
    CREATE USER judaicauser WITH ENCRYPTED PASSWORD 'securepassword';
    GRANT ALL PRIVILEGES ON DATABASE judaicalink TO judaicauser;
    \q

Setting Up Python Environment
=============================

1. Install Python dependencies
______________________________
::

    sudo apt install -y python3-pip python3-venv
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt


Setting Up Solr
===============

1. Install Solr
_______________

::

    wget https://downloads.apache.org/solr/latest/solr-9.0.0.tgz
    tar xzf solr-9.0.0.tgz
    sudo bash solr-9.0.0/bin/install_solr_service.sh solr-9.0.0.tgz

2. Start Solr and create core
_____________________________

::

    sudo systemctl start solr
    sudo -u solr solr create -c judaicalink

Setting Up Redis
================

::

    sudo apt install -y redis-server
    sudo systemctl enable redis
    sudo systemctl start redis

Setting Up Apache Jena Fuseki
==============================

1. Download and Install Fuseki
______________________________

::

    wget https://downloads.apache.org/jena/binaries/apache-jena-fuseki-4.5.0.tar.gz
    tar -xzf apache-jena-fuseki-4.5.0.tar.gz
    cd apache-jena-fuseki-4.5.0

2. Start Fuseki server
______________________

::

    ./fuseki-server --update --mem /ds &

3. Load RDF data
________________

::

    curl -X POST --data-binary @data.rdf -H "Content-Type: application/rdf+xml" http://localhost:3030/ds/data

Setting Up Nginx
================

1. Install Nginx
________________

::

    sudo apt install -y nginx

2. Configure Nginx for JudaicaLink
__________________________________

::

    sudo nano /etc/nginx/sites-available/judaicalink

Add the following configuration:

::

    server {
        listen 80;
        server_name judaicalink.org;

        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }

3. Enable the Nginx configuration
_________________________________

::

    sudo ln -s /etc/nginx/sites-available/judaicalink /etc/nginx/sites-enabled/
    sudo systemctl restart nginx

Deploying the Django Application
================================

1. Set up environment variables
_______________________________

::

    export DJANGO_SETTINGS_MODULE=judaicalink.settings.production
    export DATABASE_URL=postgres://judaicauser:securepassword@localhost/judaicalink

2. Run migrations and collect static files
__________________________________________

::

    python manage.py migrate
    python manage.py collectstatic --noinput

3. Start the Gunicorn service
_____________________________

::

    pip install gunicorn
    gunicorn --workers 3 --bind unix:/tmp/gunicorn.sock judaicalink.wsgi:application &

Automating Deployment with Docker
=================================

For easier deployment, use **Docker Compose**.

1. Install Docker and Docker Compose
____________________________________

::

    sudo apt install -y docker.io
    sudo curl -L "https://github.com/docker/compose/releases/download/latest/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose

2. Run Docker Compose
_____________________

::

    docker-compose up -d --build

Verifying the Deployment
------------------------

Check that all services are running correctly:

- **Django Application:**  http://127.0.0.1:8000
- **Nginx:**  http://localhost
- **SPARQL Endpoint:**  http://localhost:3030/ds
- **Solr Admin UI:**  http://localhost:8983/solr
- **Redis Status:**

::

    redis-cli ping

Troubleshooting & Support
=========================

* **Database connection errors?**  Ensure PostgreSQL is running and credentials are correct.
* **Nginx not serving requests?**  Check logs with:

::

    sudo journalctl -u nginx --no-pager

* **Gunicorn process stopped?**  Restart it:

::

    pkill gunicorn && gunicorn --workers 3 --bind unix:/tmp/gunicorn.sock judaicalink.wsgi:application &

* **Need help?**  Contact us at https://labs.judaicalink.org/contact/

---
This guide ensures a robust and scalable production deployment of JudaicaLink. \🚀

