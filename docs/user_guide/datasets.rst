.. _datasets:

Datasets in JudaicaLink
=======================

JudaicaLink provides structured datasets that integrate Jewish studies sources into a Linked Open Data (LOD) knowledge graph. These datasets are accessible via SPARQL queries, downloadable RDF dumps, and through the JudaicaLink API.

Available Datasets
==================
The following datasets are included in JudaicaLink:

1. YIVO Encyclopedia
--------------------

* Description: Biographical and historical entries from the YIVO Institute for Jewish Research.
* Entities: Persons, places, and organizations.
* Data Access:

  * SPARQL: Query at `https://data.judaicalink.org/sparql.html <https://data.judaicalink.org/sparql.html>`_
  * Entity Pages: `https://data.judaicalink.org/data/html/yivo/ <https://data.judaicalink.org/data/html/yivo/>`_

2. Stolpersteine in Mainz
-------------------------

* Description: Data on commemorative stones dedicated to Holocaust victims.
* Entities: Persons and memorial sites.
* Data Access:

  * SPARQL: Query dataset under `stolpersteine`
  * Entity Pages: `https://data.judaicalink.org/data/html/stolpersteine/ <https://data.judaicalink.org/data/html/stolpersteine/>`_

3. Biographisches Handbuch der Rabbiner
---------------------------------------

* Description: Biographical records of Jewish rabbis from various historical periods.
* Entities: Persons, institutions, and related documents.
* Data Access:

  * RDF: `https://data.judaicalink.org/dumps/rabbiner.rdf`
  * SPARQL queries available for detailed searches.

4. Footprints * Jewish Books through Time and Place
-------------------------------------------------

* Description: A dataset tracing the movement of Jewish books across different regions and owners.
* Entities: Books, authors, owners, locations.
* Data Access:

  * SPARQL: Query at `footprints` dataset.
  * JSON-LD Access: `https://data.judaicalink.org/data/jsonld/footprints/`

5. Compact Memory (CM) Indexed Entities
---------------------------------------

* Description: Extracted named entities (persons, locations, topics) from historical Jewish periodicals.
* Entities: Persons, places, organizations, topics.
* Data Access:

  * SPARQL Query Example:

    ``sparql
    SELECT ?entity ?label WHERE {
      ?entity a jl:Person ;
              rdfs:label ?label .
    } LIMIT 10
    ``

  * Content Negotiation: Available in RDF/XML, JSON-LD, and Turtle.


Using the Datasets
==================

1. Querying Data with SPARQL
----------------------------

Users can run SPARQL queries against the JudaicaLink *SPARQL Endpoint* :

* *Endpoint URL* : `https://data.judaicalink.org/sparql.html <https://data.judaicalink.org/sparql.html>`_
* *Example Query*  (Retrieve all persons in the dataset):

  ``sparql
  SELECT ?person ?name WHERE {
    ?person a jl:Person ;
            rdfs:label ?name .
  } LIMIT 100
  ``

2. Downloading RDF Dumps
------------------------

Users can download full dataset RDF dumps for offline use:
* *Download URL* : `https://data.judaicalink.org/dumps/ <https://data.judaicalink.org/dumps/>`_
* *Example:*  Download `yivo.rdf`

  ``sh
  wget https://data.judaicalink.org/dumps/yivo.rdf
  ``

3. Accessing Data via Content Negotiation
-----------------------------------------

JudaicaLink supports content negotiation, allowing users to request data in different formats.
* *Formats available:*  HTML, JSON-LD, RDF/XML, Turtle.
* *Example Requests:*
    * JSON-LD: `https://data.judaicalink.org/data/jsonld/yivo/moses-mendelssohn`
    * RDF/XML: `https://data.judaicalink.org/data/xml/yivo/moses-mendelssohn`

4. Using the JudaicaLink API
----------------------------

For automated access and data retrieval:
* *Base API URL* : `https://data.judaicalink.org/api/`
* *Example API Query (Get data for an entity):*

    ``sh
    curl -H "Accept: application/json" https://data.judaicalink.org/data/jsonld/yivo/moses-mendelssohn
    ``

Next Steps
==========

* Learn how to refine your *SPARQL queries*  in the :ref:`SPARQL Guide <advanced_topics_sparql_guide>`.
* Explore the *Entity Pages*  to browse individual datasets.
* If you need help, check the :ref:`FAQs <faq>` or contact us at `https://labs.judaicalink.org/contact/ <https://labs.judaicalink.org/contact/>`_.