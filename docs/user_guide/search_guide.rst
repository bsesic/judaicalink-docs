.. _user_guide_search_guide:

============
Search Guide
============

JudaicaLink offers three types of searches:

1. *Knowledge Graph Search*

   * Search for entities such as persons, places, and institutions.

2. *Full-text search in Compact Memory*

   * Search within digitized Jewish newspapers and journals.

3. *Entity Extraction Search*

   * Uses NLP techniques to extract structured data from text.

Example Query:
::

   SELECT ?person WHERE { ?person a jl:Person ; rdfs:label "Moses Mendelssohn". }
