.. _projects_rdf_generator:

=============
RDF Generator
=============

The RDF Generator is a **Python library** designed to transform structured and unstructured data into **RDF triples**, making them compatible with **Linked Data principles**. It is primarily used in the JudaicaLink project to convert datasets into RDF format for integration into the JudaicaLink **knowledge graph**.

Features of RDF Generator
==========================

- **Support for multiple data sources** (spreadsheets, XML, JSON, CSV, web scraping).
- **Automatic RDF conversion** using predefined mappings.
- **SPARQL update compatibility** for inserting RDF data into triple stores.
- **Integration with Django and external APIs**.
- **Export support for RDF/XML, Turtle, N-Triples, and JSON-LD formats**.

Setting Up the Environment
==========================

1. **Clone the repository**
::

   git clone https://github.com/judaicalink/rdf_generator.git
   cd rdf_generator

2. **Create a virtual environment** (Recommended)
::

   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows

3. **Install dependencies**
::

   pip install -r requirements.txt

Generating RDF Data
===================

To generate RDF data, use the command-line tool or integrate it into a Python script.

Example usage
::

   python rdf_generator.py --input data.csv --output output.rdf --format ttl

Supported formats:

- **RDF/XML**: `--format xml`
- **Turtle (TTL)**: `--format ttl`
- **JSON-LD**: `--format jsonld`
- **N-Triples**: `--format nt`

Integrating with Python
=======================

You can also use the RDF Generator in your Python scripts

.. code-block:: python
    :linenos:

    from rdf_generator import RDFConverter

    converter = RDFConverter(input_file="data.csv", output_format="ttl")
    converter.convert()

    with open("output.ttl", "w") as f:
        f.write(converter.get_rdf())


Defining RDF Mappings
=====================

Mappings define how input data is transformed into RDF triples. Example mapping file (YAML)::

.. code-block:: yaml
    :linenos:

prefixes:
     ex: "http://example.org/"
     foaf: "http://xmlns.com/foaf/0.1/"

    mappings:
        - column: "Name"
        predicate: "foaf:name"
        - column: "Homepage"
        predicate: "foaf:homepage"
        datatype: "xsd:anyURI"

Running with a mapping file
::

   python rdf_generator.py --input data.csv --output output.rdf --mapping mapping.yaml

Validating RDF Output
=====================

Once RDF is generated, validate it to ensure correctness
::

   rapper -i turtle -o ntriples output.ttl

Or using the RDF Generator tool
::

   python rdf_generator.py --validate output.rdf

Loading RDF into a Triple Store
===============================

To load RDF data into **Apache Jena Fuseki**
::

   curl -X POST --data-binary @output.rdf -H "Content-Type: application/rdf+xml" https://data.judaicalink.org/fuseki/ds/data

Alternatively, using SPARQL Update
::

   python rdf_generator.py --upload output.rdf --endpoint https://data.judaicalink.org/update

Troubleshooting & Support
=========================

- **Invalid RDF syntax?** Ensure mappings are correct and validate RDF output.
- **SPARQL endpoint not responding?** Check network connectivity and endpoint availability.
- **Need help?** Contact us at https://labs.judaicalink.org/contact/

---
The RDF Generator streamlines RDF data creation for JudaicaLink and other Linked Data projects. Start transforming your data today! \🚀