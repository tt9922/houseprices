
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

project = 'Houseprices'
copyright = '2025, Author'
author = 'Author'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ja'

html_theme = 'alabaster'
html_static_path = ['_static']
