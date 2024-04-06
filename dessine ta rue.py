from tkinter import *
import random

fen = Tk()
fen.title('Dessine_ta_rue')
can = Canvas(fen, width=1500, height=800, bg='white')
can.pack() # Affiche le Canvas

def arbre(x, y, hauteur, largeur):
    can.create_rectangle(x - largeur / 2, y, x + largeur / 2, y + hauteur, fill="#631A09")
    can.create_oval(x - largeur, y - hauteur / 2, x + largeur, y + hauteur / 2, fill="#137631")
def ciel():
    can.create_rectangle(0,0,1500,150,fill='skyblue')
def nuage(x,y,x1,y1):
    for i in range(5):
        can.create_oval(x - x1 / 2 + i * x1 / 5, y - y1 / 2, x + x1 / 2 + i * x1 / 5, y + y1 / 2,fill="white", outline="white")


def placer_fleur(canvas, x1, y1, x2, y2, n):
    """Place n fleurs aléatoirement dans la zone délimitée par les coordonnées (x1, y1) et (x2, y2)"""
    colors = ["red", "orange", "yellow", "pink", "purple"] # liste de couleurs possibles pour les fleurs
    for i in range(n):
        x = random.randint(x1, x2) # position x aléatoire
        y = random.randint(y1, y2) # position y aléatoire
        size = random.randint(10, 12) # taille aléatoire
        color = random.choice(colors) # couleur aléatoire
        can.create_oval(x, y, x+size, y+size, fill=color)

def route():
    can.create_rectangle(0,680,1500,765,fill='grey')
def sol():
    can.create_rectangle(0,150,1500,680,fill='dark green')

# Création des rectangles avec une boucle for pour réduire le code
def ligne_blanche():
    for i in range(16):
        x1 = 40 + i * 90
        x2 = 90 + i * 90
        can.create_rectangle(x1, 720, x2, 730, fill='white', outline='black', width=2)


def placer_herbe(canvas, x_min, y_min, x_max, y_max, nb_brins):
    for i in range(nb_brins):
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        canvas.create_line(x, y, x, y-10, fill="green", width=2)

# Dessin du toit
def toit(x,x1,x2):
    can.create_polygon(x,480,x1,420,x2,480,fill='#393939',outline='black', width=2)

def toit2(x,x1,x2):
    can.create_polygon(x,580,x1,520,x2,580,fill='#393939',outline='black', width=2)

# Dessin du corps de la maison
def maison(x1,x2,x3,x4,x5,x6):
    couleur = ['#9B0606', 'grey', 'darkgrey', '#630C0C','#FAD7A0','#212F3D']
    can.create_rectangle(x1,580,x2,680, fill=random.choice(couleur), outline='black', width=2)
    can.create_rectangle(x3,640,x4,680, fill='white', outline='black', width=2)
    can.create_rectangle(x5,600,x6,620, fill='skyblue', outline='black', width=2)
    can.create_rectangle(x5+60, 600,x6+60, 620, fill='skyblue', outline='black', width=2)
    

def etage(x1,x2,x3,x4):
    couleur = ['#9B0606', 'grey', 'darkgrey', '#630C0C','#FAD7A0','#212F3D']
    can.create_rectangle(x1, 480, x2,580, fill=random.choice(couleur), outline='black', width=2)
    can.create_rectangle(x3, 520,x4 , 540, fill='skyblue', outline='black', width=2)
    can.create_rectangle(x3+60, 520,x4+60, 540, fill='skyblue', outline='black', width=2)

#Dessin
route()
can.update()
can.after(500)
ligne_blanche()
can.update()
can.after(500)
sol()
can.update()
can.after(500)
ciel()
can.update()
can.after(500)

for i in range(7):
    x=random.randint(50,1600)
    nuage(x,80,75,60)
can.update()
can.after(500)

placer_herbe(can, 0, 170, 1500, 660, 1500)
can.update()
can.after(500)

placer_fleur(can, 0, 170, 1500, 660, 150)
can.update()
can.after(500)

positions_arbres3 = [(100, 160), (250, 205), (400, 160), (550, 205), (700, 160), (850, 205), (1000, 160), (1150, 205),(1300,160),(1450,205)]
for x, y in positions_arbres3:
    arbre(x, y, 100, 30)
can.update()
can.after(500)

positions_arbres = [(150, 225), (300, 270), (450, 225), (600, 270), (750, 225), (900, 270), (1050, 225), (1200, 270),(1350,225),(1500,270)]
for x, y in positions_arbres:
    arbre(x, y, 100, 30)
can.update()
can.after(500)

positions_arbres2 = [(100, 300), (250, 365), (400, 300), (550, 365), (700, 300), (850, 365), (1000, 300), (1150, 365),(1300,300),(1450,365)]
for x, y in positions_arbres2:
    arbre(x, y, 100, 30)
can.update()
can.after(500)
positions_maison=[(50,150,90,110,60,80),(200,300,240,260,210,230),(350,450,390,410,360,380),(500,600,540,560,510,530),(650,750,690,710,660,680),(800,900,840,860,810,830),(950,1050,990,1010,960,980),(1100,1200,1140,1160,1110,1130),(1250,1350,1290,1310,1260,1280),(1400,1500,1440,1460,1410,1430)]
for x1,x2,x3,x4,x5,x6 in positions_maison:
    maison(x1,x2,x3,x4,x5,x6)
can.update()
can.after(500)

positions_etage=[(50,150,60,80),(200,300,210,230),(350,450,360,380),(950,1050,960,980),(1250,1350,1260,1280)]
for x1,x2,x3,x4 in positions_etage:
    etage(x1,x2,x3,x4)
can.update()
can.after(500)

positions_toit=[(50,100,150),(200,250,300),(350,400,450),(950,1000,1050),(1250,1300,1350)]
for x1,x2,x3 in positions_toit:
    toit(x1,x2,x3)
can.update()
can.after(500)


positions_toit2=[(500,550,600),(650,700,750),(800,850,900),(1100,1150,1200),(1400,1450,1500)]
for x1,x2,x3 in positions_toit2:
    toit2(x1,x2,x3)
can.update()
can.after(500)







# Création du bouton "Sortir"
bouton_sortir = Button(fen, text="Sortir", command=fen.destroy,bg='black',fg='white')
bouton_sortir.pack()
fen.mainloop()