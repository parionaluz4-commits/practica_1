# datos estructurados📔
- tenemos 3 tipos de datos primarios 
(string,numericos y boleanos)
- tenemos 2 tipos de datos estructurados (listas y diccionarios)
## listas 📒
🤓son la manera de como python puede organizar multiples tipos de datos en una sola variable.
se puede tener :
- listas de tipo numerica 
- listas de tipo texto
- listas de tipo mixto
python nos permite acceder a estas listas a travez de indices los indices son ascendentes empezando del numero 0.
### creacion de listas🗒️
para crear listas solo basta encerrar los elementos que deseamos almacenar con `[]` inmediantamente despues del operador de asignacio `=`
```python
# creando una lista vacia
lista:list=[] #lista vacia
# lista numerica 
##OJO: los elementos de una lista se separan por comas 
lista_numericas:list[int]=[3,8,4] #listas de numeros enteros
listas_num_mixto:list[int|float]=[3.6,7,.7]
# lista de texto
amigos:list[str]=['eduardo','kevin']
# lista mixta
lista_mixta:list=['pedro',20,false,1.67]
```
### acceder y modificar elementos de una lista 
para poder acceder a un elemnto de la lista trabajamos con los indices que python le asigna a cada elemento que tenemos :
- los indices posivos (comienzan de 0 y van a la izquierda a derecha)
- los indices negativos (comienzan de -1 y van de derecha a izquierda)
con estos indices podemos acceder al valor del elemento y tambien podremos modificarlos 
tenemos 2 formas de acceder a estos elementos 
- por indice (posicion)
```python
frutas:list[str]=["🍎","🍒","🍍","🍑"]
# posicion o indice
#acceder al tercer elemento 
print(frutas[2])
# acceder al 2 elemnto por su indice negativo
print(futas[-3])
# modificar 
frutas[3]="naranja"
```

- por rango (slicing)
```python
vocales:str=['a','e','i','o','u']
#acceder a elementos por slicing
# esta tecnica nos permite acceder a mas de un elemento en una sola linea de codigo
vocales[0:3]
## remplazar elementos por slicing 
vocales[0:3]=['A','E','I']
```
## diccionarios📓

