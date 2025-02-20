.. _projects_labs:

================
JudaicaLink Labs
================

JudaicaLink Labs is the *main web interface* for searching, exploring, and interacting with the JudaicaLink *knowledge graph*. It provides an easy-to-use interface for users to query and browse structured data about Jewish history, culture, and scholarship.

*Features of JudaicaLink Labs*
==============================

*1. Entity Search*
------------------
* Users can search for *persons, places, institutions, and texts*.
* Results display structured RDF data enriched with external links (e.g., *GND, Wikidata, DBpedia*).

*2. Compact Memory Full-Text Search*
------------------------------------
* Search within historical Jewish newspapers and periodicals.
* Indexed texts include metadata and direct links to *Compact Memory* digital archives.

*3. Compact Memory Entity Extraction*
--------------------------------------
* Extracted *named entities* (people, places, organizations) from digitized texts.
* Helps users find references to historical figures and events.

*4. SPARQL Query Interface*
---------------------------
* Advanced users can write *SPARQL queries* to access structured data.
* SPARQL endpoint: `https://data.judaicalink.org/sparql.html <https://data.judaicalink.org/sparql.html>`_.

*How to Use JudaicaLink Labs*
=============================

*Searching for Entities*
------------------------
1. Visit `https://labs.judaicalink.org <https://labs.judaicalink.org>`_.
2. Use the *search bar* to enter a term (e.g., "Moses Mendelssohn").
3. Browse entity pages containing structured data and external references.

*Running a SPARQL Query*
------------------------
1. Go to *SPARQL Endpoint*: `https://data.judaicalink.org/sparql.html <https://data.judaicalink.org/sparql.html>`_.
2. Enter a query, such as:

.. code-block:: sparql
    :linenos:

    SELECT ?person ?name WHERE {
       ?person a jl:Person ;
               rdfs:label ?name .
    } LIMIT 10

3. Execute the query and view results in *JSON, XML, or CSV format*.

*Exploring Compact Memory Data*
-------------------------------

1. Select *"Compact Memory Search"* on the search page.
2. Enter a keyword (e.g., "Zionism").
3. View search results with text snippets and source links.

*Technical Overview*
====================

*Backend*
---------

* Built using *Django (Python)*.
* Uses *SOLR* for optimized search indexing.
* Relies on *Apache Jena Fuseki* for SPARQL query processing.

*Frontend*
----------

* Developed with *Bootstrap and jQuery*.
* Plans to migrate to *Vue.js* for better interactivity.

*Database & Data Sources*
-------------------------
* RDF data stored in *Apache Jena Fuseki*.
* Data sources include *Compact Memory, YIVO, GND, and Wikidata*.


*Contributing to JudaicaLink Labs*
==================================

*Setting Up a Development Environment*
--------------------------------------

1. *Clone the repository*

.. code-block:: bash

   git clone https://github.com/judaicalink/judaicalink-labs.git
   cd judaicalink-labs


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


5. Open *http://127.0.0.1:8000/* in your browser.

*Troubleshooting & Support*
===========================
* *Error accessing data?* Ensure the *SPARQL endpoint is online*.
* *Search not returning results?* Check if the dataset is indexed.
* *Need help?* Contact us at `https://labs.judaicalink.org/contact/ <https://labs.judaicalink.org/contact/>`_.

---
JudaicaLink Labs is an evolving platform—new features and datasets are regularly added. Stay updated with the latest changes on `https://www.judaicalink.org/news/ <https://www.judaicalink.org/news/>`_.

