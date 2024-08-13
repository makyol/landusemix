
import os
import sys
sys.path.insert(0, os.path.abspath('../landusemix'))

# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Land Use Mix'
author = 'Mehmet Ali Akyol'
release = '0.1.2'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
