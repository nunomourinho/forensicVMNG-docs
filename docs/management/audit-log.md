# Registo de auditoria

Cada ação no ForensicVM fica registada: quem a fez, quando e sobre que máquina. O registo é imutável,
tem filtros e exporta-se em vários formatos.

```{video} 14-auditoria
```

```{important}
Este registo **não é a cadeia de custódia em si**. É um registo de ações que a **apoia e documenta**. É
imutável: a base de dados tem mecanismos (*triggers*) que impedem alterar ou apagar entradas, mesmo por
um administrador da base de dados.
```

## O registo do caso

No separador **Custódia** do caso aparece a lista de ações sobre as suas máquinas: a conversão da imagem,
os arranques, os plug-ins, as capturas, as alterações de hardware, a ativação da rede. Cada linha tem o
utilizador e a hora exata.

Pode filtrar-se por **máquina** (UUID), **utilizador**, **ação** e **intervalo de datas**.

```{figure} /_static/img/14-auditoria/02a.jpg
:alt: Registo de auditoria do caso filtrado pela ação VM

O registo de ações do caso, com filtros.
```

## Exportar

O registo exporta-se em **CSV** ou **JSON**, para análise ou para anexar ao processo.

```{figure} /_static/img/14-auditoria/03a.jpg
:alt: Botões de exportação CSV e JSON no registo de auditoria

Exportação do registo.
```

## Relatório e comentários por máquina

Para cada máquina gera-se um **relatório em formato Word** (DOCX) com o histórico de ações. O investigador
pode ainda acrescentar os seus **comentários** (por exemplo "Exame inicial concluído, sem alterações"),
que ficam igualmente registados.

```{figure} /_static/img/14-auditoria/04a.jpg
:alt: Registo de uma máquina com o campo de comentário do investigador e a exportação DOCX

Comentário do investigador e exportação do relatório da máquina.
```
