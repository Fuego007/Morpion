from tkinter import *
texte = ""
terrain = [" "]*9
histo = []
game = True
quitour = 1

def aff_ter():
    print(terrain[0],"|",terrain[1],"|",terrain[2])
    print(terrain[3],"|",terrain[4],"|",terrain[5])
    print(terrain[6],"|",terrain[7],"|",terrain[8])
    print(" ")
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
    if game:
        if len(histo)% 2 == 0:
            label_title.config(text = " x ")
        else:
            label_title.config(text = " o ")
    label_title.pack()

def r1():
    play(1)
    if game:
        if len(histo)% 2 == 0:
            label_title1.config(text = " x ")
        else:
            label_title1.config(text = " o ")
        label_title1.pack()

def r2():
    play(2)
    if game:
        if len(histo)% 2 == 0:
            label_title2.config(text = " x ")
        else:
            label_title2.config(text = " o ")
        label_title2.pack()

def r3():
    play(3)
    if game:
        if len(histo)% 2 == 0:
            label_title3.config(text = " x ")
        else:
            label_title3.config(text = " o ")
        label_title3.pack()

def r4():
    play(4)
    if game:
        if len(histo)% 2 == 0:
            label_title4.config(text = " x ")
        else:
            label_title4.config(text = " o ")
        label_title4.pack()

def r5():
    play(5)
    if game:
        if len(histo)% 2 == 0:
            label_title5.config(text = " x ")
        else:
            label_title5.config(text = " o ")
        label_title5.pack()

def r6():
    play(6)
    if game:
        if len(histo)% 2 == 0:
            label_title6.config(text = " x ")
        else:
            label_title6.config(text = " o ")
        label_title6.pack()

def r7():
    play(7)
    if game:
        if len(histo)% 2 == 0:
            label_title7.config(text = " x ")
        else:
            label_title7.config(text = " o ")
        label_title7.pack()

def r8():
    play(8)
    if game:
        if len(histo)% 2 == 0:
            label_title8.config(text = " x ")
        else:
            label_title8.config(text = " o ")
        label_title8.pack()



#créer une fenetre
window = Tk()

window.title("Morpion")
window.geometry("500x500")
window.minsize(300,300)

#créer une boite
frame = Frame(window,bg= '#450')
frame2 = Frame(window,bg='#457')
frame3 = Frame(window,bg='#470')

label_title= Button(frame, font =("Arial",60),bg = 'black',fg = 'white',text = "   ",command =r0)
label_title1= Button(frame, font =("Arial",60),bg = 'black',fg = 'white',text = "   ",command =r1)
label_title2= Button(frame, font =("Arial",60),bg = 'black',fg = 'white',text = "   ",command =r2)


label_title3= Button(frame2, font =("Arial",60),bg = 'black',fg = 'white',text = "   ",command =r3)
label_title4= Button(frame2, font =("Arial",60),bg = 'black',fg = 'white',text = "   ",command =r4)
label_title5= Button(frame2, font =("Arial",60),bg = 'black',fg = 'white',text = "   ",command =r5)

#ajouter un bouton
label_title6= Button(frame3, font =("Arial",60),bg = 'black',fg = 'white',text = "   ",command =r6)
label_title7= Button(frame3, font =("Arial",60),bg = 'black',fg = 'white',text = "   ",command =r7)
label_title8= Button(frame3, font =("Arial",60),bg = 'black',fg = 'white',text = "   ",command =r8)


#afiicher les texte 
label_title.pack(side=LEFT,expand = YES)
label_title1.pack(side=LEFT,expand = YES)
label_title2.pack(side=LEFT,expand = YES)
label_title3.pack(side=LEFT,expand = YES)
label_title4.pack(side=LEFT,expand = YES)
label_title5.pack(side=LEFT,expand = YES)
label_title6.pack(side=LEFT,expand = YES)
label_title7.pack(side=LEFT,expand = YES)
label_title8.pack(side=LEFT,expand = YES)

#ajouter la boite
frame.pack(side = TOP,expand=YES)
frame2.pack(expand=YES)
frame3.pack(side  = BOTTOM,expand=YES)

#afficher la fenetre
window.mainloop()
