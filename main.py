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

# status
pok_status = Label(janela, text='Status', anchor=CENTER, relief='flat', font=('Verdana 20'), bg=cor1, fg=cor0)
pok_status.place(x=15, y=310)

# hp
pok_hp = Label(janela, text='HP: 100', anchor=CENTER, relief='flat', font=('Verdana 10'), bg=cor1, fg=cor0)
pok_hp.place(x=15, y=360)

# ataque
pok_ataque = Label(janela, text='Ataque: 600', anchor=CENTER, relief='flat', font=('Verdana 10'), bg=cor1, fg=cor0)
pok_ataque.place(x=15, y=385)

# defesa
pok_defesa = Label(janela, text='Defesa: 500', anchor=CENTER, relief='flat', font=('Verdana 10'), bg=cor1, fg=cor0)
pok_defesa.place(x=15, y=410)

# velocidade
pok_velocidade = Label(janela, text='Velocidade: 300', anchor=CENTER, relief='flat', font=('Verdana 10'), bg=cor1, fg=cor0)
pok_velocidade.place(x=15, y=435)

# total
pok_total = Label(janela, text='Total: 1.700', anchor=CENTER, relief='flat', font=('Verdana 10'), bg=cor1, fg=cor0)
pok_total.place(x=15, y=460)

# habilidades
pok_habilidades = Label(janela, text='Habilidades', anchor=CENTER, relief='flat', font=('Verdana 20'), bg=cor1, fg=cor0)
pok_habilidades.place(x=180, y=310)

# hb_1
pok_hb_1 = Label(janela, text='Choque do Trovão', anchor=CENTER, relief='flat', font=('Verdana 10'), bg=cor1, fg=cor0)
pok_hb_1.place(x=195, y=360)

# hb_2
pok_hb_2 = Label(janela, text='Cabeçada', anchor=CENTER, relief='flat', font=('Verdana 10'), bg=cor1, fg=cor0)
pok_hb_2.place(x=195, y=385)

# executor
janela.mainloop()