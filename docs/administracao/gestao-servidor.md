# Gerir o servidor

O lado técnico do servidor ForensicVM: que serviços o compõem, como se param e arrancam sem desligar as
máquinas virtuais, onde estão os registos e como se atualiza com um único comando.

```{video} 33-gestao-operacao
```

## Os serviços

```{figure} /_static/img/33-gestao-operacao/02a.jpg
:alt: Os quatro componentes do ForensicVM — nginx, forensicvm.service, MariaDB e forensicvm-vms.slice

Os componentes do servidor.
```

| Serviço | Papel |
|---|---|
| `nginx` | Servidor web: entrega a interface e encaminha `/api` e `/socket.io` para o servidor da aplicação. |
| `forensicvm` | O servidor da aplicação (Node.js), em `127.0.0.1:3000`. |
| `mariadb` | Base de dados: utilizadores, casos, registo de auditoria, metadados. |
| `forensicvm-vms.slice` | Onde correm as máquinas virtuais (QEMU/KVM), cada uma no seu próprio *scope* do systemd. Por isso sobrevivem a um reinício do servidor da aplicação. |
| `cape*` | Opcional: análise de malware. |

```bash
systemctl status forensicvm nginx mariadb --no-pager
systemd-cgls -u forensicvm-vms.slice      # máquinas virtuais ligadas
ls /forensicVM/mnt                        # vm/ iso/ acquire/: os discos de dados
```

```{figure} /_static/img/33-gestao-operacao/05a.jpg
:alt: Saída de systemctl status com os três serviços ativos

Os três serviços ativos.
```

Os dados ficam em `/forensicVM/mnt` (aquisições, máquinas virtuais, ISOs). **Em produção, cada uma destas
pastas deve estar num disco próprio.** A definição do serviço tem uma linha `RequiresMountsFor` com essas
pastas: se algum disco de dados não estiver montado, o serviço recusa arrancar, em vez de encher o disco
do sistema.

## Parar e arrancar

```bash
./stop.sh                       # pára o servidor; as máquinas virtuais ligadas continuam a correr
./start.sh                      # arranca-o e volta a encontrar as máquinas
systemctl restart forensicvm    # reiniciar (por exemplo, depois de editar o .env)
```

Com o serviço parado, o nginx responde `502 Bad Gateway` aos pedidos à API.

```{note}
Antes de desligar o servidor físico, desligue primeiro as máquinas virtuais pela interface, ou a partir de
dentro de cada uma.
```

## Registos

```bash
tail -f /var/log/forensicvm/server.log            # o servidor da aplicação
journalctl -u forensicvm -n 50 --no-pager         # arranques, falhas e reinícios do systemd
tail -50 /forensicVM/mnt/vm/<uuid>/run/qemu.log   # porque é que uma máquina virtual não arrancou
```

O `server.log` é rodado diariamente pelo `logrotate`, que guarda 90 dias comprimidos.

## Atualizar

```bash
./backup.sh       # antes de atualizar, uma cópia de segurança
./update.sh       # código, Node.js, dependências, migrações, compilação e reinício
./diagnose.sh     # confirmar que ficou tudo bem
```

O `update.sh`:

- atualiza o código e, se for preciso, o Node.js para a versão exigida;
- recompila os módulos nativos e instala as dependências;
- aplica as migrações da base de dados, dando ao utilizador da aplicação permissões de alteração só
  durante esse passo;
- atualiza os pacotes e as ferramentas do sistema;
- compila o servidor e a interface, publica-a no nginx e reinicia o serviço.

```{figure} /_static/img/33-gestao-operacao/04b.jpg
:alt: Saída do update.sh com os passos da atualização

A atualização em curso (cerca de 6 minutos na demonstração).
```

```{tip}
Numa instalação muito antiga, em que o `update.sh` ainda não seja executável, traga primeiro o código com
`git pull` e só depois corra o `./update.sh`.
```

## Verificar

O `diagnose.sh` só lê o sistema e não altera nada. Verifica os serviços, a API, a base de dados, os
discos e o espaço livre, a virtualização, o registo do servidor e as máquinas ligadas. Cada problema
aparece assinalado com ✗ e com a correção sugerida (→).

```bash
./diagnose.sh
```

```{figure} /_static/img/33-gestao-operacao/08a.jpg
:alt: Saída do diagnose.sh sem problemas encontrados

O diagnóstico, sem problemas encontrados.
```
