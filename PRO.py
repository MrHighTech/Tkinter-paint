from tkinter import *
from tkinter.colorchooser import *
from tkinter import messagebox

proz = Tk()
proz.geometry('1000x1000')
proz.resizable(False, False)
proz.title('Bojanka')

slika_olovke = PhotoImage(file = 'Pen.png')
slika_gumice = PhotoImage(file = 'eraser.png')

slika_olovke = slika_olovke.subsample(10)
slika_gumice =  slika_gumice.subsample(10)

pen_size = 2
pen_color = 'black'
back='white'
priv  = 'black'

gum = False
def getColor():
   global pen_color
   global gum
   global pen_size
   pen_color=askcolor()[1]
   gumb.configure(bg = pen_color)
   if gum==True:
      gum=False
      pen_size-=15
   return

g = Button(proz, bg ='white',command=getColor, text = 'Odaberi boju olovke')
g.grid(row = 1, column = 0, columnspan = 2, sticky = S + E +W)

gumb = Button(proz, bg ='white')
gumb.grid(row = 2, column = 0, columnspan = 2, sticky = N + E +W)

canvas = Canvas(proz,bg='white', height = 1000, width = 920)
canvas.grid(rowspan = 100, row = 0, column = 2)


def click(click_event):
    global prev
    prev = click_event


def move(move_event):
    global prev
    canvas.create_line(prev.x, prev.y, move_event.x, move_event.y,fill = pen_color, width=pen_size)
    prev = move_event  


canvas.bind('<Button-1>', click)
canvas.bind('<B1-Motion>', move)

def sizeup():
  global pen_size
  pen_size += 1
  velicina.configure(text = 'Veličina: ' + str(pen_size))
  return

def sizedown():
  global pen_size
  if pen_size == 1:
    messagebox.showwarning('Greška','Veličina olovke je već najmanja moguća!')
  else:
    pen_size -= 1
    velicina.configure(text = 'Veličina: ' + str(pen_size))
  return

def reset():
  canvas.delete('all')
  return


velicina = Label(proz, text = 'Veličina: 2')
velicina.grid(row = 4, column = 0, columnspan = 2)


def olovka():
  global priv
  global pen_color
  global gum
  global pen_size
  pen_color=priv
  if gum:
     pen_size -= 15
  gum = False
  return

back = 'white'
def gumica():
   global priv
   global pen_color
   global back
   global pen_size
   global gum
   priv = pen_color
   pen_color= back
   if gum == False:
      pen_size += 15
   gum = True
   return


def pozadina():
   global back
   back=askcolor()[1]
   canvas.configure(bg = back)
   return


g1 = Button(proz, bg = 'white', command = sizeup,text = '+')
g1.grid(row = 5, column = 1, sticky = E+W)

g2 = Button(proz, bg = 'white', command = sizedown,text = '-')
g2.grid(row = 5, column = 0, sticky = E+W)

g3 = Button(proz, bg = 'white', command = reset,text = 'Novo platno')
g3.grid(row = 0, column = 0, columnspan = 2)

g4 = Button(proz, bg = 'white', command = olovka,image = slika_olovke)
g4.grid(row = 6, column = 0, sticky = E + W)

g5 = Button(proz, bg = 'white', command = gumica,image = slika_gumice)
g5.grid(row = 6, column = 1, sticky = E+W)

g6 = Button(proz, bg = 'white', command = pozadina , text  = 'Odaberi boju pozadine')
g6.grid(row = 3, column = 0, columnspan = 2, sticky = E+W+S)



mainloop()
