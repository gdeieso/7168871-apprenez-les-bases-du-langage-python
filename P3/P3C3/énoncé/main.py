# Écrivez votre code ici !
import csv

# Fonction extract : Lire le fichier input.csv
def extract(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Fonction transform : Calculer les salaires
def transform(data):
    transformed_data = []
    for row in data:
        salaire = int(row['heures_travaillees']) * 15
        transformed_data.append({'nom': row['nom'], 'salaire': salaire})
    return transformed_data

# Fonction load : Écrire le fichier output.csv
def load(data, output_file_path):
    with open(output_file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['nom', 'salaire'])
        writer.writeheader()
        writer.writerows(data)

# Appeler les fonctions dans l'ordre pour exécuter ETL
def main():
    input_file = 'P3/P3C3/énoncé/input.csv'
    output_file = 'P3/P3C3/énoncé/output.csv'
    
    # Étape 1 : Extraction
    raw_data = extract(input_file)
    
    # Étape 2 : Transformation
    transformed_data = transform(raw_data)
    
    # Étape 3 : Chargement
    load(transformed_data, output_file)
    
    print(f"Le fichier {output_file} a été créé avec succès.")

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()