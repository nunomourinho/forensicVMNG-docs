# Gestor de processos

Numa análise forense, é essencial saber o que está a correr dentro da máquina. O gestor de processos do
ForensicVM mostra-o ao vivo, tem duas origens de dados e liga cada processo ao laboratório de malware
CAPE e ao VirusTotal.

```{video} 31-gestor-processos
```

## Dois modos

O gestor abre-se na barra da consola e fica ao lado do ecrã da máquina, que continua visível. No topo
escolhe-se a origem dos dados:

| Origem | Como funciona | Vantagens |
|---|---|---|
| **Agente (rápido)** | Fala com o agente QEMU instalado dentro da máquina. | Resposta imediata. Mostra a percentagem de CPU calculada dentro da máquina, a prioridade e a memória usada. Permite gerir serviços. |
| **Memória (sem agente)** | Lê os processos diretamente da memória da máquina, a partir do servidor. | Não precisa de nada instalado na máquina. É uma visão mais difícil de falsear por um malware que esteja a correr lá dentro. Permite o dump da memória de um processo. |

Cada coluna ordena a lista (por CPU, por memória…).

```{figure} /_static/img/31-gestor-processos/02a.jpg
:alt: Gestor de processos na origem Agente rápido com a percentagem de CPU por processo

O gestor de processos na origem *Agente (rápido)*.
```

## Serviços

Por baixo dos processos ficam os **serviços**, com o estado, o modo de arranque e o processo que os
executa. Com o agente, podem **iniciar-se** e **parar-se** sem sair do ecrã. O estado apresentado é lido
da própria máquina, e cada operação fica no registo de auditoria.

```{figure} /_static/img/31-gestor-processos/03a.jpg
:alt: Filtro de serviços com o serviço de relatório de erros do Windows e o botão iniciar

Iniciar e parar um serviço.
```

## Pausar e retomar

**Pausar não é o mesmo que terminar.** O processo fica congelado, com a memória e o estado intactos, e
pode ser retomado mais tarde com o mesmo PID, porque nunca foi terminado. É útil para examinar um
processo suspeito sem lhe dar tempo de fazer mais danos.

O botão **Terminar**, a vermelho e à parte, pede sempre confirmação. Os processos críticos do sistema e
o próprio agente estão protegidos.

```{figure} /_static/img/31-gestor-processos/04a.jpg
:alt: Processo ping pausado no gestor de processos

Um processo pausado.
```

## Separador arrastável

O gestor e o ecrã da máquina partilham a janela, e o separador entre eles arrasta-se para dar mais espaço
a um ou a outro. O ecrã da máquina reajusta-se em tempo real.

```{figure} /_static/img/31-gestor-processos/05a.jpg
:alt: Gestor de processos alargado com o ecrã da máquina reduzido

O separador arrastável.
```

## Enviar um processo ao CAPE

No menu de ações de cada processo, **CAPE Sandbox** envia o executável do processo para o laboratório de
malware. O ForensicVM vai buscar o ficheiro à máquina, ou reconstrói-o a partir da memória, e submete-o.
Só acontece quando o investigador clica. O número da tarefa e a ligação para os resultados aparecem na
faixa inferior. Veja {doc}`../malware/cape-utilizacao`.

```{figure} /_static/img/31-gestor-processos/07b.jpg
:alt: Faixa inferior com o número da tarefa CAPE e a ligação para os resultados

Processo enviado ao CAPE.
```

## Pesquisar o hash no VirusTotal

A opção **VirusTotal** calcula o SHA-256 do executável do processo e mostra-o (visível e copiável). Depois
abre um novo separador do navegador com a página desse *hash* no [VirusTotal](https://www.virustotal.com/).

- **O ficheiro não é enviado a ninguém**. Só o *hash* é pesquisado.
- Não é preciso chave de API.
- Se o ficheiro já tiver sido analisado por alguém, os resultados dos motores antivírus aparecem logo.

```{figure} /_static/img/31-gestor-processos/08b.jpg
:alt: Página do VirusTotal para um hash de malware conhecido, com dezenas de deteções

Exemplo, com o *hash* de um malware conhecido (simulação): dezenas de motores assinalam a amostra.
```

```{note}
A integração atual pesquisa um processo de cada vez e não usa a API do VirusTotal. A verificação
automática de muitas amostras pela API ainda não está implementada e exigiria um acesso pago adequado.
```

## Em resumo

O gestor de processos encurta o caminho entre ver um processo estranho e perceber o que ele é. O agente
mostra o que consome a máquina e permite pausar sem destruir prova. A memória dá uma visão que não
depende do que está lá dentro. O CAPE analisa o comportamento, e o VirusTotal diz se o ficheiro já é
conhecido. Tudo no mesmo ecrã, e tudo registado.
