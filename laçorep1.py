palavra= input ("digite uma palvra: ")
soma=0
vogais= 'aeiou'

for items in palavra:
    print(items)
    if items in vogais:
        soma +=1
    
print (soma)


