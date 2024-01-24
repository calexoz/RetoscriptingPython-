### Funcion para generar números primos del 1 al 250

###def es_primo(numeros):
###    if numeros < 2:
###        return False
###    for i in range(2, int(numeros**0.5) + 1):
###        if numeros % i == 0:
###            return False
###    return True
    
### Variables para tomar como inicio y fin     

### inicio = 1
### final = 250

### Imprimir etiqueta de que rango se esta tomando para obtner numeros primos 
### print(f"Números primos entre {inicio} y {final}:\n")

### for numeros in range(inicio, final + 1):
###    if es_primo(numeros):
###        print(numeros)
################################################################################ Se reformula scipt para la obtencion de numeros primos y almacenarlos en un txt

### Función para determinar si un número es primos

def es_primo(num): 
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

### Se declara varibales para tomar un rango y etiquetas en impresion en pantalla
Inicio = 1
Fin = 250

### Se declara varibales para tomar bucle while
Actual = Inicio
primos = []

### Bucle while para encontrar números primos en el rango
while Actual <= Fin:
    # Si el número actual es primo, lo anexa a la lista del archivo Resultados.txt
    if es_primo(Actual):
        primos.append(Actual)
    Actual += 1  # El número actual se incrementa para la próxima interación

### El resultado se va generar en el siguiente archivo 
filename = f"Resultado.txt"

### Contiene la variable With que nos indica que abrira y cerrar el archivo una vez terminado el proceso 
with open(filename, "w") as file:
    for primo in primos:
        file.write(f"{primo}\n")
        

### Se imprime en pantalla en nombre del archivo 
print(f"Se genera archivo de números primos entre el {Inicio} y {Fin} en {filename}.\n\n")


import subprocess

subprocess.run(["ls","-l","Resultado.txt"])






