

extensions = [
    "myst_nb",
    "ablog",
    "sphinx_panels",
    "sphinx.ext.intersphinx",
    # "sphinxcontrib.bibtex",
    "sphinxext.opengraph",
    #"sphinxext.rediraffe",
]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "*import_posts*",
    "**/pandoc_ipynb/inputs/*",
    ".nox/*",
    "README.md",
]


html_extra_path = []


# Panels config
panels_add_bootstrap_css = False

# -- ABlog ---------------------------------------------------

blog_baseurl = "https://chrisholdgraf.com"
blog_title = "Chris Holdgraf"
blog_path = "notes"
blog_post_pattern = "notes/*/*"
blog_feed_fulltext = True
blog_feed_subtitle = "Open communities, open science, communication, and data."
fontawesome_included = True
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

# -- MyST and MyST-NB ---------------------------------------------------

# MyST
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

# MyST-NB
# Don't execute anything by default because many old posts don't execute anymore
# and this slows down build times.
# Instead if I want something to execute, manually set it in the post's metadata.
nb_execution_mode = "off"







