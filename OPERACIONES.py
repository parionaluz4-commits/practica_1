##todas las operaciones aritmeticas  que se usan con numeros en python
# 1. suma - operador binario
#variables globales 
## son datos que se puedan utilizar en cualquier software que estes construyendo 
# variables locales 
## son datos que solo son accesibles en pequeñas porciones de codigo o "scope"
firts_numb:int|float=20
second_numb:int|float=5

print(f"la suma de {firts_numb} + {second_numb} = {firts_numb+second_numb}")
print(f"la resta de {firts_numb} - {second_numb} = {firts_numb-second_numb}")
#div
print(f"la division de {firts_numb} / {second_numb} = {firts_numb/second_numb}")

#multiplicacion
print(f"la multi de {firts_numb} * {second_numb} = {firts_numb*second_numb}")
# division exacta
print(f"la diviexac de {firts_numb} // {second_numb} = {firts_numb//second_numb}")
## incremento (++)
print(f"el incremento de  {firts_numb} es {++firts_numb} ")
## decremento (--)
print(f"el decremento de  {firts_numb} es {--firts_numb} ")
## potenciacion
print(f"la potencia de {firts_numb} ** {second_numb} = {firts_numb**second_numb}")
