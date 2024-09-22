import pandas as pd

def read_file_excel(vFile):
    vAux = pd.read_excel(vFile)
    return vAux
