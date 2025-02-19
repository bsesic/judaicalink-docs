Docker Setup and Deployment
===========================

This guide explains how to set up and deploy the JudaicaLink projects using **Docker** and **Docker Compose**. This setup allows you to run all services in isolated containers for easy deployment and management.

System Requirements
-------------------

Ensure your system has the following installed:

- **Docker:** Latest version ([Installation Guide](https://docs.docker.com/get-docker/))
- **Docker Compose:** Latest version ([Installation Guide](https://docs.docker.com/compose/install/))

Cloning the Repository
----------------------

First, clone the main Docker repository for JudaicaLink:

::

    git clone https://github.com/judaicalink/docker.git
    cd docker

Setting Up the Environment
--------------------------

Create an **.env** file to store environment variables:

::

    cp .env.example .env
    nano .env

Modify the variables to match your setup, including database credentials and service configurations.

Running Docker Containers
-------------------------

1. **Build and start containers**:

::

    docker-compose up -d --build

2. **Check running containers**:

::

    docker ps

3. **View logs for troubleshooting**:

::

    docker-compose logs -f

Services Included in Docker Compose
-----------------------------------

The `docker-compose.yml` file includes the following services:

- **Django Application** (JudaicaLink Labs & Pubby)
- **PostgreSQL** (Database backend for Django)
- **Solr** (Full-text search engine)
- **Redis** (Caching layer for Django)
- **Apache Jena Fuseki** (SPARQL endpoint)
- **Nginx** (Reverse proxy for serving the application)

Managing Docker Containers
--------------------------

1. **Stop all running containers**:

::

    docker-compose down

2. **Restart containers**:

::

    docker-compose restart

3. **Rebuild containers after making changes**:

::

    docker-compose up -d --build

Interacting with Services
-------------------------

### Running Database Migrations

To apply Django migrations inside the container:

::

    docker-compose exec web python manage.py migrate

### Collecting Static Files

To collect static files for Django:

::

    docker-compose exec web python manage.py collectstatic --noinput

### Running a Bash Shell inside a Container

To open a shell inside the Django container:

::

    docker-compose exec web bash

### Running Solr in Docker

To access the Solr admin panel:

- URL: `http://localhost:8983/solr`

To create a new Solr core:

::

    docker-compose exec solr solr create -c judaicalink

### Running Apache Jena Fuseki in Docker

To access Fuseki’s web interface:

- URL: `http://localhost:3030`

To load RDF data into Fuseki:

::

    curl -X POST --data-binary @data.rdf -H "Content-Type: application/rdf+xml" http://localhost:3030/ds/data

### Running Nginx in Docker

Nginx serves as a reverse proxy for the Django application. To reload Nginx:

::

    docker-compose exec nginx nginx -s reload

Verifying the Setup
-------------------

After deployment, verify the services are running correctly:

- **Django Application:** http://localhost
- **SPARQL Endpoint (Fuseki):** http://localhost:3030/ds
- **Solr Admin UI:** http://localhost:8983/solr
- **Redis Status:**

::

    docker-compose exec redis redis-cli ping

Troubleshooting & Support
-------------------------

- **Container not starting?** Check logs with `docker-compose logs -f`
- **Database connection errors?** Ensure PostgreSQL is running inside the container
- **Application not accessible?** Verify Nginx settings and restart services
- **Need help?** Contact us at https://labs.judaicalink.org/contact/

---
Using Docker makes it easy to deploy and manage JudaicaLink services. 🚀

