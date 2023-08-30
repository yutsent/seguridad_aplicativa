#Modificacion el codigo para generar una calculadora reciba el parametro
#por la linea de comandos y utilice funciones
#1 = suma
#2 = resta
#3 = multiplicación 
#4 = division

operacion = int(input ("""Ingerese una de las siguientes opciones:
                   1 = suma
                   2 = resta
                   3 = multiplicacion
                   4 = division
                   """))

def suma(param1,param2):
    return param1 + param2

def resta(param1,param2):
    return param1 - param2

def multiplicacion(param1,param2):
    return param1 * param2

def division (param1,param2):
    
    return param1 / param2

if operacion == 1:
    valor1 = int(input ("Ingrse el primer numero: "))
    valor2 = int(input ("Ingresa el segundo numero: "))
    x = suma(valor1,valor2)
    print ("la suma de: ",valor1, "+",valor2, "es igual a " ,x)
elif operacion == 2:
    valor1 = int(input ("Ingrse el primer numero: "))
    valor2 = int(input ("Ingresa el segundo numero: "))
    x = resta(valor1,valor2)
    print ("la resta de: ",valor1, "-",valor2, "es igual a " ,x)
elif operacion == 3:
    valor1 = int(input ("Ingrse el primer numero: "))
    valor2 = int(input ("Ingresa el segundo numero: "))
    x = multiplicacion(valor1,valor2)
    print ("la multiplicación de: ",valor1, "*",valor2, "es igual a " ,x)
elif operacion == 4:
    valor1 = int(input ("Ingrse el primer numero: "))
    valor2 = int(input ("Ingresa el segundo numero: "))
    if valor2 == 0:
        x = print ("no es posible dividir entre cero")
    else:
        x = division(valor1,valor2)
        print ("la division de: ",valor1, "/",valor2, "es igual a " ,x)
else:
    print ("opcion invalida. Hasta luego")
