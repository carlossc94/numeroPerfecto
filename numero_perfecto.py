def es_primo(numero):
    contador = 0
    for i in range(1,numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def es_perfecto(numero):
    numero_auxiliar = 0
    contador = 2
    numeros_perfectos=[]
    
    while numero_auxiliar < numero:
        formula_prima = int(((2**contador)-1))
        if es_primo(formula_prima):
            formula_perfecta = (2**(contador-1))
            formula_perfecta = formula_prima*formula_perfecta
            numero_auxiliar = formula_perfecta
            if(formula_perfecta < numero):
                numeros_perfectos.append(formula_perfecta)
        contador += 1
    return numeros_perfectos
        


def run():
    numero = int(input('Escribe un numero: '))
    numeros_perfectos = es_perfecto(numero)
    print("La lista de numeros perfectos menores a "+str(numero)+" son:")
    for numero_perfecto in numeros_perfectos:
        print(numero_perfecto)

if __name__=='__main__':
    run()