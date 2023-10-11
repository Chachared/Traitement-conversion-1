import pandas as pd

# Spécifiez le chemin vers votre fichier Excel
input_file = "./BDD_xlsx/BDD_Car.xlsx"

# Spécifiez le nom du fichier CSV de sortie
output_file = "./BDD_steps/DataCleaning.xlsx"

# Charger le fichier Excel en spécifiant le nom de la feuille
df = pd.read_excel(input_file, sheet_name='BDD_2,0')

# Étape 1 : Supprimer le préfixe "C4C_" de la colonne car_c4cID
df['car_c4cID'] = df['car_c4cID'].str.replace('C4C_', '')

# Etape 2: Supprimer les espaces des noms de colonnes
df.columns = [col.strip() for col in df.columns]

# Étape 3: Supprimer les espaces dans les cellules
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Enregistrez le fichier modifié
df.to_excel(output_file, index=False)

print(f"Le fichier '{input_file}' a été converti en '{output_file}'")