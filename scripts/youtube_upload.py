#!/usr/bin/env python3
"""Carrega os vídeos de demonstração do ForensicVM no YouTube (YouTube Data API v3).

Para cada vídeo: upload resumível do MP4, título, descrição com os capítulos e a ligação
para a página da documentação, legendas pt-PT (.srt) e inserção na playlist da série.
O estado fica em docs/_data/videos.json, gravado depois de cada vídeo; uma nova execução
salta o que já foi feito. Ao esgotar a quota diária, pára e diz para retomar no dia seguinte.

Credenciais (nunca no repositório):
    ~/.config/forensicvm/youtube-client-secret.json   cliente OAuth «Aplicação para computador»
    ~/.config/forensicvm/youtube-token.json           criado no primeiro login (0600)

Uso:
    youtube_upload.py --simular                       # mostra o que faria, sem API
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
SCOPES = ['https://www.googleapis.com/auth/youtube.upload',
          'https://www.googleapis.com/auth/youtube.force-ssl']

PLAYLIST_TITULO = 'ForensicVM NextGen — demonstrações'
PLAYLIST_DESCRICAO = ('Série de demonstrações do ForensicVM NextGen, plataforma de virtualização forense: '
                      'da imagem de disco apreendida a uma máquina virtual controlada pelo navegador.')

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
TITULO_PRINCIPAL = 'Demonstração completa'

TAGS = ['ForensicVM', 'forense digital', 'virtualização forense', 'perícia informática',
        'digital forensics', 'QEMU', 'KVM', 'CFReDS', 'NIST']
CATEGORIA = '28'  # Ciência e Tecnologia


def tempo(seg):
    seg = int(seg)
    h, r = divmod(seg, 3600)
    m, s = divmod(r, 60)
    return f'{h}:{m:02d}:{s:02d}' if h else f'{m}:{s:02d}'


def metadados(vid, videos_dir, docs_url):
    meta = json.loads((videos_dir / f'{vid}.json').read_text(encoding='utf-8'))
    titulo = TITULO_PRINCIPAL if vid == '00-principal' else meta['titulo']
    resumo = meta.get('resumo') or ('Demonstração completa do ForensicVM NextGen, do primeiro acesso à análise, '
                                    'com operações reais sobre imagens forenses públicas do CFReDS (NIST).')
    # capítulos seguidos com o mesmo título juntam-se no primeiro
    caps = [c for i, c in enumerate(meta.get('capitulos', []))
            if i == 0 or c['titulo'] != meta['capitulos'][i - 1]['titulo']]
    linhas = [resumo, '']
    # o YouTube só reconhece capítulos com pelo menos 3 entradas, a primeira em 0:00
    if len(caps) >= 3 and caps[0]['t'] == 0:
        linhas += ['Capítulos:'] + [f"{tempo(c['t'])} {c['titulo']}" for c in caps] + ['']
    linhas += [f"Documentação: {docs_url.rstrip('/')}/{PAGINAS[vid]}.html", '',
               'Demonstração feita com imagens forenses públicas do CFReDS (NIST). O ForensicVM NextGen '
               'está em desenvolvimento ativo e ainda não é recomendado para uso em produção.']
    return {
        'titulo': f'ForensicVM — {titulo}'[:100],
        'descricao': '\n'.join(linhas)[:5000],
        'mp4': videos_dir / f'{vid}.mp4',
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


def autenticar():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    cred = Credentials.from_authorized_user_file(str(TOKEN), SCOPES) if TOKEN.exists() else None
    if cred and cred.expired and cred.refresh_token:
        cred.refresh(Request())
    elif not cred or not cred.valid:
        if not CLIENTE.exists():
            sys.exit(f'Falta o cliente OAuth em {CLIENTE} — ver o README (Fase B).')
        flow = InstalledAppFlow.from_client_secrets_file(str(CLIENTE), SCOPES)
        print('Abra no browser o endereço abaixo (com o túnel ssh -L 8765:localhost:8765 ativo).')
        cred = flow.run_local_server(port=8765, open_browser=False)
    CONFIG.mkdir(parents=True, exist_ok=True)
    TOKEN.write_text(cred.to_json())
    os.chmod(TOKEN, 0o600)
    return build('youtube', 'v3', credentials=cred)


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


def upload(yt, m, privacidade):
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload

    corpo = {
        'snippet': {'title': m['titulo'], 'description': m['descricao'], 'tags': TAGS,
                    'categoryId': CATEGORIA, 'defaultLanguage': 'pt-PT', 'defaultAudioLanguage': 'pt-PT'},
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
            if e.resp.status == 403 and b'quota' in e.content.lower():
                raise QuotaEsgotada() from e
            if e.resp.status not in (500, 502, 503, 504) or tentativas >= 8:
                raise
            tentativas += 1
            time.sleep(2 ** tentativas)
    print()
    return resposta['id'], resposta.get('status', {}).get('privacyStatus')


def legendas(yt, video_id, srt):
    from googleapiclient.http import MediaFileUpload
    corpo = {'snippet': {'videoId': video_id, 'language': 'pt-PT', 'name': 'Português (Portugal)'}}
    executar(yt.captions().insert(part='snippet', body=corpo,
                                  media_body=MediaFileUpload(str(srt), mimetype='application/octet-stream')))


def playlist(yt, estado):
    pid = estado.get('_playlist')
    if not pid:
        r = executar(yt.playlists().insert(part='snippet,status', body={
            'snippet': {'title': PLAYLIST_TITULO, 'description': PLAYLIST_DESCRICAO, 'defaultLanguage': 'pt-PT'},
            'status': {'privacyStatus': 'public'}}))
        pid = estado['_playlist'] = r['id']
        gravar_estado(estado)
    return pid


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--videos', type=Path, default=Path('/forensicVM/mnt/iso/demo-pj'))
    ap.add_argument('--docs-url', default='https://forensicvmng-user-manual.readthedocs.io/pt/latest')
    ap.add_argument('--privacidade', choices=['public', 'unlisted', 'private'], default='public')
    ap.add_argument('--apenas', nargs='+', metavar='ID', help='só estes vídeos')
    ap.add_argument('--simular', action='store_true', help='mostra os metadados sem usar a API')
    args = ap.parse_args()

    ids = args.apenas or list(PAGINAS)
    desconhecidos = [i for i in ids if i not in PAGINAS]
    if desconhecidos:
        sys.exit(f'Ids desconhecidos: {", ".join(desconhecidos)}')

    estado = carregar_estado()
    pendentes = [i for i in ids if not estado.get(i, {}).get('youtube') or not estado[i].get('legendas')]
    print(f'{len(pendentes)} vídeo(s) por carregar.')

    if args.simular:
        for vid in pendentes:
            m = metadados(vid, args.videos, args.docs_url)
            tam = m['mp4'].stat().st_size / 1e6
            print(f"\n=== {vid}  ({tam:.0f} MB, legendas: {'sim' if m['srt'].exists() else 'NÃO'})")
            print(m['titulo'])
            print(m['descricao'])
        return

    yt = autenticar()
    try:
        pid = playlist(yt, estado)
        for vid in pendentes:
            m = metadados(vid, args.videos, args.docs_url)
            info = estado.setdefault(vid, {'titulo': m['titulo']})
            if not info.get('youtube'):
                print(f'→ {vid}: upload de {m["mp4"].name}')
                info['youtube'], info['privacidade'] = upload(yt, m, args.privacidade)
                gravar_estado(estado)
                executar(yt.playlistItems().insert(part='snippet', body={'snippet': {
                    'playlistId': pid, 'resourceId': {'kind': 'youtube#video', 'videoId': info['youtube']}}}))
                print(f'  https://youtu.be/{info["youtube"]}  ({info["privacidade"]})')
            if m['srt'].exists() and not info.get('legendas'):
                legendas(yt, info['youtube'], m['srt'])
                info['legendas'] = True
                gravar_estado(estado)
                print('  legendas pt-PT carregadas')
    except QuotaEsgotada:
        gravar_estado(estado)
        sys.exit('Quota diária da API esgotada. O progresso ficou guardado — volte a correr amanhã.')
    print('Concluído.')


if __name__ == '__main__':
    main()
