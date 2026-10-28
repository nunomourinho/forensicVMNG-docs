"""Configuração Sphinx da documentação pública do ForensicVM NextGen."""
import sys
from pathlib import Path

# diretiva {video}, partilhada com a documentação inglesa (docs-en/)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'ext'))

project = 'ForensicVM NextGen'
author = 'Nuno Mourinho e colaboradores'
copyright = '2026, Nuno Mourinho e colaboradores'
language = 'pt_PT'
# versão da documentação (o EPUB3 exige uma)
version = release = '2026.10'

extensions = ['myst_parser', 'forensicvm_sphinx']
myst_enable_extensions = ['colon_fence', 'deflist', 'attrs_inline', 'attrs_block']
myst_heading_anchors = 3
source_suffix = {'.md': 'markdown'}
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_title = 'ForensicVM NextGen — Documentação'
html_static_path = ['_static']
html_css_files = ['css/forensicvm.css']
html_theme_options = {
    'navigation_depth': 3,
    'collapse_navigation': False,
    'style_external_links': True,
}
html_show_sourcelink = False

# PDF (Read the Docs): XeLaTeX por causa dos caracteres Unicode (→, ✗) e A4
latex_engine = 'xelatex'
latex_documents = [('index', 'forensicvm-nextgen.tex', 'ForensicVM NextGen — Documentação', author, 'manual')]
latex_elements = {'papersize': 'a4paper', 'pointsize': '11pt'}
epub_show_urls = 'footnote'
# os exemplos de autoinstall (sem extensão) não entram no EPUB
suppress_warnings = ['epub.unknown_project_files']
