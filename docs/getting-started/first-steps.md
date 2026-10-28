# Primeiros passos

Esta página acompanha o primeiro acesso de um investigador à plataforma: idioma, autenticação com segundo
fator obrigatório, códigos de recuperação e a navegação principal.

```{video} 01-primeiros-passos
```

## Ecrã de entrada

O ForensicVM corre num servidor e usa-se a partir do navegador. Não há nada para instalar no posto do
investigador. No ecrã de entrada pode escolher-se o idioma da interface (português de Portugal, inglês e outros) e
o tema claro ou escuro, nos controlos do canto superior direito.

O investigador entra com o utilizador e a palavra-passe que o administrador lhe atribuiu.

```{figure} /_static/img/01-primeiros-passos/02b.jpg
:alt: Ecrã de entrada do ForensicVM com os campos de utilizador e palavra-passe

Ecrã de entrada.
```

## Autenticação de dois fatores (obrigatória)

No primeiro acesso, o sistema exige a configuração de um segundo fator. Sem ele, não se chega aos
indícios. Há duas opções:

- **Chave de segurança ou biometria (FIDO2/WebAuthn):** uma YubiKey, o Windows Hello ou o Touch ID.
  Exige que o servidor seja acedido por HTTPS e por nome (veja {doc}`../installation/https-intranet`).
- **Aplicação de autenticação (TOTP):** Google Authenticator, Microsoft Authenticator, Authy, 1Password
  e semelhantes.

Para configurar a aplicação de autenticação:

1. Escolha **Aplicação de autenticação**.
2. Leia o código QR com a aplicação no telemóvel.
3. Escreva o primeiro código de seis dígitos para confirmar.
4. Guarde num local seguro os **oito códigos de recuperação** que o sistema mostra. Cada um serve uma
   única vez, se perder o acesso ao autenticador.

```{figure} /_static/img/01-primeiros-passos/03a.jpg
:alt: Configuração da autenticação de dois fatores com código QR

Configuração do segundo fator com uma aplicação de autenticação.
```

```{tip}
Registe dois fatores por conta (por exemplo duas chaves de segurança, ou uma chave e uma aplicação) para
não perder o acesso se um deles se extraviar. Se mesmo assim perder o acesso, o administrador pode
repor a conta (veja {doc}`../administration/backups-and-troubleshooting`).
```

## Navegação principal

Depois de autenticado, o investigador chega ao ecrã principal: o estado do servidor (CPU, memória, disco,
rede) e as máquinas virtuais a que tem acesso. **Cada utilizador só vê as máquinas dos casos de que é
membro.**

```{figure} /_static/img/01-primeiros-passos/04a.jpg
:alt: Ecrã principal com os recursos do servidor e a lista de máquinas virtuais, ainda vazia

Ecrã principal: recursos do servidor e máquinas virtuais (ainda nenhuma).
```

A barra de navegação inferior dá acesso às áreas principais:

| Área | Para que serve |
|---|---|
| **VMs** | As máquinas virtuais forenses a que o utilizador tem acesso. |
| **Casos** | Organização das investigações. Cada máquina virtual pertence a um caso. |
| **Converter** | O assistente que transforma uma imagem forense numa máquina virtual, a partir de oito origens diferentes. |
| **Multimédia** | Biblioteca de discos de drivers VirtIO, imagens ISO, disquetes e imagens de pen USB, para montar nas máquinas. |
| **Mais** | Perfil, administração e restantes opções. |

```{figure} /_static/img/01-primeiros-passos/04b.jpg
:alt: Assistente de conversão com as oito origens de imagem

O assistente de conversão, com as origens possíveis da imagem.
```

## Acessos seguintes

Nos acessos seguintes, depois da palavra-passe, a plataforma pede o código da aplicação de autenticação
ou o toque na chave de segurança.

```{figure} /_static/img/01-primeiros-passos/05b.jpg
:alt: Pedido do código do autenticador após a palavra-passe

Nos acessos seguintes, pede-se o código do autenticador.
```

## Em resumo

- Acesso pelo navegador, sem instalação no posto do investigador.
- Segundo fator obrigatório (FIDO2 ou aplicação de autenticação), com códigos de recuperação.
- Cada investigador vê apenas as máquinas dos seus casos.

Próximo passo: {doc}`cases-and-team`.
