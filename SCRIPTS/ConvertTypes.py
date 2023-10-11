import pandas as pd
import numpy as np

# Spécifiez le chemin vers votre fichier Excel
input_file = "./BDD_steps/RenameColumns.xlsx"

# Spécifiez le nom du fichier CSV de sortie
output_file = "./BDD_steps/ConvertTypes.xlsx"

# Charger le fichier Excel en spécifiant le nom de la feuille
df = pd.read_excel(input_file)

# Créez un dictionnaire des types de données attendus
expected_data_types = {
    "car_c4cID": "c4c_id",
    "td_id": "bigint",
    "ebay_id": "bigint",
    "car_fuel": "varchar(50)",
    "car_nb_shift": "varchar(50)",
    "car_desc": "varchar(100)",
    "car_trans": "varchar(50)",
    "car_trim": "varchar(100)",
    "car_version": "varchar(100)",
    "car_plat": "varchar(100)",
    "car_y_from": "int",
    "car_y_to": "int",
    "car_d_from": "date",
    "car_d_to": "date",
    "car_ranking": "varchar(50)",
    "car_mark": "varchar(50)",
    "car_name": "varchar(100)",
    "car_doors": "varchar(50)",
    "car_chassis": "varchar(50)",
    "car_model_y_from": "int",
    "car_model_y_to": "int",
    "car_code": "varchar(50)",
    "car_engine_desc": "varchar(50)",
    "car_aspi": "varchar(50)",
    "car_alim": "varchar(50)",
    "car_name_cyl": "varchar(50)",
    "car_valve": "varchar(50)",
    "car_kw": "varchar(50)",
    "car_cv": "varchar(50)",
    "car_disp": "varchar(50)",
    "car_cyl": "int",
    "car_nb_cyl": "varchar(50)",
    "car_type":"varchar(50)",
    "car_date_add": "date",
    "car_url": "varchar(255)",
    "car_user": "varchar(100)",
    "car_method": "varchar(50)",
    "car_valid": "boolean",
    "car_comment": "varchar(255)",
}

# Boucle pour convertir les colonnes en fonction des types attendus
for column, expected_type in expected_data_types.items():
    if column in df.columns:
        if expected_type == "bigint":
            try: 
                df[column] = pd.to_numeric(df[column], errors='coerce')
                df[column] = df[column].astype('Int64')  # Notez le 'I' majuscule pour permettre les NaN
            except ValueError:
                print(f"La colonne '{column}' contient des valeurs non valides pour la conversion en int.")

        elif expected_type == "int":
            try:
                df[column] = pd.to_numeric(df[column], errors='coerce')
                df[column] = df[column].astype('Int32')
            except ValueError:
                print(f"La colonne '{column}' contient des valeurs non valides pour la conversion en int.")

        elif expected_type == "varchar(50)" or expected_type == "varchar(100)" or expected_type == "varchar(255)":
            df[column] = df[column].astype('string').str[:int(expected_type.split("(")[1][:-1])] if expected_type.startswith("varchar") else int(expected_type.split("(")[1][:-1])
        elif expected_type == "date":
            df[column] = pd.to_datetime(df[column], errors='coerce').dt.date
        elif expected_type == "boolean":
            df[column] = df[column].str.lower().map({'true': 1, 'false': 0})
            df[column] = df[column].astype('boolean')

# Vérifiez les types des colonnes après conversion
for column, expected_type in expected_data_types.items():
    if column in df.columns:
        print(f"Type de la colonne '{column}': {df[column].dtype}")

# Enregistrez le fichier modifié
df.to_excel(output_file, index=False)

print(f"Le fichier '{input_file}' a été converti en '{output_file}'")
