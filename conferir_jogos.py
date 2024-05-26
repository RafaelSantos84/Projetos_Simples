from colorama import Fore, Style
from os import system
class ConferirJogos:
    def __init__(self, *jogos):
        self.jogos = jogos
    
    def verificar_jogos(self, *aposta):
        self.aposta = aposta
        tamanho_jogos = len(self.jogos) #números sorteados
        acertos = []

        if tamanho_jogos == 6: #teste da mega
            for i in range(tamanho_jogos):
                if self.jogos[i] in aposta:
                    acertos.append(self.jogos[i])
            if len(acertos) == 4:
                print(f'Parabéns, {Fore.RED}{acertos}{Style.RESET_ALL} foram os 4 números sorteados, QUADRA.')
            elif len(acertos) == 5:
                print(f'Parabéns, {Fore.RED}{acertos}{Style.RESET_ALL} foram os 5 números sorteados, QUINA.')
            elif len(acertos) == 6:
                print(f'Parabéns, {Fore.RED}{acertos}{Style.RESET_ALL} foram os 6 números sorteados, MEGA!!!')
            if 0 < len(acertos) < 4: 
                print(f'Você acertou {Fore.GREEN}{len(acertos)}{Style.RESET_ALL} número(s) de 1 aposta.')

        if tamanho_jogos == 15: #teste da loto facil
            for i in range(tamanho_jogos):
                if self.jogos[i] in aposta:
                    acertos.append(self.jogos[i])
            if len(acertos) == 11:
                print(f'Parabéns, {Fore.RED}{acertos}{Style.RESET_ALL} foram os 11 números sorteados.')
            elif len(acertos) == 12:
                print(f'Parabéns, {Fore.RED}{acertos}{Style.RESET_ALL} foram os 12 números sorteados.')
            elif len(acertos) == 13:
                print(f'Parabéns, {Fore.RED}{acertos}{Style.RESET_ALL} foram os 13 números sorteados')
            elif len(acertos) == 14:
                print(f'Parabéns, {Fore.RED}{acertos}{Style.RESET_ALL} foram os 14 números sorteados!')
            elif len(acertos) == 15:
                print(f'Parabéns, {Fore.RED}{acertos}{Style.RESET_ALL} foram os 15 números sorteados, PRÊMIO MÁXIMO!!!')    
            if 0 < len(acertos) < 10: 
                print(f'Você acertou {Fore.GREEN}{len(acertos)}{Style.RESET_ALL} número(s) de 1 aposta.')

mega = ConferirJogos(3, 7, 10, 25, 31, 52)

system('cls')
print(f'Referência {Fore.YELLOW}xxx{Style.RESET_ALL}')
print(f'Bolão da MEGA do dia {Fore.YELLOW}xx/xx/2024{Style.RESET_ALL}')
mega.verificar_jogos(5,12,17,21,37,40,42,48)

print()

loto_facil = ConferirJogos(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

print(f'Referência {Fore.CYAN}xxx{Style.RESET_ALL}')
print(f'Bolão da LOTO FACIL do dia {Fore.CYAN}xx/xx/2024{Style.RESET_ALL}')
loto_facil.verificar_jogos(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,12)
loto_facil.verificar_jogos(1,2,3)

print()

dupla_sena = ConferirJogos(3, 7, 10, 25, 31, 52)


print(f'Referência {Fore.LIGHTMAGENTA_EX}DS-89332406{Style.RESET_ALL}')
print(f'Bolão da DUPLA SENA do dia {Fore.LIGHTMAGENTA_EX}30/03/2024{Style.RESET_ALL}')
dupla_sena.verificar_jogos(8,17,29,34,36,39,42,48)
dupla_sena.verificar_jogos(2,13,16,28,30,32,33,41)
dupla_sena.verificar_jogos(2,8,10,15,18,39,40,41)
dupla_sena.verificar_jogos(8,17,18,21,24,27,28,47)
dupla_sena.verificar_jogos(2,11,21,22,32,35,41,50)
dupla_sena.verificar_jogos(19,32,39,42,44,45,46,50)

print()
