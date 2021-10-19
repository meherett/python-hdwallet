# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
import datetime

from hdwallet import (
    __version__, __author__
)

sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(1, os.path.abspath("./extensions"))


# -- Project information -----------------------------------------------------

project = "HDWallet"
copyright = f"{datetime.datetime.now().year}, {__author__}"
author = __author__

# The full version, including alpha/beta/rc tags
release = __version__

# The master toctree document.
master_doc = "toctree"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_click.ext"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"
# Product logo name
# html_logo = "static/png/hdwallet.png"
# Theme options
html_theme_options = {
    # "canonical_url": "",
    # "analytics_id": "UA-XXXXXXX-1",  #  Provided by Google in your dashboard
    "logo_only": False,
    "display_version": True,
    # "prev_next_buttons_location": "bottom",
    # "style_external_links": False,
    # "vcs_pageview_mode": "",
    # "style_nav_header_background": "white",
    # Toc options
    # "collapse_navigation": True,
    # "sticky_navigation": True,
    # "navigation_depth": 4,
    # "includehidden": True,
    # "titles_only": False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["static", "static/css", "static/gif"]

# Autodoc member order
autodoc_member_order = "bysource"


# Sphinx docs setup.
def setup(sphinx):
    sphinx.add_css_file("css/hdwallet.css")
