# ============================================================
# Archivo: ejercicio2_verificacion_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Estudiante: Glenn Perez Rodriguez
# Fecha: 04/10/2026
# Versión: 1.1
# Descripción: Verificación de niveles de combustible.
# ============================================================

# Constante para el combustible de reserva
FUEL_RESERVE = 10

# Datos de entrada
fuel_available = int(
    input("Ingrese la cantidad de combustible disponible: ")
)
fuel_departure = int(
    input("Ingrese la cantidad de combustible para el viaje de ida: ")
)
fuel_return = int(
    input("Ingrese la cantidad de combustible para el viaje de regreso: ")
)

# Cálculos para combustible
total_fuel = (
    fuel_departure
    + fuel_return
    + FUEL_RESERVE
)
fuel_margin = (
    fuel_available
    - total_fuel
    + FUEL_RESERVE
)

# Datos de salida
print(
    "Cantidad de combustible disponible:",
    fuel_available,
)
print(
    "Cantidad de combustible para el viaje de ida:",
    fuel_departure,
)
print(
    "Cantidad de combustible para el viaje de regreso:",
    fuel_return,
)
print(
    "Cantidad de combustible de reserva:",
    FUEL_RESERVE,
)
print(
    "Cantidad total de combustible necesaria:",
    total_fuel,
)
print(
    "Margen de combustible disponible:",
    fuel_margin,
)

# Condicional de advertencia de margen bajo de combustible
if fuel_margin < FUEL_RESERVE:
    print(
        "Advertencia: el margen adicional de combustible es bajo."
    )
