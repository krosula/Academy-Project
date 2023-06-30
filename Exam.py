# Nombre: Martín Franco
# DNI: 42887241

def agregar_vuelo(vuelos):
    numero_vuelo = input("Ingrese el numero de vuelo: ")
    destino = input("Ingrese el destino del vuelo: ")
    hora_salida = input("Ingrese la hora de salida del vuelo: ")
    vuelo = {"numero_vuelo": numero_vuelo, "destino": destino, "hora_salida": hora_salida}
    vuelos[numero_vuelo] = vuelo
    print("Vuelo agregado")

def actualizar_hora_salida(vuelos):
    numero_vuelo = input("Ingrese el numero de vuelo para actualizar la hora de salida: ")
    if numero_vuelo in vuelos:
        nueva_hora_salida = input("Ingrese la nueva hora de salida: ")
        vuelos[numero_vuelo]["hora_salida"] = nueva_hora_salida
        print("Hora de salida actualizada")
    else:
        print("El numero de vuelo no existe.")

def ver_vuelos(vuelos):
    print("Detalles de los vuelos actuales:")
    for vuelo in vuelos.values():
        numero_vuelo = vuelo["numero_vuelo"]
        destino = vuelo["destino"]
        hora_salida = vuelo["hora_salida"]
        print("Número de vuelo:", numero_vuelo)
        print("Destino:", destino)
        print("Hora de salida:", hora_salida)
        print()

# Código principal
vuelos = {}

# Agregar vuelos
agregar_vuelo(vuelos)
agregar_vuelo(vuelos)
agregar_vuelo(vuelos)

# Actualizar hora de salida
actualizar_hora_salida(vuelos)

# Ver vuelos
ver_vuelos(vuelos)

# from list import sort
# "TO DO: implementar una funcion que ordene la lista de vuelos por horario de salida"

