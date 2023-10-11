import subprocess

# Liste des scripts à exécuter dans l'ordre souhaité
scripts_to_run = [
    "SCRIPTS/DataCleaning.py",
    "SCRIPTS/EncodageUTF8.py",
    "SCRIPTS/SelectColumns.py",
    "SCRIPTS/RenameColumns.py",
    "SCRIPTS/ConvertTypes.py",
    "SCRIPTS/dates_ISO8601.py",

    # "SCRIPTS/Convert_xlsx.py",
]

# Parcourez la liste des scripts et exécutez-les un par un
for script in scripts_to_run:
    try:
        subprocess.run(["python", script], check=True)
        print(f"Le script {script} a été exécuté avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du script {script}: {e}")
    except FileNotFoundError:
        print(f"Le fichier {script} n'a pas été trouvé. Veuillez vérifier le chemin ou le nom du fichier.")

print("Tous les scripts ont été exécutés.")