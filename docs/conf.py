"""Configuração Sphinx da documentação pública do ForensicVM NextGen."""
import json
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import Directive, directives

project = 'ForensicVM NextGen'
author = 'Nuno Mourinho e colaboradores'
copyright = '2026, Nuno Mourinho e colaboradores'
language = 'pt_PT'

extensions = ['myst_parser']
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

VIDEOS = Path(__file__).parent / '_data' / 'videos.json'


class VideoDirective(Directive):
    """``{video} <id>`` — incorpora o vídeo do YouTube com esse id da série.

    Os IDs do YouTube vêm de ``_data/videos.json``, escrito pelo script de upload.
    Enquanto um vídeo não tiver ID, mostra uma nota em vez do leitor.
    """

    required_arguments = 1
    option_spec = {'titulo': directives.unchanged}

    def run(self):
        vid = self.arguments[0]
        # reconstruir a página quando o videos.json mudar
        self.state.document.settings.env.note_dependency(str(VIDEOS))
        info = json.loads(VIDEOS.read_text(encoding='utf-8')).get(vid, {})
        yt = info.get('youtube')
        if not yt:
            nota = nodes.note()
            nota += nodes.paragraph(text='Vídeo em breve: esta página vai incluir o vídeo de demonstração correspondente.')
            return [nota]
        titulo = self.options.get('titulo', info.get('titulo', vid))
        html = (
            '<div class="fvm-video">'
            f'<iframe src="https://www.youtube-nocookie.com/embed/{yt}" title="{titulo}" '
            'loading="lazy" referrerpolicy="strict-origin-when-cross-origin" '
            'allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" '
            'allowfullscreen></iframe></div>'
        )
        return [nodes.raw('', html, format='html')]


def setup(app):
    app.add_directive('video', VideoDirective)
    app.add_config_value('fvm_videos', str(VIDEOS), 'env')
    return {'parallel_read_safe': True}
