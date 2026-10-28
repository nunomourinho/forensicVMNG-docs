# HTTPS on an intranet: local CA and security key

This page explains how to get trusted HTTPS on a network **isolated from the internet**: create a local
certificate authority (CA), sign the server certificate, distribute the CA to the computers and use
strong authentication with a FIDO2 security key, such as a YubiKey.

```{video} 28-https-intranet
```

## Why HTTPS is needed

- Strong authentication (WebAuthn/FIDO2: YubiKey, Windows Hello, Touch ID) **only works in a secure
  context**: HTTPS, with a certificate the browser trusts.
- The key is bound to the server's **DNS name**. So you need a name, not just an IP address, and the
  certificate must contain it. In ForensicVM, the name comes from the first address in `ALLOWED_ORIGIN`.
- With HTTPS, the session cookie is also marked as secure.

## Which certificate to use

| Option | When | Note |
|---|---|---|
| Let's Encrypt (`certbot`) | Server with a public name and internet access | Not usable on an isolated network. |
| Organisation's CA (AD CS, institutional PKI) | A PKI already exists | Request the certificate from the CA. The computers already trust it. |
| **Your own local CA** | Isolated intranet, no PKI | The case described on this page. |

In the following examples, the server is called `forensicvm.internal` and has the address
`192.168.1.10`. Replace them with your own values.

## 1. Server name

Register the name in the internal DNS (an A record). Without internal DNS, use each machine's `hosts`
file, including the server itself. Steps 1 to 5 run on the server, as root:

```bash
sudo -i
echo '192.168.1.10  forensicvm.internal' | tee -a /etc/hosts
getent hosts forensicvm.internal
```

`.internal` is a domain reserved for private use.

## 2. Creating the local CA (once)

```bash
install -d -m 700 /etc/ssl/forensicvm-ca && cd /etc/ssl/forensicvm-ca
openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:prime256v1 -nodes \
  -keyout ca.key -out ca.crt -days 3650 \
  -subj "/O=Forensic Laboratory/CN=Forensic Laboratory - internal CA" \
  -addext "basicConstraints=critical,CA:TRUE" -addext "keyUsage=critical,keyCertSign,cRLSign"
```

```{danger}
The CA's private key (`ca.key`) is the most valuable secret in the whole process: whoever has it can
issue certificates that every computer trusts. After signing, keep it **offline**, on protected media.
```

## 3. Server certificate

The browser ignores the common name (CN) and only looks at the **SAN** (*subject alternative name*),
which must contain the name users will type and, if you wish, the IP address.

```bash
openssl req -newkey ec -pkeyopt ec_paramgen_curve:prime256v1 -nodes \
  -keyout forensicvm.key -out forensicvm.csr -subj "/CN=forensicvm.internal"
printf "subjectAltName=DNS:forensicvm.internal,IP:192.168.1.10\nbasicConstraints=CA:FALSE\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth\n" | tee forensicvm.ext
openssl x509 -req -in forensicvm.csr -CA ca.crt -CAkey ca.key -CAcreateserial \
  -out forensicvm.crt -days 397 -extfile forensicvm.ext
openssl verify -CAfile ca.crt forensicvm.crt
openssl x509 -in forensicvm.crt -noout -subject -issuer -ext subjectAltName
```

397 days is the maximum validity browsers accept for server certificates.

```{figure} /_static/img/28-https-intranet/06b.jpg
:alt: Terminal with the creation and verification of the server certificate

Creating and verifying the server certificate.
```

## 4. nginx over HTTPS

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
Running `install.sh` again regenerates the nginx site file and wipes out these changes.
```

## 5. Configuring ForensicVM

In the `apps/server/.env` file, inside the installation folder:

```bash
cd <forensicvm-folder>/apps/server
sed -i 's|^ALLOWED_ORIGIN=.*|ALLOWED_ORIGIN=https://forensicvm.internal|; s|^SOCKET_CORS_ORIGIN=.*|SOCKET_CORS_ORIGIN=https://forensicvm.internal|; s|^COOKIE_SECURE=.*|COOKIE_SECURE=true|' .env
grep -E '^(ALLOWED_ORIGIN|SOCKET_CORS_ORIGIN|COOKIE_SECURE)' .env
systemctl restart forensicvm && systemctl is-active forensicvm
curl -sSI --cacert /etc/ssl/forensicvm-ca/ca.crt https://forensicvm.internal/ | head -2
```

Without the `--cacert` option, `curl` refuses the connection, because it does not know the CA. With it,
the server answers.

## 6. Distributing the CA to the computers

Distribute **only the CA's public certificate (`ca.crt`)**. Never `ca.key` or the server's key.

```bash
# Linux (system-wide)
sudo cp ca.crt /usr/local/share/ca-certificates/forensicvm-ca.crt && sudo update-ca-certificates
# Chrome/Chromium on Linux use the user's NSS database
certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n "ForensicVM CA" -i ca.crt
```

```powershell
# Windows (PowerShell as administrator)
certutil -addstore -f Root ca.crt
```

- **Many Windows computers:** use a Group Policy, under *Computer Configuration › Windows Settings ›
  Security Settings › Public Key Policies › Trusted Root Certification Authorities*.
- **Firefox:** has its own store. The `ImportEnterpriseRoots` policy makes it use the system's.

```{figure} /_static/img/28-https-intranet/11a.jpg
:alt: Browser warning "Your connection is not private"

On a computer without the CA, the browser warns that the connection is not private.
```

```{figure} /_static/img/28-https-intranet/11b.jpg
:alt: ForensicVM sign-in page over HTTPS with no warnings

With the CA distributed, the same address opens with no warnings.
```

## 7. Registering the security key

1. Open `https://forensicvm.internal`: closed padlock, no warnings.
2. Sign in and, on the second-factor screen, choose **Security key or biometrics**.
3. Give the device a name and touch the YubiKey when it flashes.
4. On subsequent sign-ins, after the password, choose **Use security key** and touch the key.

The key is bound to the name `forensicvm.internal`. On a fake site, with a different name, it would not
respond. That is what makes it resistant to *phishing*.

```{note}
The demonstration used a virtual FIDO2 authenticator, built into the browser, instead of a physical
YubiKey. It makes no difference to the application: with a physical key, the steps are the same.
```

```{figure} /_static/img/28-https-intranet/12b.jpg
:alt: ForensicVM main screen after signing in with the security key

Signing in with the security key.
```

## Good practice

- Keep `ca.key` offline, on protected media.
- Renew the server certificate before it expires (here, 397 days), repeating step 3. The CA lasts 10
  years.
- Register **two keys per account**, in case one is lost.
- If the organisation already has a PKI, request the certificate from that authority.
