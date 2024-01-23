### Funcion para generar números primos del 1 al 250

def es_primo(numeros):
    if numeros < 2:
        return False
    for i in range(2, int(numeros**0.5) + 1):
        if numeros % i == 0:
            return False
    return True
    
### Variables para tomar como inicio y fin     

inicio = 1
final = 250

### Imprimir etiqueta de que rango se esta tomando para obtner numeros primos 
print(f"Números primos entre {inicio} y {final}:\n")

for numeros in range(inicio, final + 1):
    if es_primo(numeros):
        print(numeros)
