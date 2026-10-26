# ============================================================
# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Estudiante: Glenn Perez Rodríguez
# Fecha: 25/10/2026
# Versión: 1.1
# Descripción: Actividades de exploración en destino.
# ============================================================

# Opciones disponibles en el menú
OPTION_ANALYZE = 1
OPTION_COLLECT = 2
OPTION_OBSERVE = 3
OPTION_FINISH = 4

# Recursos y puntos de la actividad Analizar terreno
ANALYZE_ENERGY = 8
ANALYZE_PROVISIONS = 0
ANALYZE_POINTS = 10

# Recursos y puntos de la actividad Recolectar muestra
COLLECT_ENERGY = 12
COLLECT_PROVISIONS = 2
COLLECT_POINTS = 20

# Recursos y puntos de la actividad Realizar observación
OBSERVE_ENERGY = 5
OBSERVE_PROVISIONS = 0
OBSERVE_POINTS = 8

# Datos de entrada
energy_available = int(
    input("Ingrese la energía disponible al llegar al destino: ")
)
provisions_available = int(
    input("Ingrese las provisiones disponibles al llegar al destino: ")
)

# Inicialización de contadores, acumuladores y variable de control
science_points = 0
activities_completed = 0
samples_collected = 0
exploration_active = True

# Menú de actividades de exploración
while exploration_active:
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")

    activity_option = int(
        input("Seleccione una actividad: ")
    )
    activity_selected = False

    if activity_option == OPTION_ANALYZE:
        activity_name = "Analizar terreno"
        activity_energy_cost = ANALYZE_ENERGY
        activity_provisions_cost = ANALYZE_PROVISIONS
        activity_points = ANALYZE_POINTS
        activity_selected = True
    elif activity_option == OPTION_COLLECT:
        activity_name = "Recolectar muestra"
        activity_energy_cost = COLLECT_ENERGY
        activity_provisions_cost = COLLECT_PROVISIONS
        activity_points = COLLECT_POINTS
        activity_selected = True
    elif activity_option == OPTION_OBSERVE:
        activity_name = "Realizar observación"
        activity_energy_cost = OBSERVE_ENERGY
        activity_provisions_cost = OBSERVE_PROVISIONS
        activity_points = OBSERVE_POINTS
        activity_selected = True
    elif activity_option == OPTION_FINISH:
        print("Exploración finalizada por la tripulación.")
        exploration_active = False
    else:
        print("Opción no válida.")

    if activity_selected:
        if (
            energy_available >= activity_energy_cost
            and provisions_available >= activity_provisions_cost
        ):
            energy_available = (
                energy_available
                - activity_energy_cost
            )
            provisions_available = (
                provisions_available
                - activity_provisions_cost
            )
            activities_completed = activities_completed + 1
            science_points = science_points + activity_points

            if activity_option == OPTION_COLLECT:
                samples_collected = samples_collected + 1

            print(
                "Actividad realizada:",
                activity_name + ".",
                "Puntos obtenidos:",
                activity_points,
            )
        else:
            print(
                "Recursos insuficientes para realizar la actividad. "
                "La exploración finaliza."
            )
            exploration_active = False

# Resumen final
print("Actividades realizadas:", activities_completed)
print("Muestras recolectadas:", samples_collected)
print("Puntos científicos:", science_points)
print("Energía restante:", energy_available, "unidades")
print(
    "Provisiones restantes:",
    provisions_available,
    "unidades",
)
