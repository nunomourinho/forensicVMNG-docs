# HTTPS numa intranet: CA local e chave de segurança

Esta página explica como ter HTTPS de confiança numa rede **isolada da internet**: criar uma autoridade
certificadora (CA) local, assinar o certificado do servidor, distribuir a CA pelos computadores e usar
autenticação forte com uma chave de segurança FIDO2, como a YubiKey.

```{video} 28-https-intranet
```

## Porque é preciso HTTPS

- A autenticação forte (WebAuthn/FIDO2: YubiKey, Windows Hello, Touch ID) **só funciona num contexto
  seguro**: HTTPS, com um certificado em que o navegador confie.
- A chave fica ligada ao **nome DNS** do servidor. Por isso é preciso um nome, não só um endereço IP, e o
  certificado tem de o conter. No ForensicVM, o nome vem do primeiro endereço de `ALLOWED_ORIGIN`.
- Com HTTPS, o cookie de sessão também passa a ser marcado como seguro.

## Que certificado usar

| Opção | Quando | Nota |
|---|---|---|
| Let's Encrypt (`certbot`) | Servidor com nome público e acesso à internet | Não serve numa rede isolada. |
| CA da organização (AD CS, PKI institucional) | Já existe uma PKI | Pede-se o certificado à CA. Os computadores já confiam nela. |
| **CA local própria** | Intranet isolada, sem PKI | É o caso descrito nesta página. |

Nos exemplos seguintes, o servidor chama-se `forensicvm.internal` e tem o endereço `192.168.1.10`.
Substitua pelos seus valores.

## 1. Nome do servidor

Registe o nome no DNS interno (registo A). Sem DNS interno, use o ficheiro `hosts` de cada máquina,
incluindo o próprio servidor. Os passos 1 a 5 correm no servidor, como root:

```bash
sudo -i
echo '192.168.1.10  forensicvm.internal' | tee -a /etc/hosts
getent hosts forensicvm.internal
```

`.internal` é um domínio reservado para uso privado.

## 2. Criar a CA local (uma vez)

```bash
install -d -m 700 /etc/ssl/forensicvm-ca && cd /etc/ssl/forensicvm-ca
openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:prime256v1 -nodes \
  -keyout ca.key -out ca.crt -days 3650 \
  -subj "/O=Laboratorio Forense/CN=Laboratorio Forense - CA interna" \
  -addext "basicConstraints=critical,CA:TRUE" -addext "keyUsage=critical,keyCertSign,cRLSign"
```

```{danger}
A chave privada da CA (`ca.key`) é o segredo mais valioso de todo o processo: quem a tiver emite
certificados em que todos os computadores confiam. Depois de assinar, guarde-a **offline**, num suporte
protegido.
```

## 3. Certificado do servidor

O navegador ignora o nome comum (CN) e só olha para a **SAN** (*subject alternative name*), que tem de
conter o nome que os utilizadores vão escrever e, se quiser, o endereço IP.

```bash
openssl req -newkey ec -pkeyopt ec_paramgen_curve:prime256v1 -nodes \
  -keyout forensicvm.key -out forensicvm.csr -subj "/CN=forensicvm.internal"
printf "subjectAltName=DNS:forensicvm.internal,IP:192.168.1.10\nbasicConstraints=CA:FALSE\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth\n" | tee forensicvm.ext
openssl x509 -req -in forensicvm.csr -CA ca.crt -CAkey ca.key -CAcreateserial \
  -out forensicvm.crt -days 397 -extfile forensicvm.ext
openssl verify -CAfile ca.crt forensicvm.crt
openssl x509 -in forensicvm.crt -noout -subject -issuer -ext subjectAltName
```

397 dias é a validade máxima que os navegadores aceitam para certificados de servidor.

```{figure} /_static/img/28-https-intranet/06b.jpg
:alt: Terminal com a criação e verificação do certificado do servidor

Criação e verificação do certificado do servidor.
```

## 4. nginx em HTTPS

```bash
install -d /etc/ssl/forensicvm
install -m 644 forensicvm.crt /etc/ssl/forensicvm/ && install -m 640 -g www-data forensicvm.key /etc/ssl/forensicvm/
S=/etc/nginx/sites-available/forensicvm
sed -i 's|listen 80 default_server;|listen 443 ssl default_server;|' $S
sed -i 's|listen \[::\]:80 default_server;|ssl_certificate /etc/ssl/forensicvm/forensicvm.crt; ssl_certificate_key /etc/ssl/forensicvm/forensicvm.key;|' $S
grep -nE "listen|ssl_certificate" $S
printf 'server {\n    listen 80 default_server;\n    return 301 https://forensicvm.internal$request_uri;\n}\n' | tee /etc/nginx/conf.d/forensicvm-redirect.conf
nginx -t && systemctl reload nginx
```

```{warning}
Voltar a correr o `install.sh` regenera o ficheiro do site do nginx e apaga estas alterações.
```

## 5. Configurar o ForensicVM

No ficheiro `apps/server/.env`, dentro da pasta de instalação:

```bash
cd <pasta-do-forensicvm>/apps/server
sed -i 's|^ALLOWED_ORIGIN=.*|ALLOWED_ORIGIN=https://forensicvm.internal|; s|^SOCKET_CORS_ORIGIN=.*|SOCKET_CORS_ORIGIN=https://forensicvm.internal|; s|^COOKIE_SECURE=.*|COOKIE_SECURE=true|' .env
grep -E '^(ALLOWED_ORIGIN|SOCKET_CORS_ORIGIN|COOKIE_SECURE)' .env
systemctl restart forensicvm && systemctl is-active forensicvm
curl -sSI --cacert /etc/ssl/forensicvm-ca/ca.crt https://forensicvm.internal/ | head -2
```

Sem a opção `--cacert`, o `curl` recusa a ligação, porque não conhece a CA. Com ela, o servidor responde.

## 6. Distribuir a CA pelos computadores

Distribui-se **apenas o certificado público da CA (`ca.crt`)**. Nunca a `ca.key` nem a chave do servidor.

```bash
# Linux (sistema)
sudo cp ca.crt /usr/local/share/ca-certificates/forensicvm-ca.crt && sudo update-ca-certificates
# Chrome/Chromium em Linux usam a base NSS do utilizador
certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n "ForensicVM CA" -i ca.crt
```

```powershell
# Windows (PowerShell como administrador)
certutil -addstore -f Root ca.crt
```

- **Muitos computadores Windows:** use uma Política de Grupo, em *Configuração do Computador › Definições
  do Windows › Definições de Segurança › Políticas de Chave Pública › Autoridades de Certificação de Raiz
  Fidedigna*.
- **Firefox:** tem repositório próprio. A política `ImportEnterpriseRoots` faz com que use o do sistema.

```{figure} /_static/img/28-https-intranet/11a.jpg
:alt: Aviso do navegador "A sua ligação não é privada"

Num computador sem a CA, o navegador avisa que a ligação não é privada.
```

```{figure} /_static/img/28-https-intranet/11b.jpg
:alt: Página de entrada do ForensicVM em HTTPS sem avisos

Com a CA distribuída, o mesmo endereço abre sem avisos.
```

## 7. Registar a chave de segurança

1. Abra `https://forensicvm.internal`: cadeado fechado, sem avisos.
2. Entre e, no ecrã do segundo fator, escolha **Chave de segurança ou biometria**.
3. Dê um nome ao dispositivo e toque na YubiKey quando ela piscar.
4. Nos acessos seguintes, depois da palavra-passe, escolha **Usar chave de segurança** e toque na chave.

A chave fica ligada ao nome `forensicvm.internal`. Num site falso, com outro nome, não responderia. É
isso que a torna resistente ao *phishing*.

```{note}
Na demonstração foi usado um autenticador FIDO2 virtual, do próprio navegador, em vez de uma YubiKey
física. Para a aplicação é indiferente: com uma chave física, os passos são os mesmos.
```

```{figure} /_static/img/28-https-intranet/12b.jpg
:alt: Ecrã principal do ForensicVM depois de entrar com a chave de segurança

Entrada com a chave de segurança.
```

## Boas práticas

- Guardar a `ca.key` offline, num suporte protegido.
- Renovar o certificado do servidor antes de expirar (aqui, 397 dias), repetindo o passo 3. A CA dura 10
  anos.
- Registar **duas chaves por conta**, para o caso de uma se perder.
- Se a organização já tiver uma PKI, pedir o certificado a essa autoridade.
