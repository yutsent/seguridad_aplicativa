#crear un programa que detecte si una palabra es un palindromo
nombre = input ("ingresa la cadena a verificar: ")
nombre = nombre.replace(" ","")
if nombre == nombre[::-1]:
    print ("la cadena que ingresaste es un palindromo")
else:
    print ("lo siento tu frase no es un palindromo")
