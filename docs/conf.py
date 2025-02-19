import os
import sys
sys.path.insert(0, os.path.abspath('..'))

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
