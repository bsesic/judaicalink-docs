.. _projects_djangordf:

=========
DjangoRDF
=========

DjangoRDF is a **Django-based RDF framework** that enables structured management, querying, and serialization of RDF data within Django applications. It provides tools to integrate **RDF triple stores**, perform **SPARQL queries**, and facilitate **Linked Data publishing**.

Features of DjangoRDF
=====================

* **Django ORM-style RDF models**: Manage RDF data like Django models.
* **SPARQL Query Integration**: Run queries against linked data.
* **RDF Serialization & Content Negotiation**: Supports **JSON-LD, RDF/XML, Turtle, and N-Triples**.
* **Triple Store Compatibility**: Works with **Apache Jena Fuseki, Virtuoso, and GraphDB**.
* **Automatic RDF Data Mapping**: Define models that automatically map to RDF properties.

How to Use DjangoRDF
====================

Setting Up the Environment
--------------------------

1. Clone the repository

::

    git clone https://github.com/judaicalink/djangordf.git
    cd djangordf

2. Create a virtual environment (Recommended)

::

    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows

3. Install dependencies

::

    pip install -r requirements.txt

Configuring DjangoRDF
---------------------

To use DjangoRDF, add it to your Django settings

::

    INSTALLED_APPS = [
        'djangordf',
        ...
    ]

Configure the SPARQL endpoint in `settings.py`

::

   RDF_CONFIG = {
       'SPARQL_ENDPOINT': 'https://data.judaicalink.org/sparql',
       'UPDATE_ENDPOINT': 'https://data.judaicalink.org/update',
       'DATASET': 'judaicalink'
   }

Running Django Commands
-----------------------

DjangoRDF provides management commands to interact with RDF data.

1. **List available RDF models**

::

   python manage.py list_rdf_models

2. **Run a SPARQL query**

::

   python manage.py sparql_query "SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10"

3. **Load RDF data into the triple store**

::

   python manage.py load_rdf path/to/data.rdf

Defining RDF Models
-------------------

DjangoRDF allows you to define RDF models similar to Django ORM models.

Example model definition

.. code-block:: python
    :linenos:

    from djangordf.models import RDFModel
    from rdflib.namespace import FOAF
    from rdflib import URIRef, Literal

    class Person(RDFModel):
        rdf_type = FOAF.Person
        name = Literal()
        homepage = URIRef()


Querying RDF Data
-----------------

You can use Django's QuerySet-like API to retrieve RDF data::

   persons = Person.objects.filter(name="Moses Mendelssohn")
   for person in persons:
       print(person.name, person.homepage)



Troubleshooting & Support
=========================


* **SPARQL queries not returning results?** Check if the endpoint URL is correct.
* **Data not loading?** Validate RDF data before importing.
* **Need help?** Contact us at https://labs.judaicalink.org/contact/


---
DjangoRDF simplifies RDF management in Django applications. Start integrating structured Linked Data today! \🚀

