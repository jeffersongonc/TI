import getpass
import os
#pip install cryptography
from cryptography.fernet import Fernet

class crypto:
    def __init__(self):
        if not os.path.exists("secret.key"):
            with open("secret.key", "wb") as f:
                f.write(Fernet.generate_key())

        with open("secret.key", "rb") as f:
            self.__key = f.read()

        self.__cipher = Fernet(self.__key)
    
    def criptografarChave(self, pChave: str) -> bytes:
        return self.__cipher.encrypt(pChave.encode())

    def decriptografarChave(self, pChaveCriptografada: bytes) -> str:
        return self.__cipher.decrypt(pChaveCriptografada).decode()


if __name__ == "__main__":
    crypto_instance = crypto()
    #chave = getpass.getpass("Digite a chave a ser criptografada: ")
    #chave_criptografada = crypto_instance.criptografarChave(chave)  
    #print(f"Chave Criptografada: {chave_criptografada.decode()}")
    chave_criptografada = input("Digite a chave criptografada: ").strip()
    chave_decriptografada = crypto_instance.decriptografarChave(chave_criptografada.encode())
    print(f"Chave Decriptografada: {chave_decriptografada}")
