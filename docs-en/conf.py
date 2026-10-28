"""Sphinx configuration for the public ForensicVM NextGen documentation (English, en-GB)."""
import sys
from pathlib import Path

# {video} directive, shared with the Portuguese documentation (docs/)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'ext'))

project = 'ForensicVM NextGen'
author = 'Nuno Mourinho and contributors'
copyright = '2026, Nuno Mourinho and contributors'
language = 'en_GB'
# documentation version (EPUB3 requires one)
version = release = '2026.10'

extensions = ['myst_parser', 'forensicvm_sphinx']
myst_enable_extensions = ['colon_fence', 'deflist', 'attrs_inline', 'attrs_block']
myst_heading_anchors = 3
source_suffix = {'.md': 'markdown'}
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_title = 'ForensicVM NextGen — Documentation'
# the stylesheet is shared with the Portuguese tree
html_static_path = ['_static', '../docs/_static/css']
html_css_files = ['forensicvm.css']
html_theme_options = {
    'navigation_depth': 3,
    'collapse_navigation': False,
    'style_external_links': True,
}
html_show_sourcelink = False

# PDF (Read the Docs): XeLaTeX for the Unicode characters (→, ✗) and A4
latex_engine = 'xelatex'
latex_documents = [('index', 'forensicvm-nextgen.tex', 'ForensicVM NextGen — Documentation', author, 'manual')]
latex_elements = {'papersize': 'a4paper', 'pointsize': '11pt'}
epub_show_urls = 'footnote'
# the autoinstall examples (no extension) are not part of the EPUB
suppress_warnings = ['epub.unknown_project_files']
