# O disco de evidências

Durante o exame, o investigador encontra elementos que interessam: um ficheiro, uma amostra, um registo.
Precisa de os recolher sem contaminar o resto. Para isso, cada máquina tem um **disco de evidências**,
criado automaticamente.

```{video} 19-evidencias
```

## Dentro da máquina

Dentro do sistema convidado, o disco de evidências aparece como uma unidade própria, chamada
**possible evidence**. É para esta unidade que o investigador copia o que encontra: a nota do exame, um
artefacto recolhido, uma amostra reservada para análise. O disco original não é tocado.

```{figure} /_static/img/19-evidencias/03a.jpg
:alt: Explorador do Windows com a pasta de indícios na unidade possible evidence

A pasta de indícios na unidade *possible evidence*.
```

## Um disco à parte

Na gestão de discos da plataforma, o disco de evidências aparece marcado como tal. As suas regras:

- é criado automaticamente com cada máquina;
- é gravável;
- **não pode ser removido**, para que nada do que lá se guarda se perca;
- é guardado **cifrado** em repouso.

```{figure} /_static/img/19-evidencias/03b.jpg
:alt: Painel de discos ligados com o disco de evidências identificado

O disco de evidências na gestão de discos.
```

## Descarregar as evidências

No painel de **aquisição** da consola, **Descarregar imagem de evidência** entrega o conteúdo do disco.
O ForensicVM decifra-o, monta-o e entrega os ficheiros num **ZIP** pronto a abrir.

```{figure} /_static/img/19-evidencias/04a.jpg
:alt: Painel de aquisição com a opção Descarregar imagem de evidência

Descarregar as evidências a partir do painel de aquisição.
```

No ZIP estão exatamente os elementos reunidos na unidade, decifrados e prontos a examinar com as
ferramentas habituais. Por exemplo:

- `Indicios/nota-do-investigador.txt`: a nota do próprio exame;
- `Indicios/hosts-recolhido.txt`: um artefacto recolhido da máquina;
- `Indicios/amostra-suspeita.txt`: uma amostra reservada para análise.

```{tip}
Depois de descarregar o ZIP, calcule e registe o seu *hash* antes de o entregar ou analisar, tal como faria
com qualquer outro elemento de prova.
```
