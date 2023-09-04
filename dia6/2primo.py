#numero primo

def primo(num):
    x = num%2
    if x == 0:
        print ("El numero no es primo")
    else:
        print ("El numero es primo")
        
a = int(input("Ingresa un numero"))

primo(a)
