while True:
    camino = []
    minas = []
    opcion = int(input("""
    1. Ingresar camino minado
    2. Detectar Minas
    3. Desactivar Minas
    4. Recorrer el camino
    5. Cerrar el programa
    Ingresar la opción que desea correr: 
    """))
    if opcion < 1 or opcion >= 5:
        print("Opción Inválida. Ingrese otra opción.")
    elif opcion == 1:
        longitud = int(input("Ingrese la longitud del camino: "))
        while len(camino) < longitud:
            baldosa = input("Ingrese el contenido de la siguiente baldosa: ")
            camino.append(baldosa)
    elif opcion == 2:
        posicion_camino = 0
        while posicion_camino < len(minas):
            baldosa_observada = camino[posicion_camino]
            if baldosa_observada == "M":
                minas.append(posicion_camino)
                print(f"Se detectó una mina en la posición {posicion_camino}")
            posicion_camino += 1
        if opcion == 3:
            numero_de_mina = 0
            while numero_de_mina < len(minas):
                camino[minas[numero_de_mina]] = "D"
                print(f"Se desactivó una mina en la posición {numero_de_mina}")
    elif opcion == 4:
        posicion_camino = 0
        minas_recuperadas = 0
        while posicion_camino <= len(camino):
            baldosa_observada = camino[posicion_camino]
            if baldosa_observada == "D":
                minas_recuperadas += 1
                print(f"Se recuperó la mina de la posición {posicion_camino}")
            if baldosa_observada == "M":
                print(f"¡BOOM! PISARON UNA MINA EN EL LUGAR {posicion_camino}!")
                break
                break
            posicion_camino += 1
        print(f"Se recorrió exitosamente el camino y se recuperaron {minas_recuperadas} minas")
    elif opcion == 5:
        break
