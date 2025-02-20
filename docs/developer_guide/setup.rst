.. _developer_guide_setup:

===========
Setup Guide
===========

This guide provides instructions on how to set up the JudaicaLink environment locally, including *Solr, Redis, Apache Jena Fuseki, and Nginx*  to run the projects efficiently.

System Requirements
-------------------

Ensure your system meets the following requirements:

- *OS:*  Ubuntu 20.04+ / macOS / Windows (WSL recommended for Windows)
- *Python:*  3.8+
- *Docker & Docker Compose:*  Latest version
- *Node.js & npm:*  Latest LTS version (for frontend projects)
- *Git:*  Latest version

Cloning the Repositories
------------------------

Clone the main JudaicaLink projects:

::

   git clone https://github.com/judaicalink/judaicalink-labs.git
   git clone https://github.com/judaicalink/judaicalink-site.git
   git clone https://github.com/lod-pubby/pubby-django.git
   git clone https://github.com/judaicalink/djangordf.git
   git clone https://github.com/judaicalink/rdf_generator.git

Setting Up Python Environment
-----------------------------

Create and activate a virtual environment:

::

   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows

Install dependencies:

::

   pip install -r requirements.txt

Setting Up Solr
---------------

Solr is used for full-text indexing in JudaicaLink Labs.

1. *Download and extract Solr:*

   ::

      wget https://downloads.apache.org/solr/latest/solr-9.0.0.tgz
      tar xzf solr-9.0.0.tgz
      cd solr-9.0.0

2. *Start Solr in standalone mode:*

   ::

      bin/solr start -e cloud -noprompt

3. *Create a core for JudaicaLink:*

   ::

      bin/solr create -c judaicalink

Setting Up Redis
----------------

Redis is used for caching and queuing operations.

1. *Install Redis:*

   ::

      sudo apt update && sudo apt install redis-server

2. *Start Redis:*

   ::

      sudo systemctl start redis
      sudo systemctl enable redis

Setting Up Apache Jena Fuseki
-----------------------------

Apache Jena Fuseki is used as the SPARQL endpoint and RDF triple store.

1. *Download and extract Fuseki:*

   ::

      wget https://downloads.apache.org/jena/binaries/apache-jena-fuseki-4.5.0.tar.gz
      tar -xzf apache-jena-fuseki-4.5.0.tar.gz
      cd apache-jena-fuseki-4.5.0

2. *Start Fuseki server:*

   ::

      ./fuseki-server --update --mem /ds

3. *Load RDF data:*

   ::

      curl -X POST --data-binary @data.rdf -H "Content-Type: application/rdf+xml" http://localhost:3030/ds/data

Setting Up Nginx
----------------

Nginx is used as a reverse proxy to serve the web applications.

1. *Install Nginx:*

   ::

      sudo apt update && sudo apt install nginx

2. *Create an Nginx configuration file:*

   ::

      sudo nano /etc/nginx/sites-available/judaicalink

   Add the following configuration:

   ::

      server {
          listen 80;
          server_name judaicalink.local;

          location / {
              proxy_pass http://127.0.0.1:8000;
              proxy_set_header Host $host;
              proxy_set_header X-Real-IP $remote_addr;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          }
      }

3. *Enable the configuration and restart Nginx:*

   ::

      sudo ln -s /etc/nginx/sites-available/judaicalink /etc/nginx/sites-enabled/
      sudo systemctl restart nginx

Running the Projects
--------------------

To run the projects locally:

1. *Run Django-based projects:*

   ::

      cd judaicalink-labs
      python manage.py runserver

2. *Run Hugo-based site:*

   ::

      cd judaicalink-site
      hugo server

3. *Run Pubby:*

   ::

      cd pubby-django
      python manage.py runserver

Verifying the Setup
-------------------

- *Labs:*  http://127.0.0.1:8000
- *Site:*  http://localhost:1313
- *SPARQL Endpoint:*  http://localhost:3030/ds
- *Solr Admin UI:*  http://localhost:8983/solr
- *Redis Status:*

   ::

      redis-cli ping

Troubleshooting & Support
-------------------------

- *Solr not starting?*  Ensure Java is installed.
- *Fuseki not responding?*  Verify it is running on port * 3030* .
- *Redis connection errors?*  Restart Redis with:

   ::

      sudo systemctl restart redis

- *Need help?*  Contact us at `https://labs.judaicalink.org/contact/`.


---------------------------------------------------------------------------------------------------------
This setup guide ensures a complete local environment for developing and testing JudaicaLink projects. \🚀

