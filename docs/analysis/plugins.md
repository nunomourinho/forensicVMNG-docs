# Plug-ins

O ForensicVM traz um catálogo de **plug-ins**: pequenas ações forenses que o investigador corre sobre a
máquina sem sair do navegador. São repetíveis (o mesmo plug-in faz o mesmo em todos os casos) e ficam
todos no registo de auditoria.

```{video} 07-plugins
```

## O catálogo

O separador **Plug-ins** do detalhe da máquina lista os plug-ins disponíveis. Cada um diz o que faz e que
parâmetros aceita. Podem filtrar-se por sistema operativo (Windows, Linux), e distinguem-se dois tipos:

- **Online:** correm com a máquina **ligada** e usam o agente do QEMU dentro do sistema convidado.
- **Offline:** correm com a máquina **parada** e atuam diretamente no disco, sempre depois de um
  snapshot automático.

```{figure} /_static/img/07-plugins/02a.jpg
:alt: Catálogo de plug-ins com filtros por sistema operativo e botões executar offline e online

O catálogo de plug-ins.
```

## Correr um comando (online)

O plug-in **SYSTEM Exec** pede à máquina que corra um comando (por exemplo `systeminfo`) e devolve o
resultado. A resposta vem do Windows em funcionamento, através do agente.

```{figure} /_static/img/07-plugins/03b.jpg
:alt: Resultado do comando systeminfo devolvido pelo plug-in SYSTEM Exec

Resultado de um comando corrido na máquina.
```

## Extrair um ficheiro (online)

O plug-in **File Pull** extrai um ficheiro do sistema convidado para o servidor: no exemplo, o ficheiro
de anfitriões `C:\Windows\System32\drivers\etc\hosts`. O resultado fica disponível para transferir e
analisar. A leitura é feita pelo agente e nada é escrito no disco do indício.

```{figure} /_static/img/07-plugins/04b.jpg
:alt: Conteúdo do ficheiro hosts extraído pelo plug-in

Um ficheiro extraído da máquina.
```

```{note}
Os plug-ins online precisam do agente do QEMU. Numa máquina convertida em modo snapshot, instale-o
primeiro com o plug-in offline *Install QEMU Guest Agent* (veja {doc}`../virtual-machines/qemu-agent`).
```

## Em resumo

- **Online, pelo agente:** correr comandos e extrair ficheiros da máquina em funcionamento.
- **Offline, sobre o disco:** com a máquina parada, atua-se no disco, depois de um snapshot.
- Em ambos os casos, a imagem original e o seu *hash* não são tocados e tudo fica no registo de
  auditoria.
