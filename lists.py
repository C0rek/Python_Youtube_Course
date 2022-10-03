demo_list = [1, "hola", True, [1,2,3]]
colors["red", "green", "blue"]

number_list= list((1,2,3,4))

#basada en un rango
r = list(range(1, 10))
#en vez de poner 1,2,3,4,5
print(r)

#con dir puedo obtener informacion

print(colors)
colors.append(("violet", "yellow")) #tupla pero me devuelve mal
colors.extend(["violeta", "gris"]) #tupla y me devuelve individual

colors.insert(1, "violeta")
print(colors)

#remover  colores

colors.pop() #quita el ultimo
colors.remove("green") #quita el elemento
colors.pop(1) #quita el indice 1
colors.clear() #remueve todo
colors.sort #ordenar alfabeticamente
colors.sort(reverse=True) #no alfabeticamente
print(colors.index("blue")) #obtiene indice de blue
colors.count("blue") #cuenta



