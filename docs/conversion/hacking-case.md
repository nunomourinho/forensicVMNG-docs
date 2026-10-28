# Hacking Case (NIST): um Windows XP

Esta página faz o percurso completo com a segunda imagem do CFReDS, o *Hacking Case* do NIST: o portátil
Dell Latitude de Greg Schardt, com Windows XP. Mostra que o mesmo fluxo serve tanto para sistemas
modernos como para sistemas antigos.

```{video} 13-hacking-case
```

## Obter a imagem

No portal CFReDS encontra-se o caso *Hacking Case* e os ficheiros da imagem, disponíveis em vários
formatos. Escolhe-se o formato E01 e descarregam-se os segmentos para a pasta de aquisições do servidor.

```{figure} /_static/img/13-hacking-case/02b.jpg
:alt: Página do Hacking Case no CFReDS com as ligações para os segmentos

Os segmentos da imagem no portal CFReDS.
```

```{figure} /_static/img/13-hacking-case/03a.jpg
:alt: Download dos segmentos da imagem no navegador

Download dos segmentos (acelerado no vídeo).
```

## Converter

No assistente escolhem-se o caso, o equipamento (o portátil de Greg Schardt), a imagem e o modo
snapshot, e inicia-se a conversão. O navegador de pastas do servidor mostra os ficheiros disponíveis.

```{figure} /_static/img/13-hacking-case/04a.jpg
:alt: Assistente de conversão com o caso e o portátil do Hacking Case escolhidos

O assistente, com o equipamento do Hacking Case.
```

```{figure} /_static/img/13-hacking-case/04b.jpg
:alt: Navegador de pastas do servidor com a imagem E01 selecionada

Escolha da imagem no navegador de pastas do servidor.
```

A ferramenta reconhece o Windows XP, regista o controlador de disco como crítico e deteta que esta
máquina, por ser antiga, precisa de arrancar em **BIOS** e não em UEFI. É a mesma conversão do Windows
11, adaptada a um sistema de 2004.

```{figure} /_static/img/13-hacking-case/05a.jpg
:alt: Registo da conversão do Windows XP

O registo da conversão do Windows XP.
```

## Arrancar

O registo de arranque mostra o arranque em BIOS, e as capturas automáticas confirmam que o Windows XP
está a carregar. Na consola surge o ambiente de trabalho clássico do Windows XP, pronto a examinar.

```{figure} /_static/img/13-hacking-case/06a.jpg
:alt: Detalhe da máquina com o registo de arranque em BIOS

Arranque em BIOS, com o registo em direto.
```

```{figure} /_static/img/13-hacking-case/07a.jpg
:alt: Ambiente de trabalho do Windows XP na consola do navegador

O ambiente de trabalho do Windows XP, na consola do navegador.
```

## Em resumo

Do Windows 11 ao Windows XP, o fluxo é o mesmo: download, verificação, conversão e arranque. O firmware
(BIOS ou UEFI) é detetado automaticamente e pode ser ajustado depois (veja
{doc}`../virtual-machines/hardware`).
