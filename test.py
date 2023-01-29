from pickle import dumps, loads
from sys import getsizeof

global b
global tnom
global tprénom
global tnuminscpt
global taffiliation
# taille du bloc: un bloc peut contenir au max b enregitrements
b = 3
"""parceque les enregitrements sont à taille fixe 
il faut définir pour chaque champ la taille max"""
# taille du champ numéro inscription
tnum = 10
# taille du champ nom
tnom = 20
# taille du champ prénom
tprénom = 20
# taille du champ affiliation
taffiliation = 20
# Tetud  c'est la taille totale d'un enregitrement
Tetud = tnum + tnom + tprénom + taffiliation + 1
# fixer la taille d'un enregitrement
Tnreg = '#' * Tetud
global buf
""" 
Dans  la déclaration on définit le typeBloc Tbloc=[0,[Tnreg]*b]

le premier élément buf[0] c le buf.NB qui est de type entier initialisé à 0

le deuxième c'est le tableau d'enregistrement de type enregistrement [Tenreg]*b
"""
Tbloc = [0, [Tnreg] * b]
global blocsize
"""
l'instruction suivante permet de calculer la taille qui sera occupée par un bloc 

"""
blocsize = getsizeof(dumps(Tbloc)) + len(Tnreg) * (b - 1) + (b - 1)
print(blocsize)

"""
Dans ce cas lorsque on lit un champ inferieur à la taille max déclarée pour ce champ
on doit compléter le reste par un #
exemple: si le numéro d'inscription=='001', or la taille déclarée =5 alors, on le transforme 
en '001##'. pour garder la notion taille fixe. 

"""


def resize_chaine(chaine, maxtaille):
    for i in range(len(chaine), maxtaille):
        chaine = chaine + '#'
    return chaine


""" la fonctin créer c'est l'algorithme de chargement initial d'un fichier T~OF
    Dans ce cas les blocs sont remplis à 100% si on veut remplir les blocs avec
    un % donné, on peut juste envoyer à la fonction créer une variable soit par
    exemple mu et pour tester le si le bloc est plein, au lieu de faire j<b on fait 
    si j<b*mu (si on veut remplir les blocs à 50%, mu alors = 0.5 )
"""


def créer_fichier():
    fn = input('Entrer le nom du fichier à créer: ')
    j = 0
    i = 0
    n = 0
    buf_tab = [Tnreg] * b
    buf_nb = 0
    try:
        f = open(fn, 'wb')
    except:
        print('impossible d\'ouvrir le fichier en mode d\'écriture ')
    rep = 'O'
    while (rep == 'O'):
        print('Entrer les information de l\'étudiant: ')
        num = input('Enter le numéro d\'inscription : ')
        nom = input('Enter le nom: ')
        prénom = input('Entrer le prénom: ')
        affiliation = input('Entrer l\'affiliation: ')
        num = resize_chaine(num, tnum)
        nom = resize_chaine(nom, tnom)
        prénom = resize_chaine(prénom, tprénom)
        affiliation = resize_chaine(affiliation, taffiliation)
        etud = num + nom + prénom + affiliation + '0'
        n = n + 1
        if (j < b):
            buf_tab[j] = etud  # mettre l'enregitrement dans le tableau
            buf_nb = buf_nb + 1  # augmenter le buf.NB
            j = j + 1
        else:
            # mettre le NB et le tableau d'eregistremnt dans une variable buf
            buf = [buf_nb, buf_tab]
            # ecrire le buf en mémoire secondaire
            ecrireBloc(f, i, buf)
            # rénitialiser le tableau d'enregitrement et le Nb
            buf_tab = [Tnreg] * b
            buf_nb = 1
            buf_tab[0] = etud
            j = 1
            i = i + 1
        rep = input('Avez vous un autre élement à entrer O/N: ')

    buf = [j, buf_tab]
    ecrireBloc(f, i, buf)
    affecter_entete(f, 0, n)
    affecter_entete(f, 1, i + 1)
    f.close()
    return


# ces fonctions sont déja expliquées
def lireBloc(file, i):
    dp = 2 * getsizeof(dumps(0)) + i * blocsize
    file.seek(dp, 0);
    buf = file.read(blocsize)
    return (loads(buf))


def ecrireBloc(file, i, bf):
    dp = 2 * getsizeof(dumps(0)) + i * blocsize
    file.seek(dp, 0)
    file.write(dumps(bf));

    return


def affecter_entete(file, of, c):
    dp = of * getsizeof(dumps(0))
    file.seek(dp, 0)
    file.write(dumps(c))
    return


def entete(file, offset):
    dp = offset * getsizeof(dumps(0))
    file.seek(dp, 0)
    c = file.read(getsizeof(dumps(0)))
    return loads(c)


def afficher_fichier():
    fn = input('Entrer le nom du fichier à afficher: ')
    f = open(fn, 'rb')
    secondcar = entete(f, 1)
    print(secondcar)
    print(f'votre fichier contient {secondcar} block \n')
    for i in range(0, secondcar):
        buf = lireBloc(f, i)
        buf_nb = buf[0]  # recupérer le nb
        buf_tab = buf[1]  # recupérer le tableau d'enregitrement
        print(f'Le contenu du block {i + 1} est:\n')
        # pour chaque enregitrement dans le tableau
        for j in range(buf_nb):
            print(afficher_enreg(buf_tab[j]))  # afficher l'enregitrement
        print('\n')

    f.close()
    return


def afficher_enreg(e):
    # recupérer les champs à partir de chaque enregistrement et remplacer les '#' par un espace
    num = e[0:tnom].replace('#', ' ')
    nom = e[tnom:tprénom].replace('#', ' ')
    prénom = e[tprénom:taffiliation].replace('#', ' ')
    affiliation = e[taffiliation:len(e) - 1].replace('#', ' ')
    return num + ' ' + nom + ' ' + prénom + ' ' + affiliation + ' ' + e[-1]


def affic_unique(e):
    # recupérer les champs à partir de chaque enregistrement et remplacer les '#' par un espace
    num = e[0].replace('#', '')
    return num


def afficher_enr_bloc():
    fn = input('Entrer le nom du fichier à afficher: ')
    f = open(fn, 'rb')
    secondcars = int(input("Entrer the bloc number : "))
    secondcarss = int(input("Entrer the enreg number : "))

    print(f'votre bloc contient {secondcars} contient \n')
    for i in range(secondcars - 1, secondcars):
        buf = lireBloc(f, i)
        buf_tab = buf[1]  # recupérer le tableau d'enregitrement
        # pour chaque enregitrement dans le tableau
        print(afficher_enreg(buf_tab[secondcarss - 1]))  # afficher l'enregitrement
        print('\n')

    f.close()
    return


def afficher_enreg1(e, id):
    # recupérer les champs à partir de chaque enregistrement et remplacer les '#' par un espace
    num = e[0:tnom].replace('#', ' ')
    nom = e[tnom:tprénom].replace('#', ' ')
    prénom = e[tprénom:taffiliation].replace('#', ' ')
    affiliation = e[taffiliation:len(e) - 1].replace('#', ' ')
    print(id)
    print(num)
    if id == num:
        return num + ' ' + nom + ' ' + prénom + ' ' + affiliation + ' ' + e[-1]


def recherche():
    fn = input('Entrer le nom du fichier à afficher: ')
    f = open(fn, 'rb')
    cleid = int(input("Enter the id : "))
    secondcar = entete(f, 1)
    ## print(f'votre fichier contient {secondcar} block \n')
    for i in range(0, secondcar):
        buf = lireBloc(f, i)
        buf_nb = buf[0]  # recupérer le nb
        buf_tab = buf[1]  # recupérer le tableau d'enregitrement

        # pour chaque enregitrement dans le tableau
        for j in range(buf_nb):
            if cleid == int(affic_unique(buf_tab[j])):
                print(f'Sucess ! :\n')
                print(afficher_enreg(buf_tab[j]))  # afficher l'enregitrement

    f.close()
    return


def insertion():
    print("<-- L'insertion d'un élement -->")
    l = recherche()
    trouv = l[0]
    i = l[1]
    j = l[2]
    fn =
    with open(f, 'rb+') as f:
        print("entrez les informations de l\'étudiant pour l'insertion : ")
        num = input("entrez le numéro d\'inscription : ")
        nom = input("entrez le nom : ")
        prenom = input("entrez le  prenom : ")
        affiliation = input("entrez l\'affiliation : ")
        num = resize_chaine(num, tnum)
        nom = resize_chaine(nom, tnom)
        prenom = resize_chaine(prenom, tprenom)
        affiliation = resize_chaine(affiliation, taffiliation)
        etud = num + nom + prenom + affiliation + efface
        if (trouv == False):
            buf = lire_bloc(f, i)
            buf_nb = buf[0]
            buf_tab = buf[1]
            if (buf_nb < b):
                k = buf_nb - 1
                while (k >= j):
                    buf_tab[k] = buf_tab[k - 1]
                    k -= 1
                buf_tab[j] = etud
                buf_nb += 1
                buf = [buf_nb, buf_tab]
                ecrireBloc(f, i, buf)
            else:
                etmp = buf_tab[buf_nb - 1]
                k = buf_nb - 1
                while (k >= j):
                    buf_tab[k] = buf_tab[k - 1]
                    k -= 1
                buf_tab[j] = etud
                ecrireBloc(f, i, buf)
                i += 1
                while i < entete(f, 1):
                    buf = lire_bloc(f, i)
                    buf_nb = buf[0]
                    buf_tab = buf[1]
                    k = buf_nb - 1
                    etmp1 = buf_tab[buf_nb - 1]
                    while (k >= 1):
                        buf_tab[k] = buf_tab[k - 1]
                        k -= 1
                    buf_tab[0] = etmp
                    etmp = etmp1
                    buf = [buf_nb, buf_tab]
                    ecrireBloc(f, i, buf)
                    i += 1
                if (etmp != tetud * '#' and i >= entete(f, 1)):
                    affecte_entete(f, 1, i + 1)
                    buf_nb = 1
                    buf_tab[0] = etmp
                    buf = [buf_nb, buf_tab]
                    ecrireBloc(f, i, buf)
            n = entete(f, 0)
            n += 1
            affecte_entete(f, 0, n)
        else:
            print("L'élément existe déjà !")
    return


def suppression_logique():
    print("<-- suppression logique d'un élement -->")
    f = open(fn, 'rb+')

    trouv = l[0]
    i = l[1]
    j = l[2]
    if (trouv == True):
        buf = lire_bloc(f, i)
        buf_nb = buf[0]
        buf_tab = buf[1]
        buf_tab[j] = buf_tab[j][:(tetud) - 2] + '1'
        buf = [buf_nb, buf_tab]
        ecrireBloc(f, i, buf)
    else:
        print("L'élement n\'existe pas !")
    f.close()
    return


def default():
    return "choix invalid"


def choix(ch):
    switcher = {
        1: créer_fichier,
        2: afficher_fichier,
        3: afficher_enr_bloc,
        4: recherche,
        5: insertion,
        6: suppression_logique,
    }
    return switcher.get(ch, default)()


def main():
    rep = 'O'
    while (rep == 'O'):
        print("""Entrer votre choix 
                 1: créer_fichier
                 2: afficher_fichier
                 3: affichage par bloc num et num de l'enregistrement
                 4: recherche par matricule
                 5: Insertion
                 6: Supression logique""")

        ch = int(input())
        choix(ch)
        rep = input('Avez vous une autre opération O/N? ')


main()
