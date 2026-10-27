# ForensicVM NextGen

**Virtualização forense, do laboratório ao tribunal.**

O ForensicVM NextGen é uma plataforma web que converte imagens forenses de disco (E01/EWF, AFF, RAW,
VMDK, QCOW2) em máquinas virtuais arrancáveis, controladas a partir do navegador. Com ele, o perito pode
ver o sistema apreendido *a funcionar*: o ambiente de trabalho do utilizador, as aplicações, a memória, o
tráfego de rede. E a imagem original nunca é alterada.

```{figure} /_static/img/32-resumo-sistema/03a.jpg
:alt: Arquitetura em camadas do ForensicVM — navegador, servidor, máquinas QEMU/KVM e imagem original

As quatro camadas do ForensicVM. O navegador fala com um servidor que gere casos, permissões e
auditoria. As máquinas virtuais correm em QEMU/KVM, sobre camadas que protegem a imagem original.
```

## O problema que resolve

Um disco apreendido é um indício. Tem de ser preservado sem alterações, e o seu *hash* tem de continuar
a coincidir com o da aquisição. Mas, para compreender o que o utilizador fazia, é muitas vezes muito útil
pôr o sistema a correr. Conciliar as duas exigências à mão é lento, arriscado e difícil de documentar.

O ForensicVM faz essa ponte:

- **Preserva o indício.** A imagem é montada só de leitura. Tudo o que muda fica em camadas por cima, a
  começar pelo {term}`snapshot de ouro`.
- **Põe o sistema a correr.** Injeta automaticamente os controladores necessários para o Windows ou o
  Linux arrancarem em hardware virtual.
- **Dá as ferramentas de análise.** Consola no navegador, plug-ins, captura de memória e análise com o
  Volatility3, captura de tráfego, introspeção de processos e análise de malware em *sandbox*.
- **Documenta tudo.** Cada ação fica num {term}`registo de auditoria` imutável, associada a um caso, a
  um utilizador e a uma hora.

```{warning}
**Estado do projeto.** O ForensicVM NextGen está em desenvolvimento ativo e **ainda não é recomendado
para uso em produção**. Todos os testes, incluindo as demonstrações desta documentação, foram feitos com
imagens forenses públicas do [CFReDS](https://cfreds.nist.gov/) (NIST), nunca em casos reais. Veja
{doc}`projeto/estado-e-colaboracao`.
```

## Por onde começar

- **Quer uma visão geral?** Comece por {doc}`introducao/visao-geral`: o sistema inteiro em sete minutos.
- **Vai usar a plataforma?** Siga {doc}`comecar/primeiros-passos` e depois a ordem das secções no menu.
  Corresponde ao percurso de um exame: do caso à conversão, à máquina virtual, à análise e ao relatório.
- **Vai instalar um servidor?** Vá a {doc}`instalacao/index`.
- **Administra um servidor já instalado?** Veja {doc}`administracao/index`.

Cada página corresponde a um vídeo de demonstração, gravado com operações reais sobre imagens públicas.
O vídeo aparece no topo da página. As imagens e o texto foram adaptados desses vídeos.

```{toctree}
:caption: Introdução
:maxdepth: 2

introducao/o-que-e
introducao/conceitos
introducao/visao-geral
```

```{toctree}
:caption: Começar
:maxdepth: 2

comecar/primeiros-passos
comecar/casos-e-equipa
```

```{toctree}
:caption: Utilização
:maxdepth: 2

conversao/index
maquinas-virtuais/index
analise/index
malware/index
gestao/index
```

```{toctree}
:caption: Instalação e administração
:maxdepth: 2

instalacao/index
administracao/index
```

```{toctree}
:caption: Projeto
:maxdepth: 1

projeto/estado-e-colaboracao
glossario
```
