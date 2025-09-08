def dividir(a, b):
    try:
        return a / b
    except:
        return None
    

    print(dividir(10, 2))   
print(dividir(10, 0))    
print(dividir(10, 'a'))  