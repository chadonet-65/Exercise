"""
   saissir le nom du caissiaire et afficher
   saissir la commande du client et sortir une facture avec les differents montants, ainsi que le montant total

"""
def super_marche():
    print("#######################")
    print("#      BIENVENUE      #")
    print("#   AU SUPER MARCHE   #")
    print("#      JONATHAN       #")
    print("#######################")

    name = input("Veillez saissir votre nom : ")
    char = 'O'
    i = 0
    list_prd = {}
    while char == 'O' or char == 'N' :

        cmd = str(input("Saissir nom du produit : "))
        prix = int(input("Prix unitaire du produit : "))
        i = i + 1
        list_prd.update({cmd:prix})

        print(list_prd.values())


