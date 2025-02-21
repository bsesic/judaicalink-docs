.. _projects_pubby:

=================
JudaicaLink Pubby
=================

JudaicaLink Pubby is a *linked data server* that provides a human-readable and machine-accessible interface for RDF data. It serves as a *SPARQL endpoint* and *Linked Data interface* for querying and browsing JudaicaLink’s structured datasets.

*Features of JudaicaLink Pubby*
===============================

*1. SPARQL Query Interface*
---------------------------

* Users can run *SPARQL queries* to retrieve structured information.
* Supports *Linked Data browsing* by providing entity URIs.
* SPARQL Endpoint: `https://data.judaicalink.org/sparql.html <https://data.judaicalink.org/sparql.html>`_.

*2. RDF Data Exploration*
--------------------------

* Each entity has a *dedicated RDF page*, accessible through content negotiation.
* Supports multiple formats, including *RDF/XML, Turtle, and JSON-LD*.
* Example entity URL: `https://data.judaicalink.org/data/html/yivo/moses-mendelssohn`

*3. Integration with Linked Data Services*
-------------------------------------------

* JudaicaLink Pubby integrates with *Wikidata, GND, VIAF, and DBpedia*.
* Provides structured URIs that link to external data sources.

*How to Use JudaicaLink Pubby*
==============================

*1. Browsing RDF Data*
-----------------------

1. Visit `https://data.judaicalink.org <https://data.judaicalink.org>`_.
2. Search for an entity (e.g., "Moses Mendelssohn").
3. Click on an entity to view its RDF representation.

### *2. Running a SPARQL Query*
1. Go to the *SPARQL Endpoint*: `https://data.judaicalink.org/sparql.html <https://data.judaicalink.org/sparql.html>`_
2. Enter a query, such as:

.. code-block:: sparql
    :linenos:

    SELECT ?person ?name WHERE {
        ?person a jl:Person ;
        rdfs:label ?name .
    } LIMIT 10

3. Execute the query and view results in *JSON, XML, or CSV format*.

*3. Accessing Data in Different Formats*
----------------------------------------
You can retrieve entity data in various formats using *content negotiation*:

* *HTML*: `https://data.judaicalink.org/data/html/yivo/moses-mendelssohn`
* *JSON-LD*: `https://data.judaicalink.org/data/jsonld/yivo/moses-mendelssohn`
* *RDF/XML*: `https://data.judaicalink.org/data/xml/yivo/moses-mendelssohn`
* *Turtle*: `https://data.judaicalink.org/data/ttl/yivo/moses-mendelssohn`

*Technical Overview*
====================

*Backend*
---------

* Built using *Apache Jena Fuseki* for RDF storage and SPARQL processing.
* Uses *Django Pubby* for serving Linked Data.

*Database & Data Sources*
-------------------------

* Stores data in *RDF triple format*.
* Integrates external resources such as *Wikidata, DBpedia, and GND*.

*Contributing to JudaicaLink Pubby*
===================================

*Setting Up a Development Environment*

1. *Clone the repository*

.. code-block:: bash

    git clone https://github.com/lod-pubby/pubby-django.git
    cd pubby-django

2. *Create a virtual environment*

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows

3. *Install dependencies*

.. code-block:: bash

   pip install -r requirements.txt

4. *Run the development server*

.. code-block:: bash

   python manage.py runserver

5. Open http://127.0.0.1:8000/ in your browser.

*Deployment*
------------
* Pubby is deployed using *Docker*.
* RDF data is loaded via *SPARQL Update queries*.

*Troubleshooting & Support*
===========================
* *SPARQL query errors?* Check syntax and dataset availability.
* *RDF data not loading?* Verify dataset ingestion.
* *Need help?* Contact us at `https://labs.judaicalink.org/contact/ <https://labs.judaicalink.org/contact/>`_.

---
JudaicaLink Pubby provides structured Linked Data access to Jewish studies datasets. Explore, query, and integrate JudaicaLink’s knowledge graph today! \🚀

