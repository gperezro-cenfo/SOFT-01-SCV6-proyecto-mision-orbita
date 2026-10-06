# Misión Órbita

Proyecto correspondiente al curso **SOFT-01 Principios de Programación I**, sección **SCV6**.

## Estudiante

- Glenn Perez Rodriguez

## Descripción del proyecto

Misión Órbita es un conjunto de programas desarrollados en Python para calcular y verificar los recursos necesarios para una misión espacial.

El proyecto está compuesto por cuatro ejercicios:

1. Cálculo de los recursos necesarios para una misión.
2. Verificación del margen de combustible.
3. Verificación del soporte para la tripulación.
4. Autorización inicial del lanzamiento.

Cada ejercicio funciona de manera independiente y solicita sus datos por medio de la terminal.


## Requisitos

Para ejecutar los programas se necesita:

- Python 3.
- Una terminal, símbolo del sistema o PowerShell.
- Opcionalmente, un entorno de desarrollo como Visual Studio Code.

Los programas utilizan únicamente funciones incluidas en Python, por lo que no es necesario instalar bibliotecas externas.

## Estructura del repositorio

```text
SOFT-01-SCV6-proyecto-mision-orbita/
├── README.md
├── AVANCEI/
│   ├── ejercicio1_calculo_recursos.py
│   ├── ejercicio2_verificacion_combustible.py
│   ├── ejercicio3_soporte_tripulacion.py
│   └── ejercicio4_autorizacion_lanzamiento.py
└── documentacion/
    └── avance_I_mision_orbita.pdf
```

## Cómo obtener el proyecto

### Opción 1: clonar el repositorio

Ejecutar el siguiente comando en una terminal:

```bash
git clone URL_DEL_REPOSITORIO
```

Luego, ingresar en la carpeta del proyecto:

```bash
cd mision-orbita
```

Se debe reemplazar `URL_DEL_REPOSITORIO` por la dirección del repositorio en GitHub.

### Opción 2: descargar el proyecto

1. Abrir el repositorio en GitHub.
2. Seleccionar el botón **Code**.
3. Seleccionar **Download ZIP**.
4. Extraer el archivo descargado.
5. Abrir una terminal en la carpeta extraída.

### Opción 3: GitHub Desktop

1. Instalar y abrir GitHub Desktop.
2. Iniciar sesión con la cuenta de GitHub.
3. En GitHub Desktop, seleccionar File → Clone repository.
4. Abrir la pestaña GitHub.com.
5. Seleccionar el repositorio.
6. En Local path, seleccionar la carpeta de la computadora donde se guardará el proyecto.
7. Presionar Clone.
8. Cuando finalice la descarga, seleccionar Repository → Show in Explorer para abrir la carpeta local del proyecto.

## Ejecución de los programas

Los siguientes comandos deben ejecutarse desde la carpeta principal del repositorio.

En Windows, si el comando `python` no está disponible, se puede sustituir por `py`.

---

## Ejercicio 1: Cálculo de recursos necesarios

### Descripción

Este programa calcula los recursos necesarios para completar una misión de ida y regreso.

Los recursos calculados son:

- Combustible para llegar al destino.
- Combustible para regresar.
- Reserva de combustible.
- Combustible total.
- Oxígeno.
- Energía.
- Provisiones.

### Ejecutar el programa

```bash
python avance1/ejercicio1_calculo_recursos.py
```

### Datos solicitados

El programa solicita los siguientes datos:

1. Nombre de la misión.
2. Número de tripulantes.
3. Cantidad de días necesarios para llegar al destino.

### Ejemplo de entrada

```text
Ingrese el nombre de la misión: Explorador I
Ingrese el número de tripulantes: 3
Ingrese la cantidad de días para llegar al destino: 5
```

### Resultado esperado

```text
Nombre de la misión: Explorador I
Número de tripulantes: 3
Duración estimada al destino: 5
Combustible requerido para llegar al destino: 40 unidades
Combustible requerido para regresar: 40 unidades
Combustible de reserva: 10 unidades
Combustible total requerido para la misión: 90 unidades
Oxígeno requerido para la misión: 65 unidades
Energía requerida para la misión: 60 unidades
Provisiones requeridas para la misión: 33 unidades
```

---

## Ejercicio 2: Verificación de combustible

### Descripción

Este programa calcula el combustible total requerido para una misión y determina el margen de combustible disponible.

Si el margen es menor que la reserva de 10 unidades, el programa muestra una advertencia.

### Ejecutar el programa

```bash
python avance1/ejercicio2_verificacion_combustible.py
```

### Datos solicitados

El programa solicita:

1. Cantidad de combustible disponible.
2. Cantidad de combustible requerida para el viaje de ida.
3. Cantidad de combustible requerida para el viaje de regreso.

### Ejemplo de entrada sin advertencia

```text
Ingrese la cantidad de combustible disponible: 100
Ingrese la cantidad de combustible para el viaje de ida: 40
Ingrese la cantidad de combustible para el viaje de regreso: 40
```

### Resultado esperado

```text
Cantidad de combustible disponible: 100
Cantidad de combustible para el viaje de ida: 40
Cantidad de combustible para el viaje de regreso: 40
Cantidad de combustible de reserva: 10
Cantidad total de combustible necesaria: 90
Margen de combustible disponible: 20
```

En este caso no se muestra la advertencia porque el margen de combustible es mayor que 10.

### Ejemplo de entrada con advertencia

```text
Ingrese la cantidad de combustible disponible: 85
Ingrese la cantidad de combustible para el viaje de ida: 40
Ingrese la cantidad de combustible para el viaje de regreso: 40
```

### Resultado esperado

```text
Cantidad de combustible disponible: 85
Cantidad de combustible para el viaje de ida: 40
Cantidad de combustible para el viaje de regreso: 40
Cantidad de combustible de reserva: 10
Cantidad total de combustible necesaria: 90
Margen de combustible disponible: 5
Advertencia: el margen adicional de combustible es bajo.
```

---

## Ejercicio 3: Verificación de recursos necesarios para la tripulación

### Descripción

Este programa verifica si la nave tiene suficiente oxígeno y provisiones para la tripulación.

El soporte se considera suficiente únicamente cuando se cumplen simultáneamente las siguientes condiciones:

- El oxígeno disponible es mayor o igual que el oxígeno requerido.
- Las provisiones disponibles son mayores o iguales que las provisiones requeridas.

### Ejecutar el programa

```bash
python avance1/ejercicio3_soporte_tripulacion.py
```

### Datos solicitados

El programa solicita:

1. Cantidad de oxígeno disponible.
2. Cantidad de oxígeno requerida.
3. Cantidad de provisiones disponibles.
4. Cantidad de provisiones requeridas.

### Ejemplo con recursos suficientes

```text
Ingrese la cantidad de oxígeno disponible: 70
Ingrese la cantidad de oxígeno requerida: 65
Ingrese la cantidad de provisiones disponibles: 40
Ingrese la cantidad de provisiones requeridas: 33
```

### Resultado esperado

```text
La nave posee recursos suficientes para la tripulación.
```

### Ejemplo con recursos insuficientes

```text
Ingrese la cantidad de oxígeno disponible: 65
Ingrese la cantidad de oxígeno requerida: 65
Ingrese la cantidad de provisiones disponibles: 32
Ingrese la cantidad de provisiones requeridas: 33
```

### Resultado esperado

```text
La nave no posee recursos suficientes para la tripulación.
```

El programa no indica cuál recurso es insuficiente, de acuerdo con los requisitos del ejercicio.

---

## Ejercicio 4: Autorización de lanzamiento

### Descripción

Este programa determina si el lanzamiento puede ser autorizado según los recursos disponibles.

El lanzamiento solamente se autoriza cuando se cumplen todas las condiciones siguientes:

- El combustible disponible es mayor o igual que el combustible total requerido.
- El oxígeno disponible es mayor o igual que el requerido.
- La energía disponible es mayor o igual que la requerida.
- Las provisiones disponibles son mayores o iguales que las requeridas.

El combustible total requerido incluye el combustible para llegar al destino, el combustible para regresar y una reserva de 10 unidades.

### Ejecutar el programa

```bash
python avance1/ejercicio4_autorizacion_lanzamiento.py
```

### Datos solicitados

El programa solicita:

1. Combustible disponible.
2. Combustible requerido para llegar al destino.
3. Combustible requerido para regresar.
4. Oxígeno disponible.
5. Oxígeno requerido.
6. Energía disponible.
7. Energía requerida.
8. Provisiones disponibles.
9. Provisiones requeridas.

### Ejemplo de lanzamiento autorizado

```text
Ingrese la cantidad de combustible disponible: 100
Ingrese la cantidad de combustible requerido hacia el destino: 40
Ingrese la cantidad de combustible requerido para el regreso: 40
Ingrese la cantidad de oxígeno disponible: 70
Ingrese la cantidad de oxígeno requerido: 65
Ingrese la cantidad de energía disponible: 65
Ingrese la cantidad de energía requerida: 60
Ingrese la cantidad de provisiones disponibles: 40
Ingrese la cantidad de provisiones requeridas: 33
```

### Resultado esperado

```text
Lanzamiento autorizado.
```

### Ejemplo de lanzamiento no autorizado

```text
Ingrese la cantidad de combustible disponible: 89
Ingrese la cantidad de combustible requerido hacia el destino: 40
Ingrese la cantidad de combustible requerido para el regreso: 40
Ingrese la cantidad de oxígeno disponible: 65
Ingrese la cantidad de oxígeno requerido: 65
Ingrese la cantidad de energía disponible: 60
Ingrese la cantidad de energía requerida: 60
Ingrese la cantidad de provisiones disponibles: 33
Ingrese la cantidad de provisiones requeridas: 33
```

### Resultado esperado

```text
Lanzamiento no autorizado. La misión debe ser revisada.
```

En este ejemplo, el combustible total requerido es de 90 unidades, pero solamente hay 89 unidades disponibles. Por esta razón, el lanzamiento no se autoriza.

## Documentación

La documentación correspondiente al primer avance se encuentra en:

```text
documentacion/avance_I_mision_orbita.pdf
```