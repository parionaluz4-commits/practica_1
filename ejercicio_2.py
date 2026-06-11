# crear un programa que me permita agregar a mi lista de compras los siguientes ingredientes (cebolla,trucha,limon,culantro,pinguita de nomo,papa,cancha)
# entrada de datos 
ingredientes:list[str]=[]
#desarrollo
for i in range(7):
    ingrediente:str=input("ingrese tu ingrediente: ")
    ingredientes.append(ingrediente)
    # datos de salida
print(ingredientes)
