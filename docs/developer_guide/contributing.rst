.. _developer_guide_contributing:

===================================
Contributing to JudaicaLink Projects
===================================

Thank you for your interest in contributing to JudaicaLink! This guide provides an overview of how you can contribute to various projects within the JudaicaLink ecosystem, including **Docs, Labs, Site, Pubby, Generators, and RDF-related tools**.

General Contribution Guidelines
===============================

JudaicaLink is an open-source initiative. Contributions can include:

* Reporting and fixing bugs
* Improving documentation
* Adding new features
* Enhancing RDF datasets and linked data
* Optimizing performance

All contributions should follow our coding standards and best practices.

Setting Up Your Development Environment
=======================================

1. Clone the Repository
------------------------
Choose the project you want to contribute to and clone its repository:
::

    # Example for Labs
    git clone https://github.com/judaicalink/judaicalink-labs.git
    cd judaicalink-labs

2. Set Up a Virtual Environment
-------------------------------
*(For Python-based projects like Labs and Pubby)*

::

    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows

3. Install Dependencies
------------------------
::

    pip install -r requirements.txt

For front-end projects like the **JudaicaLink Site**, install dependencies using **Hugo**:
::

    brew install hugo  # On macOS
    sudo apt install hugo  # On Linux

For containerized development using **Docker**:
::

    git clone https://github.com/judaicalink/docker.git
    cd docker
    docker-compose up --build -d

Project-Specific Contributions
==============================

JudaicaLink Docs
----------------

* Update or create `.rst` documentation files in `docs/`.
* Build and preview documentation:

::

    cd docs
    make html  # On macOS/Linux
    make.bat html  # On Windows

* Submit improvements via a pull request.

JudaicaLink Labs
----------------

* Improve search functionality, indexing, and data integration.
* Work on **Django-based** features.
* Run the development server:

::

    python manage.py runserver


JudaicaLink Site
----------------

* Improve UI/UX for the static site.
* Modify `config.toml` and `content/` for new pages.
* Preview site changes:

::

  hugo server

JudaicaLink Pubby
-----------------

* Enhance SPARQL querying and linked data support.
* Improve the Jena Fuseki-based triple store.
* Test Pubby:

::

    python manage.py runserver


JudaicaLink Generators & RDF Tools
----------------------------------

* Improve data ingestion pipelines.
* Enhance RDF transformation scripts.
* Validate RDF outputs with:

::

  rapper -i rdfxml -o turtle data.rdf


Submitting a Pull Request
=========================

1. Fork the repository on GitHub.
2. Create a new feature branch:

::

    git checkout -b feature-new-update

3. Make changes and commit them:

::

    git add .
    git commit -m "Added new feature"

4. Push to your fork:

::

    git push origin feature-new-update

5. Open a pull request on GitHub and describe your changes.

Reporting Issues
================

If you encounter a bug, have a feature request, or need help, open an issue in the relevant GitHub repository:

* **Docs:** `https://github.com/judaicalink/judaicalink-docs/issues <https://github.com/judaicalink/judaicalink-docs/issues>`_
* **Labs:** `https://github.com/judaicalink/judaicalink-labs/issues <https://github.com/judaicalink/judaicalink-labs/issues>`_
* **Site:** `https://github.com/judaicalink/judaicalink-site/issues <https://github.com/judaicalink/judaicalink-site/issues>`_
* **Pubby:** `https://github.com/lod-pubby/pubby-django/issues <https://github.com/lod-pubby/pubby-django/issues>`_
* **Generators:** `https://github.com/judaicalink/judaicalink-generators/issues <https://github.com/judaicalink/judaicalink-generators/issues>`_


Code of Conduct
===============

All contributors are expected to follow the **JudaicaLink Code of Conduct** to ensure a respectful and collaborative environment.

---
Thank you for contributing to JudaicaLink! \🚀

