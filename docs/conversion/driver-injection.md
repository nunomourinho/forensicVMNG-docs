# Injeção de drivers

Esta página explica porque é que um Windows apreendido não arranca tal como está numa máquina virtual, e
como o ForensicVM injeta os controladores necessários sem tocar na imagem original.

```{video} 04-injecao-de-drivers
```

## O problema

Um disco apreendido traz o Windows configurado para o hardware original. Numa máquina virtual, o
controlador de disco é outro, e o Windows não o conhece:

- o Windows só arranca se conhecer o controlador do disco de arranque;
- sem esse controlador, pára com o erro `INACCESSIBLE_BOOT_DEVICE` (ecrã azul) ou cai no ambiente de
  recuperação (WinRE);
- a solução clássica é preparar cada máquina à mão, instalando os drivers. Demora horas e mexe no
  indício.

O ForensicVM faz isto automaticamente, durante a conversão.

## Onde ficam as alterações

As alterações nunca vão para a imagem original:

1. Primeiro, cria-se o {term}`snapshot de ouro`, com o estado exato do indício.
2. Os drivers vão para uma camada por cima, guardada como {term}`snapshot de prata`.
3. O trabalho do investigador vai para uma terceira camada.

```{figure} /_static/img/04-injecao-de-drivers/03a.jpg
:alt: Diagrama das quatro camadas da máquina virtual

As camadas: imagem original, snapshot de ouro, snapshot de prata e camada de trabalho.
```

## O registo da conversão

No registo da conversão pode acompanhar-se cada passo:

1. **Snapshot de ouro:** criado antes de qualquer alteração.
2. **Inspeção:** a ferramenta abre a imagem e identifica o sistema operativo. Um Windows 11 aparece como
   *Windows 10 Pro*, porque continua a identificar-se assim no registo do Windows.
3. **Conversão para KVM:** se a imagem já traz os controladores VirtIO, a ferramenta confirma-os em vez
   de os reinstalar. Deteta também se a máquina precisa de firmware UEFI ou BIOS.
4. **Controlador de arranque:** o controlador de disco `viostor` é registado como crítico para o
   arranque (*CriticalDeviceDatabase*). Sem este passo, o Windows não encontraria o disco no primeiro
   arranque.

```{figure} /_static/img/04-injecao-de-drivers/04a.jpg
:alt: Registo da conversão com a criação do snapshot de ouro e a inspeção do sistema

O snapshot de ouro e o início da inspeção do sistema operativo.
```

```{figure} /_static/img/04-injecao-de-drivers/04b.jpg
:alt: Registo da conversão com o registo do viostor como controlador crítico

O registo do `viostor` como controlador crítico para o arranque.
```

## O que muda, e o que não muda

| | |
|---|---|
| **Muda** | O registo `SYSTEM`, para marcar o `viostor` como crítico, e os controladores em falta. Só na camada de prata. |
| **Não muda** | A imagem E01 e o seu *hash*, que continuam a coincidir com os da aquisição. |
| **Se algo correr mal** | Volta-se ao snapshot de prata ou ao de ouro, em segundos. |

```{note}
No **modo snapshot**, a injeção limita-se ao essencial para o arranque e o agente do QEMU não fica
instalado. Se precisar dos plug-ins online, veja {doc}`../virtual-machines/qemu-agent`.
```

Próximo passo: {doc}`../virtual-machines/boot-and-console`.
