#programa que muestra los 100 números primos. 
      
lista = []  
for i in range(1,1000):
    lista.append(i)

primos=[]
for i in lista:
    x = i%2
    y = i%3 
    if x == 1 and y == 1:
        primos.append(i)
    elif len(primos) == 100:
        break
    else:
        pass

print(primos)
