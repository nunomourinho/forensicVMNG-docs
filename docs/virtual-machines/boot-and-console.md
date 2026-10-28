# Arranque e consola

Esta página mostra como arrancar a máquina convertida, acompanhar o registo de arranque e as capturas
automáticas, e trabalhar na consola do sistema a partir do navegador.

```{video} 05-arranque-e-consola
```

## O detalhe da máquina

Na lista de VMs, a máquina aparece com o nome do computador (por exemplo `DESKTOP-1K54EA2`) e o sistema
operativo detetado. O detalhe da máquina tem vários separadores: Visão geral, Hardware, Snapshots,
Multimédia, Rede, Forense, Plug-ins e Sandbox. A **Visão geral** mostra a identidade da imagem, as ações
disponíveis e o registo de arranque.

```{figure} /_static/img/05-arranque-e-consola/02a.jpg
:alt: Detalhe da máquina virtual com identidade, ações e registo de arranque

O detalhe da máquina, com o caso a que pertence.
```

## Arrancar e acompanhar o registo

Ao carregar em **Arrancar VM**, o registo de arranque mostra em direto o que o QEMU e o firmware estão a
fazer: a rede isolada, o monitor e o carregamento do gestor de arranque do sistema (por exemplo o Windows
Boot Manager).

```{figure} /_static/img/05-arranque-e-consola/03a.jpg
:alt: Registo de arranque em direto, com as ações Abrir consola, Captura de ecrã, Snapshot, Desligar e Parar forçado

Registo de arranque em direto.
```

Durante o arranque, o sistema tira **duas capturas automáticas**, aos 10 e aos 30 segundos. Servem para
confirmar, de relance, que a máquina arrancou bem, sem ser preciso abrir a consola.

```{tip}
Se uma máquina não arrancar, o registo de arranque é o primeiro sítio a ver. O registo da execução
anterior também é guardado, para comparação.
```

## A consola no navegador

**Abrir consola** mostra o ecrã da máquina dentro do navegador, sem instalar nada. A consola usa um
servidor VNC disponibilizado pelo próprio QEMU. O investigador controla a máquina como se estivesse à
frente dela, mas o indício fica sempre no servidor.

```{figure} /_static/img/05-arranque-e-consola/05a.jpg
:alt: Consola no navegador com o ecrã de bloqueio do Windows 11

A consola no navegador, com o Windows a chegar ao ecrã de bloqueio.
```

A barra da consola tem o teclado, a aquisição (capturas e gravação), os snapshots, o hardware, os
plug-ins, os processos, os dispositivos (CD, disquete, USB), a rede e o menu de energia. Veja
{doc}`console`.

## Teclado e atalhos

Combinações especiais, como **Ctrl+Alt+Del**, enviam-se pelo **menu de atalhos de teclado** da barra da
consola, porque o navegador não as deixaria passar diretamente.

```{figure} /_static/img/05-arranque-e-consola/06a.jpg
:alt: Ecrã de início de sessão do Windows depois de enviar Ctrl+Alt+Del

O ecrã de início de sessão, depois de enviar Ctrl+Alt+Del pelo menu de atalhos.
```

Próximo passo: {doc}`account-access`.
