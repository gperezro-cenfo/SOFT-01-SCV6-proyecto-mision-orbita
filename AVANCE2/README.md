# Misión Órbita - Avance II

Proyecto correspondiente al curso **SOFT-01 Principios de Programación I**, sección **SCV6**.

## Descripción del proyecto

El Avance II de **Misión Órbita** contiene programas desarrollados en Python para simular la exploración científica en el destino y evaluar el regreso o la supervivencia de la tripulación según los recursos disponibles.

Los ejercicios incluidos son:

- **Ejercicio 7:** administra actividades de exploración, consumo de recursos, muestras recolectadas y puntos científicos.
- **Ejercicio 8:** determina si la nave puede iniciar el regreso; si puede hacerlo, simula cada día del viaje y, si queda varada, calcula los días estimados de supervivencia y los recursos limitantes.

Cada programa funciona de forma independiente y solicita los datos mediante la terminal.

## Integrantes

- Glenn Perez Rodríguez

## Estructura del proyecto

```text
SOFT-01-SCV6-proyecto-mision-orbita/
├── AVANCE1/
│   ├── ejercicio1_calculo_recursos.py
│   ├── ejercicio2_verificacion_combustible.py
│   ├── ejercicio3_soporte_tripulacion.py
│   └── ejercicio4_autorizacion_lanzamiento.py
├── AVANCE2/
│   ├── EJERCICIO_7/
│   │   ├── Avance_II_Ejercicio_7.pdf
│   │   └── ejercicio7_exploracion.py
│   └── EJERCICIO_8/
│       ├── Avance_II_Ejercicio8.pdf
│       └── ejercicio8_regreso.py
├── documentacion/
├── LICENSE
└── README.md
```

## Requisitos

Para ejecutar los programas se necesita:

- Python 3.
- Una terminal, PowerShell o símbolo del sistema.
- Opcionalmente, un editor como Visual Studio Code.

Los programas utilizan únicamente elementos incluidos en Python, por lo que no requieren bibliotecas externas.

## Convenciones y estilos de programación

El código sigue las recomendaciones de estilo de **PEP 8** y las restricciones académicas establecidas para el proyecto:

- Variables con nombres descriptivos en minúscula y formato `snake_case`.
- Constantes escritas en mayúscula y formato `UPPER_SNAKE_CASE`.
- Indentación uniforme de cuatro espacios.
- Espacios alrededor de operadores aritméticos, lógicos y de comparación.
- Líneas en blanco para separar bloques lógicos.
- Constantes declaradas al inicio de cada archivo para evitar números mágicos.
- Comentarios breves para identificar entradas, cálculos, decisiones, ciclos y salidas.
- Encabezado en cada archivo con nombre, curso, estudiante, fecha, versión y descripción.
- Mensajes de consola claros y con las unidades correspondientes.
- Uso de estructuras básicas estudiadas en el curso: entrada y salida de datos, cálculos, condicionales y ciclos `while`.
- Finalización de los ciclos mediante condiciones o variables de control, sin utilizar `break`, `continue`, `exit` o `quit`.
- No se utilizan colecciones, funciones definidas por el usuario, importaciones ni las funciones `min` o `max`.

## Verificar la instalación de Python

Antes de ejecutar los programas, comprobar que Python esté instalado:

```bash
python --version
```

En Windows también se puede utilizar:

```bash
py --version
```

## Instrucciones para ejecutar los programas

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta principal `SOFT-01-SCV6-proyecto-mision-orbita`.
3. Ejecutar el programa deseado con uno de los comandos indicados a continuación.
4. Ingresar los datos solicitados en la terminal.

### Ejercicio 7 - Exploración científica

Desde la carpeta principal del repositorio:

```bash
python AVANCE2/EJERCICIO_7/ejercicio7_exploracion.py
```

En Windows, si el comando `python` no está disponible:

```bash
py AVANCE2/EJERCICIO_7/ejercicio7_exploracion.py
```

El programa solicita la energía y las provisiones disponibles. Después muestra un menú para analizar el terreno, recolectar una muestra, realizar una observación o finalizar la exploración.

### Ejercicio 8 - Regreso o supervivencia

Desde la carpeta principal del repositorio:

```bash
python AVANCE2/EJERCICIO_8/ejercicio8_regreso.py
```

En Windows, si el comando `python` no está disponible:

```bash
py AVANCE2/EJERCICIO_8/ejercicio8_regreso.py
```

El programa solicita la cantidad de tripulantes, la duración del viaje de ida y los recursos disponibles. Con estos datos, simula el regreso o calcula la supervivencia de la tripulación si la nave no puede iniciarlo.

## Ejecución desde la carpeta AVANCE2

Si la terminal ya se encuentra dentro de la carpeta `AVANCE2`, se pueden utilizar estos comandos:

```bash
python EJERCICIO_7/ejercicio7_exploracion.py
python EJERCICIO_8/ejercicio8_regreso.py
```

En Windows, `python` puede sustituirse por `py`.

## Documentación

La documentación de cada ejercicio del Avance II se encuentra junto a su respectivo archivo de código:

```text
AVANCE2/EJERCICIO_7/Avance_II_Ejercicio_7.pdf
AVANCE2/EJERCICIO_8/Avance_II_Ejercicio8.pdf
```

Estos documentos incluyen el análisis, las tablas de variables, los diagramas de flujo y los casos de prueba correspondientes a los ejercicios 7 y 8.
