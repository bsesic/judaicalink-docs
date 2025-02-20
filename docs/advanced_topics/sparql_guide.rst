.. _advanced_topics_sparql_guide:

============
SPARQL Guide
============

SPARQL is a query language used to retrieve and manipulate data stored in **RDF format**. JudaicaLink provides a **public SPARQL endpoint** that allows users to query the **JudaicaLink knowledge graph**.

SPARQL Endpoint
---------------

JudaicaLink's SPARQL endpoint is accessible at:

**URL:** https://data.judaicalink.org/sparql.html

You can use this endpoint to run queries directly via a web interface or programmatically using command-line tools or programming languages.

Basic SPARQL Query Structure
----------------------------

A SPARQL query consists of:

- **SELECT Clause**: Specifies the variables to retrieve.
- **WHERE Clause**: Defines the conditions that must be met.
- **LIMIT/OFFSET**: Restricts the number of results.

Example Query
-------------

Retrieve the first 10 persons in the dataset::

    SELECT ?person ?name WHERE {
        ?person a <http://xmlns.com/foaf/0.1/Person> ;
                <http://xmlns.com/foaf/0.1/name> ?name .
    } LIMIT 10

Filtering Results
-----------------

Filter results using conditions like **strings, numbers, or dates**::

    SELECT ?person ?name WHERE {
        ?person a <http://xmlns.com/foaf/0.1/Person> ;
                <http://xmlns.com/foaf/0.1/name> ?name .
        FILTER regex(?name, "Moses", "i")
    }

Sorting and Ordering Results
----------------------------

Use **ORDER BY** to sort results::

    SELECT ?person ?name WHERE {
        ?person a <http://xmlns.com/foaf/0.1/Person> ;
                <http://xmlns.com/foaf/0.1/name> ?name .
    } ORDER BY ?name

Querying with Optional Data
---------------------------

Use **OPTIONAL** to include additional data if available::

    SELECT ?person ?name ?birthdate WHERE {
        ?person a <http://xmlns.com/foaf/0.1/Person> ;
                <http://xmlns.com/foaf/0.1/name> ?name .
        OPTIONAL { ?person <http://dbpedia.org/ontology/birthDate> ?birthdate }
    }

Accessing SPARQL Programmatically
---------------------------------

Use **cURL** to send SPARQL queries::

    curl -G --data-urlencode "query=SELECT * WHERE { ?s ?p ?o } LIMIT 10" \
    -H "Accept: application/sparql-results+json" https://data.judaicalink.org/sparql

Use **Python with rdflib**::

    from rdflib import Graph

    g = Graph()
    g.parse("https://data.judaicalink.org/sparql", format="xml")

    for s, p, o in g:
        print(s, p, o)

Troubleshooting & Support
-------------------------

- **Query returning no results?** Ensure the dataset contains relevant data.
- **SPARQL syntax errors?** Validate your query using a SPARQL validator.
- **Need help?** Contact us at https://labs.judaicalink.org/contact/

---
JudaicaLink’s SPARQL endpoint allows for rich, structured data retrieval. Start exploring now! \🚀

