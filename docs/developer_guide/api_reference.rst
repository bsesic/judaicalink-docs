.. _developer_guide_api_reference:

=============
API Reference
=============

The JudaicaLink API provides programmatic access to linked data, including **entities, datasets, and SPARQL queries**. This guide outlines available API endpoints and how to interact with them.

Base API URL: `https://data.judaicalink.org/api/`

Authentication
==============

Currently, the JudaicaLink API is **publicly accessible** and does not require authentication.

Endpoints
---------

### 1. Retrieve Entity Data

**Endpoint:**

::

    GET /entity/{id}

**Description:**
Retrieves structured RDF data about a specific entity.

**Example Request:**

::

    GET https://data.judaicalink.org/api/entity/moses-mendelssohn

**Response (JSON-LD Example):**

::

    {
        "@context": "https://schema.org",
        "@id": "https://data.judaicalink.org/entity/moses-mendelssohn",
        "@type": "Person",
        "name": "Moses Mendelssohn",
        "birthDate": "1729-09-06",
        "deathDate": "1786-01-04"
    }

### 2. Search Entities

**Endpoint:**

::

    GET /search

**Description:**
Performs a full-text search across JudaicaLink’s knowledge graph.

**Parameters:**

- `q` (required) - Search query term
- `limit` (optional, default: 10) - Number of results to return

**Example Request:**

::

    GET https://data.judaicalink.org/api/search?q=Mendelssohn&limit=5

### 3. List Available Datasets

**Endpoint:**

::

    GET /datasets

**Description:**
Returns metadata about all datasets available in JudaicaLink.

**Example Request:**

::

    GET https://data.judaicalink.org/api/datasets

**Example Response:**

::

    [
        {
            "id": "yivo",
            "title": "YIVO Encyclopedia",
            "description": "Jewish history and culture dataset"
        },
        {
            "id": "stolpersteine",
            "title": "Stolpersteine Memorials",
            "description": "Database of Holocaust memorials in Europe"
        }
    ]

### 4. Run SPARQL Queries

**Endpoint:**

::

    GET /sparql

**Description:**
Executes a SPARQL query on the JudaicaLink knowledge graph.

**Parameters:**

- `query` (required) - SPARQL query string

**Example Request:**

::

    GET https://data.judaicalink.org/api/sparql?query=SELECT+%3Fperson+%3Fname+WHERE+%7B+%3Fperson+a+foaf%3APerson+%3B+foaf%3Aname+%3Fname+%7D+LIMIT+10

**Response Format:**
- JSON (`Accept: application/json`)
- XML (`Accept: application/xml`)

Error Handling
--------------

The API returns standard HTTP status codes:

- `200 OK` - Successful request
- `400 Bad Request` - Invalid parameters
- `404 Not Found` - Resource does not exist
- `500 Internal Server Error` - Server-side issue

Usage Limits & Best Practices
-----------------------------

- **Rate Limits**: The API enforces request limits to prevent abuse. If you encounter a `429 Too Many Requests` response, reduce the request frequency.
- **Efficient Queries**: Use filters and `LIMIT` clauses in SPARQL queries to improve response times.
- **Data Caching**: Cache frequently accessed results to reduce load on the API.

Support
-------

For assistance, contact: [https://labs.judaicalink.org/contact/](https://labs.judaicalink.org/contact/)

---
The JudaicaLink API provides structured, linked data for Jewish studies. Explore the datasets and integrate them into your projects! \🚀

