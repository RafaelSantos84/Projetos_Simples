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
