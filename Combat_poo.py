import random as rd
import time
from tkinter import *
from PIL import Image, ImageTk
import pygame
import os


script_dir = os.path.dirname(os.path.abspath(__file__))

combat_poo_dir = os.path.join(script_dir)


class Personnage:
    def __init__(self, nom, nbreDeVie):
        self.nom = nom
        self.vie = nbreDeVie

    def pvrestant(self):
        return self.vie

    def jab(self):
        self.vie -= 20

    def uppercut(self):
        self.vie -= 30

    def hook(self):
        self.vie -= 15

class CombatApplication:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.can = Canvas(self.fenetre, width=1000, height=680, bg='white')
        self.can.pack()
        self.photo = None  # Initialize photo attribute

    def afficher(self, image_path):
        image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(image)
        self.can.delete("all")
        self.can.create_image(0, 0, anchor=NW, image=self.photo)


def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()



def recap(jp1, jesp1, up1, upes1, h1, hes1, jp2, jesp2, up2, upes2, h2, hes2):
    print('Récapitulatif du combat :')
    print('------------------------------')
    print(perso1.nom ,':')
    print(f"Jabs envoyés : {jp1}\nJabs esquivés : {jesp1}\nUppercuts envoyés : {up1}\nUppercuts esquivés : {upes1}\nCrochets envoyés : {h1}\nCrochets esquivés : {hes1}")
    print('------------------------------')
    print(perso2.nom ,':')
    print(f"Jabs envoyés : {jp2}\nJabs esquivés : {jesp2}\nUppercuts envoyés : {up2}\nUppercuts esquivés : {upes2}\nCrochets envoyés : {h2}\nCrochets esquivés : {hes2}")
    print('------------------------------')

def combat():
    
    jp1, jesp1, up1, upes1, h1, hes1, jp2, jesp2, up2, upes2, h2, hes2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    while perso1.pvrestant() > 0 and perso2.pvrestant() > 0:
        atckfrst = rd.randint(1, 2)
        jabpro = rd.randint(1, 5)
        hookproba = rd.randint(1, 7)
        uppercutproba = rd.randint(1, 10)

        if atckfrst == 1:
            choixatt = input('Quel coup voulez vous envoyer ? jab, uppercut, hook ')
            if choixatt == 'jab':
                if jabpro > 2:
                    perso2.jab()
                    jp1+=1
                    print(perso1.nom, 'envoie un jab')
                    play_sound(os.path.join(combat_poo_dir, "punch.mp3"))
                    app.afficher(os.path.join(combat_poo_dir, "P1_jab_p2.png"))

                else:
                    jesp1+=1
                    print(perso1.nom, 'a raté son coup')
                    play_sound(os.path.join(combat_poo_dir, "esquive.mp3"))
                    app.afficher(os.path.join(combat_poo_dir, "P2_esj_p1.png"))

            if choixatt == 'uppercut':
                if uppercutproba > 8:
                    perso2.uppercut()
                    up1+=1
                    print(perso1.nom, 'décroche un uppercut')
                    play_sound(os.path.join(combat_poo_dir, "punch.mp3"))
                    app.afficher(os.path.join(combat_poo_dir, "P1_up_p2.png"))
                else:
                    upes1+=1
                    print(perso1.nom, 'a raté son coup')
                    play_sound(os.path.join(combat_poo_dir, "esquive.mp3"))
                    app.afficher(os.path.join(combat_poo_dir, "P2_esu_p1.png"))

            if choixatt == 'hook':
                if hookproba > 3:
                    perso2.hook()
                    h1+=1
                    print(perso1.nom, 'qui corrige', perso2.nom, 'avec un crochet')
                    play_sound(os.path.join(combat_poo_dir, "punch.mp3"))
                    app.afficher(os.path.join(combat_poo_dir, "P1_hook_p2.png"))
                else:
                    hes1+=1
                    print(perso1.nom, 'a raté son coup')
                    play_sound(os.path.join(combat_poo_dir, "esquive.mp3"))
                    app.afficher(os.path.join(combat_poo_dir, "P2_esh_p1.png"))

        elif atckfrst == 2:
            c = rd.randint(1, 3)
            if c == 1:
                if jabpro > 2:
                    perso1.jab()
                    jp2+=1
                    print(perso2.nom, 'envoie un jab')
                    play_sound(os.path.join(combat_poo_dir, "punch.mp3"))
                    app.afficher(os.path.join(combat_poo_dir, "P2_jab_p1.png"))
                else:
                    jesp2+=1
                    print(perso2.nom, 'a raté son coup')
                    play_sound(os.path.join(combat_poo_dir, "esquive.mp3"))
                    app.afficher(os.path.join(combat_poo_dir, "P1_esj_p2.png"))

            elif c == 2:
                if uppercutproba > 8:
                    perso1.uppercut()
                    up2+=1
                    print(perso2.nom, 'décroche un uppercut')
                    play_sound(os.path.join(combat_poo_dir, "punch.mp3"))
                    app.afficher(os.path.join(combat_poo_dir, "P2_up_p1.png"))
                else:
                    upes2+=1
                    print(perso2.nom, 'a raté son coup')
                    play_sound(os.path.join(combat_poo_dir, "esquive.mp3"))
                    app.afficher(os.path.join(combat_poo_dir, "P1_esu_p2.png"))

            elif c == 3:
                if hookproba > 3:
                    perso1.hook()
                    h2+=1
                    print(perso2.nom, 'qui corrige', perso1.nom, 'avec un crochet')
                    play_sound(os.path.join(combat_poo_dir, "punch.mp3"))
                    app.afficher(os.path.join(combat_poo_dir, "P2_hook_p1.png"))
                else:
                    hes2+=1
                    print(perso2.nom, 'a raté son coup')
                    play_sound(os.path.join(combat_poo_dir, "esquive.mp3"))
                    app.afficher(os.path.join(combat_poo_dir, "P1_esh_p2.png"))

        time.sleep(1)
        fen.update_idletasks()
        print('-------------------------------')
        print('PV de', perso1.nom, ':', perso1.pvrestant())
        print('PV de', perso2.nom, ':', perso2.pvrestant())
        print('-------------------------------')
        time.sleep(2)

    if perso2.pvrestant() <= 0:
        print(perso1.nom, 'remporte le combat')
        recap(jp1, jesp1, up1, upes1, h1, hes1, jp2, jesp2, up2, upes2, h2, hes2)
        fen.title(perso1.nom +' à gagné')
        play_sound(os.path.join(combat_poo_dir, "final_punch.mp3"))
        app.afficher(os.path.join(combat_poo_dir, "p1 KO p2.png"))
        fen.after(4000, fen.update_idletasks())
        app.afficher(os.path.join(combat_poo_dir, "p1_win.png"))
        fen.update_idletasks()
        play_sound(os.path.join(combat_poo_dir, "Bell.mp3"))
        fen.after(20000, fen.destroy())

    if perso1.pvrestant() <= 0:
        print(perso2.nom, 'remporte le combat')
        recap(jp1, jesp1, up1, upes1, h1, hes1, jp2, jesp2, up2, upes2, h2, hes2)
        fen.title(perso2.nom +' à gagné')
        play_sound(os.path.join(combat_poo_dir, "final_punch.mp3"))
        app.afficher(os.path.join(combat_poo_dir, "p2 KO p1.png"))
        fen.after(4000, fen.update_idletasks())
        app.afficher(os.path.join(combat_poo_dir, "p2_win.png"))
        fen.update_idletasks()
        play_sound(os.path.join(combat_poo_dir, "Bell.mp3"))
        fen.after(20000, fen.destroy())
    fen.mainloop()




nom_perso1 = input('Quel est votre nom ? ')
nom_perso2 = input('Quel est le nom de l\'adversaire ? ')
perso1 = Personnage(nom_perso1, 50)
perso2 = Personnage(nom_perso2, 50)
fen = Tk()
fen.title('Combat_poo')
app = CombatApplication(fen)
app.afficher(os.path.join(combat_poo_dir,"Black.png"))
fen.update_idletasks()
app.afficher(os.path.join(combat_poo_dir,"Start.png"))
fen.after(6000,combat())




combat()