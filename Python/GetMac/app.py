from getmac import get_mac_address as gma
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


DEFAULT_MAC_ADDRESS = os.environ.get('DEFAULT_MAC_ADDRESS') or "NONE"
MAC_ADDRESS = gma()

if (DEFAULT_MAC_ADDRESS.upper() != MAC_ADDRESS.upper()):
    print("Entre em contato com o suporte e informe o código: D1FM4(.")
else:
    print("Acesso concedido!")