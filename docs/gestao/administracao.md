# Administração

A administração do ForensicVM está numa só página, na área **Mais → Administração**, e está reservada
aos administradores.

```{video} 15-administracao
```

## O que se encontra na administração

- **Autenticação de dois fatores** e **chaves de segurança e biometria** da própria conta;
- **Chaves de API** para clientes externos;
- **Utilizadores** e os seus papéis;
- **Chaves SSH** (para integrações que usam SSH, como o Proxmox);
- **Configuração do sistema**, incluindo a verificação do sistema com inventário de software (SBOM) e o
  armazenamento;
- **Integrações** com o Veeam, o Proxmox e o Sandbox CAPEv2.

```{figure} /_static/img/15-administracao/02a.jpg
:alt: Página de administração com as secções e a lista de utilizadores

A página de administração.
```

## Utilizadores e papéis

Os utilizadores criam-se e gerem-se aqui: nome, palavra-passe inicial, estado (ativo ou inativo) e se
são **superutilizadores** (administradores). O acesso às máquinas é depois controlado caso a caso, pelos
papéis de cada membro (veja {doc}`../comecar/casos-e-equipa`).

## Chaves de API

As chaves de API permitem que clientes externos (por exemplo o Autopsy, ou scripts de automação) falem
com o ForensicVM em nome de um utilizador.

- Cada chave tem uma etiqueta e fica atribuída a um utilizador.
- O valor só é mostrado por inteiro no momento da criação.
- As chaves são **revogáveis, mas nunca apagadas**, para manter o rasto, tal como o registo de ações.

```{figure} /_static/img/15-administracao/03a.jpg
:alt: Lista de chaves de API com etiqueta, utilizador, chave mascarada, data e estado

As chaves de API.
```
