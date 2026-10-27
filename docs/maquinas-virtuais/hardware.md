# Hardware e firmware

O hardware virtual da máquina é configurável: memória e núcleos de CPU, perfil de firmware e os
requisitos do Windows 11 (TPM 2.0 e Arranque Seguro), emulados por software.

```{video} 12-hardware
```

Todas estas opções estão no separador **Hardware** do detalhe da máquina. As alterações entram em vigor
no **próximo arranque** da máquina.

## Memória

Escolhe-se o valor (há atalhos para 2, 4 e 8 GB) e carrega-se em **Aplicar**.

```{figure} /_static/img/12-hardware/02b.jpg
:alt: Configuração da memória da máquina virtual com atalhos 2, 4 e 8 GB

Configuração da memória.
```

## Núcleos de CPU

Escolhe-se o número de núcleos virtuais. O Windows 11 exige pelo menos dois.

## Perfil de firmware

O perfil de firmware é detetado na conversão: **UEFI** para sistemas modernos, **BIOS** para sistemas
antigos como o Windows XP. Pode também ser forçado manualmente, se a deteção não acertar.

```{figure} /_static/img/12-hardware/04a.jpg
:alt: Perfil de firmware BIOS, UEFI ou automático, e requisitos do Windows 11

O perfil de firmware e os requisitos do Windows 11.
```

## Requisitos do Windows 11: TPM 2.0 e Arranque Seguro

O ForensicVM pode emular por software um **TPM 2.0** e o **Arranque Seguro** (*Secure Boot*), quando são
precisos: por exemplo, para arrancar uma instalação de Windows 11 que os exija ou para abrir discos com
BitLocker. Ficam desligados por omissão e ligam-se quando a investigação precisar.

```{figure} /_static/img/12-hardware/05a.jpg
:alt: Opções de TPM 2.0 e Arranque Seguro desligadas, cache de leitura e ajuste de relógio

TPM 2.0, Arranque Seguro e outras opções de hardware.
```

## Outras opções

No mesmo separador encontram-se ainda:

- **Cache de leitura local:** acelera máquinas em modo snapshot cuja imagem está num armazenamento lento.
- **Ajuste de relógio (RTC):** arranca a máquina com uma data e hora definidas. É útil para reproduzir o
  contexto temporal do indício.
- **Placa de rede (hotplug):** adiciona uma placa de rede com a máquina em execução.
- **Discos e encriptação:** veja {doc}`encriptacao-discos`.

Com o hardware e o firmware ajustados, a máquina reproduz fielmente o computador apreendido.
