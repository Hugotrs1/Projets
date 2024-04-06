import random as rd
from tkinter import *
    
def resultat_dé():
    result = rd.randint(1, 6)
    draw_dice(canvas, result)


def draw_dice(canvas, result):
    # Clear previous drawings
    canvas.delete("all")

    # Draw the outer rectangle
    canvas.create_rectangle(300, 100, 500, 300, outline="black",fill="black", width=2)

    # Draw dots based on the dice result
    if result in [1, 3, 5]:
        canvas.create_oval(375, 175, 425, 225, outline="black",width=2,fill="white")  # Center dot

    if result in [2, 3, 4, 5, 6]:
        canvas.create_oval(305,105, 355, 155, outline="black",width=2,fill="white")  # Top left dot
        canvas.create_oval(445, 245, 495, 295, outline="black",width=2,fill="white")  # Bottom right dot

    if result in [4, 5]:
        canvas.create_oval(305, 245, 355, 295, outline="black",width=2,fill="white")  # Top right dot
        canvas.create_oval(445, 105, 495, 155, outline="black",width=2,fill="white")  # Bottom left dot
    if result==6:
        canvas.create_oval(305, 245, 355, 295, outline="black",width=2,fill="white")  # Top right dot
        canvas.create_oval(445, 105, 495, 155, outline="black",width=2,fill="white")   
        canvas.create_oval(305, 175, 355, 225, outline="black",width=2,fill="white") 
        canvas.create_oval(445, 175, 495, 225, outline="black",width=2,fill="white")


fen = Tk()#creation de la fenetre
fen.title('dé_6_faces')  #titre

canvas = Canvas(fen, width=800, height=400, bg="white")
canvas.pack(pady=10)

bouton_lancer = Button(fen, text="Lancer le dé", command=resultat_dé, bg='white', fg='black')
bouton_lancer.pack(pady=10)



bouton_sortir = Button(fen, text="Fermer", command=fen.destroy,bg='white',fg='black') # Création du bouton "Sortir"
bouton_sortir.pack()
fen.mainloop()