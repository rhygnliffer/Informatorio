from random import randint

palabras = ["messi", "casa", "auto", "maradona", "river", "bicicleta"]
frases_error = ["Mmmm, no.", "No, bro, no.","Esa no era.", "Letra incorrecta.", "No eres muy listo."]
imagenes = []
indice_aleatorio = 0
almacenamiento_palabra = ""
numero_intentos = 5
letra_ingresada = ""
palabra_elegida = []
palabra_actual = []
palabra_secreta = ""
letras = []

def maxi(lista):
    indice_max = len(lista) - 1
    return indice_max

def elegir_indice_aleatorio(lista):
    indice_elegido = randint(0, maxi(lista))
    return indice_elegido


def elegir_frase():
    return frases_error[elegir_indice_aleatorio(frases_error)]


def comprobar(letra_comprobar, lista):
    valores_index = []
    for index, letra in enumerate(lista):
        if letra == letra_comprobar:
            valores_index.append(index)
    return valores_index


def reemplazar(lista_index, letra):
    for elemento in lista_index:
        palabra_elegida[elemento] = letra + " "

def hay_guiones(lista):
    return lista.count("_ ")


#esta parte es para dar los guiones respecto a la palabra
almacenamiento_palabra = palabras[elegir_indice_aleatorio(palabras)]
for letra in almacenamiento_palabra:
    palabra_elegida.append(letra)
    letras.append(letra)
palabra_elegida  = ["_ " for elemento in palabra_elegida]
palabra_secreta = "".join(palabra_elegida)
print (palabra_secreta)

while numero_intentos > 0 and hay_guiones(palabra_elegida):
    letra_ingresada = input("Ingresa una letra: ")
    if letra_ingresada in letras:
        lista_valores = comprobar(letra_ingresada, letras)
        reemplazar(lista_valores, letra_ingresada)
        palabra_secreta = "".join(palabra_elegida) 
        print (palabra_secreta)
    else:
        numero_intentos -= 1
        print(elegir_frase())
        print(imagenes) 
        print(palabra_secreta)


print("salí del bucle")