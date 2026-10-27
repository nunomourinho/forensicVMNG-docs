# Do CFReDS à máquina virtual

Esta página segue uma imagem forense real, desde o portal onde está publicada até a uma máquina virtual
pronta a arrancar. A imagem é o dataset do «Bart»: um computador com Windows 11 Pro, com aplicações
locais e na nuvem, publicado no CFReDS do NIST.

```{video} 03-bart-cfreds-conversao
```

## Encontrar a imagem

No portal [CFReDS](https://cfreds.nist.gov/) pesquisa-se *ForensicVM*. O dataset descreve o desafio:
entrar na conta do Bart sem alterar a palavra-passe original e recolher indícios locais e na nuvem. A
página aponta para os ficheiros, alojados no Zenodo.

```{figure} /_static/img/03-bart-cfreds-conversao/02a.jpg
:alt: Pesquisa no portal CFReDS do NIST

Pesquisa no portal CFReDS.
```

```{figure} /_static/img/03-bart-cfreds-conversao/02b.jpg
:alt: Página do dataset do Bart com a descrição do desafio e as ligações para download

A página do dataset, com a descrição do desafio e as ligações para os ficheiros.
```

## Descarregar

No Zenodo, a imagem está dividida em **dez segmentos E01**, num total de 14,9 GB. Cada segmento tem o seu
MD5 publicado. Descarregam-se todos os segmentos para uma pasta do servidor (o navegador transfere
alguns de cada vez).

```{figure} /_static/img/03-bart-cfreds-conversao/03a.jpg
:alt: Página do Zenodo com os segmentos da imagem

Os ficheiros no Zenodo.
```

```{figure} /_static/img/03-bart-cfreds-conversao/03b.jpg
:alt: Lista de transferências do navegador com vários segmentos em curso

Transferência dos segmentos (acelerada no vídeo).
```

## Verificar a integridade

Antes de converter, deve confirmar-se que os ficheiros chegaram intactos:

1. Calcular no servidor o MD5 de cada segmento e compará-lo com o publicado no Zenodo. Na demonstração,
   os onze ficheiros coincidiram (dez segmentos e as instruções).
2. O *hash* da aquisição está guardado dentro do próprio E01. O ForensicVM lê-o durante a conversão e
   regista-o na identidade da imagem.

```bash
md5sum /caminho/para/os/segmentos/*.E??
```

```{tip}
Este passo é uma boa prática forense em qualquer transferência de indícios. Confirme sempre o *hash*
antes de trabalhar com uma imagem e guarde o resultado com a documentação do caso.
```

## Converter

1. Em **Converter**, escolha o **caso** (obrigatório) e o **equipamento** onde a máquina vai ficar (aqui,
   o computador do Bart).
2. Como a imagem já está no servidor, a origem é **Caminho no servidor**. Navegue até à pasta e escolha
   o **primeiro segmento** (`.E01`). O ForensicVM encontra os restantes sozinho.
3. Escolha o **modo**:
   - **Snapshot:** arranca depressa e quase não ocupa disco. A imagem original é lida, mas nunca escrita.
   - **Cópia:** demora mais, mas a máquina fica independente da fonte.
4. Inicie a conversão.

```{figure} /_static/img/03-bart-cfreds-conversao/05a.jpg
:alt: Assistente de conversão com o caso, o equipamento, o caminho da imagem e o modo snapshot

O assistente de conversão: caso, equipamento, origem e modo.
```

## O que acontece durante a conversão

A conversão começa por ler os metadados do E01: o examinador, a data da aquisição, a ferramenta usada e
os *hashes* MD5 e SHA1 originais. Depois monta a imagem, só de leitura, e cria o {term}`snapshot de
ouro`, antes de qualquer alteração.

A seguir, reconhece o Windows e injeta os controladores VirtIO numa camada própria, por cima da imagem.
A página {doc}`injecao-drivers` explica este passo em detalhe.

```{figure} /_static/img/03-bart-cfreds-conversao/05b.jpg
:alt: Conversão em curso com a identidade da imagem e o registo de cada passo

A identidade da imagem e o registo da conversão, em direto.
```

Na demonstração, a conversão de um disco de 80 GB ficou concluída em um minuto e 38 segundos. A máquina
aparece no caso, pronta a arrancar.

## Em resumo

- Uma imagem pública de referência (NIST CFReDS), descarregada e verificada por MD5.
- Conversão a partir de um caminho no servidor, com caso e equipamento obrigatórios.
- No modo snapshot, a imagem original nunca é escrita.

Próximo passo: {doc}`injecao-drivers` e depois {doc}`../maquinas-virtuais/arranque-e-consola`.
