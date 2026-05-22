











## F-strings 
# formato de string esto sirve para formatear string con variables de python y para sus se requiere de un f antes de escribir un string si se desea incluir codigo python en el string, si se desea incluir codigo python en el string se de encerrar en llaves
nombre:str = "gianfranco"
edad: int = 14
#mensaje de salifda me diga hola mi nombre es {}  y tengo {}
print(f"hola mi nombre es {nombre} y tengo{edad}")

## plantillas de string
nombre_cliente :str= input("ingresa tu nombre: ")
ruc_cliente:int=input("ingresa ruc: ")
direccion_cliente:str=input("digite direccion: ")
codigo_producto:str=input("ingresa nombre: ")
nombre_producto:str=input("ingrese nombre: ")
precio_unidad:float=float(input("el precio del producto"))
cantidad_producto:float=float(input("cantidad a comprar: "))
precio_total:float=float=precio_unidad*cantidad_producto

plantilla:str=f""""
cliente: {nombre_cliente}
cliente: {nombre_cliente}.......RUC: {ruc_cliente}
direccion: {direccion_cliente}

codigo producto   |  nombre producto  |    p_unidad      |  cantidad
{codigo_producto}    {nombre_producto}  {precio_unidad}      {cantidad_producto}
------------------------------------------------------------------------------------
el precio total de su compra es de: {precio_total}
---
print(plantila)
