import os
import sys
sys.path.insert(0, os.path.abspath(''))

# Sphinx project settings
project = 'JudaicaLink Documentation'
author = 'JudaicaLink Team'
version = '0.1'
release = '0.1.0'


# Add language support
language = 'en'  # Default language
locale_dirs = ['locale/']  # Path to translation files
gettext_compact = False  # Keep translation structure

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages"
]

html_theme = "sphinx_rtd_theme"
