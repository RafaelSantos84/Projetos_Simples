cont = contador_acerto = 0
resposta = ''
perguntas = [
{
    'Pergunta': 'Quanto é 2+2?',
    'Opções': ['1', '2', '4', '5'],
    'Resposta': '4',
},
{
    'Pergunta': 'Quanto é 5*5?',
    'Opções': ['25', '55', '10', '51'],
    'Resposta': '25',
},
{
    'Pergunta': 'Quanto é 10/2?',
    'Opções': ['4', '5', '2', '1'],
    'Resposta': '5',
}
]
while cont < len(perguntas):
    print(perguntas[cont]['Pergunta'])
    
    for indice, valor in enumerate(perguntas[cont]['Opções']):
        print(f'{indice}) {valor}')
    
    resposta = input('Escolha uma opção: ')
    try:
        if perguntas[cont]['Opções'][int(resposta)] == perguntas[cont]['Resposta']:
            print('Acerto Miserável!\n')
            contador_acerto += 1
        else:
            print('Resposta Errada\n')
    except:
        print('Resposta Errada\n')
    
    cont += 1
print(f'Você acertou {contador_acerto} de {cont} perguntas!')