import requests

inf=requests.get('https://68dea903898434f41355979b.mockapi.io/Fastfood')

print (inf.json())

result=inf.json()

print(result)

for item in result:
    print(item.get('bebidas'))