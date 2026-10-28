# ForensicVM NextGen — documentação pública

Documentação pública do **ForensicVM NextGen**, plataforma web de virtualização forense, publicada no
Read the Docs em duas línguas, a partir das duas séries de vídeos de demonstração:

| Língua | Fonte | Configuração RTD | Endereço |
|---|---|---|---|
| Português (pt-PT) | `docs/` | `.readthedocs.yaml` | <https://forensicvmng-user-manual.readthedocs.io/pt/latest/> |
| English (en-GB) | `docs-en/` | `.readthedocs-en.yaml` | <https://forensicvmng-user-manual.readthedocs.io/en/latest/> |

- Fonte: Markdown (MyST), compilado com Sphinx e o tema `sphinx_rtd_theme`.
- Imagens: fotogramas dos vídeos de cada língua, em `docs*/_static/img/<id-do-vídeo>/` (os nomes das
  pastas são os ids da série, iguais nas duas línguas).
- Vídeos: incorporados do YouTube. Os IDs estão em `docs/_data/videos.json` (pt na raiz, en em `"en"`).
- A diretiva `{video}` está em `ext/forensicvm_sphinx.py`, partilhada pelas duas árvores. O CSS está em
  `docs/_static/css/` e o `docs-en/conf.py` reutiliza-o.
- As páginas inglesas têm nomes ingleses (`virtual-machines/snapshots`, `analysis/process-manager`…). A
  árvore é a mesma: cada página PT tem a sua equivalente, com o mesmo vídeo e as mesmas figuras.

## Compilar localmente

```bash
python3 -m venv .venv
.venv/bin/pip install -r docs/requirements.txt
.venv/bin/sphinx-build -W -b html docs docs/_build/html          # pt
.venv/bin/sphinx-build -W -b html docs-en docs-en/_build/html    # en
xdg-open docs/_build/html/index.html
```

O build usa `-W` (avisos tratam-se como erros), tal como no Read the Docs (`fail_on_warning`).

## Escrever uma página

Cada página de funcionalidade segue o mesmo padrão:

````markdown
# Título

Parágrafo: para que serve.

```{video} 09-snapshots
```

## Secção

Texto…

```{figure} /_static/img/09-snapshots/02a.jpg
:alt: Descrição da imagem (acessibilidade)

Legenda.
```
````

A diretiva `{video} <id>` (definida em `docs/conf.py`) incorpora o vídeo do YouTube correspondente ao id
da série. Enquanto o vídeo não tiver ID em `docs/_data/videos.json`, mostra a nota "Vídeo em breve".

### Fotogramas

`scripts/extrair_imagens.py` extrai dois fotogramas candidatos por capítulo de cada vídeo (a partir dos
MP4 e dos JSON de capítulos da série). A escolha das imagens que entram na documentação é feita à mão.

```bash
.venv/bin/pip install pyyaml
.venv/bin/python scripts/extrair_imagens.py --videos /forensicVM/mnt/iso/demo-pj \
    --guioes ../forensicVmNG/docs/demo-pj/guioes --saida /tmp/candidatos
```

## Publicar no Read the Docs

1. Entrar em <https://readthedocs.org> com a conta GitHub.
2. **Add project** → importar `nunomourinho/forensicVMNG-docs`.
3. Em *Settings*, escolher o idioma **Portuguese**. O resto vem de `.readthedocs.yaml`.

### O projeto inglês (tradução)

1. **Add project** → importar outra vez `nunomourinho/forensicVMNG-docs`, com o nome
   `forensicvmng-user-manual-en` e o idioma **English**.
2. Nesse projeto, *Settings* → *Build configuration file*: `.readthedocs-en.yaml`.
3. No projeto português, *Settings* → *Translations* → adicionar `forensicvmng-user-manual-en`. O inglês
   passa a servir-se em `/en/latest/` e o seletor de língua aparece no menu.

Cada *push* para `main` reconstrói as duas documentações.

## Carregar os vídeos no YouTube

`scripts/youtube_upload.py` carrega os vídeos da série com a YouTube Data API v3: a versão com as
legendas gravadas na imagem, título, descrição com capítulos e ligação para a página da documentação, e
uma playlist por língua (`--lang pt|en`). Os vídeos ficam **não listados** por omissão. Grava o ID de
cada vídeo em `docs/_data/videos.json`. Depois de um *commit* + *push* desse ficheiro, os vídeos aparecem
nas páginas. No primeiro uso, fixa o canal (`_canal`) e recusa depois carregar para outro.

### 1. Preparar o projeto Google Cloud (uma vez)

1. <https://console.cloud.google.com> → criar um projeto (por exemplo `forensicvm-docs`).
2. **APIs e serviços → Biblioteca** → ativar a **YouTube Data API v3**.
3. **APIs e serviços → Ecrã de consentimento OAuth** (ou *Google Auth Platform*): tipo **Externo**, nome
   da aplicação e email de contacto. Em **Público-alvo → Utilizadores de teste**, adicionar a conta Google
   dona do canal.
4. **Credenciais → Criar credenciais → ID do cliente OAuth** → tipo **Aplicação para computador** →
   transferir o JSON.
5. Copiar o JSON para o servidor:

   ```bash
   install -d -m 700 ~/.config/forensicvm
   install -m 600 client_secret_*.json ~/.config/forensicvm/youtube-client-secret.json
   ```

6. A conta tem de ter um canal YouTube. Para vídeos com mais de 15 minutos (o vídeo completo tem cerca de
   76), o canal tem de estar **verificado** em <https://www.youtube.com/verify>.

### 2. Instalar as dependências

```bash
.venv/bin/pip install -r scripts/requirements-youtube.txt
```

### 3. Primeiro login (uma vez)

O login não precisa de browser no servidor nem de túnel:

```bash
.venv/bin/python scripts/youtube_upload.py --auth-url
```

Abra o endereço impresso no browser do seu computador, escolha o **canal** para onde vão os vídeos e
autorize. O browser acaba numa página `http://localhost:8765/?state=…&code=…` que não abre: copie esse
endereço completo e passe-o ao script:

```bash
.venv/bin/python scripts/youtube_upload.py --auth-code 'http://localhost:8765/?state=…&code=…'
```

O token fica em `~/.config/forensicvm/youtube-token.json` (0600) e o script mostra o canal autorizado.
Comece por um vídeo (`--apenas 32-resumo-sistema`) e confirme-o no YouTube Studio antes de continuar.

### 4. Carregar o resto

```bash
.venv/bin/python scripts/youtube_upload.py --simular   # ver os metadados sem usar a API
.venv/bin/python scripts/youtube_upload.py             # carregar os que faltam (pt)
.venv/bin/python scripts/youtube_upload.py --lang en   # série inglesa
git add docs/_data/videos.json && git commit -m "docs: vídeos do YouTube" && git push
```

### Limitações a conhecer

- **Vídeos privados:** em projetos Google Cloud que não passaram a auditoria da API, os vídeos carregados
  pela API ficam bloqueados como **privados**, seja qual for a opção pedida. Mude-os para públicos no
  YouTube Studio (é possível selecionar vários de uma vez), ou peça a auditoria no formulário *YouTube API
  Services — Audit and Quota Extension*. Vídeos privados não se veem incorporados nas páginas.
- **Quota diária:** 10 000 unidades. Um upload gasta cerca de 1 600 e uma legenda 400.
- **Limite de uploads do canal:** um canal não verificado por telefone aceita poucos vídeos por dia
  (`uploadLimitExceeded`; na prática foram 10). A verificação em <https://www.youtube.com/verify> levanta-o.
- Ao esgotar a quota ou o limite, o script pára, guarda o progresso e retoma onde ficou na execução
  seguinte.
- **Credenciais:** nunca as ponha no repositório. O `.gitignore` exclui `client_secret*.json` e
  `youtube-token*.json`.

## Licença e contribuições

Comentários e correções são bem-vindos nas *issues* deste repositório.
