import base64
import getpass
import os
#pip install python-dotenv
from dotenv import load_dotenv
#pip install cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

load_dotenv()

class crypto:
    def __init__(self, pKey: str = None):
        '''Inicializa a classe de criptografia e decriptação usando Fernet.
        A criptografia Fernet é simétrica, ou seja, a mesma chave é usada para criptografar e decriptografar os dados.
        É utilizado um hash SHA256 para garantir a integridade dos dados.
        Caso não seja informada uma chave, uma nova chave é gerada e salva.
        pKey => Chave de criptografia Fernet (opcional). Lê variaável de ambiente SECRET_KEY.'''
        try:
            if not pKey:
                if not os.path.exists("secret.key"):
                    self.__password = getpass.getpass("Digite uma VALOR para gerar a CHAVE de criptografia: ").encode()
                    self.__salt = os.urandom(32)
                    self.__kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=self.__salt,
                        iterations=1_200_000,)
                    self.__key = base64.urlsafe_b64encode(self.__kdf.derive(self.__password))
                    with open("secret.key", "wb") as f:
                        f.write(self.__key)
                
                with open("secret.key", "rb") as f:
                    self.__cipher = Fernet(f.read())
            else:
                self.__cipher = Fernet(pKey.encode())
        except Exception as e:
            print(f"Erro ao inicializar a classe de criptografia: {e}")
    
    def criptografarChave(self, pChave: str) -> bytes:
        '''Criptografa a chave informada utilizando a chave Fernet.
        pChave => Dado a ser criptografada.'''
        try:
            return self.__cipher.encrypt(pChave.encode())
        except Exception as e:
            print(f"Erro ao criptografar a chave: {e}")

    def decriptografarChave(self, pChaveCriptografada: bytes) -> str:
        '''Decriptografa a chave informada utilizando a chave Fernet.
        pChaveCriptografada => Dado a ser decriptografada.'''
        try:
            return self.__cipher.decrypt(pChaveCriptografada).decode()
        except Exception as e:
            print(f"Erro ao decriptografar a chave: {e}")

def menu():
    print("1 - Criptografar chave")
    print("2 - Decriptografar chave")
    print("0 - Sair")
    return input("Escolha uma opção: ").strip()

if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == "1":
            crypto_instance = crypto()
            password = getpass.getpass("Digite a SENHA a ser criptografada: ")
            chave_criptografada = crypto_instance.criptografarChave(password)  
            print(f"Chave Criptografada: {chave_criptografada.decode()}")
        elif opcao == "2":
            crypto_instance = crypto(os.getenv("SECRET_KEY"))
            chave_decriptografada = crypto_instance.decriptografarChave(os.getenv("KEY_CRIPTO").encode())
            print(f"Chave Decriptografada: {chave_decriptografada}")
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
    
    
    
    ''''
    crypto_instance = crypto()
    password = getpass.getpass("Digite a SENHA a ser criptografada: ")
    chave_criptografada = crypto_instance.criptografarChave(password)  
    print(f"Chave Criptografada: {chave_criptografada.decode()}")
    
    #crypto_instance = crypto(input("Digite a CHAVE de criptografia: ").strip())
    crypto_instance = crypto(os.getenv("SECRET_KEY"))
    #chave_criptografada = input("Digite a chave criptografada: ").strip()
    #chave_decriptografada = crypto_instance.decriptografarChave(chave_criptografada.encode())
    chave_decriptografada = crypto_instance.decriptografarChave(os.getenv("KEY_CRIPTO").encode())
    print(f"Chave Decriptografada: {chave_decriptografada}")
    '''