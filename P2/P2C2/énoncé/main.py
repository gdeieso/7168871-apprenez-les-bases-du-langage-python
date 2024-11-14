def main():
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire

    # 1. Demandez à l'utilisateur de saisir une liste de nombres entiers séparés par des virgules
    nombres_input = input("Entrez une liste de nombres entiers séparés par des virgules : ")
    nombres_str = nombres_input.split(",")  # Utilisez split() pour diviser la chaîne de caractères
    nombres = [int(num) for num in nombres_str]  # Convertissez chaque élément en entier
    print("Liste des nombres :", nombres)

    # 2. Calculez et affichez la somme des nombres dans la liste
    somme = 0
    for num in nombres:
        somme += num
    print("Somme des nombres :", somme)

    # 3. Calculez et affichez la moyenne des nombres dans la liste
    moyenne = somme / len(nombres)
    print("Moyenne des nombres :", moyenne)

    # 4. Calculez et affichez le nombre de nombres supérieurs à la moyenne
    count_sup_moyenne = 0
    for num in nombres:
        if num > moyenne:
            count_sup_moyenne += 1
    print("Nombre de nombres supérieurs à la moyenne :", count_sup_moyenne)

    # 5. Calculez et affichez le nombre de nombres pairs dans la liste
    count_paires = 0
    index = 0
    while index < len(nombres):
        if nombres[index] % 2 == 0:
            count_paires += 1
        index += 1
    print("Nombre de nombres pairs :", count_paires)

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()