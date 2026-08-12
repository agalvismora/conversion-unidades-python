def convertir_unidades():
    while True:
        print("\n======================================")
        print("       CONVERSOR DE UNIDADES")
        print("======================================")
        print("1. Longitud")
        print("2. Masa")
        print("3. Tiempo")
        print("4. Salir")
        print("======================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            convertir_longitud()

        elif opcion == "2":
            convertir_masa()

        elif opcion == "3":
            convertir_tiempo()

        elif opcion == "4":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nERROR: Debe seleccionar una opción del 1 al 4.")


def convertir_longitud():
    print("\n======================================")
    print("       CONVERSIÓN DE LONGITUD")
    print("======================================")
    print("Escala:")
    print("km -> hm -> dam -> m -> dm -> cm -> mm")
    print("--------------------------------------")
    print("1. Kilómetros (km)")
    print("2. Hectómetros (hm)")
    print("3. Decámetros (dam)")
    print("4. Metros (m)")
    print("5. Decímetros (dm)")
    print("6. Centímetros (cm)")
    print("7. Milímetros (mm)")
    print("--------------------------------------")

    unidades = ["km", "hm", "dam", "m", "dm", "cm", "mm"]

    factores = {
        "km": 1000,
        "hm": 100,
        "dam": 10,
        "m": 1,
        "dm": 0.1,
        "cm": 0.01,
        "mm": 0.001
    }

    try:
        origen = int(input("Unidad de origen (1-7): "))
        destino = int(input("Unidad de destino (1-7): "))

        if origen < 1 or origen > 7 or destino < 1 or destino > 7:
            print("\nERROR: Seleccione un número entre 1 y 7.")
            return

        cantidad = float(input("Ingrese la cantidad: "))

        unidad_origen = unidades[origen - 1]
        unidad_destino = unidades[destino - 1]

        resultado = cantidad * factores[unidad_origen] / factores[unidad_destino]

        print("\n--------------------------------------")
        print("RESULTADO")
        print("--------------------------------------")
        print(f"{cantidad} {unidad_origen} = {resultado} {unidad_destino}")
        print("--------------------------------------")

    except ValueError:
        print("\nERROR: Debe ingresar números válidos.")


def convertir_masa():
    print("\n======================================")
    print("          CONVERSIÓN DE MASA")
    print("======================================")
    print("Escala:")
    print("kg -> hg -> dag -> g -> dg -> cg -> mg")
    print("--------------------------------------")
    print("1. Kilogramos (kg)")
    print("2. Hectogramos (hg)")
    print("3. Decagramos (dag)")
    print("4. Gramos (g)")
    print("5. Decigramos (dg)")
    print("6. Centigramos (cg)")
    print("7. Miligramos (mg)")
    print("--------------------------------------")

    unidades = ["kg", "hg", "dag", "g", "dg", "cg", "mg"]

    factores = {
        "kg": 1000,
        "hg": 100,
        "dag": 10,
        "g": 1,
        "dg": 0.1,
        "cg": 0.01,
        "mg": 0.001
    }

    try:
        origen = int(input("Unidad de origen (1-7): "))
        destino = int(input("Unidad de destino (1-7): "))

        if origen < 1 or origen > 7 or destino < 1 or destino > 7:
            print("\nERROR: Seleccione un número entre 1 y 7.")
            return

        cantidad = float(input("Ingrese la cantidad: "))

        unidad_origen = unidades[origen - 1]
        unidad_destino = unidades[destino - 1]

        resultado = cantidad * factores[unidad_origen] / factores[unidad_destino]

        print("\n--------------------------------------")
        print("RESULTADO")
        print("--------------------------------------")
        print(f"{cantidad} {unidad_origen} = {resultado} {unidad_destino}")
        print("--------------------------------------")

    except ValueError:
        print("\nERROR: Debe ingresar números válidos.")


def convertir_tiempo():
    print("\n======================================")
    print("         CONVERSIÓN DE TIEMPO")
    print("======================================")
    print("Escala:")
    print("días -> horas -> minutos -> segundos")
    print("--------------------------------------")
    print("1. Días")
    print("2. Horas")
    print("3. Minutos")
    print("4. Segundos")
    print("--------------------------------------")

    unidades = ["días", "horas", "minutos", "segundos"]

    factores = {
        "días": 86400,
        "horas": 3600,
        "minutos": 60,
        "segundos": 1
    }

    try:
        origen = int(input("Unidad de origen (1-4): "))
        destino = int(input("Unidad de destino (1-4): "))

        if origen < 1 or origen > 4 or destino < 1 or destino > 4:
            print("\nERROR: Seleccione un número entre 1 y 4.")
            return

        cantidad = float(input("Ingrese la cantidad: "))

        unidad_origen = unidades[origen - 1]
        unidad_destino = unidades[destino - 1]

        resultado = cantidad * factores[unidad_origen] / factores[unidad_destino]

        print("\n--------------------------------------")
        print("RESULTADO")
        print("--------------------------------------")
        print(f"{cantidad} {unidad_origen} = {resultado} {unidad_destino}")
        print("--------------------------------------")

    except ValueError:
        print("\nERROR: Debe ingresar números válidos.")


# INICIAR PROGRAMA
convertir_unidades()
