from fastapi import FastAPI
from DB import DataBase

app = FastAPI(debug=True)

@app.get("/")
def home():
    db = DataBase()
    data = db.get_data()
    return data

@app.get("/cliente/{cliente_id}")
def get_cliente(cliente_id: int):
    db = DataBase()
    data = db.get_data()
    return data[cliente_id - 1] if 0 < cliente_id <= len(data) else {"Erro": "Cliente não encontrado"}

@app.get("/cliente_nome/{cliente_nome}")
def get_cliente_nome(cliente_nome: str):
    db = DataBase()
    data = db.get_data()
    data_aux = []
    for nome in data:
        print(nome["nome"].upper())
        if cliente_nome.upper() in nome["nome"].upper():
            print(nome)
            data_aux.append(nome)

    return data_aux if data_aux else {"Erro": "Cliente não encontrado"}