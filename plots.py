import pandas as pd
import glob
import numpy as np

def round_up_average_csv(input_folder, output_csv_file):
    # Obtener la lista de nombres de archivos CSV en la carpeta de entrada
    csv_files = glob.glob(input_folder + '/*.csv')

    # Inicializar un DataFrame vacío con las mismas columnas que el primer archivo CSV
    first_df = pd.read_csv(csv_files[0])
    result_df = pd.DataFrame(columns=first_df.columns)

    # Contar la cantidad de archivos CSV en la carpeta de entrada
    num_files = len(csv_files)

    # Leer y sumar los datos de cada archivo CSV
    for file in csv_files:
        df = pd.read_csv(file)
        result_df = result_df.add(df, fill_value=0)

    # Promediar los valores sumados dividiéndolos por la cantidad de archivos
    result_df = result_df / num_files

    # Redondear todos los valores hacia arriba
    result_df = np.ceil(result_df)

    # Guardar el resultado en un nuevo archivo CSV
    result_df.to_csv(output_csv_file, index=False)

# Llamar a la función con la carpeta de entrada y el archivo de salida
input_folder = 'resultados'
output_csv_file = 'simulaciones.csv'
round_up_average_csv(input_folder, output_csv_file)
