.. _user_guide_content_negotiation:

===================
Content Negotiation
===================

JudaicaLink supports *content negotiation*, allowing users to retrieve linked data in multiple formats such as *HTML, JSON-LD, RDF/XML, and Turtle (TTL)*. This enables seamless integration with various linked data tools and applications.

What is Content Negotiation?
----------------------------
Content negotiation is a mechanism that allows clients to request a resource in a specific format by specifying the desired format in the HTTP `Accept` header.

For example:

* A web browser requests *HTML* by default.
* A linked data application may request *JSON-LD or RDF/XML* .

Available Formats
-----------------
JudaicaLink supports the following formats:

+-------------+---------------------------------+-----------------------------------------------------------------+
| Format      | MIME Type                       | Example Request                                                 |
+=============+=================================+=================================================================+
| HTML        | `text/html`                     | https://data.judaicalink.org/data/html/yivo/moses-mendelssohn   |
+-------------+---------------------------------+-----------------------------------------------------------------+
| JSON-LD     | `application/ld+json`           | https://data.judaicalink.org/data/jsonld/yivo/moses-mendelssohn |
+-------------+---------------------------------+-----------------------------------------------------------------+
| RDF/XML     | `application/rdf+xml`           | https://data.judaicalink.org/data/xml/yivo/moses-mendelssohn    |
+-------------+---------------------------------+-----------------------------------------------------------------+
| Turtle      | `text/turtle`                   | https://data.judaicalink.org/data/ttl/yivo/moses-mendelssohn    |
+-------------+---------------------------------+-----------------------------------------------------------------+

How to Request Data in Different Formats
----------------------------------------
There are two primary ways to request a specific format:

1. Using URL Paths
~~~~~~~~~~~~~~~~~~
JudaicaLink allows users to specify the desired format directly in the URL:

* HTML: `https://data.judaicalink.org/data/html/{dataset}/{entity}`
* JSON-LD: `https://data.judaicalink.org/data/jsonld/{dataset}/{entity}`
* RDF/XML: `https://data.judaicalink.org/data/xml/{dataset}/{entity}`
* Turtle: `https://data.judaicalink.org/data/ttl/{dataset}/{entity}`

Example:
::
    curl -L https://data.judaicalink.org/data/jsonld/yivo/moses-mendelssohn


2. Using HTTP Headers
~~~~~~~~~~~~~~~~~~~~~~
Advanced users and applications can specify the desired format using the `Accept` header in HTTP requests:

Example Requests
________________
- *JSON-LD:*
::
  curl -H "Accept: application/ld+json" https://data.judaicalink.org/data/yivo/moses-mendelssohn

- *RDF/XML:*
::
  curl -H "Accept: application/rdf+xml" https://data.judaicalink.org/data/yivo/moses-mendelssohn

- *Turtle:*
::
  curl -H "Accept: text/turtle" https://data.judaicalink.org/data/yivo/moses-mendelssohn

Programmatic Access
-------------------
Applications can integrate JudaicaLink's content negotiation capabilities by dynamically requesting data formats based on their needs.

For example, in *Python*:

.. code-block:: python
    :linenos:

    import requests
    headers = {"Accept": "application/ld+json"}
    response = requests.get("https://data.judaicalink.org/data/yivo/moses-mendelssohn", headers=headers)
    data = response.json()
    print(data)


Best Practices
--------------
* When using *SPARQL endpoints*, consider requesting results in *JSON-LD* for better integration with semantic web tools.
* For *human-readable data*, use the *HTML* format.
* For *machine-readable RDF*, request *Turtle (TTL)* or *RDF/XML* .

Troubleshooting
---------------

1. Receiving the Wrong Format
_____________________________
If you are not getting the expected format:

* Check the *URL path*  (make sure you are using `/jsonld/`, `/xml/`, etc.).
* Ensure the *`Accept` header*  is correctly set.

2. Data Not Found
__________________
If a specific entity does not exist in the requested format, try checking:

* The dataset availability at `https://data.judaicalink.org <https://data.judaicalink.org)>`_.
* Whether the entity exists by first requesting the *HTML*  version.

Next Steps
----------

* Learn more about *SPARQL querying*  in the :ref:`SPARQL Guide <advanced_topics_sparql_guide>`.
* Explore available *datasets*  in :ref:`Datasets Guide <datasets>`.
* If you encounter any issues, check the :ref:`FAQs <faq>` or contact us at `https://labs.judaicalink.org/contact/ <https://labs.judaicalink.org/contact/>`_.

---
Thank you for using JudaicaLink! \🚀

