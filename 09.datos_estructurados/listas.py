lista_vacia:list=[]
print(len(lista_vacia))
# por regla el nombre de la variable no debe tener el tipo de dato que se va almacenar 
amores:list[str]=['wicho','pocohuanca','cesar','perci','guido']
print(f"la cantidad de elementos que tiene la variable amores es {len(amores)}")

frutas:list[str]=['🍎','🍒','🍑','🍊']
# posicion o indice
#acceder al tercer elemento 
print(frutas[2])
# acceder al 2 elemnto por su indice negativo
print(frutas[-3])
# acceder por rango
# Crear una lista de frutas
frutas:list[str] = ['🍎', '🍒', '🍊', '🍑']

# Acceder por indice
print("Por indice:")
print(frutas[2]) #🍊
print(frutas[-3]) # 🍒
##por indice (posicion)
frutas:list[str]=["🍎","🍒","🍌","🍑","🍊"]
# posicion o indice
#acceder al tercer elemento 
print(frutas[2])
# acceder al 2 elemnto por su indice negativo
print(frutas[-3])

# modificar el ultimo elemento con una naranja 
frutas[-1]="🍊"
print(frutas)
## slicing
ciudades:list[str]=['lima','ica','chincha','pauza','urcus']
## si deseamos que los datos extraidos sean persistentes osea se manten gan almacenados durante la ejecucion de mi programa los almaceno en una variable 
datos_extraidos:list[str]=ciudades[-2:]
## si solo deseo mostrar y no almacenqr el slicing lo realizo en  el print 
print(ciudades[0:3])
print(datos_extraidos)
### remplazo de elementos por slicing
num_pares:list[int]=[1,2,3,5,6,8,10]
print(num_pares)
num_pares[0:3]=[2,4]
print(f"mi lista modificada es: {num_pares}")