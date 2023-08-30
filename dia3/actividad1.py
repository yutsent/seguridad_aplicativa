#crear un programa que detecte si una palabra es un palindromo
nombre = input ("ingresa la palabra a verificar: ")

if nombre == nombre[::-1]:
    print ("la palabra que ingresaste es un palindromo")
else:
    print ("lo siento tu palabra no es un palindromo")
