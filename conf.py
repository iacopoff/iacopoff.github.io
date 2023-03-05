

extensions = [
    "myst_nb",
    "ablog",
    "sphinx_panels",
    "sphinx_design",
    "sphinx.ext.intersphinx",
    # "sphinxcontrib.bibtex",
    #"sphinxext.opengraph",
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


html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "search_bar_text": "Search this site...",
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
    #"index": ["hello.html"],
    #"about": ["hello.html"],
    #"publications": ["hello.html"],
    #"projects": ["hello.html"],
    #"talks": ["hello.html"],
    "blog": ["ablog/categories.html", "ablog/tagcloud.html", "ablog/archives.html"],
    #"notes/**": ["ablog/postcard.html", "ablog/recentposts.html", "ablog/archives.html"],
}



# -- ABlog ---------------------------------------------------

blog_baseurl = "https://iacopoff.github.io/"
blog_title = "Iacopo"
blog_path = "blog"
blog_post_pattern = "blog/*/*"
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






def setup(app):
    app.add_css_file("custom.css")
