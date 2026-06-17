alumnos:list[str]=['eduardo','noemi','victor','emerson','yo']
print(alumnos)
# eliminar por valor
alumnos .remove('yo')
print(alumnos)
# eliminar el ultimo valor por defecto
alumnos.pop()
print(alumnos)
## pop tambien elimina elementos por indice y recupera lo eliminado 
a=alumnos.pop(1)
print(f"elimine: {a}")
alumnos.pop(1)
print(f"mi lista de desaprobados sera : {alumnos}")

## tengo una lista de marcas de vehiculos (toyota,nissan,datsun,daewod,simo mack,mazda,honda), crear un programa que realice los siguientes :
"""
1. eliminar el 5 elemento.
2. en su lugar agregar la marca mitsubishi
3. buscar nissan y mostrar su valor por terminal
4. mostrar si existe honda en mi lista de vehiculos
"""
vehiculos = ["toyota", "nissan", "datsun", "mazda", "ford"] 
print(vehiculos)

# 1. eliminar el 5 elemento
vehiculos.pop(4) 
print(vehiculos)

# 2. en su lugar agregar mitsubishi
vehiculos.insert(4, "mitsubishi") 
print(vehiculos)

# 3. buscar nissan y mostrar su valor
buscar:int=vehiculos.index("nissan")
print(buscar) 
print(vehiculos[buscar]) 

# 4. mostrar si existe honda
existe:bool="honda" in vehiculos
print(existe)
