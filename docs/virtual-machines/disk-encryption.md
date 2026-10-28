# Encriptar e desencriptar discos

Os discos das máquinas virtuais podem ser cifrados em repouso com **LUKS**. Esta página mostra como
desencriptar (ou encriptar) um disco já existente, sem perder dados.

```{video} 30-desencriptar-disco
```

## Política de cifra

- Por omissão, os **discos novos não são cifrados**, porque a cifra pesa no processador, sobretudo em
  servidores mais antigos.
- Um administrador pode ligar a opção de cifrar os discos novos por omissão. Exige que o servidor tenha
  uma chave-mestra de cifra configurada.
- **Qualquer disco existente** pode ser cifrado ou decifrado a qualquer momento, com a máquina parada.

```{warning}
As chaves dos discos cifrados dependem da chave-mestra do servidor (`DISK_ENCRYPTION_MASTER_KEY`). Sem
ela, os discos cifrados **não se recuperam**. Guarde-a com as cópias de segurança (veja
{doc}`../administration/backups-and-troubleshooting`).
```

## Desencriptar um disco

1. Com a máquina **parada**, abra o separador **Hardware** e o cartão **Discos e encriptação**. Cada
   disco mostra se está cifrado.
2. Carregue em **Desencriptar** no disco pretendido.
3. Leia o aviso: o disco inteiro é reescrito sem cifra, e o resultado é verificado contra o original
   antes de o substituir. Pode demorar e precisa de espaço livre no servidor.

```{figure} /_static/img/30-desencriptar-disco/02a.jpg
:alt: Diálogo de confirmação para desencriptar o disco sda

Confirmação da desencriptação.
```

4. Se a máquina tiver snapshots de memória, o sistema pede uma confirmação adicional: a operação não
   lhes toca, mas restaurá-los depois deixa de estar garantido.

```{figure} /_static/img/30-desencriptar-disco/02b.jpg
:alt: Aviso de que a máquina tem snapshots, com a opção de continuar

Aviso sobre os snapshots existentes.
```

## Conversão e verificação

O disco é reescrito para um ficheiro novo, ao lado do original, que não é tocado. Uma barra mostra o
progresso. Na demonstração, um disco de 80 GB com cerca de 29 GB ocupados demorou menos de um minuto.

Depois, o disco novo é **verificado**: a estrutura e, byte a byte, o conteúdo, comparado com o original.
Só se forem idênticos é que o substitui. Se houvesse a mínima diferença, o original ficava como estava.

```{figure} /_static/img/30-desencriptar-disco/03b.jpg
:alt: Barra de progresso da conversão do disco

A converter o disco.
```

```{figure} /_static/img/30-desencriptar-disco/04b.jpg
:alt: Verificação do disco novo concluída, com a notificação de disco desencriptado

Verificação concluída: disco desencriptado.
```

```{note}
Se o servidor reiniciar a meio da operação, o original continua intacto e a operação é recuperada no
arranque seguinte.
```

## Em resumo

- Cifrar ou decifrar é uma decisão por disco, tomada com a máquina parada e sem perda de dados.
- O original fica protegido até o resultado estar verificado, e só é removido no fim.
- As operações ficam no registo de auditoria.
