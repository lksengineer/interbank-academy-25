"""
* Modulo para leer un archivo csv y 
* calcular el balance de transacciones restando la suma del balance de débito a la suma del 
balance de crédito 
* Obtener la Transacción de mayor monto con su respectivo ID y
calcular total de transacciones según su tipo (Crédito o Débito).
"""

# Importar el modulo os para verificar si el archivo existe
from os.path import exists

# Importar el modulo cvs para leer el archivo csv
import csv


# Instanciar el archivo csv y verificar si existe, sino existe lanzar un mensaje de error
datafile = 'data.csv'
if not exists(datafile):
    raise FileNotFoundError(f"El archivo {datafile} no existe.")

# Abrir el archivo csv y leerlo
with open(datafile, "r", encoding="utf-8") as fl:
    cvsreader = csv.reader(fl, delimiter=",")

    # Saltar la primera fila del archivo csv y poder iterar los valores que se quieren
    next(cvsreader)

    # Declarar las variables para el balance
    balance_credito = 0
    balance_debito = 0
    
    # Declarar las variables para la transacción de mayor monto y su ID
    trasaccion_mayor_monto = 0
    id_trasaccion_mayor_monto = 0

    # Declarar un diccionario para contar las transacciones por tipo inicializando en 0
    conteo_transacciones = {
        "Crédito": 0,
        "Débito": 0
    }

    # Iterar el archivo csv fila por fila
    for cvs in cvsreader:
        #  Calcular el balance comparando el tipo de transacción
        if cvs[1] == "Crédito":
            balance_credito += float(cvs[2])

            # Contar las transacciones de tipo crédito y nos ayuda a obtener el total al finalizar la iteración
            conteo_transacciones["Crédito"] += 1

        elif cvs[1] == "Débito":
            balance_debito += float(cvs[2])

            # Contar las transacciones de tipo débito y nos ayuda a obtener el total al finalizar la iteración
            conteo_transacciones["Débito"] += 1

        else:
            raise ValueError(f"Tipo de transacción desconocido: {cvs[1]}")

        # Calcular la transacción de mayor monto identificanco el ID y el monto de la transacción con el valor más alto.
        if float(cvs[2]) > trasaccion_mayor_monto:
            trasaccion_mayor_monto = float(cvs[2])
            id_trasaccion_mayor_monto = int(cvs[0])

        # Contar las transacciones por tipo

    # Imprimir el balance total
    print("Reporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {balance_credito - balance_debito:.2f}")
    print(f"Transacción de Mayor Monto: ID {id_trasaccion_mayor_monto} - {trasaccion_mayor_monto:.2f}")
    print(f"Conteo de Transacciones: Crédito: {conteo_transacciones['Crédito']}, Débito: {conteo_transacciones['Débito']}")
