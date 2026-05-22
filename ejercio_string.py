## crear un programa que busque en el pensamiento de cesar acuña la palabra politicos 
# hay politicos que no hacen nada por que nunca han echo nada.
## y mostrar por la terminar si lo encuentra 

parrafo:str="hay politicos que no hacen nada por que nunca han echo nada"
(parrafo.find("politicos"))
print(parrafo[3:13])
##
pensamiento_uno:str="hay politicos que no hacen nada por que nunca han echo nada"
palabra_buscar="politicos"
print("politicos" if pensamiento_uno.find(palabra_buscar)>0 else "texto no encontrado")

## crear un programa que en el siguiente texto busque 'ya no vivo en trujillo, vivo en peru' busque peru y remplaze por narnia finalmente mostrarlo por la terminal 
texto_incorrecto:str="ya no vivo en trujillo, vivo en peru"
print(texto_incorrecto.replace("peru","narnia"))
