def insertion():
    l = recherche()
    find = l[0]
    f = open(fn, 'wb')
    num = input("ID : ")
    nom = input("Name : ")
    prenom = input("Last Name : ")
    affiliation = input("Affiliation : ")
    num = resize_chaine(num, T_ID)
    nom = resize_chaine(nom, Tname)
    prenom = resize_chaine(prenom, TLName)
    affiliation = resize_chaine(affiliation, taff)
    etud = num + nom + prenom + affiliation + efface
    if (find == False):
        i = entete(f, 1)
        buf = lire_bloc(f, i - 1)
        buf_nb = buf[0]
        buf_tab = buf[1]
        if (buf_nb < b):
            buf_tab[buf_nb] = etud
            buf_nb += 1
            buf = [buf_nb, buf_tab]
            ecrireBloc(f, i - 1, buf)
        else:
            ecrireBloc(f, i - 1, buf)
            buf_tab = [tnreg] * b
            buf_nb = 0
            buf_tab[0] = etud
            buf_nb += 1
            buf = [buf_nb, buf_tab]
            affecte_entete(f, 1, i + 1)
            ecrireBloc(f, i, buf)
        n = entete(f, 0)
        n += 1
        affecte_entete(f, 0, n)
    else:
        print("Error")
    f.close()
    return