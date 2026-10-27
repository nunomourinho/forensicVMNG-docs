# Instalar o Ubuntu Server 24.04

O instalador do Ubuntu Server 24.04 do princípio ao fim: idioma e teclado, rede, discos com LVM,
utilizador, servidor SSH, instalação, primeiro arranque e, no fim, como automatizar tudo com autoinstall.

```{video} 26-ubuntu-server
```

## Descarregar

Em <https://ubuntu.com/download/server>, desça até *Previous releases* e carregue em
**Download 24.04.5 LTS**. O ISO tem cerca de 3 GB (veja {doc}`pre-requisitos`).

```{figure} /_static/img/26-ubuntu-server/02a.jpg
:alt: Página de download do Ubuntu Server com as versões anteriores

A página de download, na secção das versões anteriores.
```

## Passo a passo no instalador

Arranque o servidor pelo ISO e escolha **Try or Install Ubuntu Server**. Depois, ecrã a ecrã:

1. **Idioma:** `Português`.
2. **Teclado:** layout e variante `Portuguese` (vêm pré-selecionados). Confirme. É o que garante que as
   teclas, sobretudo nas palavras-passe, saem como esperado.
3. **Tipo de instalação:** `Ubuntu Server` (por omissão).
4. **Rede:** DHCP por omissão. Anote o endereço IP. **Em produção, fixe um endereço IP**, para que o
   ForensicVM responda sempre no mesmo endereço.
5. **Proxy:** em branco, a não ser que a rede o exija.
6. **Espelho (*mirror*):** o detetado, por exemplo `http://pt.archive.ubuntu.com/ubuntu/`. Espere pela
   mensagem *This mirror location passed tests*.
7. **Armazenamento:** `Use an entire disk` com `Set up this disk as an LVM group`. O LVM facilita
   aumentar o espaço mais tarde, à medida que as imagens se acumulam. Confirme o resumo e, no aviso
   *Confirm destructive action*, escolha **Continue**. O disco vai ser formatado.
8. **Perfil:** o seu nome, o nome do servidor (por exemplo `forensicvm`), o utilizador administrador e
   uma palavra-passe forte.
9. **Ubuntu Pro:** `Skip for now`.
10. **SSH:** marque `Install OpenSSH server`, para administração remota segura.
11. **Snaps em destaque:** não escolha nenhum. O ForensicVM instala o que precisa.
12. Aguarde o fim da instalação e escolha **Reboot Now**. Retire o suporte de arranque quando for pedido
    e prima Enter.

```{figure} /_static/img/26-ubuntu-server/04a.jpg
:alt: Escolha do idioma Português no instalador do Ubuntu Server

Escolha do idioma.
```

```{figure} /_static/img/26-ubuntu-server/07a.jpg
:alt: Configuração do armazenamento com o disco inteiro e LVM

Armazenamento: disco inteiro com LVM.
```

```{figure} /_static/img/26-ubuntu-server/08a.jpg
:alt: Ecrã de perfil com nome, nome do servidor, utilizador e palavra-passe

Perfil e utilizador administrador.
```

```{figure} /_static/img/26-ubuntu-server/09a.jpg
:alt: Ecrã de configuração SSH com a opção Install OpenSSH server marcada

Servidor OpenSSH.
```

```{figure} /_static/img/26-ubuntu-server/10a.jpg
:alt: Registo da instalação do sistema em curso

A instalação em curso (cerca de 18 minutos na demonstração).
```

## Primeiro arranque e fuso horário

No primeiro arranque, entre na consola com o utilizador criado. O ecrã de boas-vindas mostra o **endereço
IP** do servidor. É com ele que vai abrir o ForensicVM no navegador.

```{figure} /_static/img/26-ubuntu-server/13b.jpg
:alt: Ecrã de boas-vindas do Ubuntu Server depois do primeiro login

O primeiro login, com o endereço IP do servidor.
```

O instalador não pergunta o fuso horário, e o servidor fica em UTC. Defina-o (exemplo para Portugal
continental):

```bash
timedatectl                                  # ver o fuso atual
sudo timedatectl set-timezone Europe/Lisbon  # definir
timedatectl                                  # confirmar
```

```{tip}
A hora correta do servidor importa num contexto forense: é ela que fica no registo de auditoria. Confirme
também que a sincronização NTP está ativa (`System clock synchronized: yes`).
```

## Automatizar com autoinstall

Para instalar vários servidores sem perguntas, o Ubuntu suporta o **autoinstall**: um ficheiro
`user-data`, em YAML, descreve as escolhas feitas acima, e o instalador segue-o sozinho, entregue por
cloud-init ou numa pen com a etiqueta `CIDATA`.

Exemplo pronto a adaptar: {download}`user-data </_static/autoinstall/user-data>` e
{download}`meta-data </_static/autoinstall/meta-data>`. Antes de usar, troque o nome do servidor, o
utilizador e, sobretudo, a *hash* da palavra-passe:

```bash
openssl passwd -6 'a-sua-palavra-passe-forte'
```

Próximo passo: {doc}`forensicvm`.
