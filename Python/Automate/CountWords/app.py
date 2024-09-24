import pandas as pd
import re
from collections import Counter

tabela = pd.read_csv("ReviewsIPhoneX.csv")

texto = "".join(tabela["body"].astype(str))
texto= texto.lower()
lista_palavras = re.findall(r"\b\w+\b", texto)

contagem_palavras = Counter(lista_palavras)

for item in contagem_palavras.most_common(200):
    print(item)