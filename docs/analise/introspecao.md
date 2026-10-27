# Introspeção: processos e memória ao vivo

Uma máquina em execução tem muito para contar enquanto está viva. O ForensicVM observa-a **de fora**, a
partir do hipervisor (*virtual machine introspection*): mostra ao vivo os processos e os serviços e
permite extrair a memória de qualquer processo, sem sair da consola.

```{video} 18-introspecao
```

## Na consola

Na barra da consola, o botão **Processos** abre o gestor de processos ao lado do ecrã da máquina. Não é
o gestor de tarefas do Windows: é o ForensicVM a observar a máquina de fora, sem nada instalado lá dentro.

```{figure} /_static/img/18-introspecao/03b.jpg
:alt: Gestor de processos aberto ao lado da consola com a lista de processos

Os processos em execução, lidos a partir do hipervisor.
```

## Processos e serviços

A lista mostra os processos em execução dentro da máquina, com o identificador (PID) e o nome de cada
um, atualizável ao vivo, do núcleo do sistema às aplicações. Para cada processo pode **pausar**,
**retomar** ou **terminar**.

Logo a seguir aparecem os **serviços** do sistema em execução, com o nome de cada um e o processo que o
aloja.

```{figure} /_static/img/18-introspecao/04b.jpg
:alt: Lista de processos com as ações pausar, dump e terminar

Ações sobre cada processo.
```

## Extrair a memória de um processo

1. Escolha um processo e carregue em **Dump**.
2. O ForensicVM percorre as regiões de memória desse processo, ao vivo, e mostra o progresso.
3. No fim, a memória extraída fica num ficheiro, pronta a descarregar e a analisar com as ferramentas
   habituais.

A extração é feita de fora da máquina, pelo hipervisor. O indício é lido, não é alterado, e a operação
fica registada no caso.

```{figure} /_static/img/18-introspecao/06a.jpg
:alt: Resultado da extração da memória de um processo, com as regiões extraídas

O resultado da extração, pronto a descarregar.
```

```{tip}
Por ser feita de fora, a introspeção funciona mesmo que o sistema convidado esteja bloqueado ou em falha,
e é mais difícil de enganar por um malware que tente esconder-se dentro da máquina. Veja também
{doc}`gestor-processos`.
```
