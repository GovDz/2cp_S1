#EXTRA WORK
def eq():
    f = input("Please enter the file name")
    fn = open(f, "wb")
    buf = lireBloc(fn, n)
    buf2 = lireBloc(fn, m)
    q = abs(buf:NB - buf2:NB) / 2
    if q>=2:
        if buf:NB - buf2:NB:
        j = buf2:NB
        while j>=1:
            buf:tab[j+q] = buf:tab[j]
            j = j - 1
        for j in range(q):
            buf:tab[j] = buf1:tab[buf1:NB-q+j]
        buf:NB = buf:NB-q
        buf2:NB = buf2:NB + q
    else:
        for j in range(q):
            buf:tab[buf1.NB+j] = buf2:tab[j]
        for j in range(q+1, buf2:NB):
            buf2:tab[j-q] = buf2:tab[j]
        buf1:NB = buf:NB + q
        buf2:NB = buf.NB - q
ecrireBloc(fn, n , buf)
ecrireBloc(fn, m , buf2)
fermer(fn)
return





