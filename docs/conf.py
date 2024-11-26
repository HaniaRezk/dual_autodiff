# docs/conf.py
# Configuration file for the Sphinx documentation builder.
nbsphinx_kernel_name = 'python3'
import os
import sys
sys.path.insert(0, os.path.abspath('../'))
#sys.path.insert(0, os.path.abspath('../dual_autodiff'))

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'Automatic differentiation using dual numbers package'
author = 'Hania RezK'

# The full version, including alpha/beta/rc tags
release = 'beta'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'nbsphinx',
	'sphinx.ext.mathjax',
	'sphinx_rtd_theme',
    'sphinx_gallery.load_style',  # load CSS for gallery (needs SG >= 0.6)
    'sphinx.ext.githubpages',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'tutorial_notebooks/tutorial*/*_empty.ipynb']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
master_doc = 'index'

highlight_language = 'python3'

nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]
# pygments_style = 'sphinx'


# Disable section numbering
secnumber_suffix = ''  # No suffix means no section numbers
# numfig = False  # Disable figure/table numbering if you don't need them

# Add GitHub repository settings
html_theme_options = {
    'repository_url': 'https://github.com/HaniaRezk/',
}
autodoc_default_flags = ['members', 'undoc-members']
autodoc_default_options = {
    'members': True,         # Include all class members
    'special-members': '__str__,__add__,__iadd__,__radd__,__sub__,__isub__,__rsub__,__mul__,__imul__,_rmul__,__eq__,__ne__,__truediv__,__itruediv__,__rtruediv__,__pow__,__ipow__,__neg__,__eq__,__mod__,__imod__,__rmod__,__floordiv__,__ifloordiv__,__rfloordiv__,',  # Add specific special methods you want documented
    'undoc-members': True,   # Include members without docstrings
    'show-inheritance': True # Show class inheritance hierarchy
}

