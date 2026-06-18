# modulos y libreria estandar 
# libreria estandar typing tipar datos a list y diccionarios para hacer mas optimo el codigo
# modulo es una porcion de codigo utilizable para poder usarlo nesecitamos importar la parte del codigo que deseamos utilizar.

# en este codigo estoy importando desde la libreria typing la funcion union
from typing import union ,Dict,List
#union me permite tipar una coleccion de tipos, que si no sabes el tipo de dato con union le podemos pasar una lista de los posibles tipos de datos que puede tener mi valo
from typing import union 
# sin libreria 
# alumno:dict[str:str|int]
alumno:dict[str:union [int,float,bool]]=(
"id_alumno":1,
"dni":78654328,
"nombre":"mio",
"edad":20,
"matricula":true
)

#acceder
#clasica
print(alumno["dni"])
print(alumno["matricula"])
# codigo erroneo print(alumno["matricula"])
## metodos
print(alumno.get("edad","valor no encontrado"))
# crear/modificar
print(alumno)
alumno["nombre"]="otro" # si existe la clave actualizza el valor

alumno["ruc"]=90876543267 # si no existe la clave lo crea

print(alumno)
# crear/modificar varios
alumno.update({"nombre":"celia","edad":15})
alumno.update({"carrera":"agro","semestre":"III"})
print(alumno)
# eliminar
