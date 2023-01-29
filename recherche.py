def recherche():
    f = open(fn, 'wb')
    ID = input("Put the id : ")
    i = 0;
    find = False
    while (i < entete(f, 1) and find == False):
        buf = lire_bloc(f, i)
        buf_nb = buf[0]
        buf_tab = buf[1]
        j = 0
        while (j < buf_nb and find == False):
            if (int(buf_tab[j][0:T_ID].replace('#', '')) == int(ID) and buf_tab[j][tetud - 1:] == '0'):
                find = True
            else:
                j += 1
        if (not (find)):
            i += 1
    if (find == True):
        List = [find, i, j]
    else:
        List = [find, 0, 0]
    f.close()
    return List