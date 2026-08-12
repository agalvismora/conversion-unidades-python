print("\nUnidades disponibles:")
print("1. Kilómetros (km)")
print("2. Hectómetros (hm)")
print("3. Decámetros (dam)")
print("4. Metros (m)")
print("5. Decímetros (dm)")
print("6. Centímetros (cm)")
print("7. Milímetros (mm)")

unidades = ["km", "hm", "dam", "m", "dm", "cm", "mm"]

try:
    origen = int(input("Seleccione la unidad de origen (1-7): ")) - 1
    destino = int(input("Seleccione la unidad de destino (1-7): ")) - 1
    valor = float(input("Ingrese el valor a convertir: "))

    factores = {
        "km": 1000,
        "hm": 100,
        "dam": 10,
        "m": 1,
        "dm": 0.1,
        "cm": 0.01,
        "mm": 0.001
    }

    resultado = valor * factores[unidades[origen]] / factores[unidades[destino]]

    print(f"\n{valor} {unidades[origen]} = {resultado} {unidades[destino]}")

except (ValueError, IndexError):
    print("Error: seleccione opciones válidas.")




print("\nUnidades disponibles:")
print("1. Kilogramos (kg)")
print("2. Hectogramos (hg)")
print("3. Decagramos (dag)")
print("4. Gramos (g)")
print("5. Decigramos (dg)")
print("6. Centigramos (cg)")
print("7. Miligramos (mg)")

unidades = ["kg", "hg", "dag", "g", "dg", "cg", "mg"]

try:
    origen = int(input("Seleccione la unidad de origen (1-7): ")) - 1
    destino = int(input("Seleccione la unidad de destino (1-7): ")) - 1
    valor = float(input("Ingrese el valor a convertir: "))

    factores = {
        "kg": 1000,
        "hg": 100,
        "dag": 10,
        "g": 1,
        "dg": 0.1,
        "cg": 0.01,
        "mg": 0.001
    }

    resultado = valor * factores[unidades[origen]] / factores[unidades[destino]]

    print(f"\n{valor} {unidades[origen]} = {resultado} {unidades[destino]}")

except (ValueError, IndexError):
    print("Error: seleccione opciones válidas.")




print("\nUnidades disponibles:")
print("1. Días")
print("2. Horas")
print("3. Minutos")
print("4. Segundos")

unidades = ["días", "horas", "minutos", "segundos"]

try:
    origen = int(input("Seleccione la unidad de origen (1-4): ")) - 1
    destino = int(input("Seleccione la unidad de destino (1-4): ")) - 1
    valor = float(input("Ingrese el valor a convertir: "))

    factores = {
        "días": 86400,
        "horas": 3600,
        "minutos": 60,
        "segundos": 1
    }

    resultado = valor * factores[unidades[origen]] / factores[unidades[destino]]

    print(f"\n{valor} {unidades[origen]} = {resultado} {unidades[destino]}")

except (ValueError, IndexError):
    print("Error: seleccione opciones válidas.")



try:
    opcion = int(input("\nSeleccione una opción: "))

    if opcion == 1:
        conversion_longitud()
    elif opcion == 2:
        conversion_masa()
    elif opcion == 3:
        conversion_tiempo()
    elif opcion == 4:
        print("\nPrograma finalizado. ¡Gracias!")
        break
    else:
        print("Opción no válida.")

except ValueError:
    print("Error: debe ingresar un número.")
