# Instalar o agente QEMU num indício em modo snapshot

Um indício convertido em **modo snapshot** fica sem o agente QEMU (*QEMU Guest Agent*), e os plug-ins
online que dependem dele deixam de funcionar. O plug-in **Install QEMU Guest Agent** resolve isto
offline, antes do primeiro arranque, sem descarregar nada da internet.

```{video} 29-instalar-agente
```

## O sintoma

Numa máquina convertida em modo snapshot, um plug-in online (por exemplo o **SYSTEM Exec**, que corre um
comando com privilégios de SISTEMA através do agente) fica à espera e acaba em erro: não há agente do
lado de lá.

```{figure} /_static/img/29-instalar-agente/02a.jpg
:alt: Plug-in SYSTEM Exec à espera de resposta numa máquina sem agente

Um plug-in online sem resposta, por falta de agente.
```

## Porque acontece

| Modo | Ferramenta de conversão | Agente QEMU |
|---|---|---|
| **Snapshot** (rápido) | `virt-v2v-in-place`, que injeta só os controladores de disco | Não fica instalado |
| **Cópia** (completo) | `virt-v2v` completo | Instalado automaticamente no primeiro arranque |

Sem o agente (e o controlador `virtio-serial`), os plug-ins online ficam cegos.

## O plug-in Install QEMU Guest Agent

O plug-in corre **com a máquina parada, antes do primeiro arranque**. Não precisa do agente para
instalar o agente.

- A fonte é a imagem `virtio-win.iso` que o instalador do ForensicVM já deixou no servidor. Nada é
  descarregado no momento.
- O indício original nunca é tocado: a ação fica numa nova camada, por cima.

```{figure} /_static/img/29-instalar-agente/04a.jpg
:alt: Catálogo de plug-ins filtrado com o plug-in Install QEMU Guest Agent

O plug-in no catálogo.
```

## Executar

1. Com a máquina parada, abra **Plug-ins** e procure *Install QEMU Guest Agent*.
2. Indique a pasta de drivers que corresponde à versão do Windows (por exemplo `w10`).
3. Carregue em **Executar offline**. O plug-in monta a `virtio-win.iso`, extrai o controlador
   `virtio-serial` e o instalador do agente, e deixa-os prontos para correr automaticamente no próximo
   arranque real da máquina.

```{figure} /_static/img/29-instalar-agente/05b.jpg
:alt: Execução offline do plug-in com o registo dos passos

Execução offline do plug-in.
```

## O resultado

No primeiro arranque, o Windows instala o controlador e o agente sozinho. O mesmo plug-in online passa
então a responder, e todo o catálogo online volta a estar disponível: extrair ficheiros, correr comandos,
inspecionar controladores.

```{figure} /_static/img/29-instalar-agente/06b.jpg
:alt: Plug-in SYSTEM Exec a responder depois de reiniciar a máquina

Depois de reiniciar, o plug-in online já responde.
```

## Em resumo

- A conversão em modo snapshot continua rápida, e o investigador já não fica sem plug-ins online.
- Nada se descarrega da internet. A fonte é local, já verificada pelo instalador.
- A ação fica no registo de auditoria, como qualquer outro plug-in.
