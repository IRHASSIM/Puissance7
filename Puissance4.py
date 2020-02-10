grille=[[0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0]]
import random

def grille_vide():
    return [[0 for j in range(7)] for i in range(6)]
grille_vide()     
assert len(grille_vide())==6
assert len(grille_vide()[0])==7 

def affiche(gril):
    n=6
    print("  0 1 2 3 4 5 6")
    for i in gril:
        print(n,end="")
        n=n-1
        for j in i:
            if j==0:
                print ("|.",end="")
            if j==1:
                print("|x",end="")
            if j==2:
                print("|O",end="")
        print("|")
                

def coup_possible(gril,col):   
    if gril[0][col]==0:
        return True
    else:
        return False
assert coup_possible(grille_vide(),2)==True

def jouer(gril,j,col):
    if gril[5][col]==0:
        gril[5][col]=j
    elif gril[4][col]==0:
        gril[4][col]=j
    elif gril[3][col]==0:
        gril[3][col]=j
    elif gril[2][col]==0:
        gril[2][col]=j
    elif gril[1][col]==0:
        gril[1][col]=j
    elif gril[0][col]==0:
        gril[0][col]=j
    return gril

def horiz(gril,j,lig):
    if gril[lig][0]==j and gril[lig][1]==j and gril[lig][2]==j and gril[lig][3]==j:
        return True
    if gril[lig][1]==j and gril[lig][2]==j and gril[lig][3]==j and gril[lig][4]==j:
        return True
    if gril[lig][2]==j and gril[lig][3]==j and gril[lig][4]==j and gril[lig][5]==j:
        return True
    if gril[lig][3]==j and gril[lig][4]==j and gril[lig][5]==j and gril[lig][6]==j:
        return True

def vert(gril,j,col):
    if gril[5][col]==j and gril[4][col]==j and gril[3][col]==j and gril[2][col]:
        return True
    if gril[4][col]==j and gril[3][col]==j and gril[2][col]==j and gril[1][col]:
        return True
    if gril[3][col]==j and gril[2][col]==j and gril[1][col]==j and gril[0][col]:
        return True

def victoire():
    while vert==False or horiz==False or diag_bas==False or diag_haut== False:
        return False
    return True

def match_nul(gril):
    if gril[0][0]!=0 and gril[0][1]!=0 and gril[0][2]!=0 and gril[0][3]!=0 and gril[0][4]!=0 and gril[0][5]!=0 and gril[0][6]!=0:
        return True
    return False

def coup_aléatoire(gril,j):
    a=random.randint(0,6)
    if gril[5][a]==0:
        gril[5][a]=j
    elif gril[4][a]==0:
        gril[4][a]=j
    elif gril[3][a]==0:
        gril[3][a]=j
    elif gril[2][a]==0:
        gril[2][a]=j
    elif gril[1][a]==0:
        gril[1][a]=j
    elif gril[0][a]==0:
        gril[0][a]=j
    return gril
