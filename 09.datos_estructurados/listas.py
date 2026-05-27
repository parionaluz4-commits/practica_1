lista_vacia:list=[]
print(len(lista_vacia))
# por regla el nombre de la variable no debe tener el tipo de dato que se va almacenar 
amores:list[str]=['wicho','pocohuanca','cesar','perci','guido']
print(f"la cantidad de elementos que tiene la variable amores es {len(amores)}")

frutas:list[str]=['🍎','🍒','🍍','🍑']
# posicion o indice
#acceder al tercer elemento 
print(frutas[2])
# acceder al 2 elemnto por su indice negativo
print(frutas[-3])
# acceder por rango
# Crear una lista de frutas
frutas:list[str] = ['🍎', '🍒', '🍍', '🍑']

# Acceder por indice
print("Por indice:")
print(frutas[2]) # 🍍
print(frutas[-3]) # 🍒

# Acceder por rango - Slicing
print("\nPor rango:")
print(frutas[0:2]) # ['🍎', '🍒'] → Primeros 2 elementos
print(frutas[1:3]) # ['🍒', '🍍'] → Del segundo al tercero
print(frutas[2:]) # ['🍍', '🍑'] → Desde el tercero hasta el final
print(frutas[:2]) # ['🍎', '🍒'] → Desde inicio hasta antes del 2
print(frutas[-3:]) # ['🍒', '🍍', '🍑'] → Los últimos 3
print(frutas[::2]) # ['🍎', '🍍'] → De 2 en 2
print(frutas[::-1]) # ['🍑', '🍍', '🍒', '🍎'] → Lista invertida