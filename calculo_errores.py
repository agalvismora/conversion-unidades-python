import math


def calcular_promedio(datos):
    """Calcula el promedio aritmético."""
    return sum(datos) / len(datos)


def calcular_desviacion_estandar(datos):
    """
    Calcula la desviación estándar muestral.
    Si solo existe un dato, devuelve 0.
    """
    if len(datos) < 2:
        return 0.0

    promedio = calcular_promedio(datos)
    suma = sum((x - promedio) ** 2 for x in datos)

    return math.sqrt(suma / (len(datos) - 1))


def calcular_error_relativo(valor_medido, valor_referencia):
    """
    Error relativo:
    |valor medido - valor de referencia| / |valor de referencia|
    """
    if valor_referencia == 0:
        return None

    return abs(valor_medido - valor_referencia) / abs(valor_referencia)


def calcular_error_porcentual(error_relativo):
    """Convierte el error relativo a porcentaje."""
    if error_relativo is None:
        return None

    return error_relativo * 100


def mostrar_resultados(datos, unidad, valor_referencia):
    """Calcula y muestra todos los resultados."""

    promedio = calcular_promedio(datos)
    desviacion = calcular_desviacion_estandar(datos)
    error_relativo = calcular_error_relativo(promedio, valor_referencia)
    error_porcentual = calcular_error_porcentual(error_relativo)

    print("\n" + "=" * 50)
    print("           RESULTADOS DEL CÁLCULO")
    print("=" * 50)

    print(f"Número de datos:          {len(datos)}")
    print(f"Unidad:                   {unidad}")
    print(f"Valor de referencia:      {valor_referencia:.6f} {unidad}")
    print(f"Valor promedio:           {promedio:.6f} {unidad}")
    print(f"Desviación estándar:      {desviacion:.6f} {unidad}")

    if error_relativo is None:
        print("Error relativo:           No definido")
        print("Error porcentual:         No definido")
        print("\nEl valor de referencia no puede ser cero.")
    else:
        print(f"Error relativo:           {error_relativo:.6f}")
        print(f"Error porcentual:         {error_porcentual:.4f}%")

    print("=" * 50)


def ingresar_datos():
    """Solicita al usuario una cantidad variable de datos."""

    datos = []

    print("\nIngrese los datos de la medición.")
    print("Escriba 'fin' cuando haya terminado.")

    while True:
        entrada = input(f"Dato {len(datos) + 1}: ").strip()

        if entrada.lower() == "fin":
            break

        try:
            dato = float(entrada)
            datos.append(dato)
        except ValueError:
            print("Entrada no válida. Introduzca un número.")

    return datos


def main():
    print("=" * 50)
    print("       PROGRAMA DE CÁLCULO DE ERRORES")
    print("=" * 50)

    # Solicitar unidad
    unidad = input("Ingrese la unidad de los datos (m, kg, s, °C, etc.): ").strip()

    if not unidad:
        unidad = "unidades"

    # Ingresar datos
    datos = ingresar_datos()

    # Validar que existan datos
    if len(datos) == 0:
        print("\nNo se ingresaron datos.")
        return

    # Solicitar valor de referencia
    while True:
        try:
            valor_referencia = float(
                input(f"\nIngrese el valor de referencia ({unidad}): ")
            )
            break
        except ValueError:
            print("Entrada no válida. Introduzca un número.")

    # Mostrar resultados
    mostrar_resultados(datos, unidad, valor_referencia)


if __name__ == "__main__":
    main()

