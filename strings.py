myStr = "Hello world" #My_String

#print(dir(myStr))
 #aparecen varios metodos
#upper, cambia todo a mayus

print(myStr.upper()) #el punto indica la funcion que necesita
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("Hello", 'bye').upper())
#metodos encadenados
print(myStr.count("l")) #cuenta 

print(myStr.startswith("hola")) #arroja False

myStr.split() #separa mi texto en dos en espacios
myStr.split(",") #separa por la coma
#crea listas
myStr.find("o") #devuelve posicion de la letra o

len(myStr) #muestra longitud
myStr.index("e") #muestra indice

myStr.isnumeric() #es numerico
myStr.isalpha() 

myStr[4] #valor o
myStr[-1] #devuelve desde la derecha

print("My name is " + myStr)
print(f"My name is {myStr}")
print("My name is {0}".format(myStr))


