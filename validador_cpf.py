from colorama import Fore, Style
class Validador_cpf:
    def __init__(self, cpf:str):
        self.cpf = cpf.strip()
    
    def verificar_entrada(self):
        if not self.cpf.isnumeric(): #verifica se o cpf contém apenas números
            raise ValueError(f'{Fore.RED}O cpf deve conter apenas números!{Style.RESET_ALL}')

        if len(self.cpf) != 11:#verifica se o cpf tem 11 números
            raise ValueError(f'{Fore.RED}O cpf deve conter 11 números!{Style.RESET_ALL}')

        if self.cpf.count(self.cpf[0]) == 11:
            raise ValueError(f'{Fore.RED}O cpf não deve conter os 11 números repetidos!{Style.RESET_ALL}')
        
    def validar_cpf(self):
        self.verificar_entrada()
        lista_cpf = []
        for numero in self.cpf:
            lista_cpf.append(int(numero))
        
        multiplicadores_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        multiplicadores_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

        resultado_final_1 = 0

        for digito in range(0, 9):
            resultado_1 = lista_cpf[digito]*multiplicadores_1[digito]
            resultado_final_1 += resultado_1
        
        resultado_final_2_multiplicado_10 = resultado_final_1*10
        
        resto_resultado_1_final_multiplicado_10 = resultado_final_2_multiplicado_10 % 11
        if resto_resultado_1_final_multiplicado_10 > 9:
            penultimo_numero_cpf = 0
        else:
            penultimo_numero_cpf = resto_resultado_1_final_multiplicado_10

        resultado_final_2 = 0

        for digito in range(0, 10):
            resultado_2 = lista_cpf[digito]*multiplicadores_2[digito]
            resultado_final_2 += resultado_2

        resultado_final_2_multiplicado_10 = resultado_final_2*10
        
        resto_resultado_final_2_multiplicado_10 = resultado_final_2_multiplicado_10 % 11
        if resto_resultado_final_2_multiplicado_10 > 9:
            ultimo_numero_cpf = 0
        else:
            ultimo_numero_cpf = resto_resultado_final_2_multiplicado_10

        if penultimo_numero_cpf == lista_cpf[9] and ultimo_numero_cpf == lista_cpf[10]:
            return print(f'{Fore.GREEN}O CPF {self.cpf} é Válido!{Style.RESET_ALL}')
        else:
            return print(f'{Fore.RED}O CPF {self.cpf} é Inválido!{Style.RESET_ALL}')


teste_validador = input('Digite seu CPF: ')  #digite seu cpf
cpf = Validador_cpf(teste_validador)
Validador_cpf.validar_cpf(cpf)