from faker import Faker

class DataBase:
    def __init__(self):
        self.faker = Faker()
    
    def get_data(self):
        listaClientes = []
        for i in range(1000):
            cliente = {
                "id": i+1,
                "nome": self.faker.name(),
                "email": self.faker.email(),
                "telefone": self.faker.phone_number(),
                "endereco": self.faker.address(),
                "company": self.faker.company(),
                "job": self.faker.job(),
                "text": self.faker.text()
            }
            listaClientes.append(cliente)
        return listaClientes