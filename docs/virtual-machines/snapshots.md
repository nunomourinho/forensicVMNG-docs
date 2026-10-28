# Snapshots

Um snapshot guarda o estado exato da máquina num instante: o disco e a memória. Serve para experimentar
sem receio e para voltar atrás.

```{video} 09-snapshots
```

## O snapshot de ouro

No painel de snapshots da consola aparece o {term}`snapshot de ouro`, criado automaticamente na
conversão. Está protegido com um cadeado: é o estado exato do indício e não se pode apagar. É a
referência a que se pode sempre voltar.

Há também o {term}`snapshot de prata`: o estado logo após a injeção de controladores, antes do primeiro
arranque.

```{figure} /_static/img/09-snapshots/02a.jpg
:alt: Painel de snapshots com os snapshots de prata e de ouro e o campo para criar um novo

O painel de snapshots, com o snapshot de ouro protegido.
```

## Criar e restaurar

1. Antes de uma operação arriscada (executar uma amostra, mudar uma configuração), dê um nome ao
   snapshot e carregue em **Guardar**. Com a máquina em execução, o snapshot inclui a memória.
2. Para voltar atrás, escolha o snapshot e **Restaurar**. A máquina volta exatamente ao ponto em que
   estava, incluindo os programas abertos.
3. **Restaurar para a origem** devolve a máquina ao estado de partida protegido.

```{figure} /_static/img/09-snapshots/02b.jpg
:alt: Snapshot com nome a ser guardado no painel

Criação de um snapshot com nome.
```

```{figure} /_static/img/09-snapshots/03a.jpg
:alt: Máquina restaurada para o snapshot criado, com notificação de confirmação

Restauro de um snapshot.
```

```{note}
A memória dos snapshots é cifrada quando o servidor tem uma chave-mestra de cifra configurada. Criar,
restaurar e apagar snapshots fica no registo de auditoria.
```
