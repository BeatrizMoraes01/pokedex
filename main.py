# importar modulo tkinter
from tkinter import *
from tkinter import ttk

# importar modulo math
import math

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

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, column=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# executor
janela.mainloop()