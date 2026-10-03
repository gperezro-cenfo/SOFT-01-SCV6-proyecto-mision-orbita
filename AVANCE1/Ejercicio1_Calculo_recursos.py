# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Estudiante: Glenn Perez Rodríguez
# Fecha: 03/10/2026
# Versión: 1.0
# Descripción: Cálculo de recursos necesarios para una misión.
# ============================================================

# Constantes que representan los recursos necesarios para la misión.
# PROVISIONS_DAILY permite ajustar el consumo diario de provisiones
# por tripulante si cambian los requerimientos de la misión.

TRIP_LEGS = 2
FUEL_DAILY = 8
FUEL_RESERVE = 10
OXYGEN_DAILY = 2
OXYGEN_EMERGENCY = 5
ENERGY_DAILY = 5
ENERGY_OPERATIONS = 10
PROVISIONS_DAILY = 1
PROVISIONS_EXTRA = 3

# Datos de entrada
mission_name = input(
    "Ingrese el nombre de la misión: "
)
crew_count = int(
    input("Ingrese el número de tripulantes: ")
)
travel_days = int(
    input("Ingrese la cantidad de días para llegar al destino: ")
)

# Cálculos para combustible
fuel_departure = (
    travel_days
    * FUEL_DAILY
)
fuel_return = (
    travel_days
    * FUEL_DAILY
)
total_fuel = (
    fuel_departure
    + fuel_return
    + FUEL_RESERVE
)

# Cálculos para oxígeno
total_oxygen = (
    travel_days
    * TRIP_LEGS
    * OXYGEN_DAILY
    * crew_count
    + OXYGEN_EMERGENCY
)

# Cálculos para energía
total_energy = (
    travel_days
    * TRIP_LEGS
    * ENERGY_DAILY
    + ENERGY_OPERATIONS
)

# Cálculos para provisiones
total_provisions = (
    travel_days
    * TRIP_LEGS
    * PROVISIONS_DAILY
    * crew_count
    + PROVISIONS_EXTRA
)

# Datos de salida
print(
    "Nombre de la misión:",
    mission_name,
)
print(
    "Número de tripulantes:",
    crew_count,
)
print(
    "Duración estimada al destino:",
    travel_days,
)
print(
    "Combustible requerido para llegar al destino:",
    fuel_departure,
    "unidades",
)
print(
    "Combustible requerido para regresar:",
    fuel_return,
    "unidades",
)
print(
    "Combustible de reserva:",
    FUEL_RESERVE,
    "unidades",
)
print(
    "Combustible total requerido para la misión:",
    total_fuel,
    "unidades",
)
print(
    "Oxígeno requerido para la misión:",
    total_oxygen,
    "unidades",
)
print(
    "Energía requerida para la misión:",
    total_energy,
    "unidades",
)
print(
    "Provisiones requeridas para la misión:",
    total_provisions,
    "unidades",
)