# A consola, o posto de comando

A consola noVNC não é só o ecrã da máquina. É a interface principal de trabalho do ForensicVM: na barra
inferior tem tudo o que é preciso, sem sair da sessão.

```{video} 17-consola
```

## A barra da consola

Na barra inferior encontram-se, da esquerda para a direita: **aquisição**, **snapshots**, **teclado**,
**hardware**, **discos**, **plug-ins**, **processos**, **CD**, **disquete**, **USB**, **rede** e
**energia**.

```{figure} /_static/img/17-consola/02a.jpg
:alt: Consola com um Windows 11 em execução e a barra de ferramentas inferior

A consola, com a barra de ferramentas em baixo.
```

## CD-ROM: inserir uma ISO

Pode montar-se uma imagem ISO no leitor de CD virtual (por exemplo os controladores VirtIO ou uma
ferramenta de análise) diretamente a partir da biblioteca **Multimédia**, sem parar a máquina.

## USB: ligar uma pen

Da mesma forma, liga-se uma imagem de pen USB à máquina. É útil para introduzir ferramentas, ou para
montar a imagem de uma pen apreendida num ambiente controlado.

```{figure} /_static/img/17-consola/03b.jpg
:alt: Painel de imagem USB virtual com uma imagem de pen selecionada

Ligar uma imagem de pen USB à máquina.
```

## Hardware e discos

O hardware da máquina (memória, relógio, placa de rede) e os discos que a compõem também se consultam na
consola, sem mudar de ecrã.

```{figure} /_static/img/17-consola/04b.jpg
:alt: Painel de hardware na consola com memória, relógio e placa de rede

O painel de hardware, aberto na consola.
```

## Capturas de ecrã e vídeo

Para documentar o exame, o botão de **aquisição** tira capturas de ecrã e grava vídeo da sessão. A
gravação fica a correr com um indicador vermelho. No fim, o vídeo e as capturas ficam guardados no
servidor, prontos a juntar ao processo. Veja {doc}`../analysis/recording`.

```{figure} /_static/img/17-consola/06b.jpg
:alt: Painel de aquisição com capturas de ecrã, gravação em curso e evidências

O painel de aquisição, com uma gravação em curso.
```
