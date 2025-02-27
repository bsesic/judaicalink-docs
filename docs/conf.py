import os
import sys
import datetime
sys.path.insert(0, os.path.abspath(''))
year = datetime.datetime.now().year

# Sphinx project settings
project = 'JudaicaLink Documentation'
author = 'JudaicaLink Team'
version = '0.1'
release = '0.1.0'
copyright = f'{year}, JudaicaLink Team'

# Add language support
language = 'en'  # Default language
locale_dirs = ['locale/']  # Path to translation files
gettext_compact = False  # Keep translation structure

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages"
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.doctest',
    'sphinx_intl'
]

html_theme = "sphinx_rtd_theme"
