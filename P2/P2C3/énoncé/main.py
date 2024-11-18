# Ecrivez vos fonctions ici

# # Contexte

# Vous devez créer un programme qui calcule le salaire horaire d'un employé, en fonction de son salaire mensuel et de son nombre d'heures travaillées par semaine. Le programme doit utiliser des fonctions pour effectuer les calculs.

# # Instructions  

#   1. **Créez** une fonction appelée `salaire_mensuel(salaire_annuel)` qui prend en *paramètre* un **salaire annuel** et *retourne* le **salaire mensuel** correspondant en **divisant** le salaire annuel par *12*. *(Faites un copier-coller sur le nom de la fonction sinon les tests risquent de ne pas passer)*
#   2. **Créez** une fonction appelée `salaire_hebdomadaire(salaire_mensuel)` qui prend en paramètre un **salaire mensuel** et *retourne* le **salaire hebdomadaire** correspondant en **divisant** le salaire mensuel par *4*. *(Faites un copier-coller sur le nom de la fonction sinon les tests risquent de ne pas passer)*
#   3. **Créez** une fonction appelée `salaire_horaire(salaire_hebdomadaire, heures_travaillees)` qui prend en *paramètres* un **salaire hebdomadaire** et le **nombre d'heures travaillées par semaine**, et *retourne* le **salaire horaire** correspondant en **divisant** le salaire hebdomadaire par le nombre d'heures travaillées par semaine. *(Faites un copier-coller sur le nom de la fonction sinon les tests risquent de ne pas passer)*
#   4. **Crééz** une fonction main pour *appeler* les fonctions :
#      * **Demandez** à l'utilisateur de **saisir** son *salaire annuel*.
#      * **Demandez** à l'utilisateur de **saisir** le *nombre d'heures travaillées par semaine*.
#      * **Appelez** les fonctions précédemment créées pour calculer le salaire horaire correspondant.
#      * **Affichez** le résultat sous la forme : `"Votre salaire horaire est de XX euros"`.
# Fonction pour calculer le salaire mensuel
def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

# Fonction pour calculer le salaire hebdomadaire
def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

# Fonction pour calculer le salaire horaire
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

# Fonction principale
def main():
    # Demande à l'utilisateur de saisir son salaire annuel
    salaire_annuel = float(input("Veuillez saisir votre salaire annuel (en euros) : "))
    
    # Demande à l'utilisateur de saisir le nombre d'heures travaillées par semaine
    heures_travaillees = float(input("Veuillez saisir le nombre d'heures travaillées par semaine : "))
    
    # Calculs
    mensuel = salaire_mensuel(salaire_annuel)
    hebdomadaire = salaire_hebdomadaire(mensuel)
    horaire = salaire_horaire(hebdomadaire, heures_travaillees)
    
    # Affichage du résultat
    print(f"Votre salaire horaire est de {horaire:.2f} euros")

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()