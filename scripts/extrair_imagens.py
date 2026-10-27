#!/usr/bin/env python3
"""Extrai fotogramas candidatos dos vídeos de demonstração do ForensicVM.

Para cada vídeo, tira dois fotogramas por capítulo (a 35 % e a 75 % da duração do
capítulo) e escreve um manifesto JSON com o título do capítulo e se é um diapositivo
ou uma gravação real. A escolha final das imagens que entram na documentação é feita
à mão, a partir deste conjunto.

Uso:
    extrair_imagens.py --videos /forensicVM/mnt/iso/demo-pj \
                       --guioes ../forensicVmNG/docs/demo-pj/guioes \
                       --saida /tmp/candidatos
"""
import argparse
import json
import subprocess
from pathlib import Path

import yaml

POSICOES = (0.35, 0.75)


def tipos_capitulos(guiao):
    """Lista [(titulo do capítulo, 'diapositivo'|'gravacao')] pela ordem do guião."""
    tipos = []
    for cena in guiao.get('cenas', []):
        if 'capitulo' in cena:
            tipos.append((cena['capitulo'], 'diapositivo' if 'diapositivo' in cena else 'gravacao'))
    return tipos


def extrair(mp4, t, destino):
    subprocess.run(
        ['ffmpeg', '-loglevel', 'error', '-y', '-ss', f'{t:.2f}', '-i', str(mp4),
         '-frames:v', '1', '-vf', 'scale=1280:-2', '-q:v', '3', str(destino)],
        check=True, shell=False,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--videos', type=Path, required=True)
    ap.add_argument('--guioes', type=Path, required=True)
    ap.add_argument('--saida', type=Path, required=True)
    args = ap.parse_args()

    manifesto = {}
    for meta_path in sorted(args.videos.glob('[0-9][0-9]-*.json')):
        meta = json.loads(meta_path.read_text())
        vid = meta['id']
        mp4 = args.videos / f'{vid}.mp4'
        guiao_path = args.guioes / f'{vid}.yaml'
        if not mp4.exists() or not guiao_path.exists():
            continue
        tipos = dict(tipos_capitulos(yaml.safe_load(guiao_path.read_text())))
        caps = meta['capitulos']
        pasta = args.saida / vid
        pasta.mkdir(parents=True, exist_ok=True)
        entradas = []
        for i, cap in enumerate(caps):
            inicio = cap['t']
            fim = caps[i + 1]['t'] if i + 1 < len(caps) else meta['duracao']
            for j, pos in enumerate(POSICOES):
                nome = f'{i + 1:02d}{"ab"[j]}.jpg'
                extrair(mp4, inicio + (fim - inicio) * pos, pasta / nome)
                entradas.append({'ficheiro': nome, 'capitulo': cap['titulo'],
                                 'tipo': tipos.get(cap['titulo'], '?')})
        manifesto[vid] = entradas
        print(vid, len(entradas))
    (args.saida / 'manifesto.json').write_text(json.dumps(manifesto, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
