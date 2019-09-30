# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path Setup --------------------------------------------------------------

# If extensions (or modules to a document with autodoc) are in another
# directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here:
#
import os
import sys

sys.path.insert(0, os.path.abspath("../exonum"))


# -- Project Information -----------------------------------------------------

project = "Exonum Python light client"
copyright = "2019, The Exonum team"
author = "The Exonum team"

# The full version, including alpha/beta/rc tags:
release = "0.3.0"


# -- General Configuration ---------------------------------------------------

# Add any Sphinx extension module names as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones:
extensions = ["sphinx.ext.napoleon"]

# Add any paths that contain templates relative to this directory:
templates_path = []

# List of patterns, relative to the source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path:
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The suffix(es) of source filenames.
# You can specify multiple suffixes as a list of strings.
#
# `source_suffix = ['.rst', '.md']`:
source_suffix = ".rst"

# The master toctree document:
master_doc = "index"

# The language for the content autogenerated by Sphinx. Refer to the
# documentation for a list of supported languages.
#
# Use this parameter if you do content translation via gettext catalogs.
# Preferably, set "language" from the command line for these cases:
language = "python"

# The name of the Pygments (syntax highlighting) style to use:
pygments_style = None

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::):
add_module_names = False

# -- Options for HTML Output -------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of built-in themes:
#
html_theme = "classic"

# Add any paths that contain custom static files (such as style sheets),
# relative to this directory. They are copied after the built-in static files.
# A file named "default.css" will overwrite the builtin "default.css":
html_static_path = []

# Output file base name for HTML help builder:
htmlhelp_basename = "exonumdoc"

# Napoleon settings:
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
