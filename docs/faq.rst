================================
Frequently Asked Questions (FAQ)
================================

Below are the most common questions about JudaicaLink, its functionality, and how to use it effectively.

General Questions
-----------------

What is JudaicaLink?
~~~~~~~~~~~~~~~~~~~~
JudaicaLink is a Linked Open Data project that provides structured, interconnected knowledge about Jewish history, culture, and scholarship. It integrates data from various sources and makes it available for researchers, historians, and digital humanities projects.

Who maintains JudaicaLink?
~~~~~~~~~~~~~~~~~~~~~~~~~~
JudaicaLink is developed and maintained by *Hochschule Mannheim* in collaboration with *FID Jüdische Studien*, *UB Frankfurt*, and other partners.

Is JudaicaLink free to use?
~~~~~~~~~~~~~~~~~~~~~~~~~~
Yes! JudaicaLink follows the principles of *Open Data, Open Knowledge, and Open Source*. All datasets are freely accessible.

How can I contribute to JudaicaLink?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can contribute by:

* Providing datasets related to Jewish Studies.
* Contributing to RDF data generation.
* Enhancing entity linking and enrichment.
* Developing additional tools using the SPARQL endpoint.

For detailed contribution guidelines, see the `Contributing Guide <contributing>`.

Using JudaicaLink
-----------------

How can I search for information in JudaicaLink?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
JudaicaLink offers multiple search methods:

1. *Knowledge Graph Search* – Explore structured data about persons, places, and institutions.
2. *Full-text search in Compact Memory* – Find relevant excerpts in historical Jewish newspapers.
3. *Entity Extraction Search* – Use NLP-extracted entities from Compact Memory to discover connections.

Where can I find the SPARQL endpoint?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The SPARQL endpoint for querying the knowledge graph is available at:
\🔗 `https://data.judaicalink.org/sparql.html <https://data.judaicalink.org/sparql.html>`_

Can I download datasets from JudaicaLink?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Yes. JudaicaLink provides RDF dumps that can be downloaded and processed locally. Contact the team if you need a specific dataset.

Does JudaicaLink support content negotiation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Yes. You can access data in different formats using content negotiation:

* *HTML*: `https://data.judaicalink.org/data/html/<dataset>/<entity>`
* *JSON-LD*: `https://data.judaicalink.org/data/jsonld/<dataset>/<entity>`
* *RDF/XML*: `https://data.judaicalink.org/data/xml/<dataset>/<entity>`

Technical Questions
-------------------

How is data stored and structured in JudaicaLink?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
JudaicaLink uses *RDF (Resource Description Framework)* to structure data. It is stored in an *Apache Jena Fuseki* triple store and follows the Linked Open Data principles.

What technologies does JudaicaLink use?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- *Backend*: Django (Labs, Pubby)
- *Frontend*: Hugo (Site), Vue.js (planned improvements)
- *Data Storage*: Apache Jena Fuseki (RDF Triple Store)
- *Search*: Elasticsearch, Redis
- *Deployment*: Docker, Nginx

How often is the data updated?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
JudaicaLink updates its data regularly. The frequency depends on external dataset updates and internal processing cycles.

How can I integrate JudaicaLink with my project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Developers can integrate JudaicaLink data by:
* Using the *SPARQL endpoint* for live queries.
* Downloading RDF datasets for local processing.
* Embedding entity URIs into their knowledge bases.

Data and Licensing
------------------

What are the licensing terms for using JudaicaLink data?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
JudaicaLink data is available under open licenses, including *CC BY-SA* and *CC0*, depending on the dataset. Check individual dataset licenses for specifics.

Can I use JudaicaLink data for commercial purposes?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Yes, but you must adhere to the respective dataset license. Some datasets require attribution.

Troubleshooting & Support
-------------------------

I found incorrect data. How can I report it?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you find incorrect or outdated data, please contact the JudaicaLink team via the `Contact Page <https://labs.judaicalink.org/contact/>`_.

My SPARQL query is too slow. What can I do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Try *limiting results* with `LIMIT` and `OFFSET`.
- Optimize queries by *filtering entities early*.
- Use *indexed fields* where possible.

I need a dataset that is not available. Can you add it?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
JudaicaLink is open to dataset suggestions. If you have a dataset you’d like to contribute, reach out to us.

Getting Help
------------

Where can I find more information about JudaicaLink?

- *Documentation*: `https://judaicalink-docs.readthedocs.io/ <https://judaicalink-docs.readthedocs.io/>`_
- *FAQ Updates*: Check `https://web.judaicalink.org/faq/ <https://web.judaicalink.org/faq/>`_ for the latest FAQs.
- *Community & Support*: Contact us at `https://labs.judaicalink.org/contact/ <https://labs.judaicalink.org/contact/>`_.

________________________________________________________
If your question isn't listed here, feel free to contact us or check the JudaicaLink documentation!

