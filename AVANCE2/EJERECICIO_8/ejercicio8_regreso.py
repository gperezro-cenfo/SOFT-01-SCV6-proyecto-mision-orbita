# ============================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Estudiante: Glenn Perez Rodríguez
# Fecha: 25/10/2026
# Versión: 1.1
# Descripción: Evaluación de retorno de la tripulación
# ============================================================

# Consumo diario de recursos
FUEL_DAILY = 8
OXYGEN_DAILY = 2
ENERGY_DAILY = 5
PROVISIONS_DAILY = 1

# Datos de entrada
crew_count = int(
    input("Ingrese la cantidad de tripulantes: ")
)
travel_days = int(
    input("Ingrese la cantidad de días del viaje de ida: ")
)
fuel_available = int(
    input("Ingrese la cantidad de combustible disponible: ")
)
oxygen_available = int(
    input("Ingrese la cantidad de oxígeno disponible: ")
)
energy_available = int(
    input("Ingrese la cantidad de energía disponible: ")
)
provisions_available = int(
    input("Ingrese la cantidad de provisiones disponibles: ")
)

# Recursos necesarios para evaluar el regreso
fuel_return_required = travel_days * FUEL_DAILY
oxygen_daily_required = crew_count * OXYGEN_DAILY
provisions_daily_required = crew_count * PROVISIONS_DAILY

# Caso A: la nave tiene combustible suficiente para iniciar el regreso
if fuel_available >= fuel_return_required:
    days_completed = 0
    return_active = True

    while days_completed < travel_days and return_active:
        if (
            fuel_available >= FUEL_DAILY
            and oxygen_available >= oxygen_daily_required
            and energy_available >= ENERGY_DAILY
            and provisions_available >= provisions_daily_required
        ):
            fuel_available = fuel_available - FUEL_DAILY
            oxygen_available = (
                oxygen_available
                - oxygen_daily_required
            )
            energy_available = energy_available - ENERGY_DAILY
            provisions_available = (
                provisions_available
                - provisions_daily_required
            )
            days_completed = days_completed + 1

            print(
                "Día",
                days_completed,
                "| Combustible:",
                fuel_available,
                "| Oxígeno:",
                oxygen_available,
                "| Energía:",
                energy_available,
                "| Provisiones:",
                provisions_available,
            )
        else:
            return_active = False

    if days_completed == travel_days:
        print(
            "La tripulación regresó exitosamente a la Tierra."
        )
        print(
            "Combustible restante:",
            fuel_available,
            "unidades",
        )
        print(
            "Oxígeno restante:",
            oxygen_available,
            "unidades",
        )
        print(
            "Energía restante:",
            energy_available,
            "unidades",
        )
        print(
            "Provisiones restantes:",
            provisions_available,
            "unidades",
        )
    else:
        print(
            "El regreso se interrumpió en el día "
            + str(days_completed + 1)
            + "."
        )

        insufficient_resources = ""

        if oxygen_available < oxygen_daily_required:
            insufficient_resources = "oxígeno"

        if energy_available < ENERGY_DAILY:
            if insufficient_resources != "":
                insufficient_resources = (
                    insufficient_resources
                    + ", "
                )
            insufficient_resources = (
                insufficient_resources
                + "energía"
            )

        if provisions_available < provisions_daily_required:
            if insufficient_resources != "":
                insufficient_resources = (
                    insufficient_resources
                    + ", "
                )
            insufficient_resources = (
                insufficient_resources
                + "provisiones"
            )

        print(
            "Recurso insuficiente:",
            insufficient_resources,
        )
        print("La tripulación no completó el regreso.")

# Caso B: la nave no tiene combustible suficiente para regresar
else:
    print("La tripulación quedó varada en el destino.")

    oxygen_days = (
        oxygen_available
        // oxygen_daily_required
    )
    energy_days = energy_available // ENERGY_DAILY
    provisions_days = (
        provisions_available
        // provisions_daily_required
    )

    # Determinación de la supervivencia mediante comparaciones
    survival_days = oxygen_days

    if energy_days < survival_days:
        survival_days = energy_days

    if provisions_days < survival_days:
        survival_days = provisions_days

    # Identificación de todos los recursos limitantes
    limiting_resources = ""

    if oxygen_days == survival_days:
        limiting_resources = "oxígeno"

    if energy_days == survival_days:
        if limiting_resources != "":
            limiting_resources = limiting_resources + ", "
        limiting_resources = limiting_resources + "energía"

    if provisions_days == survival_days:
        if limiting_resources != "":
            limiting_resources = limiting_resources + ", "
        limiting_resources = limiting_resources + "provisiones"

    print("Días por oxígeno:", oxygen_days)
    print("Días por energía:", energy_days)
    print("Días por provisiones:", provisions_days)
    print("Supervivencia estimada:", survival_days, "días")
    print("Recurso(s) limitante(s):", limiting_resources)
