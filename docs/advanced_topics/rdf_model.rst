RDF Model
=========

The RDF Model provides a structured way to represent and manage RDF data within applications. It allows users to define **entities, properties, and relationships** in a structured format that aligns with Linked Data principles.

Features of RDF Model
---------------------

- **Ontology-based data modeling** to maintain semantic consistency.
- **SPARQL query support** for retrieving and manipulating data.
- **Serialization in multiple RDF formats**, including **RDF/XML, Turtle, JSON-LD, and N-Triples**.
- **Integration with external linked data sources** like **Wikidata, DBpedia, and GND**.

Setting Up the Environment
--------------------------

1. **Clone the repository**
::

   git clone https://github.com/judaicalink/rdf_model.git
   cd rdf_model

2. **Create a virtual environment** (Recommended)
::

   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows

3. **Install dependencies**
::

   pip install -r requirements.txt

Defining an RDF Model
---------------------

Define an RDF model using Python classes. Example model::

   from rdflib import Graph, Namespace, URIRef, Literal
   from rdflib.namespace import RDF, FOAF

   g = Graph()
   ex = Namespace("http://example.org/")

   entity = URIRef("http://example.org/person/1")
   g.add((entity, RDF.type, FOAF.Person))
   g.add((entity, FOAF.name, Literal("Moses Mendelssohn")))

   g.serialize("output.ttl", format="turtle")

Querying RDF Data
-----------------

Run SPARQL queries on the RDF model to extract relevant data::

   from rdflib.plugins.sparql import prepareQuery

   query = prepareQuery(
       """
       SELECT ?name WHERE {
           ?person a <http://xmlns.com/foaf/0.1/Person> ;
                   <http://xmlns.com/foaf/0.1/name> ?name .
       }
       """, initNs={"foaf": FOAF})

   for row in g.query(query):
       print(row.name)

Validating RDF Data
-------------------

Ensure RDF data is valid before integration::

   rapper -i turtle -o ntriples output.ttl

Alternatively, use an online RDF validator.

Loading RDF Data into a Triple Store
------------------------------------

To upload RDF data to a **SPARQL endpoint**::

   curl -X POST --data-binary @output.ttl -H "Content-Type: text/turtle" https://data.judaicalink.org/fuseki/ds/data

Troubleshooting & Support
-------------------------

- **SPARQL query not returning results?** Ensure the RDF model is correctly defined.
- **Serialization errors?** Validate the RDF syntax before saving.
- **Need help?** Contact us at https://labs.judaicalink.org/contact/

---------------------------------------------------------------------------------------------------------------------
The RDF Model simplifies Linked Data management, making it easier to structure, query, and integrate semantic data. \🚀

