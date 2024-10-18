def seleccionar_proceso():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora')
        print('3: Finalizar')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_comentario()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                finalizar_proceso()
                break
            else:
                print('Por favor, introduzca un número del 1 al 3')
        else:
            print('Por favor, introduzca un número del 1 al 3')

def ingresar_puntuacion_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        punto = input()
        
        if punto.isdecimal():
            punto = int(punto)
            if punto < 1 or punto > 5:
                print('Por favor, introduzca un valor entre el 1 y 5')
            else:
                print('Por favor, introduzca un comentario')
                comentario = input()
                guardar_en_archivo(punto, comentario)
                break
        else:
            print('Por favor, introduzca la puntuación en números')

def comprobar_resultados():
    try:
        with open("data.txt", "r") as archivo:
            contenido = archivo.read()
            if contenido:
                print("Resultados hasta la fecha:")
                print(contenido)
            else:
                print("No hay datos registrados hasta el momento.")
    except FileNotFoundError:
        print("No se encontraron resultados. Aún no se ha registrado ningún dato.")

def finalizar_proceso():
    print('Finalizando el proceso. ¡Hasta pronto!')

def guardar_en_archivo(punto, comentario):
    with open("data.txt", 'a') as archivo:
        archivo.write(f'Punto: {punto}, Comentario: {comentario} \n')

# Ejecutar el programa
seleccionar_proceso()
