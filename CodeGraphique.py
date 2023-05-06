import turtle as trt
import operator as op

largeur = 5
hauteur = 4*largeur
nextSymb = 2
debutX = -275
debutY = 200
maxLigne = 10
ligneHauteY = debutY + hauteur + largeur
TailleMaxMessage = 100


def genMatrice(texte):
    txt = list(map(ord, texte))
    matrice = []
    for i in range(len(txt)) :
        matrice.append([])
        charBin =  bin(txt[i]) [2::]
        for j in charBin :
            matrice[i].append(j)
    return matrice

def faireForme(height, width, t, fill):
    x, y = t.pos()
    if (fill):
        t.begin_fill()
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    if (fill):
        t.end_fill()
    t.right(90)

    t.penup()
    t.goto(x + largeur + nextSymb, y)    
    t.pendown()

def genLettre(l, t):
    position = 7
    k = l [::-1]
    for j in reversed(range(7)):
        if j >= len(l):
            if position > 4:
                faireForme(hauteur, largeur, t, False)
            else :
                faireForme(largeur, largeur, t, False)
        else :
            if k[j] == "1" :
                if position > 4:
                    faireForme(hauteur, largeur, t, True)
                else :
                    faireForme((hauteur/2), largeur, t, True)
            else :
                if position > 4:
                    faireForme(hauteur, largeur, t, False)
                else :
                    faireForme(largeur, largeur, t, False)
        
        position = position - 1

    if (op.countOf(l, '1')%2 == 0):
        faireForme((hauteur/2), largeur, t, True)
    else :
        faireForme((hauteur/2), largeur, t, False)
    
    x, y = t.pos()
    t.penup()
    t.goto(x + largeur - nextSymb, y)
    t.pendown()
    return x, y

def genCode(texte):
    matrice = genMatrice(texte)
    print(matrice)
    t = trt.Turtle()
    t.speed(0)
    t.penup()
    t.goto(debutX - largeur, ligneHauteY)
    t.pendown()
    t.left(90)
    t.hideturtle()

    #ligne horizontale haute
    limiteDroite = min (maxLigne, len(matrice))*(8*largeur + 7*nextSymb + largeur) + largeur
    t.penup()
    t.goto(debutX - largeur, ligneHauteY)
    t.pendown()
    faireForme(largeur, limiteDroite, t, True)
    
    #ligne verticale gauche
    t.penup()
    t.goto(debutX - largeur, ligneHauteY)
    t.pendown()
    faireForme(largeur, -largeur, t, False)
    t.penup()
    _, y = t.pos()
    t.goto(debutX- largeur, y - largeur)
    t.pendown()

    if len(matrice) <= maxLigne :
        r = 7
        limiteHaute = (hauteur + largeur) + 3*largeur
    else :
        if (len(matrice) % maxLigne) == 0 :
            limiteHaute = ((len(matrice) // maxLigne)) * (hauteur + largeur) + 3*largeur
            r = (len(matrice) // maxLigne)*5 + 2
        else :
            limiteHaute = ((len(matrice) // maxLigne) + 1) * (hauteur + largeur) + 3*largeur
            r = ((len(matrice) // maxLigne)+1)*5 + 2
    taille = bin(len(matrice))[2::][::-1]
    print(taille)
    for i in range(r):
        #Pour spécifier la taille sur la gauche
        if i<len(taille):
            if taille[i]=='1':
                faireForme(largeur, -largeur, t, True)
            else :
                faireForme(largeur, -largeur, t, False)
        else :
            faireForme(largeur, -largeur, t, False)
        t.penup()
        _, y = t.pos()
        t.goto(debutX- largeur, y - largeur)
        t.pendown()


    t.penup()
    t.goto(debutX, debutY)
    t.pendown()
    
    compteur = 0
    nbLigne = 0
    for i in matrice :
        x, y = genLettre(i, t)
        compteur = compteur + 1
        if compteur >= maxLigne:
            t.penup()
            t.goto(debutX, y - hauteur - largeur)
            t.pendown()
            compteur = 0
            nbLigne = nbLigne + 1

    #On complète la dernière ligne pour ne pas qu'elle soit vide
    if (maxLigne < len(matrice) and (compteur != 0)):
        for i in range(maxLigne - compteur) :
            for j in range(8):
                x, y = t.pos()
                if j < 3:
                    faireForme(hauteur, largeur, t, False)
                else :
                    faireForme((hauteur/2), largeur, t, False)
                t.penup()
                t.goto(x + largeur + nextSymb, y)    
                t.pendown()
            t.penup()
            t.goto(x + 2*largeur, y)
            t.pendown()

    #ligne horizontale basse
    t.penup()
    t.goto(debutX - largeur, y - 2*largeur)
    t.pendown()
    faireForme(largeur, limiteDroite, t, False)
    
    #ligne verticale droite

    t.penup()
    t.goto(debutX + limiteDroite - largeur, y - 2*largeur)
    t.pendown()
    faireForme(limiteHaute, largeur, t, False)

    return

def generation():
    texte = input("Bienvenu. Quel texte voulez-vous transformer en code ?\n")
    if (len(texte) > TailleMaxMessage):
        print("message trop long")
        return
    elif (len(texte) < 1):
        print("le message doit contenir au moins 1 caractère")
        return
    genCode(texte)
    return

generation()
trt.done()