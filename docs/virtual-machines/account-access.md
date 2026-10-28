# Acesso à conta sem alterar a credencial

Numa máquina apreendida, o investigador raramente tem a palavra-passe do utilizador. Esta página mostra
como aceder à sessão para **exame autorizado**, sem alterar a credencial original nem tocar na imagem.

```{video} 06-acesso-sem-alterar-password
```

```{important}
Este procedimento destina-se exclusivamente a exames forenses **legalmente autorizados**, no âmbito de
uma investigação. A operação fica registada no registo de auditoria do caso, com o utilizador e a hora.
```

## A conta está protegida

Sem a palavra-passe correta, o Windows recusa o acesso, tal como faria no computador original.

```{figure} /_static/img/06-acesso-sem-alterar-password/02a.jpg
:alt: Ecrã de início de sessão do Windows com a conta protegida por palavra-passe

A conta do utilizador está protegida.
```

## O plug-in de acesso

O ForensicVM inclui um plug-in **em direto** com um único fim: dar ao investigador acesso à sessão do
utilizador quando a credencial não é conhecida.

- Atua sobre a máquina virtual **em funcionamento**, na memória, e não sobre o disco.
- A imagem original e o seu *hash* não são tocados.
- A palavra-passe real da conta fica exatamente como estava no indício.

## Executar o plug-in

1. Na consola, abra o catálogo de **plug-ins em direto** na barra inferior.
2. Escolha o plug-in de acesso (desbloqueio da sessão Windows) e execute-o contra a máquina.
3. O plug-in corre sobre a máquina virtual e devolve o resultado. Nada é escrito no disco do indício.

```{figure} /_static/img/06-acesso-sem-alterar-password/04a.jpg
:alt: Catálogo de plug-ins em direto na consola

O catálogo de plug-ins em direto, aberto na consola.
```

```{figure} /_static/img/06-acesso-sem-alterar-password/04b.jpg
:alt: Plug-in de desbloqueio em execução com o respetivo registo

O plug-in em execução.
```

## Entrar na sessão

A partir daí, o investigador entra na sessão e pode examinar a conta tal como o utilizador a via: o
ambiente de trabalho, as aplicações locais e os serviços na nuvem com sessão iniciada.

```{figure} /_static/img/06-acesso-sem-alterar-password/06b.jpg
:alt: Ambiente de trabalho do utilizador depois de entrar na sessão

O ambiente de trabalho do utilizador, pronto a examinar.
```

## O que fica garantido

- A imagem original (E01) e o seu *hash* continuam a coincidir com os da aquisição.
- A palavra-passe real da conta fica como estava na máquina apreendida.
- A operação fica no registo de auditoria do caso, com o utilizador e a hora.
- Quando a máquina é desligada, o acesso deixa de estar em vigor. Nada persiste no indício.
