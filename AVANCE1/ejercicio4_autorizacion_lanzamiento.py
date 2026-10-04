# ============================================================
# Archivo: ejercicio4_autorizacion_lanzamiento.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Estudiante: Glenn Perez Rodriguez
# Fecha: 04/10/2026 
# Versión: 1.3
# Descripción: Verifica si se puede autorizar el lanzamiento de una misión.
# ============================================================

# Constante de reserva de combustible
FUEL_RESERVE = 10

# Datos de entrada
fuel_available = int(
    input("Ingrese la cantidad de combustible disponible: ")
)
fuel_departure = int(
    input("Ingrese la cantidad de combustible requerido hacia el destino: ")
)
fuel_return = int(
    input("Ingrese la cantidad de combustible requerido para el regreso: ")
)
oxygen_available = int(
    input("Ingrese la cantidad de oxígeno disponible: ")
)
oxygen_required = int(
    input("Ingrese la cantidad de oxígeno requerido: ")
)
energy_available = int(
    input("Ingrese la cantidad de energía disponible: ")
)
energy_required = int(
    input("Ingrese la cantidad de energía requerida: ")
)
provisions_available = int(
    input("Ingrese la cantidad de provisiones disponibles: ")
)
provisions_required = int(
    input("Ingrese la cantidad de provisiones requeridas: ")
)

# Cálculos requeridos para el lanzamiento
fuel_required = (
    fuel_departure
    + fuel_return
    + FUEL_RESERVE
)

# Condicional de verificación de lanzamiento
if (
    fuel_available >= fuel_required
    and oxygen_available >= oxygen_required
    and energy_available >= energy_required
    and provisions_available >= provisions_required
):
    print("Lanzamiento autorizado.")
else:
    print(
        "Lanzamiento no autorizado. La misión debe ser revisada."
    )