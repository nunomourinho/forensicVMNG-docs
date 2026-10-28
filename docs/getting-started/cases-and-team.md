# Casos e equipa

No ForensicVM, tudo começa num caso. O caso agrupa os equipamentos apreendidos, as máquinas virtuais
criadas a partir deles e as pessoas que lhes podem aceder. **Sem caso, não há conversão.**

```{video} 02-casos-e-equipa
```

## Criar o caso

Em **Casos → Novo caso**, preenchem-se:

- **Número do caso** (por exemplo, o número do processo ou do pedido de perícia);
- **Nome** e **descrição**;
- **Jurisdição** e **classificação** (por exemplo *Reservado* ou *Confidencial*).

```{figure} /_static/img/02-casos-e-equipa/02a.jpg
:alt: Formulário de novo caso com número, nome, descrição, jurisdição e classificação

Criação de um caso.
```

O caso fica aberto, com quem o criou como **proprietário**. Só o proprietário pode fechar ou arquivar o
caso. A partir desse momento, os restantes membros passam a poder apenas consultar.

```{figure} /_static/img/02-casos-e-equipa/02b.jpg
:alt: Visão geral do caso com o estado, o proprietário e as ações de fechar e arquivar

Visão geral do caso.
```

## Equipamentos apreendidos

No separador **Equipamento** regista-se o material apreendido: o tipo (computador de secretária,
portátil…), o nome, a marca, o modelo e o número de série. Estes dados vêm muitas vezes das notas de
aquisição incluídas na própria imagem E01.

Cada equipamento recebe depois a sua máquina virtual. É aqui que o assistente de conversão os vai
procurar. Até haver imagem convertida, o equipamento aparece como **pendente**.

```{figure} /_static/img/02-casos-e-equipa/03b.jpg
:alt: Registo de um portátil Dell Latitude com marca, modelo e número de série

Registo de um equipamento com marca, modelo e número de série.
```

## Membros e papéis

No separador **Membros** dá-se acesso a colegas, escolhendo o papel de cada um:

| Papel | Pode |
|---|---|
| **Leitor** | Consultar o caso e as máquinas. |
| **Investigador** | O anterior, mais operar as máquinas virtuais (arrancar, usar a consola, correr plug-ins…). |
| **Gestor** | O anterior, mais gerir membros e equipamentos. |
| **Proprietário** | O anterior, mais fechar e arquivar o caso. |

```{figure} /_static/img/02-casos-e-equipa/04a.jpg
:alt: Adição de um membro ao caso com o papel de investigador

Adição de uma colega ao caso, com o papel de investigadora.
```

```{note}
Além do papel, é possível definir exceções por equipamento ou por disco: dar só leitura num disco
específico, por exemplo. Essas exceções prevalecem sobre o papel.
```

## Registo de auditoria do caso

O separador **Custódia** mostra o registo de auditoria das ações sobre as máquinas do caso. Num caso
novo está vazio. A primeira entrada será a conversão da imagem. Veja {doc}`../management/audit-log`.

```{figure} /_static/img/02-casos-e-equipa/05a.jpg
:alt: Separador Custódia com o registo de auditoria vazio

O registo de auditoria de um caso acabado de criar.
```

## Em resumo

- Cada máquina virtual pertence a um caso. Sem caso não há conversão.
- Os equipamentos registam o material apreendido, com marca, modelo e número de série.
- O acesso decide-se caso a caso, com quatro papéis: leitor, investigador, gestor e proprietário.

Próximo passo: {doc}`../conversion/cfreds-bart`.
