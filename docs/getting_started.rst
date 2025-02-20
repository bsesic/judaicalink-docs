.. _getting_started:

===============
Getting Started
===============

Welcome to JudaicaLink! This guide will help you set up the documentation environment and get started with exploring and contributing to the JudaicaLink project and its sub-projects.

Prerequisites
-------------

Before getting started, ensure you have the following installed:

* Python 3.8 or later
* pip (Python package manager)
* Virtual environment (optional but recommended)
* Git (for cloning the repository)
* Docker (if using containerized deployments)

Setting Up Locally
------------------

Follow these steps to set up the different projects locally:

JudaicaLink Docs
=================

1. *Clone the Repository*

   ```sh
   git clone https://github.com/judaicalink/judaicalink-docs.git
   cd judaicalink-docs
   ```

2. *Create and Activate a Virtual Environment (Recommended)*

   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. *Install Dependencies*

   ```sh
   pip install -r requirements.txt
   ```

4. *Build the Documentation Locally*

   ```sh
   cd docs
   make html  # On Linux/macOS
   # or
   make.bat html  # On Windows
   ```

   The generated HTML files will be located in `docs/_build/html/`. Open `index.html` in a browser to view the documentation.

JudaicaLink Labs
====================

1. *Clone the Repository*

   ```sh
   git clone https://github.com/judaicalink/judaicalink-labs.git
   cd judaicalink-labs
   ```

2. *Install Dependencies*

   ```sh
   pip install -r requirements.txt
   ```

3. *Run the Development Server*

   ```sh
   python manage.py runserver
   ```

JudaicaLink Site
====================

1. *Clone the Repository*

   ```sh
   git clone https://github.com/judaicalink/judaicalink-site.git
   cd judaicalink-site
   ```

2. *Install Hugo* (if not installed already)

   ```sh
   brew install hugo  # On macOS
   sudo apt install hugo  # On Linux
   ```

3. *Build and Serve the Site*

   ```sh
   hugo server
   ```

JudaicaLink Pubby
=====================

1. *Clone the Repository*

   ```sh
   git clone https://github.com/lod-pubby/pubby-django.git
   cd pubby-django
   ```

2. *Install Dependencies*

   ```sh
   pip install -r requirements.txt
   ```

3. *Run the Development Server*

   ```sh
   python manage.py runserver
   ```

Using Docker for Local Deployment
=====================================

For a full-stack deployment of all projects together, use Docker:

1. *Clone the Docker Repository*

   ```sh
   git clone https://github.com/judaicalink/docker.git
   cd docker
   ```

2. *Set Up the Environment*

   ```sh
   cp .env.example .env
   ```

3. *Build and Start Containers*

   ```sh
   docker-compose up --build -d
   ```

Using Read the Docs
-------------------

JudaicaLink documentation is hosted on *Read the Docs*. You can view the latest version online at:

\📖 `JudaicaLink Docs <https://judaicalink-docs.readthedocs.io/>`_

Updating Documentation
----------------------

To contribute updates to the documentation:

1. Make changes to the `.rst` files in the `docs/` directory.
2. Rebuild the documentation using:

   ```sh
   make html
   ```
3. Preview the changes locally by opening `_build/html/index.html` in a browser.
4. Commit and push changes:

   ```sh
   git add .
   git commit -m "Updated documentation"
   git push origin main
   ```

Next Steps
----------

* Read the :ref:`User Guide <user_guide_overview>`_ for more details on using JudaicaLink.
* Check the :ref:`Developer Guide <developer_guide_setup>`_ for information on contributing code.
* Visit the :ref:`FAQ <faq>`_ if you encounter any issues.

