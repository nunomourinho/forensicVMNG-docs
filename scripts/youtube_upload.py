#!/usr/bin/env python3
"""Carrega os vídeos de demonstração do ForensicVM no YouTube (YouTube Data API v3).

Para cada vídeo: upload resumível do MP4 legendado (legendas gravadas na imagem), título,
descrição com os capítulos e a ligação para a página da documentação (só pt) e inserção na
playlist da série da língua. Se não houver versão legendada, envia a -musica.mp4 e carrega
o .srt/.vtt como faixa de legendas.
O estado fica em docs/_data/videos.json (pt na raiz, en em "en"), gravado depois de cada
vídeo; uma nova execução salta o que já foi feito. Ao esgotar a quota diária, pára e diz
para retomar no dia seguinte. Os vídeos vão para o canal fixado em "_canal" no primeiro login.

Credenciais (nunca no repositório):
    ~/.config/forensicvm/youtube-client-secret.json   cliente OAuth «Aplicação para computador»
    ~/.config/forensicvm/youtube-token.json           criado no primeiro login (0600)

Autenticação sem browser local (servidor remoto):
    youtube_upload.py --auth-url                      # imprime o endereço a abrir
    youtube_upload.py --auth-code 'http://localhost:8765/?state=…&code=…'
                                                      # colar o endereço da página que falha

Uso:
    youtube_upload.py --simular                       # mostra o que faria, sem API
    youtube_upload.py --lang en                       # série inglesa (demo-en)
    youtube_upload.py --apenas 32-resumo-sistema      # um vídeo (teste)
    youtube_upload.py                                 # todos os que faltam, pela ordem da série
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ESTADO = RAIZ / 'docs' / '_data' / 'videos.json'
CONFIG = Path.home() / '.config' / 'forensicvm'
CLIENTE = CONFIG / 'youtube-client-secret.json'
TOKEN = CONFIG / 'youtube-token.json'
PENDENTE = CONFIG / 'youtube-auth-pendente.json'   # state + code_verifier entre --auth-url e --auth-code
REDIRECT = 'http://localhost:8765/'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload',
          'https://www.googleapis.com/auth/youtube.force-ssl']

LINGUAS = {
    'pt': {
        'videos': Path('/forensicVM/mnt/iso/demo-pj'),
        'codigo': 'pt-PT', 'nome_legendas': 'Português (Portugal)',
        'playlist': 'ForensicVM NextGen — demonstrações',
        'playlist_desc': ('Série de demonstrações do ForensicVM NextGen, plataforma de virtualização forense: '
                          'da imagem de disco apreendida a uma máquina virtual controlada pelo navegador.'),
        'principal': 'Demonstração completa',
        'resumo_principal': ('Demonstração completa do ForensicVM NextGen, do primeiro acesso à análise, '
                             'com operações reais sobre imagens forenses públicas do CFReDS (NIST).'),
        'capitulos': 'Capítulos:', 'documentacao': 'Documentação:',
        'aviso': ('Demonstração feita com imagens forenses públicas do CFReDS (NIST). O ForensicVM NextGen '
                  'está em desenvolvimento ativo e ainda não é recomendado para uso em produção.'),
        'tags': ['ForensicVM', 'forense digital', 'virtualização forense', 'perícia informática',
                 'digital forensics', 'QEMU', 'KVM', 'CFReDS', 'NIST'],
        'docs': True,
    },
    'en': {
        'videos': Path('/forensicVM/mnt/iso/demo-en'),
        'codigo': 'en-GB', 'nome_legendas': 'English (United Kingdom)',
        'playlist': 'ForensicVM NextGen — demos',
        'playlist_desc': ('Demo series of ForensicVM NextGen, a forensic virtualisation platform: '
                          'from a seized disk image to a virtual machine controlled from the browser.'),
        'principal': 'Full demonstration',
        'resumo_principal': ('Full demonstration of ForensicVM NextGen, from first sign-in to analysis, '
                             'with real operations on public forensic images from CFReDS (NIST).'),
        'capitulos': 'Chapters:', 'documentacao': None,
        'aviso': ('Demonstration made with public forensic images from CFReDS (NIST). ForensicVM NextGen '
                  'is under active development and is not yet recommended for production use.'),
        'tags': ['ForensicVM', 'digital forensics', 'forensic virtualisation', 'computer forensics',
                 'DFIR', 'QEMU', 'KVM', 'CFReDS', 'NIST'],
        'docs': False,
    },
}

# Ordem de visionamento (a mesma da documentação) e página de cada vídeo.
PAGINAS = {
    '32-resumo-sistema': 'introducao/visao-geral',
    '01-primeiros-passos': 'comecar/primeiros-passos',
    '02-casos-e-equipa': 'comecar/casos-e-equipa',
    '03-bart-cfreds-conversao': 'conversao/cfreds-bart',
    '04-injecao-de-drivers': 'conversao/injecao-drivers',
    '13-hacking-case': 'conversao/hacking-case',
    '16-outras-origens': 'conversao/outras-origens',
    '05-arranque-e-consola': 'maquinas-virtuais/arranque-e-consola',
    '06-acesso-sem-alterar-password': 'maquinas-virtuais/acesso-a-conta',
    '17-consola': 'maquinas-virtuais/consola',
    '09-snapshots': 'maquinas-virtuais/snapshots',
    '12-hardware': 'maquinas-virtuais/hardware',
    '29-instalar-agente': 'maquinas-virtuais/agente-qemu',
    '30-desencriptar-disco': 'maquinas-virtuais/encriptacao-discos',
    '07-plugins': 'analise/plugins',
    '08-gravacao-da-sessao': 'analise/gravacao',
    '10-memoria': 'analise/memoria',
    '11-rede': 'analise/rede',
    '18-introspecao': 'analise/introspecao',
    '19-evidencias': 'analise/evidencias',
    '31-gestor-processos': 'analise/gestor-processos',
    '20-cape-introducao': 'malware/cape',
    '22-cape-utilizacao': 'malware/cape-utilizacao',
    '14-auditoria': 'gestao/auditoria',
    '15-administracao': 'gestao/administracao',
    '24-relatorio-do-caso': 'gestao/relatorio-caso',
    '23-estado-e-colaboracao': 'projeto/estado-e-colaboracao',
    '25-pre-requisitos': 'instalacao/pre-requisitos',
    '26-ubuntu-server': 'instalacao/ubuntu-server',
    '27-forensicvm': 'instalacao/forensicvm',
    '28-https-intranet': 'instalacao/https-intranet',
    '21-cape-instalacao': 'instalacao/cape',
    '33-gestao-operacao': 'administracao/gestao-servidor',
    '34-copias-troubleshooting': 'administracao/copias-e-problemas',
    '00-principal': 'index',
}
CATEGORIA = '28'  # Ciência e Tecnologia


def tempo(seg):
    seg = int(seg)
    h, r = divmod(seg, 3600)
    m, s = divmod(r, 60)
    return f'{h}:{m:02d}:{s:02d}' if h else f'{m}:{s:02d}'


def metadados(vid, videos_dir, docs_url, L):
    meta = json.loads((videos_dir / f'{vid}.json').read_text(encoding='utf-8'))
    titulo = L['principal'] if vid == '00-principal' else meta['titulo']
    resumo = meta.get('resumo') or L['resumo_principal']
    # capítulos seguidos com o mesmo título juntam-se no primeiro
    caps = [c for i, c in enumerate(meta.get('capitulos', []))
            if i == 0 or c['titulo'] != meta['capitulos'][i - 1]['titulo']]
    linhas = [resumo, '']
    # o YouTube só reconhece capítulos com pelo menos 3 entradas, a primeira em 0:00
    if len(caps) >= 3 and caps[0]['t'] == 0:
        linhas += [L['capitulos']] + [f"{tempo(c['t'])} {c['titulo']}" for c in caps] + ['']
    if L['docs']:
        linhas += [f"{L['documentacao']} {docs_url.rstrip('/')}/{PAGINAS[vid]}.html", '']
    linhas += [L['aviso']]
    # versão com as legendas gravadas na imagem; sem ela, a com música + faixa de legendas
    legendado = videos_dir / f'{vid}-legendado.mp4'
    gravadas = legendado.exists()
    return {
        'titulo': (titulo if titulo.startswith('ForensicVM') else f'ForensicVM — {titulo}')[:100],
        'descricao': '\n'.join(linhas)[:5000],
        'mp4': legendado if gravadas else videos_dir / f'{vid}-musica.mp4',
        'gravadas': gravadas,
        # o YouTube aceita SRT e WebVTT; o vídeo completo só tem .vtt
        'srt': next((f for f in (videos_dir / f'{vid}.srt', videos_dir / f'{vid}.vtt') if f.exists()),
                    videos_dir / f'{vid}.srt'),
    }


def carregar_estado():
    return json.loads(ESTADO.read_text(encoding='utf-8')) if ESTADO.exists() else {}


def gravar_estado(estado):
    tmp = ESTADO.with_suffix('.tmp')
    tmp.write_text(json.dumps(estado, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    tmp.replace(ESTADO)


def gravar_privado(caminho, texto):
    CONFIG.mkdir(parents=True, exist_ok=True)
    fd = os.open(caminho, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, 'w') as f:
        f.write(texto)
    os.chmod(caminho, 0o600)


def novo_flow(state=None, verifier=None):
    from google_auth_oauthlib.flow import Flow
    if not CLIENTE.exists():
        sys.exit(f'Falta o cliente OAuth em {CLIENTE} — ver o README (Fase B).')
    flow = Flow.from_client_secrets_file(str(CLIENTE), SCOPES, state=state, redirect_uri=REDIRECT)
    if verifier:
        flow.code_verifier = verifier
    return flow


def auth_url():
    """Passo 1 do login sem browser local: imprime o endereço e guarda o state/PKCE."""
    flow = novo_flow()
    url, state = flow.authorization_url(access_type='offline', prompt='consent select_account')
    gravar_privado(PENDENTE, json.dumps({'state': state, 'verifier': flow.code_verifier}))
    print('Abra este endereço, escolha o canal ForensicVM e autorize:\n')
    print(url)
    print('\nO browser acaba numa página http://localhost:8765/… que não abre — copie esse endereço '
          'completo e passe-o a --auth-code.')


def auth_code(resposta):
    """Passo 2: troca o código pelo token e mostra o canal autorizado."""
    if not PENDENTE.exists():
        sys.exit('Corra primeiro --auth-url.')
    p = json.loads(PENDENTE.read_text())
    flow = novo_flow(p['state'], p['verifier'])
    # o redirect é http://localhost; o oauthlib só o aceita com esta variável
    os.environ.setdefault('OAUTHLIB_INSECURE_TRANSPORT', '1')
    flow.fetch_token(authorization_response=resposta.strip())
    gravar_privado(TOKEN, flow.credentials.to_json())
    PENDENTE.unlink()
    from googleapiclient.discovery import build
    yt = build('youtube', 'v3', credentials=flow.credentials)
    for c in canais(yt):
        print(f"Canal autorizado: {c['snippet']['title']}  ({c['id']})")


def canais(yt):
    return executar(yt.channels().list(part='snippet', mine=True)).get('items', [])


def autenticar():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    cred = Credentials.from_authorized_user_file(str(TOKEN), SCOPES) if TOKEN.exists() else None
    if cred and cred.expired and cred.refresh_token:
        cred.refresh(Request())
        gravar_privado(TOKEN, cred.to_json())
    elif not cred or not cred.valid:
        sys.exit('Sem token válido — corra --auth-url e depois --auth-code.')
    return build('youtube', 'v3', credentials=cred)


def confirmar_canal(yt, raiz):
    """Fixa o canal no primeiro uso e recusa carregar para outro."""
    ch = canais(yt)
    if len(ch) != 1:
        sys.exit(f'A conta autorizada tem {len(ch)} canais visíveis — esperado 1.')
    cid, nome = ch[0]['id'], ch[0]['snippet']['title']
    fixo = raiz.get('_canal')
    if not fixo:
        if 'forensicvm' not in nome.lower():
            sys.exit(f'O canal autorizado é «{nome}» ({cid}), não o ForensicVM. Volte a autorizar '
                     'escolhendo o canal ForensicVM.')
        raiz['_canal'] = {'id': cid, 'titulo': nome}
    elif fixo['id'] != cid:
        sys.exit(f'O canal autorizado é «{nome}» ({cid}), não o fixado «{fixo["titulo"]}» ({fixo["id"]}).')
    print(f'Canal: {nome} ({cid})')


class QuotaEsgotada(Exception):
    pass


def executar(pedido):
    """Executa um pedido simples, convertendo quotaExceeded em QuotaEsgotada."""
    from googleapiclient.errors import HttpError
    try:
        return pedido.execute()
    except HttpError as e:
        if e.resp.status == 403 and b'quota' in e.content.lower():
            raise QuotaEsgotada() from e
        raise


def upload(yt, m, privacidade, L):
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload

    corpo = {
        'snippet': {'title': m['titulo'], 'description': m['descricao'], 'tags': L['tags'],
                    'categoryId': CATEGORIA, 'defaultLanguage': L['codigo'], 'defaultAudioLanguage': L['codigo']},
        'status': {'privacyStatus': privacidade, 'selfDeclaredMadeForKids': False, 'embeddable': True},
    }
    media = MediaFileUpload(str(m['mp4']), mimetype='video/mp4', chunksize=8 * 1024 * 1024, resumable=True)
    pedido = yt.videos().insert(part='snippet,status', body=corpo, media_body=media)
    resposta, tentativas = None, 0
    while resposta is None:
        try:
            estado, resposta = pedido.next_chunk()
            if estado:
                print(f'  … {int(estado.progress() * 100)}%', end='\r', flush=True)
        except HttpError as e:
            if (e.resp.status == 403 and b'quota' in e.content.lower()) or b'uploadLimitExceeded' in e.content:
                raise QuotaEsgotada() from e
            if e.resp.status not in (500, 502, 503, 504) or tentativas >= 8:
                raise
            tentativas += 1
            time.sleep(2 ** tentativas)
    print()
    return resposta['id'], resposta.get('status', {}).get('privacyStatus')


def legendas(yt, video_id, srt, L):
    from googleapiclient.http import MediaFileUpload
    corpo = {'snippet': {'videoId': video_id, 'language': L['codigo'], 'name': L['nome_legendas']}}
    executar(yt.captions().insert(part='snippet', body=corpo,
                                  media_body=MediaFileUpload(str(srt), mimetype='application/octet-stream')))


def playlist(yt, estado, raiz, L, privacidade):
    pid = estado.get('_playlist')
    if not pid:
        r = executar(yt.playlists().insert(part='snippet,status', body={
            'snippet': {'title': L['playlist'], 'description': L['playlist_desc'], 'defaultLanguage': L['codigo']},
            'status': {'privacyStatus': privacidade}}))
        pid = estado['_playlist'] = r['id']
        gravar_estado(raiz)
    return pid


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--lang', choices=list(LINGUAS), default='pt')
    ap.add_argument('--videos', type=Path, help='pasta dos vídeos (por omissão, a da língua)')
    ap.add_argument('--docs-url', default='https://forensicvmng-user-manual.readthedocs.io/pt/latest')
    ap.add_argument('--privacidade', choices=['public', 'unlisted', 'private'], default='unlisted')
    ap.add_argument('--apenas', nargs='+', metavar='ID', help='só estes vídeos')
    ap.add_argument('--simular', action='store_true', help='mostra os metadados sem usar a API')
    ap.add_argument('--auth-url', action='store_true', help='login, passo 1: imprime o endereço a abrir')
    ap.add_argument('--auth-code', metavar='URL', help='login, passo 2: endereço localhost:8765 colado')
    args = ap.parse_args()

    if args.auth_url:
        return auth_url()
    if args.auth_code:
        return auth_code(args.auth_code)

    L = LINGUAS[args.lang]
    videos = args.videos or L['videos']
    ids = args.apenas or list(PAGINAS)
    desconhecidos = [i for i in ids if i not in PAGINAS]
    if desconhecidos:
        sys.exit(f'Ids desconhecidos: {", ".join(desconhecidos)}')

    # pt fica na raiz (é o que a diretiva {video} lê); as outras línguas numa secção própria
    raiz = carregar_estado()
    estado = raiz if args.lang == 'pt' else raiz.setdefault(args.lang, {})
    pendentes = [i for i in ids if not estado.get(i, {}).get('youtube') or not estado[i].get('legendas')]
    print(f'{len(pendentes)} vídeo(s) por carregar ({args.lang}).')

    if args.simular:
        for vid in pendentes:
            m = metadados(vid, videos, args.docs_url, L)
            tam = m['mp4'].stat().st_size / 1e6
            leg = 'gravadas' if m['gravadas'] else ('faixa ' + m['srt'].suffix if m['srt'].exists() else 'NÃO')
            print(f"\n=== {vid}  ({m['mp4'].name}, {tam:.0f} MB, legendas: {leg})")
            print(m['titulo'])
            print(m['descricao'])
        return

    yt = autenticar()
    confirmar_canal(yt, raiz)
    gravar_estado(raiz)
    aviso_bloqueio = False
    try:
        pid = playlist(yt, estado, raiz, L, args.privacidade)
        for vid in pendentes:
            m = metadados(vid, videos, args.docs_url, L)
            info = estado.setdefault(vid, {'titulo': m['titulo']})
            if not info.get('youtube'):
                print(f'→ {vid}: upload de {m["mp4"].name}')
                info['youtube'], info['privacidade'] = upload(yt, m, args.privacidade, L)
                if m['gravadas']:
                    info['legendas'] = 'gravadas'
                gravar_estado(raiz)
                executar(yt.playlistItems().insert(part='snippet', body={'snippet': {
                    'playlistId': pid, 'resourceId': {'kind': 'youtube#video', 'videoId': info['youtube']}}}))
                print(f'  https://youtu.be/{info["youtube"]}  ({info["privacidade"]})')
                if info['privacidade'] != args.privacidade and not aviso_bloqueio:
                    aviso_bloqueio = True
                    print(f'  AVISO: pedido {args.privacidade}, o YouTube devolveu {info["privacidade"]} — '
                          'o projeto da API provavelmente não está auditado (vídeos bloqueados como privados).')
            if not info.get('legendas'):
                if m['srt'].exists():
                    legendas(yt, info['youtube'], m['srt'], L)
                    info['legendas'] = True
                    print(f"  legendas {L['codigo']} carregadas")
                else:
                    info['legendas'] = 'nenhumas'
                gravar_estado(raiz)
    except QuotaEsgotada:
        gravar_estado(raiz)
        sys.exit('Quota diária da API (ou limite de uploads do canal) esgotada. O progresso ficou guardado — volte a correr amanhã.')
    print('Concluído.')


if __name__ == '__main__':
    main()
