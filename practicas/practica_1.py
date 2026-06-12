## una ferreteria tiene separada en dos listas los sigientes procductos
"""
1. lista de productos de limpieza (10 productos)
2. lista de materiales de construccion 

el dueño desea realizar las siguientes acciones
1. en su lista de productos de limpieza existe un meterial de  construccion, 
debes eliminarlos y pasar el producto a la lista que corresponde 
2. indicar si en la lista M.C existe cemento
3. en la lista de P.L buscar el producto lejia y cambiar su valor por lejia sapolio.
4. mostrar un mensaje donde se detalle cual es la lista de M.C y la lista de P.L formateado.
"""
productos_limpieza: list[str] = ['lejia', 'detergente', 'esponja', 'guantes', 'cemento',
                                 'desinfectante', 'trapeador', 'cloro', 'ambientador', 'lavavajilla']
print(productos_limpieza)

materiales_construccion: list[str] = ['ladrillo', 'arena', 'pintura', 'martillo', 'clavos',
                                      'tubo', 'yeso', 'wincha', 'brocha', 'calamina']
print(materiales_construccion)
# 1. cambiar de lista cemento
elemento_retirado=productos_limpieza.pop(productos_limpieza.index("cemento"))
materiales_construccion.append(elemento_retirado)
# 2. indicar si en la lista M.C existe cemento
existe:bool="cemento" in materiales_construccion
print(f"existe el cemento?:{existe}")
# 3. cambiar lejia por lejia sapolio
buscar=productos_limpieza.index("lejia")
productos_limpieza[buscar]="lejia sapolio"
print(productos_limpieza)
# 4. mostrar mensaje
mensaje:str=f"""
   | mi lista de productos de limpieza despues de la modificacion queda de la siguiente manera{productos_limpieza}
   | mi lista de materiales de construccion despues de la modificacion queda de la siguiente manera{materiales_construccion}
"""
