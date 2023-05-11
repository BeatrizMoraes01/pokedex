# importar modulo tkinter
from tkinter import *
from tkinter import ttk

# importar Pillow
from PIL import Image, ImageTk

from dados import *

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

# função de interação
def trocar_pokemon (i):
    global img_pok, pok_img

    #trocando fundo do frame
    frame_pokemon ['bg'] = pokemon[i]['tipo'][3]

    #tipo pokemon
    pok_nome['text'] = i
    pok_nome['bg'] = pokemon[i]['tipo'][3]
    pok_tipo['text'] = pokemon[i]['tipo'][1]
    pok_tipo['bg'] = pokemon[i]['tipo'][3]
    pok_id['text'] = pokemon[i]['tipo'][0]
    pok_id['bg'] = pokemon[i]['tipo'][3]

    img_pok = pokemon[i]['tipo'][2]

    # imagem do pokemon
    img_pok = Image.open(img_pok)
    img_pok = img_pok.resize((238, 238))
    img_pok = ImageTk.PhotoImage(img_pok)

    pok_img = Label(frame_pokemon, image=img_pok, relief='flat', bg=pokemon[i]['tipo'][3], fg=cor1)
    pok_img.place(x=60, y=50)

    pok_tipo.lift()

    #status
    pok_hp['text'] = pokemon[i]['status'][0]
    pok_ataque['text'] = pokemon[i]['status'][1]
    pok_defesa['text'] = pokemon[i]['status'][2]
    pok_velocidade['text'] = pokemon[i]['status'][3]
    pok_total['text'] = pokemon[i]['status'][4]

    #habilidades
    pok_hb_1['text'] = pokemon[i]['habilidades'][0]
    pok_hb_2['text'] = pokemon[i]['habilidades'][1]

# nome
pok_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font='Fixedsys 20', fg=cor1)
pok_nome.place(x=12, y=15)

# tipo
pok_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font='Ivy 10 bold', bg=cor1, fg=cor1)
pok_tipo.place(x=12, y=50)

# id
pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font='Ivy 10 bold', bg=cor1, fg=cor1)
pok_id.place(x=12, y=75)

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

# botões pokemons
img_pok_1 = Image.open('images/cabeca-pikachu.png')
img_pok_1 = img_pok_1.resize((40, 40))
img_pok_1 = ImageTk.PhotoImage(img_pok_1)

b_pok_1 = Button(janela,command=lambda:trocar_pokemon('Pikachu'), image=img_pok_1, text='Pikachu', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
b_pok_1.place(x=375, y=10)

img_pok_2 = Image.open('images/cabeca-bulbasaur.png')
img_pok_2 = img_pok_2.resize((40, 40))
img_pok_2 = ImageTk.PhotoImage(img_pok_2)

b_pok_2 = Button(janela,command=lambda:trocar_pokemon('Bulbasaur'), image=img_pok_2, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
b_pok_2.place(x=375, y=65)

img_pok_3 = Image.open('images/cabeca-charmander.png')
img_pok_3 = img_pok_3.resize((40, 40))
img_pok_3 = ImageTk.PhotoImage(img_pok_3)

b_pok_3 = Button(janela,command=lambda:trocar_pokemon('Charmander'), image=img_pok_3, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
b_pok_3.place(x=375, y=120)

img_pok_4 = Image.open('images/cabeca-gyarados.png')
img_pok_4 = img_pok_4.resize((40, 40))
img_pok_4 = ImageTk.PhotoImage(img_pok_4)

b_pok_4 = Button(janela,command=lambda:trocar_pokemon('Gyarados'), image=img_pok_4, text='Gyarados', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
b_pok_4.place(x=375, y=175)

img_pok_5 = Image.open('images/cabeca-gengar.png')
img_pok_5 = img_pok_5.resize((40, 40))
img_pok_5 = ImageTk.PhotoImage(img_pok_5)

b_pok_5 = Button(janela,command=lambda:trocar_pokemon('Gengar'), image=img_pok_5, text='Gengar', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
b_pok_5.place(x=375, y=230)

img_pok_6 = Image.open('images/cabeca-dragonite.png')
img_pok_6 = img_pok_6.resize((40, 40))
img_pok_6 = ImageTk.PhotoImage(img_pok_6)

b_pok_6 = Button(janela,command=lambda:trocar_pokemon('Dragonite'), image=img_pok_6, text='Dragonite', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
b_pok_6.place(x=375, y=285)

import random
Lista_Pokemons = ['Dragonite', 'Gengar', 'Gyarados', 'Charmander', 'Bulbasaur', 'Pikachu']

pokemon_escolhido = random.sample(Lista_Pokemons, 1)
trocar_pokemon(pokemon_escolhido[0])

# executor
janela.mainloop()