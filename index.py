import os
import paramiko
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


# Informações do servidor SFTP
host = os.getenv("HOST")
port = os.getenv("PORT")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD") # Altere para o passphrase da sua chave

simulacao_de_dados_em_memoria = """
    Processo bem sucedido!

    linha1: valor1
    linha2: valor2
    linha3: valor3
"""

# Onde irá ficar o arquivo no servidor
# Caminho completo no container será: /home/mateu/data.txt
remote_file_path = "/home/data.txt" 

# Criar uma instância de SSHClient e configurar
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(host, port, username, password) # Conectar ao server SFTP
    sftp = ssh.open_sftp() # Abrir ocanal para transferência

    try:
        with sftp.file(remote_file_path, 'w') as remote_file:
            remote_file.write(simulacao_de_dados_em_memoria)

        print("Transferência concluída com sucesso!")
    finally:
        sftp.close() # Fechar o canal e a conexão SFTP
except paramiko.AuthenticationException:
    print(f"Autenticação falhou para usuário {username}.")
except paramiko.SSHException as e:
    print(f"Houve um erro de SSH: {e}")
except Exception as e:
    import traceback
    print(f"Ocorreu um erro inesperado: {e.__str__()}")
    print(traceback.format_exc())
finally:
    ssh.close()

print("Programa encerrado.")
