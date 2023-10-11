import pandas as pd

# Spécifiez le chemin vers votre fichier Excel
input_file = "./BDD_steps/ConvertTypes.xlsx"

# Spécifiez le nom du fichier CSV de sortie
output_file = "./BDD_ready_for_import.xlsx"

# Charger le fichier Excel en spécifiant le nom de la feuille
df = pd.read_excel(input_file)

# Étape 1: Renommer et formater "car_YFrom"
if 'car_YFrom' in df.columns:
    df['car_YFrom'] = pd.to_datetime(df['car_YFrom'], format='%d/%m/%Y', errors='coerce')
    df['car_YFrom'] = df['car_YFrom'].dt.strftime('%Y-%m-%d')
    df.rename(columns={'car_YFrom': 'car_d_from'}, inplace=True)

# Étape 2: Renommer et formater "car_Yto"
if 'car_Yto' in df.columns:
    df['car_Yto'] = pd.to_datetime(df['car_Yto'], format='%d/%m/%Y', errors='coerce')
    df['car_Yto'] = df['car_Yto'].dt.strftime('%Y-%m-%d')
    df.rename(columns={'car_Yto': 'car_d_to'}, inplace=True)

# Étape 3: Créer une colonne "car_y_from" et y écrire la première année de la colonne "car_year"
if 'car_year' in df.columns:
    df['car_y_from'] = df['car_year'].str.split('-').str[0]

# Étape 4: Créer une colonne "car_y_to" et y écrire la deuxième année de la colonne "car_year"
if 'car_year' in df.columns:
    df['car_y_to'] = df['car_year'].str.split('-').str[1]

# Étape 5: Vérifier que toutes les données de "car_year" ont bien été réécrites dans les colonnes "car_y_from" et "car_y_to"
if 'car_year' in df.columns:
    df.drop('car_year', axis=1, inplace=True)

# Étape 6: Réorganiser les colonnes
if 'car_y_from' in df.columns and 'car_y_to' in df.columns:
    cols = list(df.columns)
    cols.remove('car_y_from')
    cols.remove('car_y_to')
    idx_d_to = cols.index('car_d_to')
    cols.insert(idx_d_to + 1, 'car_y_from')
    cols.insert(idx_d_to + 2, 'car_y_to')
    df = df[cols]

# Étape 7: formater ISO8601 la colonne "info_dateAdd"
df['car_date_add'] = pd.to_datetime(df['car_date_add'], format='%d/%m/%Y', errors='coerce')
df['car_date_add'] = df['car_date_add'].dt.strftime('%Y-%m-%d')

# Enregistrez le fichier modifié
df.to_excel(output_file, index=False)

print(f"Le fichier '{input_file}' a été converti en '{output_file}'")