# Rede: isolamento e captura de tráfego

Por segurança, a máquina arranca **isolada da rede**. O investigador decide se e quando lhe dá acesso, e
tudo o que passa pela rede pode ser capturado.

```{video} 11-rede
```

## Isolada por omissão

No separador **Rede** do detalhe da máquina, o indicador mostra que a interface de rede está desligada
(*TAP disabled*). A máquina não vê a internet nem a rede local.

```{figure} /_static/img/11-rede/02a.jpg
:alt: Separador Rede com a interface desligada e a lista de capturas anteriores

A rede isolada, com as capturas anteriores.
```

```{important}
Ligar a rede de um sistema apreendido pode ter consequências: sincronização com serviços na nuvem,
contacto com servidores de comando e controlo, alteração de dados remotos. Ligue-a só quando for
necessário e justificado, e documente-o.
```

## Captura de tráfego em direto

1. Carregue em **Iniciar captura**. A rede é ligada e o sistema começa a registar todos os pacotes.
2. Os pedidos da máquina aparecem em direto: consultas DNS e ligações remotas, com o anfitrião, o
   serviço, a porta e o volume.
3. Carregue em **Parar captura**. A captura é guardada e a máquina volta a ficar isolada.

```{figure} /_static/img/11-rede/03a.jpg
:alt: Inspeção de tráfego em direto com consultas DNS e ligações remotas

Captura de tráfego em direto.
```

## O ficheiro PCAP

O tráfego fica num ficheiro **PCAP**, que se transfere para analisar com ferramentas como o
[Wireshark](https://www.wireshark.org/) e para juntar ao processo. **Descarregar todos** junta todas as
capturas num ZIP.

```{figure} /_static/img/11-rede/04a.jpg
:alt: Lista de ficheiros PCAP capturados com a opção de transferir

Os ficheiros PCAP, prontos a transferir.
```
