def suppres_L():
    f = open(fn, 'wb')
    l = recherche()
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
        print("Error")
    f.close()
    return


def suppres_P():
    l = recherche()
    f = open(fn, 'rb+')
    trouv = l[0];
    i = l[1];
    j = l[2]
    if (trouv == True):
        i1 = entete(f, 1)
        buf = lire_bloc(f, i1 - 1)
        buf_nb = buf[0]
        buf_tab = buf[1]
        enreg_tmp = buf_tab[buf_nb - 1]
        buf_tab[buf_nb - 1] = tetud * '#'
        buf_nb -= 1
        if (buf_nb == 0):
            i1 -= 1
            affecte_entete(f, 1, i1)
        else:
            buf = [buf_nb, buf_tab]
            ecrireBloc(f, i1 - 1, buf)
        buf = lire_bloc(f, i)
        buf_nb = buf[0]
        buf_tab = buf[1]
        buf_tab[j] = enreg_tmp
        ecrireBloc(f, i, buf)
    else:
        print("Error")
    f.close()
    return