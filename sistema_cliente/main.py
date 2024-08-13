import models
import database

resposta = 'sim'
#self, codigo, nome, cpf, data_nascimento, endereco, numero, complemento, bairro, municipio, uf, telefone, telefone_alternativo
while resposta == 'sim':
    codigo = len(database.db_cliente)
    nome = str(input("Nome = "))
    cpf = models.teste_int("cpf")
    data_nascimento = str(input("Data de nascimento = "))
    endereco = str(input("Endereço = "))
    numero = str(input("Numero = "))
    complemento = str(input("Complemento = "))
    bairro = str(input("Bairro = "))
    municipio = str(input("Município = "))
    uf = str(input("UF = "))
    telefone = models.teste_int("telefone")
    telefone_alternativo = models.teste_int("telefone alternativo")

    clientes = models.Cliente(codigo, nome, cpf, data_nascimento, endereco, numero, complemento, bairro, municipio, uf, telefone, telefone_alternativo)
    cadastro = clientes.__dict__
    database.db_cliente.append(cadastro)
    print(clientes)
    resposta = input("Deseja continuar? [sim / nao] = ")
    while resposta not in database.respostas:
        print("ERRADO!")
        resposta = input('Deseja continuar? [sim / nao] = ')
print(clientes.relatorio())
