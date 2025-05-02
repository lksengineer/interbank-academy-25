# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Objetivo:

Desarrolla una aplicación de línea de comandos (CLI) que procese un archivo CSV con transacciones bancarias y genere un reporte que incluya:

- **Balance Final:**  
  Suma de los montos de las transacciones de tipo "Crédito" menos la suma de los montos de las transacciones de tipo "Débito".

- **Transacción de Mayor Monto:**  
  Identificar el ID y el monto de la transacción con el valor más alto.

- **Conteo de Transacciones:**  
  Número total de transacciones para cada tipo ("Crédito" y "Débito").

---

## Instrucciones

1. **Repositorio Base:**  
   Clona o haz un fork del repositorio base disponible en:  
   `https://github.com/codeableorg/interbank-academy-25`

2. **Entrada de Datos:**  
   La aplicación deberá leer un archivo CSV. Ejemplo de contenido:

   ```
   id,tipo,monto
   1,Crédito,100.00
   2,Débito,50.00
   3,Crédito,200.00
   4,Débito,75.00
   5,Crédito,150.00
   ```

3. **Salida del Programa:**  
   La aplicación debe mostrar el reporte final en la terminal.  
   Ejemplo de salida:

   ```
   Reporte de Transacciones
   ---------------------------------------------
   Balance Final: 325.00
   Transacción de Mayor Monto: ID 3 - 200.00
   Conteo de Transacciones: Crédito: 3 Débito: 2
   ```

4. **Lenguaje de Programación:**  
   Utiliza el lenguaje de tu preferencia. Opciones recomendadas:

   - Python
   - Java
   - C#
   - JavaScript (Node.js)

5. **README del Proyecto:**  
   Incluye un archivo `README.md` con la siguiente estructura:

   - **Introducción:** Breve descripción del reto y su propósito.
   - **Instrucciones de Ejecución:** Cómo instalar dependencias y ejecutar la aplicación.
   - **Enfoque y Solución:** Lógica implementada y decisiones de diseño.
   - **Estructura del Proyecto:** Archivos y carpetas principales.

6. **Documentación y Calidad del Código:**
   - Código bien documentado y fácil de leer.
   - Comentarios explicando pasos clave y lógica del programa.


## 1.Introducción
Programa que permite leer un archivo csv y calcular el balance de transacciones restando la suma del balance de débito a la suma del balance de crédito.
Segundo calculo es obtener la Transacción de mayor monto con su respectivo ID y tercero, calcular total de transacciones según su tipo (Crédito o Débito).


## 1. Instrucciones de Ejecución:
Clona o haz un fork del repositorio base disponible en:
https://github.com/lksengineer/interbank-academy-25

Desde el directorio raíz, Ejecutar:
python3 run.py

## 2 Enfoque y Solución:

La lógica principal de la aplicación se centra en abrir y leer el archivo CSV línea por línea después de omitir la fila de encabezado y en cada itersación, se realiza lo siguiente:

Cálculo del Balance: Se verifica el tipo de transacción en indice [1] de la lista. Si es "Crédito", el monto se suma al balance de crédito; si es "Débito", se suma al balance de débito. Al final, el balance final se calcula restando el balance de débito al balance de crédito.

Calculo de la Transacción de Mayor Monto: Se compara el monto de cada transacción en el indice [2] de la lista que se está iterando con el monto máximo encontrado hasta el momento, defini. Si la transacción actual tiene un monto mayor, se actualiza la variable que almacena el monto máximo y su respectivo ID.

Conteo de Transacciones por Tipo: e utiliza un diccionario para mantener un registro del número de transacciones de cada tipo ("Crédito" y "Débito"). Cada vez que se procesa una transacción, se incrementa el contador correspondiente en el diccionario.

## 3 Estructura del Proyecto:
.
├── run.py        archivo en Python para ejcutar el programa
└── data.csv       Archivo cvs que contiene los datos de las transacciones
└── README.md      Erchivo con la documentación del proyecto