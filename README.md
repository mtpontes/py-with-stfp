# Python + SFTP

## How to run
- Se você for usar uma chave SSH, informe sua chave pública no arquivo .env
    - Se sua chave possuir um passphrase, passe esse valor na variável `PASSWORD`, se não, deixe em branco

```
docker-compose up -d
python index.py
```

## Connect to server with SSH
```
sftp -P 2222 test@localhost
```
