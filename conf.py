

extensions = [
    "myst_nb",
    "ablog",
    "sphinx_panels",
    "sphinx_design",
    "sphinx.ext.intersphinx",
    # "sphinxcontrib.bibtex",
    "sphinxext.rediraffe",
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

# HTML 

templates_path = ["_templates"]
html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "search_bar_text": "Search ...",
    "analytics": {"google_analytics_id": "UA-88310237-1"},
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/iacopoff/",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/iacopoff",
            "icon": "fa-brands fa-twitter",
        },
    ],
}


html_title = "Iacopo Ferrario"
html_sidebars = {
        "*": ["sidebar.html"],
        }


rediraffe_redirects = {}


# Update the posts/* section of the rediraffe redirects to find all files
redirect_folders = {
    "posts": "blog",
}

from pathlib import Path

for old, new in redirect_folders.items():
    for newpath in Path(new).rglob("**/*"):
        if newpath.suffix in [".ipynb", ".md"] and "ipynb_checkpoints" not in str(
            newpath
        ):
            oldpath = str(newpath).replace("blog/", "posts/", 1)
            # Skip pandoc because for some reason it's broken
            if "pandoc" not in str(newpath):
                rediraffe_redirects[oldpath] = str(newpath)



# -- ABlog ---------------------------------------------------

blog_baseurl = "https://iacopoff.github.io"
blog_title = "Iacopo's notes"
blog_path = "blog"
blog_post_pattern = "blog/*/*"
blog_feed_subtitle = "Open communities, open science, communication, and data."
fontawesome_included = True
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2
post_show_prev_next = True
blog_feed_fulltext = True

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






def setup(app):
    app.add_css_file("custom.css")
