# programa para calcular raiz cuadratica

# input

A = int(input("Digite el valor de A: "))
B = int(input("Digite el valor de B: "))
C = int(input("Digite el valor de C: "))

# processing
d=B*2-4*A*C
if d == 0:
    print ("es un número imaginario")
else: