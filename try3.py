lista= ['joao' , 'celia' , 'julia']
try:
    print(lista[2])

except:
    print ('nao existe esta posiçao mas irei criar, digite um nome')
    nome = input()

    lista.append(nome)