import pandas as pd

# Spécifiez le chemin vers votre fichier Excel
excel_file = "./BDD_csv/EncodageUTF8.xlsx"

# Spécifiez le nom du fichier CSV de sortie
output_file = "./BDD_csv/BDD.csv"

# Lire le fichier Excel
df = pd.read_excel(excel_file)

# Écrire le DataFrame dans un fichier CSV
df.to_csv(output_file, index=False)

print(f"Le fichier Excel '{excel_file}' a été converti en '{output_file}'")
