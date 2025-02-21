.. _projects_generators:

======================
JudaicaLink Generators
======================

JudaicaLink Generators is a collection of scripts and tools designed to transform structured and unstructured data into RDF triples for integration into the JudaicaLink knowledge graph. These generators take input from diverse sources such as **websites, spreadsheets, and bibliographic databases** and convert them into **Linked Data**.

Features of JudaicaLink Generators
=================================

- **Automatic RDF generation** from different data formats.
- **Data enrichment** using external authority files like GND and Wikidata.
- **Batch processing** of large datasets.
- **Integration with Django commands** for managing and running generators.

How to Use JudaicaLink Generators
=================================

Setting Up the Environment
--------------------------

1. **Clone the repository**
::

   git clone https://github.com/judaicalink/judaicalink-generators.git
   cd judaicalink-generators

2. **Create a virtual environment** (Recommended)
::

   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows

3. **Install dependencies**
::

   pip install -r requirements.txt

Running a Generator
-------------------

Each generator script is responsible for processing specific datasets. To run a generator
::

   python generators/<generator_script>.py

For example
::
   python generators/yivo_generator.py

Running Django Commands
-----------------------
Some generators are integrated with Django management commands for better orchestration. You can run them as follows:

1. **Navigate to the project directory**
::

   cd judaicalink-generators

2. **Run a specific Django command**::
::

   python manage.py run_generator yivo

Available commands:

- `run_generator <dataset>` – Runs a generator for a specific dataset.
- `list_generators` – Lists all available generators.
- `validate_rdf` – Checks RDF output for errors.

Validating RDF Output
---------------------

Once RDF data is generated, it is essential to validate it before loading it into the triple store. Use the following command
::
   rapper -i rdfxml -o turtle output.rdf

Or validate using the Django management command
::

   python manage.py validate_rdf output.rdf

Loading Data into JudaicaLink
-----------------------------

After validation, RDF data can be loaded into the JudaicaLink SPARQL endpoint
::

   curl -X POST --data-binary @output.rdf -H "Content-Type: application/rdf+xml" https://data.judaicalink.org/fuseki/ds/data

Alternatively, if using Django commands
::

   python manage.py load_rdf output.rdf

Adding a New Generator
======================

To create a new generator:

1. **Create a new Python script in the `generators/` folder**.
2. **Implement data extraction and RDF transformation**.
3. **Use the RDFLib library to generate triples**

.. code-block:: sparql
    :linenos:
    from rdflib import Graph, URIRef, Literal, Namespace

    g = Graph()
    jl = Namespace("https://data.judaicalink.org/ontology/")

    entity = URIRef("https://data.judaicalink.org/resource/example")
    g.add((entity, jl.label, Literal("Example Entity")))

    g.serialize("output.rdf", format="xml")

4. **Test and validate RDF output**.

Troubleshooting & Support
=========================

- **Generator not producing output?** Check the data source and ensure it is accessible.
- **RDF validation errors?** Run `validate_rd`` and fix syntax issues.
- **SPARQL endpoint not updating?** Ensure that the RDF data is correctly loaded.
- **Need help?** Contact us at https://labs.judaicalink.org/contact/

---
JudaicaLink Generators play a crucial role in transforming raw data into Linked Open Data. Follow best practices to ensure high-quality RDF output! \🚀

