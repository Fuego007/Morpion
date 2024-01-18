from tkinter import *
texte = ""
terrain = [" "]*9
histo = []
game = True
quitour = 1

#==================================================================================================================================================
#=====================================Partie 1 fonctions et jeu===============================================================================================
#==================================================================================================================================================
def aff_ter():
    print(terrain[0],"|",terrain[1],"|",terrain[2])
    print(terrain[3],"|",terrain[4],"|",terrain[5])
    print(terrain[6],"|",terrain[7],"|",terrain[8])
    print(" ")
def verification():
    global game,terrain
    if len(histo)== 9 :
        textes.config(text = "Grille pleine fin de la partie !")
        game = False
    if terrain[0] == terrain[1] == terrain[2] != " ":
        if terrain[0] == "x":
            textes.config(text = "Joueur 1 gagne !")
        else:
            textes.config(text = "Joueur 2 gagne !")
        game = False
    if terrain[3] == terrain[4] == terrain[5] != " ":
        if terrain[3] == "x":
            textes.config(text = "Joueur 1 gagne !")
        else:
            textes.config(text = "Joueur 2 gagne !")
        game = False
    if terrain[6] == terrain[7] == terrain[8] != " ":
        if terrain[6] == "x":
            textes.config(text = "Joueur 1 gagne !")
        else:
            textes.config(text = "Joueur 2 gagne !")
        game = False
    if terrain[0] == terrain[4] == terrain[8] != " ":
        if terrain[0] == "x":
            textes.config(text = "Joueur 1 gagne !")
        else:
            textes.config(text = "Joueur 2 gagne !")
        game = False
    if terrain[2] == terrain[4] == terrain[6] != " ":
        if terrain[2] == "x":
            textes.config(text = "Joueur 1 gagne !")
        else:
            textes.config(text = "Joueur 2 gagne !")
        game = False
    if terrain[0] == terrain[3] == terrain[6] != " ":
        if terrain[0] == "x":
            textes.config(text = "Joueur 1 gagne !")
        else:
            textes.config(text = "Joueur 2 gagne !")
        game = False
    if terrain[1] == terrain[4] == terrain[7] != " ":
        if terrain[1] == "x":
            textes.config(text = "Joueur 1 gagne !")
        else:
            textes.config(text = "Joueur 2 gagne !")
        game = False
    if terrain[2] == terrain[5] == terrain[8] != " ":
        if terrain[2] == "x":
            textes.config(text = "Joueur 1 gagne !")
        else:
            textes.config(text = "Joueur 2 gagne !")
        game = False


def play(were =0):
    global quitour,j1,j2,histo,terrain,game,texte
    if game:
        if quitour == 1:
            if were not in histo:
                histo.insert(0,were)
                terrain[were] = "x"
                texte = " x "
                
            else :
                print("Impossible !")
            aff_ter()
            verification()
            quitour = 2
        else:    
            if were not in histo:
                histo.insert(0,were)
                terrain[were] = "o"
                texte = " o "
            else :
                print("Impossible !")
            aff_ter()
            verification()
            quitour = 1

def r0():
    play(0)
    if game and 0 not in histo:
        if len(histo)% 2 == 0:
            label_title.config(text = " X ")
        else:
            label_title.config(text = " O ")
    label_title.pack()

def r1():
    play(1)
    if game and 1 not in histo:
        if len(histo)% 2 == 0:
            label_title1.config(text = " X ")
        else:
            label_title1.config(text = " O ")
        label_title1.pack()

def r2():
    play(2)
    if game and 2 not in histo:
        if len(histo)% 2 == 0:
            label_title2.config(text = " X ")
        else:
            label_title2.config(text = " O ")
        label_title2.pack()

def r3():
    play(3)
    if game and 3 not in histo:
        if len(histo)% 2 == 0:
            label_title3.config(text = " X ")
        else:
            label_title3.config(text = " O ")
        label_title3.pack()

def r4():
    play(4)
    if game and 4 not in histo:
        if len(histo)% 2 == 0:
            label_title4.config(text = " X ")
        else:
            label_title4.config(text = " O ")
        label_title4.pack()

def r5():
    play(5)
    if game and 5 not in histo:
        if len(histo)% 2 == 0:
            label_title5.config(text = " X ")
        else:
            label_title5.config(text = " O ")
        label_title5.pack()

def r6():
    play(6)
    if game and 6 not in histo:
        if len(histo)% 2 == 0:
            label_title6.config(text = " X ")
        else:
            label_title6.config(text = " O ")
        label_title6.pack()

def r7():
    play(7)
    if game and 7 not in histo:
        if len(histo)% 2 == 0:
            label_title7.config(text = " X ")
        else:
            label_title7.config(text = " O ")
        label_title7.pack()

def r8():
    play(8)
    if game and 8 not in histo:
        if len(histo)% 2 == 0:
            label_title8.config(text = " X ")
        else:
            label_title8.config(text = " O ")
        label_title8.pack()


#==================================================================================================================================================
#=====================================Partie 2 Graphique===============================================================================================
#==================================================================================================================================================
#créer une fenetre
window = Tk()
window.title("Morpion")
window.geometry("500x400")
window.minsize(300,300)
window.iconbitmap = ('C:\\Users\\g.devillerussi\\Desktop\\Maison\\Morpion toutes les versions\\morpion.ico')


#création des boites
frame =  Frame(window,bg='#450')
frame2 = Frame(window,bg='#457')
frame3 = Frame(window,bg='#470')
frame4 = Frame(window,bg='#457')
#ajout des bouttons

label_title= Button(frame, font =("Arial",30),width=4, height=2,bg = 'black',fg = 'white',text = "   ",command =r0)
label_title1= Button(frame, font =("Arial",30),width=4, height=2,bg = 'black',fg = 'white',text = "   ",command =r1)
label_title2= Button(frame, font =("Arial",30),width=4, height=2,bg = 'black',fg = 'white',text = "   ",command =r2)


label_title3= Button(frame2, font =("Arial",30),width=4, height=2,bg = 'black',fg = 'white',text = "   ",command =r3)
label_title4= Button(frame2, font =("Arial",30),width=4, height=2,bg = 'black',fg = 'white',text = "   ",command =r4)
label_title5= Button(frame2, font =("Arial",30),width=4, height=2,bg = 'black',fg = 'white',text = "   ",command =r5)


label_title6= Button(frame3, font =("Arial",30),width=4, height=2,bg = 'black',fg = 'white',text = "   ",command =r6)
label_title7= Button(frame3, font =("Arial",30),width=4, height=2,bg = 'black',fg = 'white',text = "   ",command =r7)
label_title8= Button(frame3, font =("Arial",30),width=4, height=2,bg = 'black',fg = 'white',text = "   ",command =r8)

#ajout d'un texte
textes = Label(frame4,font =("Arial",20),fg = 'black',text = 'Cliquer sur les cases pour jouer')


#aficher les bouttons 
label_title.pack(side=LEFT,expand = YES)
label_title1.pack(side=LEFT,expand = YES)
label_title2.pack(side=LEFT,expand = YES)
label_title3.pack(side=LEFT,expand = YES)
label_title4.pack(side=LEFT,expand = YES)
label_title5.pack(side=LEFT,expand = YES)
label_title6.pack(side=LEFT,expand = YES)
label_title7.pack(side=LEFT,expand = YES)
label_title8.pack(side=LEFT,expand = YES)
#afficher le texte
textes.pack()

#ajouter les boites
frame.pack(side = TOP,expand=YES)
frame2.pack(expand=YES)
frame4.pack(side  = BOTTOM,expand=YES)
frame3.pack(side  = BOTTOM,expand=YES)


#afficher la fenetre
window.mainloop()
