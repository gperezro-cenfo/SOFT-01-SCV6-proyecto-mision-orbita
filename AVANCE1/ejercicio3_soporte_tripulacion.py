# ============================================================
# Archivo: ejercicio3_Soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Estudiante: Glenn Perez Rodriguez
# Fecha: 04/10/2026
# Versión: 1.3
# Descripción: Verificación de recursos necesarios para la tripulación.
# ============================================================

# Datos de entrada
oxygen_available = int(
    input("Ingrese la cantidad de oxígeno disponible: ")
)
oxygen_required = int(
    input("Ingrese la cantidad de oxígeno requerida: ")
)
provisions_available = int(
    input("Ingrese la cantidad de provisiones disponibles: ")
)
provisions_required = int(
    input("Ingrese la cantidad de provisiones requeridas: ")
)

# Condicional para verificar si los recursos son suficientes
if (
    oxygen_available >= oxygen_required
    and provisions_available >= provisions_required
):
    print(
        "La nave posee recursos suficientes para la tripulación."
    )
else:
    print(
        "La nave no posee recursos suficientes para la tripulación."
    )
