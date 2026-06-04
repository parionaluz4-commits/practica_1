#Crear una lista de 5 animales vertebrados  y 5 animales invertebrados El orden deberá ser aleatorio
#Tendrás que hacer las siguientes correcciones:
"""
1.Modificar los 3 primeros elementos por aves 
2.Modificar el 6 y último elemento por reptiles 
3.modificar el elemento 8 por gianfranco 
4.mostrar toda la lista nueva con las modificaciones
"""
animales: list[str] = ['leon', 'zancudo', 'jaguar', 'saltamontes', 'jabali',
            'araña', 'perro', 'cangrejo', 'estrella de mar', 'aguila']

animales[0:3] = ['loro', 'gallina', 'pato']
animales[5] = 'cocodrilo'
animales[-1] = 'iguana'
animales[7] = 'gianfranco'

print(f"la lista modificada es: {animales}")