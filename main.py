#!/usr/bin/python
def mainfunc(group):
    for x in range(group):
        nombre = int(input("Introduire le nombre des étudiants : "))
        path = str("Introduire ou vous voulez sauvegarder les informations : ")
        for i in range(nombre):
            id = input("ID : ")
            nom = input("Nom : ")
            prenom = input("Prenom : ")
            Aff = input("Aff : ")
            Moy = input("Moyenne : ")
            f = open(path, "a")
            f.write(
                "ID : " + id + "| Name : " + nom + "| Last Name : " + prenom + "| Aff :" + Aff + "| Moy :" + Moy + "\n")
            f.close()


def new():
    filename = input("Please Introduce the file name : ")
    try:
        with open('C:/Users/feth-/Desktop\Data/'+filename+'.txt' , 'w') as f:
            f.write('Create a new text file!')
    except FileNotFoundError:
        print("The 'docs' directory does not exist")

def choose():
    print("Welcome to My program :) ")
    print(
        "Choose an option : \n 1-Creating a new file \n 2-Adding New Students \n 3-Removing a student \n 4-Removing "
        "entire file ")
    a = int(input("--> : "))
    return a

def remove():
    ttr = input("Please give the group of the student : ")
    idstu = input("Please give the ID : ")
    with open('C:/Users/feth-/Desktop\Data/'+ttr+'.txt', "r") as f:
        lines = f.readlines()
    with open('C:/Users/feth-/Desktop\Data/'+ttr+'.txt', "w") as f:
        for line in lines:
            if line.strip("\n") != "ID : "+idstu+":
                f.write(line)

def switch(choose):
    if choose == 1:
        new()
    elif choose == 2:
        mainfunc(group)
    elif choose == 3:
        return "You can become a Data Scientist"
    elif choose == 4:




choose()
group = int(input("Veuillez introduire le nombre de groupe : "))
mainfunc(group)
