#VARIABLES

#Asignamos una variable al espacio de memoria
a = 5
print(a)
#imprime el typo
type(a)
print(type(a))
#id() indica el puntero de memoria
print(id(a))


# Si cambiamos la variable se sobrescribe, pero el espacio en memoria son inmutables y dinamico
a = 6
print(a)
#imprime el typo
type(a)
print(type(a))
#id() indica el puntero de memoria que ha cambiado, se ha sobrescrito, son referencias a una zona de memoria donde hay un valor exacto.
print(id(a))

#Volvemos a la variable 5
a = 5
print(a)
#imprime el typo
type(a)
print(type(a))
#id() indica el puntero de memoria del 5
print(id(a))


#CADENAS DE TEXTO
texto = 'hola'
#da fallo si queremos sobrescribirla 
#texto[1] = 'g'

#TUPLAS una especie de arrays inmutables

variable = ('a',3,'b')
id(variable)
#da fallo si queremos sobrescribirla 
#variable[1] = '2'


#LISTAS (SE PUEDEN ALTERAR)

lista= ['a','b','c']
print(lista)

#modificamos la lista
print('modificamos la lista con una C mayuscula:')
lista[2] = 'C'

print(lista)

print('Eliminamos de la lista la C')

lista.remove('C')

print(lista)

print('Concatenar de la lista la C y D')

lista.append('C')

lista.append('D')
print(lista)