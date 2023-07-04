def sumar(x,y,z):
    resultado = x+y+z
    return resultado
def multiplicar(lista):
    r = 1
    for x in range (len(lista)):
        r = r * lista[x]
    return r
numeros = [2,3,5,2]
print(multiplicar(numeros))

def factorial(numero):
    arreglo = [] 
    for i in range(1,numero+1):
        arreglo.append(i)
    resultado = multiplicar(arreglo)
    return resultado
print(factorial(8))
