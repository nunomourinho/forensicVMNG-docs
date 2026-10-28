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


REDIRECTS = VIDEOS.parent / 'redirects.json'
REDIRECT_HTML = (
    '<!DOCTYPE html><html><head><meta charset="utf-8"><title>{alvo}</title>'
    '<link rel="canonical" href="{alvo}"><meta http-equiv="refresh" content="0; url={alvo}">'
    '</head><body><a href="{alvo}">{alvo}</a></body></html>\n'
)


def redirecionar(app, exc):
    """Páginas antigas (nomes em português) → nomes atuais, só na árvore pt.

    As páginas pt passaram a ter os mesmos nomes que as en, para o seletor de língua
    do Read the Docs abrir a página equivalente. Os endereços antigos (e as ligações
    nas descrições dos vídeos do YouTube) continuam a funcionar com estas páginas.
    """
    if exc or app.builder.format != 'html' or lingua(app.builder.env) != 'pt' or not REDIRECTS.exists():
        return
    import posixpath
    suffix = app.builder.out_suffix
    for antigo, novo in json.loads(REDIRECTS.read_text(encoding='utf-8')).items():
        destino = Path(app.outdir) / f'{antigo}{suffix}'
        if destino.exists():
            continue
        alvo = posixpath.relpath(f'{novo}{suffix}', posixpath.dirname(antigo) or '.')
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(REDIRECT_HTML.format(alvo=alvo), encoding='utf-8')


def setup(app):
    app.add_directive('video', VideoDirective)
    app.connect('build-finished', redirecionar)
    return {'parallel_read_safe': True}
