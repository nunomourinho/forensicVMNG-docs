# Instalar o CAPE

A instalação do módulo de análise de malware CAPE faz-se toda a partir da consola de administração do
ForensicVM, sem linha de comandos. Para saber para que serve o CAPE, veja {doc}`../malware/cape`.

```{video} 21-cape-instalacao
```

## As três fases

1. **Módulo CAPEv2:** o laboratório de análise, instalado no servidor.
2. **ISO do Windows:** o sistema que a máquina de análise vai correr.
3. **Máquina de análise:** um Windows isolado e descartável, com um snapshot limpo para onde reverte
   depois de cada amostra.

## O painel Sandbox CAPEv2

Em **Administração → Sandbox CAPEv2** está tudo reunido: o estado do módulo, os serviços, a interface
web e as máquinas de análise registadas.

```{figure} /_static/img/21-cape-instalacao/03a.jpg
:alt: Painel Sandbox CAPEv2 da administração com as fases e o estado das máquinas de análise

O painel Sandbox CAPEv2.
```

## Descarregar o ISO do Windows

O ISO do Windows (10 ou 11) é descarregado diretamente da Microsoft, a partir da própria consola. O
progresso aparece ao vivo. É um ficheiro grande: na demonstração demorou cerca de 47 minutos.

```{figure} /_static/img/21-cape-instalacao/04a.jpg
:alt: Download do ISO do Windows 11 com o registo do progresso

Descarregar o ISO do Windows.
```

## Construir a máquina de análise

Com o ISO pronto, o ForensicVM constrói a máquina de análise sozinho:

- instala o Windows de forma desatendida;
- instala o agente do CAPE;
- grava um snapshot limpo.

É a fase mais longa (cerca de 74 minutos na demonstração) e decorre em segundo plano, sem intervenção.

```{figure} /_static/img/21-cape-instalacao/05a.jpg
:alt: Construção da máquina de análise com o registo da instalação desatendida

A construir a máquina de análise.
```

## Pronto

No fim, a máquina de análise aparece registada e com o snapshot limpo. O CAPE fica pronto a receber
amostras. Veja {doc}`../malware/cape-utilizacao`.

```{figure} /_static/img/21-cape-instalacao/06a.jpg
:alt: Painel Sandbox CAPEv2 com o módulo instalado, serviços ativos e máquinas registadas

Instalação concluída.
```
