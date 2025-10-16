import requests

dados=requests.get('https://68dea903898434f41355979b.mockapi.io/Fastfood')

result= dados.json()

for item in result:
    id =item.get('id')
    pedido=item.get('Prato')
    if 'pizza' in pedido:
        dados=requests.delete(f'https://68dea903898434f41355979b.mockapi.io/Fastfood/{id}')


                                                                                                                                                                                                                                                                                                                                                                                                        

    
