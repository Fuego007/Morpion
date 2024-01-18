terrain = [" "]*9
histo = []
game = True
quitour = 1
print("0|1|2")
print("3|4|5")
print("6|7|8")
def aff_ter():
    print(terrain[0],"|",terrain[1],"|",terrain[2])
    print(terrain[3],"|",terrain[4],"|",terrain[5])
    print(terrain[6],"|",terrain[7],"|",terrain[8])
def verification():
    global game,terrain
    if len(histo)== 9 :
        print("Fin de la partie !")
        game = False
    if terrain[0] == terrain[1] == terrain[2] != " ":
        if terrain[0] == "x":
            print("Joueur 1 gagne !")
        else:
            print("Joueur 2 gagne !")
        game = False
    if terrain[3] == terrain[4] == terrain[5] != " ":
        if terrain[3] == "x":
            print("Joueur 1 gagne !")
        else:
            print("Joueur 2 gagne !")
        game = False
    if terrain[6] == terrain[7] == terrain[8] != " ":
        if terrain[6] == "x":
            print("Joueur 1 gagne !")
        else:
            print("Joueur 2 gagne !")
        game = False
    if terrain[0] == terrain[4] == terrain[8] != " ":
        if terrain[0] == "x":
            print("Joueur 1 gagne !")
        else:
            print("Joueur 2 gagne !")
        game = False
    if terrain[2] == terrain[4] == terrain[6] != " ":
        if terrain[2] == "x":
            print("Joueur 1 gagne !")
        else:
            print("Joueur 2 gagne !")
        game = False
    if terrain[0] == terrain[3] == terrain[6] != " ":
        if terrain[0] == "x":
            print("Joueur 1 gagne !")
        else:
            print("Joueur 2 gagne !")
        game = False
    if terrain[1] == terrain[4] == terrain[7] != " ":
        if terrain[1] == "x":
            print("Joueur 1 gagne !")
        else:
            print("Joueur 2 gagne !")
        game = False
    if terrain[2] == terrain[5] == terrain[8] != " ":
        if terrain[2] == "x":
            print("Joueur 1 gagne !")
        else:
            print("Joueur 2 gagne !")
        game = False
while game:
    if quitour == 1:
        j1 = int(input("Joueur 1 | Que souhaite tu jouer ?"))
        if j1 not in histo:
            histo.insert(0,j1)
            terrain[j1] = "x"
        else :
            print("Impossible !")
        aff_ter()
        verification()
        quitour = 2
    else:    
        j2 = int(input("Joueur 2 | Que souhaite tu jouer ?"))
        if j2 not in histo:
            histo.insert(0,j2)
            terrain[j2] = "o"
        else :
            print("Impossible !")
        aff_ter()
        verification()
        quitour = 1

