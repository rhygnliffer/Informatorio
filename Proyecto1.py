from random import randint

#Aca están todas las variables que usa el programa. La mayoría son almacenamientos vacios.

palabras = ["chocolate", "desoxirribonucleico", "variable", "langosta", "portal", "bicicleta"]
frases_error = ["Mmmm, no.", "No, bro, no.","Esa no era.", "Letra incorrecta.", "No eres muy listo."]
frases_perdida = [
    "Bueno, lo intentaste", "Deberías estar avergonzado",
    "La proxima capaz te va mejor", "Que lástima",
    "No te preocupes, era bastante difícil",
    "No importa, el premio tampoco es la gran cosa"
    ]
imagenes = [
    "   _______\n   |     |\n   |     \n   |    \n   |      \\",
    "   _______\n   |     |\n   |     \n   |    \n   |    / \\",
    "   _______\n   |     |\n   |     \n   |     |\n   |    / \\",
    "   _______\n   |     |\n   |     \n   |     |\\\n   |    / \\",
    "   _______\n   |     |\n   |     \n   |    /|\\\n   |    / \\",
    "   _______\n   |     |\n   |     O\n   |    /|\\\n   |    / \\"
    ]
indice_imagenes = 0
indice_aleatorio = 0
almacenamiento_palabra = ""
numero_intentos = 6
letra_ingresada = ""
palabra_elegida = []
palabra_secreta = ""
letras = []

#Le siguen todas las definiciones que hice para el juego

def maxi(lista):
    indice_max = len(lista) - 1
    return indice_max

def elegir_indice_aleatorio(lista):
    indice_elegido = randint(0, maxi(lista))
    return indice_elegido

def ocultar_palabra():
    global palabra_elegida
    global palabra_secreta
    for letra in almacenamiento_palabra:
        palabra_elegida.append(letra)
        letras.append(letra)
    palabra_elegida  = ["_ " for elemento in palabra_elegida]
    palabra_secreta = "".join(palabra_elegida)

def elegir_palabra_aleatoria():
    global almacenamiento_palabra
    almacenamiento_palabra = palabras[elegir_indice_aleatorio(palabras)]
    ocultar_palabra()

def bucle_juego():
    global numero_intentos
    global palabra_secreta
    global imagenes
    while numero_intentos > 0 and hay_guiones(palabra_elegida):
        print(palabra_secreta)
        letra_ingresada = input("Ingresa una letra: ")
        if letra_ingresada in letras:
            lista_valores = comprobar(letra_ingresada, letras)
            reemplazar(lista_valores, letra_ingresada)
            palabra_secreta = "".join(palabra_elegida)
        else:
            numero_intentos -= 1
            print(elegir_frase())
            imprimir_imagen()
            
def elegir_frase():
    return frases_error[elegir_indice_aleatorio(frases_error)]

def imprimir_imagen():
    global indice_imagenes    
    print(imagenes[indice_imagenes])
    indice_imagenes += 1

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


# Este es el cuerpo del programa

print("Hola, querés jugar un juego? Hay un premio si ganás.")
respuesta = input("Escribe \"si\" si deseás participar: ")
if respuesta.lower() == "si":
    print("Querés elegir una palabra?")
    respuesta2 = input("Escribí cual, o \"no\" para elegir una aleatoria: ")
    if respuesta2 == "no":
        elegir_palabra_aleatoria()
        bucle_juego()
    else:
        almacenamiento_palabra = respuesta2
        ocultar_palabra()
        bucle_juego()

    if not hay_guiones(palabra_elegida):
        print("¡Felicidades!, adivinaste la palabra: " + almacenamiento_palabra)
        print("Te cuento algo muy curioso.")
        print("No hay premio.")
        print("Chau.")
    if numero_intentos == 0:
        print(frases_perdida[elegir_indice_aleatorio(frases_perdida)])
        print("La palabra era: " + almacenamiento_palabra)
else:
    print("Bueno, hasta luego.")

