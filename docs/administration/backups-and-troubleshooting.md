# Cópias de segurança e resolução de problemas

Uma cópia de segurança só vale se a soubermos repor. Esta página mostra como fazer uma cópia com o
`backup.sh`, guardá-la num disco à parte e agendá-la; como um arquivo alterado é recusado; como repor
tudo com o `restore.sh`; e como diagnosticar e resolver as falhas mais comuns.

```{video} 34-copias-troubleshooting
```

```{note}
Na demonstração, o desastre e as falhas foram provocados de propósito, num servidor de laboratório.
**Nunca** reproduza esses passos num servidor em produção.
```

## O que entra na cópia

| Conteúdo | Notas |
|---|---|
| Base de dados | Utilizadores, casos, permissões e o registo de auditoria, com os *triggers* de imutabilidade. |
| Ficheiro `.env` | Inclui o `JWT_SECRET` e a chave-mestra dos discos cifrados. |
| Configuração do sistema | Serviço systemd, nginx e certificados TLS, sudoers, logrotate. |
| Metadados das máquinas virtuais | |
| Discos das máquinas e ISOs | Só com `--incluir-vms` e `--incluir-iso`, por serem grandes. |
| `MANIFEST` e somas SHA-256 | Origem e data da cópia, e a soma de cada ficheiro. |

```{danger}
O arquivo leva a **chave-mestra dos discos cifrados**. Sem ela, esses discos não se abrem, e com ela
qualquer pessoa os pode abrir. A cópia é um segredo: guarde-a **fora do servidor**, com acesso restrito.
```

## Fazer a cópia

```bash
./backup.sh --help
./backup.sh                                   # → /var/backups/forensicvm/forensicvm-AAAAMMDD-HHMMSS.tar.gz
./backup.sh --destino /mnt/nas/forensicvm --incluir-vms --incluir-iso
```

A cópia da base de dados é feita sem parar o servidor. No fim, o `backup.sh` indica o que guardou
(utilizadores, casos, *triggers*), calcula as somas SHA-256 e lembra que o arquivo contém segredos. Ao
lado do arquivo fica um ficheiro `.sha256` com a sua soma.

```{figure} /_static/img/34-copias-troubleshooting/04a.jpg
:alt: O arquivo da cópia e a sua soma SHA-256 em /var/backups/forensicvm

O arquivo e a sua soma SHA-256.
```

## Guardar fora do servidor

A cópia não pode ficar só no próprio servidor. Copie o arquivo e a sua soma para um disco externo, um NAS
ou outra máquina, e confirme no destino que chegou intacto:

```bash
cp /var/backups/forensicvm/forensicvm-*.tar.gz* /mnt/disco-externo/
cd /mnt/disco-externo && sha256sum -c forensicvm-*.tar.gz.sha256
```

```{figure} /_static/img/34-copias-troubleshooting/04b.jpg
:alt: Cópia para um disco à parte com a verificação sha256sum OK

Cópia para um disco à parte e verificação da soma.
```

## Agendar todas as noites

```bash
echo '30 2 * * * root '"$PWD"'/backup.sh --destino /mnt/backup/forensicvm >>/var/log/forensicvm/backup.log 2>&1' \
  | tee /etc/cron.d/forensicvm-backup
```

## Verificar uma cópia

```bash
./restore.sh --verificar /var/backups/forensicvm/forensicvm-AAAAMMDD-HHMMSS.tar.gz
```

A opção `--verificar` não altera nada. Confere todas as somas SHA-256 e mostra o manifesto (data, servidor,
versão, contagens). Um arquivo alterado, por exemplo com uma única linha acrescentada ao `MANIFEST`, é
**recusado** e nada é reposto.

```{figure} /_static/img/34-copias-troubleshooting/05b.jpg
:alt: restore.sh --verificar a validar as somas e a mostrar o manifesto

Verificação de um arquivo íntegro.
```

## Repor

```bash
./restore.sh /var/backups/forensicvm/forensicvm-AAAAMMDD-HHMMSS.tar.gz
```

O `restore.sh`:

1. volta a confirmar as somas SHA-256 e recusa um arquivo alterado;
2. avisa que vai substituir a base de dados e pede o **nome deste servidor**, para não repor no sítio
   errado;
3. guarda o estado atual em `/var/backups/forensicvm/pre-restauro/`;
4. pára o serviço, repõe a base de dados e confirma as contagens e os *triggers* do registo de auditoria;
5. repõe o `.env` e a configuração do sistema, recarrega o nginx e repõe os metadados das máquinas que
   faltem (nunca sobrescreve uma máquina que já exista);
6. volta a arrancar o serviço e só termina quando a API responde.

```{figure} /_static/img/34-copias-troubleshooting/07a.jpg
:alt: Saída do restore.sh com a confirmação pelo nome do servidor e os passos do restauro

O restauro, com a confirmação pelo nome do servidor.
```

Depois do restauro, os utilizadores voltam a entrar com a mesma palavra-passe e o **mesmo segundo fator**
de antes: também estavam na cópia.

## Resolver problemas

O método é sempre o mesmo:

1. Correr `./diagnose.sh`. Só lê, e cada problema traz a correção sugerida.
2. Ver o serviço em causa: `systemctl status <serviço>` e `journalctl -u <serviço>`.
3. Corrigir e voltar a correr o `./diagnose.sh`.

| Sintoma | Causa provável | Correção |
|---|---|---|
| O navegador mostra *502 Bad Gateway*. O ecrã de entrada diz que o servidor ForensicVM não está a responder. | Serviço `forensicvm` parado. | `./start.sh` e depois ver o `server.log`. |
| O ecrã de entrada diz que o servidor não consegue usar a base de dados. | MariaDB parado, ou base de dados apagada. | `systemctl start mariadb`. Se foi apagada, `./restore.sh <cópia>`. |
| O ecrã de entrada diz *Utilizador ou palavra-passe inválidos*. | Credenciais erradas (servidor e base de dados estão bem). | Ver a linha seguinte. |
| O administrador esqueceu a palavra-passe e/ou perdeu o autenticador. | | `apps/server/scripts/reset-admin-password.sh admin --clear-2fa` |
| Uma máquina virtual não arranca. | Ver o `run/qemu.log` da máquina. | Conforme a mensagem (disco em falta, KVM, memória). |
| Disco de dados quase cheio. | Máquinas ou aquisições antigas. | Apagar pela interface. `journalctl --vacuum-size=500M`. |

```{figure} /_static/img/34-copias-troubleshooting/08a.jpg
:alt: Página de entrada com a mensagem de erro quando o servidor não responde

A mensagem do ecrã de entrada quando o servidor da aplicação está parado.
```

### Recuperar o acesso do administrador

```bash
apps/server/scripts/reset-admin-password.sh admin --clear-2fa
```

Sem a opção `--password`, o script gera uma palavra-passe aleatória e mostra-a **uma única vez**. Com
`--clear-2fa`, apaga também o segundo fator. No acesso seguinte, o sistema obriga a configurá-lo de novo.

### Quando uma máquina virtual não arranca

- O registo de arranque da máquina está em `/forensicVM/mnt/vm/<uuid>/run/qemu.log`.
- A execução anterior fica em `qemu.log.prev`.
- O `diagnose.sh` lista as máquinas ligadas e indica este caminho.

## Em resumo

- **Cópia:** `./backup.sh`, guardada fora do servidor e agendada no cron.
- **Verificar:** `./restore.sh --verificar <arquivo>`, que recusa arquivos alterados.
- **Repor:** `./restore.sh <arquivo>`, que pede o nome do servidor e guarda antes o estado atual.
- **Diagnosticar:** `./diagnose.sh`, e depois `systemctl status` e `journalctl`.
- **Acesso perdido:** `apps/server/scripts/reset-admin-password.sh admin --clear-2fa`.
