# Indícios e conversão

Esta secção mostra como uma imagem forense chega ao ForensicVM e se transforma numa máquina virtual
arrancável. Os exemplos usam duas imagens públicas do [CFReDS](https://cfreds.nist.gov/), o repositório
de imagens forenses de referência do NIST:

- o dataset **Windows 11 «Bart»**, um computador com Windows 11 Pro, aplicações locais e serviços na
  nuvem;
- o **Hacking Case** do NIST, o portátil de Greg Schardt, com Windows XP.

Qualquer pessoa pode descarregar estas imagens para reproduzir as demonstrações.

## Os passos da conversão

Seja qual for a origem, a conversão segue sempre os mesmos passos:

1. **Caso e equipamento obrigatórios:** a máquina virtual fica associada ao equipamento apreendido
   certo.
2. **Leitura da identidade da imagem:** examinador, data e ferramenta de aquisição, *hashes* MD5 e SHA1
   originais (lidos dos metadados do E01).
3. **Montagem só de leitura** e criação do {term}`snapshot de ouro`, antes de qualquer alteração.
4. **Deteção do sistema operativo e injeção de controladores** num {term}`snapshot de prata`.
5. **Deteção do firmware** necessário (UEFI ou BIOS).
6. **Máquina pronta**, associada ao caso, com a conversão no registo de auditoria.

```{toctree}
:maxdepth: 1

cfreds-bart
injecao-drivers
hacking-case
outras-origens
```
