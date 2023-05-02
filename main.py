# importar modulo tkinter
from tkinter import *
from tkinter import ttk

# importar Pillow
from PIL import Image, ImageTk

# ----------------cores------------------- #
cor0 = "#444466"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#6f9fbd"  # azul
cor3 = "#38576b"  # valor
cor4 = "#403d3d"   # letra
cor5 = "#ef5350"   # vermelha

# janela principal

janela = Tk()
janela.title("")
janela.geometry("550x510")
janela.config(bg=cor1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

# nome
pok_nome = Label(frame_pokemon, text='Pickachu', relief='flat', anchor=CENTER, font='Fixedsys 20', bg=cor1, fg=cor0)
pok_nome.place(x=12, y=15)

# tipo
pok_tipo = Label(frame_pokemon, text='Eletrico', relief='flat', anchor=CENTER, font='Ivy 10 bold', bg=cor1, fg=cor0)
pok_tipo.place(x=12, y=50)

# id
pok_id = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font='Ivy 10 bold', bg=cor1, fg=cor0)
pok_id.place(x=12, y=75)

# imagem do pokemon
img_pok = Image.open('images/pikachu.png')
img_pok = img_pok.resize((238, 238))
img_pok = ImageTk.PhotoImage(img_pok)

pok_img = Label(frame_pokemon, image=img_pok, relief='flat', bg=cor1, fg=cor0)
pok_img.place(x=60, y=50)

pok_tipo.lift()

# executor
janela.mainloop()