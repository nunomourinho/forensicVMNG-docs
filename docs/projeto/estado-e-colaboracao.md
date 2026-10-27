# Estado do projeto e colaboração

Esta página descreve com franqueza o estado do ForensicVM NextGen: o que já está maduro, o que ainda está
a ser estabilizado e como se pode colaborar.

```{video} 23-estado-e-colaboracao
```

## De onde vem o projeto

- Nasceu de uma dissertação de mestrado na **Universidade Politécnica de Beja (Upbeja)**.
- O propósito original é a conversão de imagens forenses em máquinas virtuais.
- Desde fevereiro de 2026 foi reconstruído de raiz para a web, com uma arquitetura nova, mantendo os
  scripts de conversão do projeto original.

## O núcleo mais avançado

Converter uma imagem forense (VMDK, E01, AFF, RAW, QCOW2) numa máquina virtual arrancável e controlá-la
pelo navegador, com arranque, consola, snapshots e registo de ações. É o propósito original e a parte mais
madura do sistema.

## Nunca testado em casos reais

```{warning}
O ForensicVM NextGen **nunca foi usado em casos reais**. Todos os testes, incluindo as demonstrações
desta documentação, foram feitos com imagens forenses públicas do CFReDS (NIST). Nenhum resultado aqui
mostrado deve ser tomado como validação em contexto operacional.
```

## O que ainda está a ser estabilizado

```{figure} /_static/img/23-estado-e-colaboracao/05a.jpg
:alt: Funcionalidades em estabilização — funcionalidades ao vivo, CAPE e integrações de aquisição

As funcionalidades em estabilização.
```

| Área | Estado |
|---|---|
| **Funcionalidades forenses ao vivo** (introspeção de memória, plug-ins, consola, aquisição) | Entregues, a precisar de testes. |
| **CAPE, o laboratório de malware** | Em desenvolvimento ativo. Ainda não é considerado estável. Depende do agente dentro da máquina, que na conversão mais rápida (modo snapshot) não fica instalado. |
| **Integrações de aquisição** (Veeam, Proxmox, contentores LXC) | Entregues, mas ainda por validar em cenários reais. |

## A posição do projeto

- **Ainda não se recomenda** o ForensicVM NextGen para uso em produção.
- O projeto está disponível, desde já, **para testes**, com transparência total sobre o que funciona e o
  que ainda não funciona.

## Como colaborar

1. **Aponte o que melhorar:** o que falha, o que confunde, o que falta para o trabalho real.
2. **Proponha o que criar:** novas funcionalidades e novos plug-ins. As necessidades de quem investiga
   definem o rumo.
3. **Use-o para o que precisar:** experimente-o em casos de teste, no seu contexto.

A ambição é uma parceria entre a academia, que constrói, documenta e endurece a ferramenta, e quem pratica
forense digital, que a usa, testa e aponta o que realmente importa: pilotos, validação conjunta e um ciclo
de melhoria contínua.

Para comentários sobre esta documentação, use as
[*issues* do repositório da documentação](https://github.com/nunomourinho/forensicVMNG-docs/issues).
