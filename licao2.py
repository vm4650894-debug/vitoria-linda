nomes = ['a','b','c','d']


#removendo elementos
del nomes [3]  #remove o elemento no indice 3
print ("apos del:", nomes)

nomes.remove ("maria") #remove a primeira ocorrencia de "maria"
print ("apos remove:", nomes)

removido = nomes.pop (2) #remove e retorna o elemento no indice 2
print (f" apos pop(removido  {removido}):")

nomes.clear ()  # esvavia a lista
print ("apos clear:" , nomes)
