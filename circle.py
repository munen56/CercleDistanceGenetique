from tkinter import *
from time import sleep

def deplacement():
        global i,id1,id2
        i+=1
        fenetre_dessin.delete(id1)
        id1 = fenetre_dessin.create_arc(50, 50, 550, 450, extent=i+5, start=i, outline="snow", style="arc",width=3 )
        id2 = fenetre_dessin.create_arc(50, 50, 550, 450, extent=i+3, outline="gold", style="arc")
        fenetre_dessin.create_arc(50, 50, 550, 450, extent=i, outline="orange", style="arc")

        if i < 359:
            tk.after(100, deplacement)



#-----------------------------------------------------------------------------------------------------------------------
i=1
id1=""
id2=""

tk = Tk()
fenetre_dessin = Canvas(width=1000, height=500, bg='black')
fenetre_dessin.pack(expand=YES, fill=BOTH)

fenetre_dessin.create_line(600,0,600,500,fill="navy",width=2)

deplacement()
#fenetre_dessin.create_oval(50, 50, 550, 450, outline="red")

mainloop()
