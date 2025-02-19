Introduction to JudaicaLink
===========================

## What is JudaicaLink?

JudaicaLink is a Linked Open Data project that provides structured, interconnected knowledge about Jewish history, culture, and scholarship. The goal is to make Jewish studies data easily accessible, searchable, and reusable for researchers, historians, librarians, and the broader academic community.

By integrating various datasets, JudaicaLink connects existing digital archives, authority files, and bibliographic resources into a **knowledge graph**, enabling more efficient exploration of Jewish sources.

## Project Goals and Functions

JudaicaLink serves as a **centralized hub** for structured Jewish studies data, offering:

- **Knowledge Graph**: A linked data framework connecting Jewish historical, biographical, and bibliographical datasets.
- **Entity-Based Search**: Users can search for people, places, events, and publications through a semantically enriched database.
- **Integration with Other Projects**: JudaicaLink integrates with established databases such as **GND, Wikidata, DBpedia, VIAF, and Geonames**.
- **Data Enrichment**: It enhances existing datasets by linking them with external sources and extracting meaningful relationships between entities.
- **Open Access and Reuse**: All data is **openly available** under principles of Linked Open Data (LOD), making it usable by other institutions and projects.

## Project Partners

JudaicaLink is developed and maintained in collaboration with several institutions and projects, including:

- **Hochschule Mannheim** (Mannheim University of Applied Sciences)
- **University Library Frankfurt** (UB Frankfurt)
- **FID Jüdische Studien** (Specialized Information Service for Jewish Studies)
- **Deutsche Nationalbibliothek (DNB)**
- **Europeana** (A European digital cultural heritage initiative)
- **National Library of Israel (NLI)**
- **DM2E (Digitised Manuscripts to Europeana)**
- **GND (Gemeinsame Normdatei)**
- **Wikidata and Wikipedia**

## JudaicaLink Components

JudaicaLink consists of multiple sub-projects that work together to support the knowledge graph and its applications:

### **1. JudaicaLink Labs**
JudaicaLink Labs is the **core application** that powers the search and entity exploration interface. It allows users to explore Jewish-related datasets through **SPARQL queries, entity linking, and structured search**.

- Built using **Django**
- Provides a **searchable knowledge graph**
- Supports **Natural Language Processing (NLP)** for entity recognition

🔗 **Labs URL**: [https://labs.judaicalink.org](https://labs.judaicalink.org)

### **2. JudaicaLink Site**
The JudaicaLink Site is the **public-facing static website** providing background information, project news, and dataset overviews. It is built using **Hugo** and integrates dynamically with the knowledge graph.

🔗 **Site URL**: [https://www.judaicalink.org](https://www.judaicalink.org)

### **3. JudaicaLink Pubby**
JudaicaLink Pubby provides a **SPARQL endpoint** and a **Linked Data interface** for accessing and querying RDF data.

- Powered by **Apache Jena Fuseki**
- Provides **triple-store access** for external applications

🔗 **SPARQL Endpoint**: [https://data.judaicalink.org/sparql.html](https://data.judaicalink.org/sparql.html)

### **4. JudaicaLink Generators**
This project contains **data ingestion scripts** that transform external data sources into **RDF triples**, making them usable in JudaicaLink.

🔗 **GitHub Repo**: [https://github.com/judaicalink/judaicalink-generators](https://github.com/judaicalink/judaicalink-generators)

### **5. RDF Generator**
A library for generating RDF files from structured and unstructured data sources, such as websites, spreadsheets, and full-text documents.

🔗 **GitHub Repo**: [https://github.com/judaicalink/rdf_generator](https://github.com/judaicalink/rdf_generator)

### **6. JudaicaLink Loader**
A script that loads datasets into the triple store. It processes RDF dumps, enriches them with metadata, and uploads them to Fuseki.

🔗 **GitHub Repo**: [https://github.com/judaicalink/judaicalink-loader](https://github.com/judaicalink/judaicalink-loader)

## How JudaicaLink Works

JudaicaLink aggregates, processes, and serves structured Jewish studies data. The main workflow involves:

1. **Data Collection**: Extracting datasets from archives, digital libraries, and authority files.
2. **Data Transformation**: Converting collected data into RDF format using the **JudaicaLink RDF Generator**.
3. **Data Enrichment**: Linking entities across different sources and connecting them to **external databases** (e.g., GND, Wikidata, VIAF).
4. **Data Storage**: Storing RDF data in **Apache Jena Fuseki** (triple store) for efficient querying.
5. **Public Access**: Making the data available via:
   - **SPARQL Endpoint** for custom queries
   - **JudaicaLink Labs** for easy entity search
   - **JudaicaLink Site** for human-readable overviews

## How to Use JudaicaLink

### **For Researchers and Historians**
- **Search for Jewish figures, places, and events** using the Labs interface.
- **Access structured datasets** to support academic research.
- **Run SPARQL queries** to extract complex relationships and insights.

### **For Developers and Data Scientists**
- **Integrate JudaicaLink data** into external applications via **SPARQL**.
- **Contribute to RDF generation scripts** and help expand the knowledge graph.
- **Develop new visualizations and analysis tools** based on the dataset.

### **For Institutions and Digital Libraries**
- **Link existing digital collections** to JudaicaLink’s structured data.
- **Share bibliographic and archival metadata** using the RDF format.
- **Collaborate on data enrichment efforts** to enhance Jewish studies resources.

## Conclusion

JudaicaLink is an open, collaborative project that enables **structured access to Jewish studies data**. By connecting datasets, enriching metadata, and providing search and query tools, it serves as a valuable **resource for academia, libraries, and digital humanities projects**.

🔗 **Start Exploring**: [https://www.judaicalink.org](https://www.judaicalink.org)

