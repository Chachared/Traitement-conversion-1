import pandas as pd

# Spécifiez le chemin vers votre fichier Excel
input_file = "./BDD_steps/DataCleaning.xlsx"

# Spécifiez le nom du fichier CSV de sortie
output_file = "./BDD_steps/EncodageUTF8.xlsx"

# Charger le fichier Excel en spécifiant le nom de la feuille
df = pd.read_excel(input_file)

def encode_cell(cell):
    if isinstance(cell, str):
        return cell.encode('utf-8').decode('utf-8')
    return cell

df_encoded = df.applymap(encode_cell)

# Enregistrez le fichier modifié
df.to_excel(output_file, index=False)

print(f"Le fichier '{input_file}' a été converti en '{output_file}'")