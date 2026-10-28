"""Extensão Sphinx partilhada pelas duas línguas da documentação (docs/ = pt, docs-en/ = en).

``{video} <id>`` — incorpora o vídeo do YouTube com esse id da série. Os IDs vêm de
``docs/_data/videos.json``, escrito por scripts/youtube_upload.py: pt na raiz, en em ``"en"``.
Enquanto um vídeo não tiver ID, mostra uma nota em vez do leitor.
"""
import json
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import Directive, directives

VIDEOS = Path(__file__).resolve().parent.parent / 'docs' / '_data' / 'videos.json'

TEXTOS = {
    'pt': {'em_breve': 'Vídeo em breve: esta página vai incluir o vídeo de demonstração correspondente.',
           'ligacao': 'Vídeo de demonstração: '},
    'en': {'em_breve': 'Video coming soon: this page will include the corresponding demonstration video.',
           'ligacao': 'Demonstration video: '},
}


def lingua(env):
    return 'en' if (env.config.language or '').startswith('en') else 'pt'


class VideoDirective(Directive):
    required_arguments = 1
    option_spec = {'titulo': directives.unchanged}

    def run(self):
        vid = self.arguments[0]
        env = self.state.document.settings.env
        # reconstruir a página quando o videos.json mudar
        env.note_dependency(str(VIDEOS))
        lang = lingua(env)
        dados = json.loads(VIDEOS.read_text(encoding='utf-8'))
        if lang != 'pt':
            dados = dados.get(lang, {})
        info = dados.get(vid, {})
        yt = info.get('youtube')
        t = TEXTOS[lang]
        if env.app.builder.format != 'html':
            # PDF/EPUB: sem leitor — uma ligação para o vídeo, ou nada enquanto não existir
            if not yt:
                return []
            url = f'https://youtu.be/{yt}'
            par = nodes.paragraph(text=t['ligacao'])
            par += nodes.reference(url, url, refuri=url)
            return [par]
        if not yt:
            nota = nodes.note()
            nota += nodes.paragraph(text=t['em_breve'])
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
    return {'parallel_read_safe': True}
