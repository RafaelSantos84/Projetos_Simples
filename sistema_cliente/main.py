import models
import database

resposta = 'sim'
#self, codigo, nome, cpf, data_nascimento, endereco, numero, complemento, bairro, municipio, uf, telefone, telefone_alternativo
while resposta == 'sim':
    codigo = len(database.db_cliente)
    nome = str(input("Nome = "))
    cpf = int(input("CPF = "))
    data_nascimento = str(input("Data de nascimento = "))
    endereco = str(input("Endereço = "))
    numero = str(input("Numero = "))
    complemento = str(input("Complemento = "))
    bairro = str(input("Bairro = "))
    municipio = str(input("Município = "))
    uf = str(input("UF = "))
    telefone = int(input("Telefone = "))
    telefone_alternativo = int(input("Telefone alternativo = "))

    print(database.db_cliente)

    cliente1 = models.Cliente(codigo, nome, cpf, data_nascimento, endereco, numero, complemento, bairro, municipio, uf, telefone, telefone_alternativo)
    cadastro = cliente1.__dict__
    database.db_cliente.append(cadastro)
    print(cliente1)
    print(database.db_cliente)

    resposta = input("Deseja continuar? ")