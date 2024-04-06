# Créé par trousseh, le 09/12/2022 en Python 3.7
import random
import time
hub=1 #designe le hub principale
score_human=0 #le score total du joueur
score_bot=0 #score total du bot
titre="""
  _    _                     _                            _
 | |  | |                   | |                          | |
 | |__| |_   _  __ _  ___   | |     __ _ _   _ _ __   ___| |__   ___ _ __
 |  __  | | | |/ _` |/ _ \  | |    / _` | | | | '_ \ / __| '_ \ / _ \ '__|
 | |  | | |_| | (_| | (_) | | |___| (_| | |_| | | | | (__| | | |  __/ |
 |_|  |_|\__,_|\__, |\___/  |______\__,_|\__,_|_| |_|\___|_| |_|\___|_|
                __/ |
               |___/
                                                                """ #Le titre principale

print(titre)
time.sleep(2) #Attends 2sec avant d'afficher la suite
print('→ Bonjour, bienvenue sur le Hugo Luncher, ici se trouve différents jeux auquel vous pouvez jouer.')
time.sleep(4)
while hub==1: #tant que la variable hub est égale à 1 on continue de jouer
    jeu=int(input('→ À quel jeu voulez-vous jouer ? Tapez 1-le Morpion, 2-le Pierre, Feuille, Ciseaux, 3-le C+C-, 4-le Jeu de Nim et 5-arrêter de jouer ─>')) #Donne le choix du jeu
    if jeu==1: #si l'utilisateur tape 1 il renvoie le jeu Morpion
        titre1="""
     __  __                  _
    |  \/  |                (_)
    | \  / | ___  _ __ _ __  _  ___  _ __
    | |\/| |/ _ \| '__| '_ \| |/ _ \| '_ \ 
    | |  | | (_) | |  | |_) | | (_) | | | |
    |_|  |_|\___/|_|  | .__/|_|\___/|_| |_|
                      | |
                      |_|                    """
        print(titre1)
        time.sleep(2)
        print('Bienvenue sur le jeu du Morpion')
        time.sleep(2)
        regle1=input('Connaissez-vous les règles du Morpion ? (Oui/Non)') #demande à l'utilisateur si il connaît les règles du jeu
        if regle1=='Non' or regle1=='non' or regle1=='N' or regle1=='n': #si il ne connaît pas les règles le programme renvoie les règles du jeu puis le jeu
            print('•----------------------------------------------------------------------------•')
            time.sleep(2)
            print('•Les règles sont simples:')                                                          #Les Règles du Morpion
            time.sleep(2)
            print('•Le jeu se joue à deux')
            time.sleep(2)
            print('•Il y a un plateau constitué de 9 cases')
            time.sleep(2)
            print('•Le premier des deux joueurs à former\nune suite de 3 cases verticale, horizontale, ou diagonale remporte la partie')
            time.sleep(2)
            print('•----------------------------------------------------------------------------•')
            game1=1
            while game1==1:
                def afficher_grille(p, gagnant=None):                           #AFFICHAGE DE LA GRILLE DE JEU
                    print(" " + p[0] + " | " + p[1] + " | " + p[2] + " ")
                    print("---+---+---")
                    print(" " + p[3] + " | " + p[4] + " | " + p[5] + " ")
                    print("---+---+---")
                    print(" " + p[6] + " | " + p[7] + " | " + p[8] + " ")


                def tour(grille, joueur):                                       #Tour des deux joueurs
                    print("C'est le tour du joueur "+str(joueur))
                    colonne=input("Entrez le numéro de la colonne (0,1,ou 2) : ")
                    ligne=input("Entrez le numero de la ligne (0,1,ou 2): ")
                    print("Vous avez joué la case ("+colonne+","+ligne+")")

                    while grille[int(colonne)+int(ligne)*3]!=" ":
                        afficher_grille(grille)
                        print("Cette case est deja jouée ! Saisissez une autre case svp !")
                        colonne=input("Entrez le numéro de la colonne (0,1,ou 2) : ")
                        ligne=input("Entrez le numero de la ligne (0,1,ou 2): ")
                        print("Vous avez joué la case ("+colonne+","+ligne+")")

                    if joueur==1 :   #Le joueur 1 possède le symbole X et le joueur 2 possède le symbole O
                        grille[int(colonne)+int(ligne)*3]="X"
                    if joueur==2 :
                        grille[int(colonne)+int(ligne)*3]="O"
                    afficher_grille(grille)

                def est_gagnant(grille):   #Toutes les possibilités gagnantes
                    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
                        return 1
                    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=" "):
                        return 1
                    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=" "):
                        return 1
                    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=" "):
                        return 1
                    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=" "):
                        return 1
                    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]!=" "):
                        return 1
                    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=" "):
                        return 1
                    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=" "):
                        return 1

                def est_match_nul(grille):  #Si les neufs cases sont remplies alors il y a match nul
                    for i in range(9):
                        if grille[i]==" ":
                            return 0
                    return 1

                joueur=1
                print("Joueur 1 ─> X Et Joueur 2 ─> O")
                grille=[" "," "," "," "," "," "," "," "," "]
                afficher_grille(grille)
                gagne=0
                while gagne==0:
                        tour(grille,joueur)
                        if est_gagnant(grille):
                            print("Félicitation, le joueur "+str(joueur)+" remporte la partie !")
                            gagne=1

                        else:
                            if est_match_nul(grille):
                                print("Match nul !")
                                gagne=1
                        if joueur==1:
                            joueur=2
                        else:
                            joueur=1
                new1=input('Voulez vous rejouer ? (Oui/Non)─>') #Pose la question "voulez-vous rejouer ?"
                if new1=='Oui' or new1=='oui' or new1=='O' or new1=='o': #si oui alors on continue
                    print("On continue")
                    game1=1
                if new1=='Non' or new1=='non' or new1=='N' or new1=='n': #sinon on soustrait 1 à la variable game1 ce qui à pour effet de mettre fin au jeu
                    game1=game1-1
        if regle1=='Oui' or regle1=='oui' or regle1=='O' or regle1=='o': #En revanche, si il connaît les règles le programme renvoie juste le jeu
            game1=1
            while game1==1:
                def afficher_grille(p, gagnant=None):     #AFFICHAGE DE LA GRILLE DE JEU
                    print(" " + p[0] + " | " + p[1] + " | " + p[2] + " ")
                    print("---+---+---")
                    print(" " + p[3] + " | " + p[4] + " | " + p[5] + " ")
                    print("---+---+---")
                    print(" " + p[6] + " | " + p[7] + " | " + p[8] + " ")


                def tour(grille, joueur):                 #Tour des deux joueurs
                    print("C'est le tour du joueur "+str(joueur))
                    colonne=input("Entrez le numéro de la colonne (0,1,ou 2) : ")
                    ligne=input("Entrez le numero de la ligne (0,1,ou 2): ")
                    print("Vous avez joué la case ("+colonne+","+ligne+")")

                    while grille[int(colonne)+int(ligne)*3]!=" ":
                        afficher_grille(grille)
                        print("Cette case est deja jouée ! Saisissez une autre case svp !")
                        colonne=input("Entrez le numéro de la colonne (0,1,ou 2) : ")
                        ligne=input("Entrez le numero de la ligne (0,1,ou 2): ")
                        print("Vous avez joué la case ("+colonne+","+ligne+")")

                    if joueur==1 :  #Le joueur 1 possède le symbole X et le joueur 2 possède le symbole O
                        grille[int(colonne)+int(ligne)*3]="X"
                    if joueur==2 :
                        grille[int(colonne)+int(ligne)*3]="O"
                    afficher_grille(grille)

                def est_gagnant(grille): #Toutes les possibilités gagnantes
                    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
                        return 1
                    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=" "):
                        return 1
                    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=" "):
                        return 1
                    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=" "):
                        return 1
                    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=" "):
                        return 1
                    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]!=" "):
                        return 1
                    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=" "):
                        return 1
                    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=" "):
                        return 1

                def est_match_nul(grille): #Si les neufs cases sont remplies alors il y a match nul
                    for i in range(9):
                        if grille[i]==" ":
                            return 0
                    return 1

                joueur=1
                print("Joueur 1 ─> X Et Joueur 2 ─> O")
                grille=[" "," "," "," "," "," "," "," "," "]
                afficher_grille(grille)
                gagne=0
                while gagne==0:
                        tour(grille,joueur)
                        if est_gagnant(grille):
                            print("Félicitation, le joueur "+str(joueur)+" remporte la partie !")
                            gagne=1

                        else:
                            if est_match_nul(grille):
                                print("Match nul !")
                                gagne=1
                        if joueur==1:
                            joueur=2
                        else:
                            joueur=1
                new1=input('Voulez vous rejouer ? (Oui/Non)─>') #Pose la question "voulez-vous rejouer ?"
                if new1=='Oui' or new1=='oui' or new1=='O' or new1=='o': #si oui alors on continue
                    print("On continue")
                    game1=1
                if new1=='Non' or new1=='non' or new1=='N' or new1=='n': #sinon on soustrait 1 à la variable game1 ce qui à pour effet de mettre fin au jeu
                    game1=game1-1
    if jeu==2: #si l'utilisateur tape 2 alors le programme renvoie le jeu Pierre , Feuille, Ciseau
        titre2="""
         _____ _                        ______         _ _ _           _____ _
        |  __ (_)                      |  ____|       (_) | |         / ____(_)
        | |__)  | ___ _ __ _ __ ___    | |__ ___ _   _ _| | | ___    | |     _ ___  ___  __ _ _   _
        |  ___/ |/ _ \ '__| '__/ _ \   |  __/ _ \ | | | | | |/ _ \   | |    | / __|/ _ \/ _` | | | \ 
        | |   | |  __/ |  | | |  __/   | | |  __/ |_| | | | |  __/   | |____| \__ \  __/ (_| | |_| |
        |_|   |_|\___|_|  |_|  \___    |_|  \___|\__,_|_|_|_|\___     \_____|_|___/\___|\__,_|\__,_/
                                                                                                    """
        print(titre2)
        time.sleep(2)
        print('Bienvenue sur le jeu du Pierre, Feuille, Ciseaux')
        time.sleep(2)
        regle2=input('Connaissez-vous les règles du Pierre, Feuille, Ciseaux ? (Oui/Non)') #demande à l'utilisateur si il connaît les règles du jeu
        if regle2=='Non' or regle2=='non' or regle2=='N' or regle2=='n':#si il ne connaît pas les règles le programme renvoie les règles du jeu puis le jeu
            possiblite = ['p','f','c'] #liste des choix disponibles
            print('•-----------------------------------------------------------------------------------------------•')
            time.sleep(2)
            print('•Règles: Il vous suffit de choisir entre la pierre, la feuile ou le ciseaux')                            #Les règles du pierre, feuille, ciseau
            time.sleep(2)
            print('•Les symboles forment un trio :\n•la pierre écrase le ciseaux qui lui même coupe la feuille qui lui même recouvre la pierre ')
            time.sleep(2)
            print('•-----------------------------------------------------------------------------------------------•')
            time.sleep(2)
            game2=1
            while game2==1:
                ordi = random.choice(possiblite) #l'ordinateur choisi dans la liste nommé "posibilite" pierre, feuille, ciseaux
                j1=input('Choissisez entre "p" la pierre, "f" la feuille, ou "c" le ciseau')
                if(j1==ordi): #si l'ordi à le même symbole que vous alors il renvoie "égalité"
                    time.sleep(2)
                    print('égalité vous avez le même symbole que le bot')
                else:
                    if(j1 == 'p' and ordi == 'f'):
                        time.sleep(2)
                        print('Vous avez perdu ! Le bot avait choisi la feuille qui recouvre donc la', j1)
                        score_bot=score_bot+1
                    elif(j1 == 'f' and ordi == 'p'):
                        time.sleep(2)
                        print('Vous avez gagné ! La feuille recouvre la',ordi)
                        score_human=score_human+1
                    elif(j1 == 'c' and ordi == 'p'):
                        time.sleep(2)
                        print('Vous avez perdu ! Le bot avait choisi la pierre qui écrase le',j1)
                        score_bot=score_bot+1
                    elif(j1 == 'p' and ordi == 'c'):
                        time.sleep(2)
                        print('Vous avez gagné ! La pierre écrase le',ordi)
                        score_human=score_human+1
                    elif(j1 == 'c' and ordi == 'f'):
                        time.sleep(2)
                        print('Vous avez gagné ! Le ciseaux coupe la',ordi)
                        score_human=score_human+1
                    elif(j1 == 'f' and ordi == 'c'):
                        time.sleep(2)
                        print('Vous avez perdu ! Le bot avait choisi le ciseaux coupe donc la',j1)
                        score_bot=score_bot+1


                new2 = input('Voulez vous rejouer ? (Oui/Non)─>') #Pose la question "voulez-vous rejouer ?"
                if new2=='Oui' or new2=='oui' or new2=='O' or new2=='o':  #si oui alors on continue
                    print("Let's GO")
                    game2=1
                if new2=='Non' or new2=='non' or new2=='N' or new2=='n': #sinon on soustrait 1 à la variable game2 ce qui à pour effet de mettre fin au jeu
                    game2=game2-1
        if regle2=='Oui' or regle2=='oui' or regle2=='O' or regle2=='o': #En revanche, si il connaît les règles le programme renvoie juste le jeu
            possiblite = ['p','f','c'] #liste des choix disponibles
            game2=1
            while game2==1:
                ordi = random.choice(possiblite) #l'ordinateur choisi dans la liste nommé "posibilite" pierre, feuille, ciseaux
                j1=input('Choissisez entre "p" la pierre, "f" la feuille, ou "c" le ciseau')
                if(j1==ordi):
                    print('égalité vous avez le même symbole que le bot')
                else:
                    if(j1 == 'p' and ordi == 'f'):
                        time.sleep(2)
                        print('Vous avez perdu ! Le bot avait choisi la feuille qui recouvre donc la', j1)
                        score_bot=score_bot+1
                    elif(j1 == 'f' and ordi == 'p'):
                        time.sleep(2)
                        print('Vous avez gagné ! La feuille recouvre la',ordi)
                        score_human=score_human+1
                    elif(j1 == 'c' and ordi == 'p'):
                        time.sleep(2)
                        print('Vous avez perdu ! Le bot avait choisi la pierre qui écrase le',j1)
                        score_bot=score_bot+1
                    elif(j1 == 'p' and ordi == 'c'):
                        time.sleep(2)
                        print('Vous avez gagné ! La pierre écrase le',ordi)
                        score_human=score_human+1
                    elif(j1 == 'c' and ordi == 'f'):
                        time.sleep(2)
                        print('Vous avez gagné ! Le ciseaux coupe la',ordi)
                        score_human=score_human+1
                    elif(j1 == 'f' and ordi == 'c'):
                        time.sleep(2)
                        print('Vous avez perdu ! Le bot avait choisi le ciseaux coupe donc la',j1)
                        score_bot=score_bot+1


                new2 = input('Voulez vous rejouer ? (Oui/Non)─>') #Pose la question "voulez-vous rejouer ?"
                if new2=='Oui' or new2=='oui' or new2=='O' or new2=='o': #si oui alors on continue
                    print("Let's GO")
                    game2=1
                if new2=='Non' or new2=='non' or new2=='N' or new2=='n': #sinon on soustrait 1 à la variable game2 ce qui à pour effet de mettre fin au jeu
                    game2=game2-1
    if jeu==3: #si l'utilisateur tape 3 alors le programme revoie Le C+ C-
        import random as rd
        titre3="""
          _____            _____
         / ____|    _     / ____|
        | |       _| |_  | |       ______
        | |      |_   _| | |      |______|
        | |____    |_|   | |____
         \_____|          \_____|
                                            """
        print(titre3)
        time.sleep(2)
        print('Bienvenue sur le jeu du C\'est plus C\'est moins')
        time.sleep(2)
        regle3=input('Connaissez-vous les règles du C\'est plus C\'est moins ? (Oui/Non)') #demande à l'utilisateur si il connaît les règles du jeu
        if regle3=='Non' or regle3=='non' or regle3=='N' or regle3=='n':  #si il ne connaît pas les règles le programme renvoie les règles du jeu puis le jeu
            print("•-----------------------------------------------------------------------------------------------------------------•")
            time.sleep(2)
            print("•Le principe est simple: L'odinateur choisi un nombre entre 1 et 99.")                                           #Les règles du C+ C-
            time.sleep(2)
            print("•Votre but: devinez le nombre que le bot à choisi en proposant des nombre")
            time.sleep(2)
            print("•Ensuite, le bot vous indiquera si le nombre à trouver est plus grand ou plus petit que ce que vous allez proposer")
            time.sleep(2)
            print("Pour finir, vous avez seulement 6 éssais pour devinez le nombre")
            time.sleep(2)
            print("•-----------------------------------------------------------------------------------------------------------------•")
            time.sleep(2)
            print('Le bot à choisi son nombre à vous de le devinez')
            game3=1
            while game3==1:
                a = rd.randint(1,99)
                u=0
                e=1
                while u!=a:
                    e=e+1
                    u=int(input("Tapez un nombre entier :"))
                    if e==6:
                        print('Vous n\'avez pas réussi à trouver le nombre en 6 éssais')
                        score_bot=score_bot+1
                        new3=input('Voulez vous rejouer ? (Oui/Non)─>') #Pose la question "voulez-vous rejouer ?"
                        if new3=='Oui' or new3=='oui' or new3=='O' or new3=='o': #si oui alors on continue
                            print("Let's GO")
                            game3=1
                        if new3=='Non' or new3=='non' or new3=='N' or new3=='n': #sinon on soustrait 1 à la variable game3 ce qui à pour effet de mettre fin au jeu
                            print('Dommage')
                            game3=game3-1
                    if u > a :
                        print("c'est moins\n\n")
                    elif u < a:
                        print("c'est plus\n\n")
                    if u==a :
                        print('Félicitation, vous avez trouvé le nombre')
                        score_human=score_human+1
                        new3=input('Voulez vous rejouer ? (Oui/Non)─>') #Pose la question "voulez-vous rejouer ?"
                        if new3=='Oui' or new3=='oui' or new3=='O' or new3=='o': #si oui alors on continue
                            print("Let's GO")
                            game3=1
                        if new3=='Non' or new3=='non' or new3=='N' or new3=='n': #sinon on soustrait 1 à la variable game3 ce qui à pour effet de mettre fin au jeu
                            print('Dommage')
                            game3=game3-1
        if regle3=='Oui' or regle3=='oui' or regle3=='O' or regle3=='o':        #En revanche, si il connaît les règles le programme renvoie juste le jeu
            game3=1
            while game3==1:
                a = rd.randint(1,99)
                u=0
                e=0
                while u!=a:
                    e=e+1
                    u=int(input("Tapez un nombre entier :"))
                    if e==6:
                        print('Vous n\'avez pas réussi à trouver le nombre en 6 éssais')
                        score_bot=score_bot+1
                        new3=input('Voulez vous rejouer ? (Oui/Non)─>') #Pose la question "voulez-vous rejouer ?"
                        if new3=='Oui' or new3=='oui' or new3=='O' or new3=='o': #si oui alors on continue
                            print("Let's GO")
                            game3=1
                        if new3=='Non' or new3=='non' or new3=='N' or new3=='n': #sinon on soustrait 1 à la variable game3 ce qui à pour effet de mettre fin au jeu
                            print('Dommage')
                            game3=game3-1
                    if u > a :
                        print("c'est moins\n\n")
                    elif u < a:
                        print("c'est plus\n\n")
                    if u==a :
                        print('Félicitation, vous avez trouvé le nombre')
                        score_human=score_human+1
                        new3=input('Voulez vous rejouer ? (Oui/Non)─>') #Pose la question "voulez-vous rejouer ?"
                        if new3=='Oui' or new3=='oui' or new3=='O' or new3=='o': #si oui alors on continue
                            print("Let's GO")
                            game3=1
                        if new3=='Non' or new3=='non' or new3=='N' or new3=='n': #sinon on soustrait 1 à la variable game3 ce qui à pour effet de mettre fin au jeu
                            print('Dommage')
                            game3=game3-1
    if jeu==4: #si l'utilisateur tape 4 alors le programme revoie le Jeu de Nim
        titre4="""
              _                  _        _   _ _
             | |                | |      | \ | (_)
             | | ___ _   _    __| | ___  |  \| |_ _ __ ___
         _   | |/ _ \ | | |  / _` |/ _ \ | . ` | | '_ ` _ \ 
        | |__| |  __/ |_| | | (_| |  __/ | |\  | | | | | | |
         \____/ \___|\__,_|  \__,_|\___| |_| \_|_|_| |_| |_|
                                                         """
        print(titre4)
        time.sleep(2)
        print('Bienvenue sur le Jeu de Nim')
        time.sleep(2)
        regle4=input('Connaissez-vous les règles du jeu de Nim ? (Oui/Non)') #demande à l'utilisateur si il connaît les règles du jeu
        if regle4=='Non' or regle4=='non' or regle4=='N' or regle4=='n': #si il ne connaît pas les règles le programme renvoie les règles du jeu puis le jeu
            print('•-----------------------------------------------------------------------•')
            time.sleep(1)
            print('•Les règles du jeu de Nim sont les suivantes:')                  #Les règles du Jeu de Nim
            time.sleep(2)
            print('•Le jeu se joue a 2')
            time.sleep(2)
            print('•Premièrement, on dispose 20 batons sur une table')
            time.sleep(3)
            print('•Ensuite, le joueur a le choix de supprimer soit 1, soit 2, soit 3 batons')
            time.sleep(2)
            print('•Pour finir, le joueur supprimant le dernier baton perds la partie')
            time.sleep(2)
            print('•-----------------------------------------------------------------------•')
            time.sleep(2)
            game4=1
            while game4==1:
                baton=20
                bot2=0
                humain2=0
                print('Il y a 20 batons disposés sur la table')
                while baton >= 1:
                    if baton>= 1:
                        nbbaton = int(input("Tu prends: "))
                        baton -= nbbaton
                        print("Il reste",baton,"batons")
                        humain2=humain2+1
                        time.sleep(2)
                    if baton>= 1:
                        nbbaton = random.randrange(1, 3)
                        print("Le bot prend",nbbaton,"batons")
                        baton -= nbbaton
                        print("Il reste",baton,"batons")
                        bot2=bot2+1
                    if baton <1:
                        if bot2>humain2 :
                            print("Bravo, tu remportes la partie !")
                            score_human=score_human+1
                        elif humain2>bot2:
                            print("Dommage, le Bot remporte la partie !")
                            score_bot=score_bot+1
                        elif humain2==bot2:
                            print("Bravo, tu remportes la partie !")
                            score_human=score_human+1
                new4=str(input("Veux-tu rejouer ? (Oui/Non)─>")) #Pose la question "voulez-vous rejouer ?"
                if new4=='Oui' or new4=='oui' or new4=='O' or new4=='o': #si oui alors on continue
                    print("Let's GO")
                    game4=1
                if new4=='Non' or new4=='non' or new4=='N' or new4=='n': #sinon on soustrait 1 à la variable game4 ce qui à pour effet de mettre fin au jeu
                    print('Dommage')
                    game4=game4-1
        if regle4=='Oui' or regle4=='oui' or regle4=='O' or regle4=='o': #En revanche, si il connaît les règles le programme renvoie juste le jeu
            game4=1
            while game4==1:
                baton=20
                bot2=0
                humain2=0
                print('Il y a 20 batons disposés sur la table')
                while baton >= 1:
                    if baton>= 1:
                        nbbaton = int(input("Tu prends: "))
                        baton -= nbbaton
                        print("Il reste",baton,"batons")
                        humain2=humain2+1
                        time.sleep(2)
                    if baton>= 1:
                        nbbaton = random.randrange(1, 3)
                        print("Le bot prend",nbbaton,"batons")
                        baton -= nbbaton
                        print("Il reste",baton,"batons")
                        bot2=bot2+1
                    if baton <1:
                        if bot2>humain2 :
                            print("Bravo, tu remportes la partie !")
                            score_human=score_human+1
                        elif humain2>bot2:
                            print("Dommage, le Bot remporte la partie !")
                            score_bot=score_bot+1
                        elif humain2==bot2:
                            print("Bravo, tu remportes la partie !")
                            score_human=score_human+1
                new4=str(input("Veux-tu rejouer ? (Oui/Non)─>")) #Pose la question "voulez-vous rejouer ?"
                if new4=='Oui' or new4=='oui' or new4=='O' or new4=='o': #si oui alors on continue
                    print("Let's GO")
                    game4=1
                if new4=='Non' or new4=='non' or new4=='N' or new4=='n':  #sinon on soustrait 1 à la variable game4 ce qui à pour effet de mettre fin au jeu
                    print('Dommage')
                    game4=game4-1
    if jeu==5: #si l'utilisateur tape 5 alors le programme déclare la fin du jeu complet
        print('Avant de partir')
        time.sleep(2)
        print('Voilà ton score:',score_human) #Il affiche ton score
        time.sleep(2)
        print('Puis voilà le score du bot:',score_bot) #puis le score de l'odinateur
        time.sleep(2)
        if score_bot>score_human:
            win_bot="""
  _      _  ____          _ _             _                                                        _         _              _             
 | |    ( )/ __ \        | (_)           | |                                                      | |       | |            (_)            
 | |    |/| |  | |_ __ __| |_ _ __   __ _| |_ ___ _   _ _ __   _ __ ___ _ __ ___  _ __   ___  _ __| |_ ___  | |     ___     _  ___ _   _  
 | |      | |  | | '__/ _` | | '_ \ / _` | __/ _ \ | | | '__| | '__/ _ \ '_ ` _ \| '_ \ / _ \| '__| __/ _ \ | |    / _ \   | |/ _ \ | | | 
 | |____  | |__| | | | (_| | | | | | (_| | ||  __/ |_| | |    | | |  __/ | | | | | |_) | (_) | |  | ||  __/ | |___|  __/   | |  __/ |_| | 
 |______|  \____/|_|  \__,_|_|_| |_|\__,_|\__\___|\__,_|_|    |_|  \___|_| |_| |_| .__/ \___/|_|   \__\___| |______\___|   | |\___|\__,_| 
                                                                                 | |                                      _/ |            
                                                                                 |_|                                     |__/             """
            print(win_bot)
            time.sleep(2)
        if score_human>score_human:
            win_human="""
  ____                         _                                               _              _          _             
 |  _ \                       | |                                             | |            | |        (_)            
 | |_) |_ __ __ ___   _____   | |_ _   _   _ __ ___ _ __ ___  _ __   ___  _ __| |_ ___  ___  | | ___     _  ___ _   _  
 |  _ <| '__/ _` \ \ / / _ \  | __| | | | | '__/ _ \ '_ ` _ \| '_ \ / _ \| '__| __/ _ \/ __| | |/ _ \   | |/ _ \ | | | 
 | |_) | | | (_| |\ V / (_) | | |_| |_| | | | |  __/ | | | | | |_) | (_) | |  | ||  __/\__ \ | |  __/   | |  __/ |_| | 
 |____/|_|  \__,_| \_/ \___/   \__|\__,_| |_|  \___|_| |_| |_| .__/ \___/|_|   \__\___||___/ |_|\___|   | |\___|\__,_| 
                                                             | |                                       _/ |            
                                                             |_|                                      |__/             """    
            print(win_human)
            time.sleep(2)
        if score_bot==score_human:
            egalite="""
  ______            _ _ _                                                                                                         _         _             _            
 |  ____|          | (_) |                                                                                                       | |       | |           | |           
 | |__   __ _  __ _| |_| |_ ___     _ __   ___ _ __ ___  ___  _ __  _ __   ___   _ __   ___   _ __ ___ _ __ ___  _ __   ___  _ __| |_ ___  | | ___       | | ___ _   _ 
 |  __| / _` |/ _` | | | __/ _ \   | '_ \ / _ \ '__/ __|/ _ \| '_ \| '_ \ / _ \ | '_ \ / _ \ | '__/ _ \ '_ ` _ \| '_ \ / _ \| '__| __/ _ \ | |/ _ \  _   | |/ _ \ | | |
 | |___| (_| | (_| | | | ||  __/_  | |_) |  __/ |  \__ \ (_) | | | | | | |  __/ | | | |  __/ | | |  __/ | | | | | |_) | (_) | |  | ||  __/ | |  __/ | |__| |  __/ |_| |
 |______\__, |\__,_|_|_|\__\___( ) | .__/ \___|_|  |___/\___/|_| |_|_| |_|\___| |_| |_|\___| |_|  \___|_| |_| |_| .__/ \___/|_|   \__\___| |_|\___|  \____/ \___|\__,_|
         __/ |                 |/  | |                                                                          | |                                                    
        |___/                      |_|                                                                          |_|                                                     """    
            print(egalite)
            time.sleep(2)
        
        outro="""
                                      _        _
     /\                              (_)      | |
    /  \  _   _   _ __ _____   _____  _ _ __  | |
   / /\ \| | | | | '__/ _ \ \ / / _ \| | '__| | |
  / ____ \ |_| | | | |  __/\ V / (_) | | |    |_|
 /_/    \_\__,_| |_|  \___| \_/ \___/|_|_|    (_)
                                                """
        print(outro)
        hub=hub-1 #Pour finir, le programme soustrait 1 à la variable hub ce qui entraîne la fin du programme