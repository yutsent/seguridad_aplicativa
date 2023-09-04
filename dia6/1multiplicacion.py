#tabla de multiplicación

def multi(num1,num2):
    return num1 * num2

for i in range(1,11):
    print ("Tabla del numero: ",i)
    for b in range(1,10):
        print (i," x ",b, " = ",multi(i,b))
