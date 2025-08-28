nome= input('digite seu nome')
horario=input('digite seu horario')

def estresse (nome, horario):
    if horario =='dia':
        print(f'bom dia, {nome}')

    elif horario =='tarde':
        print (f'boa tarde, {nome}') 

    else:
        print (f' boa noite, {nome}')       

estresse(nome,horario)