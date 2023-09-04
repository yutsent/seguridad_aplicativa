#programa que muestra los 100 números primos. 

#def primo(num):
#    x = num%2
#    if x == 0:
#        print ("El numero no es primo")
#    else:
#        print ("El numero es primo")
      
lista = []  
for i in range(1,1000):
    lista.append(i)

primos=[]
for i in lista:
    x = i%2
    if x != 0:
        primos.append(i)
    elif len(primos) == 100:
        break
    else:
        pass

print(primos)
print(len(primos))