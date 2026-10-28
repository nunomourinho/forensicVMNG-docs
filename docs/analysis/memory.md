# Análise de memória com o Volatility3

A memória de uma máquina em funcionamento guarda o que o disco não mostra: processos em execução,
ligações de rede abertas e código malicioso que só existe em memória (*fileless*). O ForensicVM captura
a memória da máquina e analisa-a com o [Volatility3](https://github.com/volatilityfoundation/volatility3),
uma ferramenta de referência em forense de memória, sem desligar a máquina.

```{video} 10-memoria
```

## A introspeção de memória

A página **Introspeção de memória** permite escolher a análise (o *plugin* do Volatility3) e executá-la.
A opção **Dump fresco** força uma nova captura da memória. Sem ela, reutiliza-se a última captura.

```{figure} /_static/img/10-memoria/02a.jpg
:alt: Página de introspeção de memória ainda sem resultados

A página de introspeção de memória.
```

## Lista de processos

A primeira análise captura a memória e lista todos os processos: os do sistema (`lsass.exe`,
`services.exe`, `svchost.exe`…) e os do utilizador, com PID, PPID, *threads*, sessão e hora de criação.

As análises seguintes reutilizam a mesma captura, sem voltar a tocar na máquina.

```{figure} /_static/img/10-memoria/03b.jpg
:alt: Lista de processos extraída da memória com PID, nome e hora de criação

Lista de processos (85 resultados na demonstração).
```

## Ligações de rede

A análise de **ligações de rede** mostra as ligações e portas em escuta que existiam na memória. É útil
para reconstruir com quem a máquina comunicava.

```{figure} /_static/img/10-memoria/04b.jpg
:alt: Lista de ligações de rede extraída da memória

Ligações de rede encontradas em memória.
```

## Memória suspeita

A procura de **memória suspeita** (o equivalente ao *malfind*) assinala zonas de memória executável e
gravável (`PAGE_EXECUTE_READWRITE`) com código injetado, um indício clássico de malware e o ponto de
partida para uma análise de intrusão.

```{figure} /_static/img/10-memoria/05a.jpg
:alt: Resultados da procura de memória suspeita com proteção PAGE_EXECUTE_READWRITE

Regiões de memória suspeita.
```

```{note}
O dump de memória também pode ser descarregado (no painel de aquisição da consola), para análise externa
com outras ferramentas.
```
