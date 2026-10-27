# Instalar o ForensicVM

Com o Ubuntu Server pronto, instalar o ForensicVM é, no essencial, **um único comando**. Esse comando
trata de tudo: dependências, base de dados, serviços e servidor web.

```{video} 27-forensicvm
```

## Obter o código

Instale o `git`, se ainda não existir, e clone o repositório do ForensicVM. Substitua
`<URL-DO-REPOSITORIO>` pelo endereço do repositório que lhe foi disponibilizado:

```bash
sudo apt install -y git
git clone --depth 1 <URL-DO-REPOSITORIO> forensicVmNG
cd forensicVmNG
ls
```

`--depth 1` descarrega só a versão mais recente, o que poupa tempo e espaço. O instalador é o
`install.sh`.

```{figure} /_static/img/27-forensicvm/03b.jpg
:alt: Terminal com o git clone, a listagem da pasta e o início do install.sh

`git clone` e o início do `install.sh`.
```

## Correr o instalador

Dentro da pasta do repositório, como administrador:

```bash
sudo ./install.sh
```

O instalador mostra cada passo e segue até ao fim praticamente sem perguntas:

1. **Node.js** e **pnpm**, na versão exata fixada pelo projeto;
2. **Dependências do sistema:** MariaDB, QEMU/KVM, ferramentas forenses e de análise de memória
   (algumas compiladas de raiz) e os controladores VirtIO para Windows (`virtio-win.iso`);
3. **A aplicação:** dependências, compilação do servidor e da interface web;
4. **A base de dados**, com um utilizador de privilégios mínimos, as migrações e o administrador inicial;
5. **O serviço systemd e o nginx.**

Na instalação de referência demorou cerca de 25 minutos. Varia com a rede e o processador.

A meio, há uma única pergunta. Responda `y`:

```text
Instalar e activar o serviço systemd forensicvm? [y/N] y
```

```{figure} /_static/img/27-forensicvm/04a.jpg
:alt: Instalador a mostrar a instalação das dependências do sistema

O instalador, passo a passo.
```

## O resumo final

No fim, o instalador mostra:

- o endereço do servidor (`http://<IP-do-servidor>`);
- a conta de administrador inicial (`admin`) e a palavra-passe por omissão;
- o caminho do ficheiro de configuração (`apps/server/.env`) e os próximos passos.

```{figure} /_static/img/27-forensicvm/07a.jpg
:alt: Resumo da instalação concluída e estado do serviço forensicvm

Instalação concluída e serviço ativo.
```

```{danger}
**Guarde a `DISK_ENCRYPTION_MASTER_KEY`** (no ficheiro `apps/server/.env`) num local seguro, fora do
servidor. Sem ela, os discos cifrados **não se recuperam**. As cópias de segurança do `backup.sh`
incluem-na (veja {doc}`../administracao/copias-e-problemas`).
```

## Verificar

```bash
systemctl status forensicvm --no-pager   # deve estar «active (running)» e «enabled»
curl -s http://localhost/api/v2/health   # deve responder {"status":"ok",...}
```

## Primeiro acesso

Abra `http://<IP-do-servidor>` no navegador e entre com a conta inicial. O sistema leva-o logo à
configuração do **segundo fator, obrigatória**. Depois **mude a palavra-passe por omissão**
(**Perfil → Alterar palavra-passe**). Veja {doc}`../comecar/primeiros-passos`.

```{figure} /_static/img/27-forensicvm/08b.jpg
:alt: Configuração obrigatória do segundo fator no primeiro acesso

No primeiro acesso, o segundo fator é obrigatório.
```

## Reforço para produção

- **HTTPS:** com o `certbot` (servidor com nome público) ou com uma autoridade certificadora local
  (rede isolada, veja {doc}`https-intranet`). Depois de ativar o HTTPS, defina `COOKIE_SECURE=true` no
  `.env` e reinicie o serviço (`sudo systemctl restart forensicvm`).
- **Firewall:** abra só as portas 80 e 443 (e a 22 para administração). Feche o resto ao exterior.
- **Cópias de segurança** regulares da base de dados e dos discos das máquinas (veja
  {doc}`../administracao/copias-e-problemas`).
