import database

class Cliente:
    def __init__(
        self,
        codigo,
        nome,
        cpf,
        data_nascimento,
        endereco,
        numero,
        complemento,
        bairro,
        municipio,
        uf,
        telefone,
        telefone_alternativo,
    ):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.municipio = municipio
        self.uf = uf
        self.telefone = telefone
        self.telefone_alternativo = telefone_alternativo

    def __repr__(self):
        return f"O cliente {self.nome} foi cadastrado com sucesso!"
        
    def relatorio(self):
        '''
        Função que exibe o relatório de todos os clientes do sistema
        '''
        print('')    
        for cliente in database.db_cliente:
            for chave, valor in cliente.items():
                print(f"{chave}: {valor}")
            print('')

def teste_int(variavel):
    '''
    Função que verifica se o valor digitado pelo usuário é um número inteiro
    A variável 'variavel' é o nome da variável que o usuário digitou
    '''
    while True:
        try:
            inteiro = int(input(f"Digite o {variavel}: "))
            return inteiro
        except ValueError:
            print(f"Entrada inválida. Digite o valor corretamente!")