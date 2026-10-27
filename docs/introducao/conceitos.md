# Conceitos fundamentais

Esta página explica as ideias em que assenta o ForensicVM. Convém lê-la antes das restantes, sobretudo
se a virtualização forense for nova para si.

## Virtualização forense

Na forense tradicional, a imagem de disco é examinada "a frio": monta-se só de leitura e analisam-se os
ficheiros, o registo do Windows e os artefactos com ferramentas próprias. É o método de referência e
continua a sê-lo.

A virtualização forense **complementa** esse exame. Põe o sistema apreendido a correr, para observar o
que só se vê com ele vivo: o ambiente de trabalho tal como o utilizador o via, as aplicações abertas, as
sessões em serviços na nuvem, o comportamento de um programa suspeito, os processos em memória, as
ligações de rede. O desafio é fazê-lo **sem alterar o indício** e documentando tudo o que se faz.

## Camadas: a imagem original nunca é escrita

O ForensicVM nunca escreve na imagem adquirida. A máquina virtual é construída em camadas, cada uma por
cima da anterior:

```{figure} /_static/img/04-injecao-de-drivers/03a.jpg
:alt: Diagrama das camadas — camada de trabalho, snapshot de prata, snapshot de ouro e imagem original

Onde ficam as alterações: a imagem original na base e as camadas de trabalho por cima.
```

| Camada | Conteúdo | Proteção |
|---|---|---|
| **Imagem original** (E01, RAW…) | O indício, tal como foi adquirido. | Montada só de leitura; nunca é escrita. |
| **{term}`Snapshot de ouro`** | O estado exato da imagem, antes de qualquer alteração. | Protegido; não se apaga. |
| **{term}`Snapshot de prata`** | O estado depois da injeção de controladores, antes do primeiro arranque. | Protegido. |
| **Camada de trabalho** | Tudo o que acontece com a máquina a correr. | Pode ser cifrada; pode voltar-se atrás a qualquer momento. |

Se algo correr mal, volta-se em segundos ao snapshot de prata ou ao de ouro. O *hash* da imagem original
continua sempre a coincidir com o da aquisição.

## Modo snapshot e modo cópia

Na conversão escolhe-se um de dois modos:

- **Modo snapshot.** A máquina usa a imagem original diretamente, como base só de leitura. Arranca
  depressa e quase não ocupa espaço em disco, mas depende da imagem de origem continuar disponível. A
  injeção de controladores limita-se ao essencial para arrancar, e o agente do QEMU não fica instalado.
  Veja {doc}`../maquinas-virtuais/agente-qemu`.
- **Modo cópia.** O disco é copiado para um ficheiro próprio. Demora mais e ocupa mais espaço, mas a
  máquina fica independente da fonte e a conversão instala também o agente do QEMU.

## Análise "online" e "offline"

Muitas ferramentas do ForensicVM existem em duas variantes:

- **Online (em direto):** atuam sobre a máquina em funcionamento. Umas usam o **agente do QEMU**
  instalado dentro do sistema convidado: correr um comando, extrair um ficheiro, gerir serviços. Outras
  leem a memória **de fora**, a partir do hipervisor, sem depender de nada instalado na máquina.
- **Offline:** atuam sobre o disco com a máquina parada, sempre depois de um snapshot.

A leitura feita de fora, pelo hipervisor (*virtual machine introspection*), tem uma vantagem forense
importante: não deixa rasto dentro do sistema examinado e é mais difícil de enganar por um malware que
esteja a correr lá dentro.

## Casos, equipamentos e papéis

Tudo no ForensicVM pertence a um **caso**. Um caso agrupa:

- os **equipamentos** apreendidos (computadores, portáteis…), com marca, modelo e número de série;
- as **máquinas virtuais** criadas a partir das imagens desses equipamentos;
- os **membros** da equipa que lhes podem aceder, cada um com um papel.

| Papel | Pode |
|---|---|
| Leitor | Consultar. |
| Investigador | Consultar e operar as máquinas virtuais. |
| Gestor | O anterior, mais gerir membros e equipamentos. |
| Proprietário | O anterior, mais fechar e arquivar o caso. |

Um caso fechado ou arquivado passa a ser só de consulta para todos menos o proprietário. As permissões
podem ainda ser afinadas por equipamento ou por disco.

## Registo de auditoria e cadeia de custódia

Cada ação (converter, arrancar, correr um plug-in, capturar memória, criar um snapshot…) fica registada
com o utilizador, a hora e a máquina. O registo é **imutável**: a base de dados impede que as entradas
sejam alteradas ou apagadas.

```{important}
O {term}`registo de auditoria` **não é a cadeia de custódia em si**. É um registo de ações que a
**apoia e documenta**. A cadeia de custódia continua a ser responsabilidade do perito e da organização,
segundo os seus procedimentos.
```

## Segurança do acesso

- **Segundo fator obrigatório** para todas as contas: aplicação de autenticação (TOTP) ou chave de
  segurança FIDO2 (YubiKey, Windows Hello, Touch ID).
- **Cifra em repouso** opcional dos discos das máquinas virtuais (LUKS).
- **Rede isolada por omissão:** as máquinas virtuais não têm rede até o investigador decidir ligá-la.
