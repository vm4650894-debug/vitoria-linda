import requests 


option =input('bem vindo digite a opçao que voce deseja: 1 para add produto ,2 para deletar , 3 para alterar')


if option =='1':

    prato =  input('escolha o seu prato : pizza , macarrao, lasanha ')
    bebida =  input('escolha a sua bebida')
    mesa =  input('escolha a sua mesa')

    pedido={
        'Prato':prato,
        'Bebida':bebida,
        'Mesa':mesa
    }

    requests.post('https://68dea903898434f41355979b.mockapi.io/Fastfood',pedido)

elif option =='2':
    dados =requests.get('https://68dea903898434f41355979b.mockapi.io/Fastfood').json()
    print(dados)

    for item in dados:
        print(item.get('id'))

    option= input('qual pedido voce deseja deletar?')
    
    requests.delete(f'https://68dea903898434f41355979b.mockapi.io/Fastfood/{option}')

else:
    option= input('qual pedido voce deseja alterar?')
    
    prato =  input('escolha o seu prato : pizza , macarrao, lasanha ')
    bebida =  input('escolha a sua bebida')
    mesa =  input('escolha a sua mesa')

    novoPedido={
        'Prato':prato,
        'Bebida':bebida,
        'Mesa':mesa
    }

    for item in novoPedido:
        print(item.get('id'))


    requests.put('https://68dea903898434f41355979b.mockapi.io/Fastfood/{option}',novoPedido)







