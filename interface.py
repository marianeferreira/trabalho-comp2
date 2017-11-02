# -*- coding: utf-8 -*-

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from functions import *

class Minha_Aplicacao(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.layout(master)

        self.widgets()

        self.menu(master)

        self.centraliza(master)

        self.canvas_grafico()

        self.pack()

    def layout(self, master):
        master.title("Gerador de gráficos")
        self.frame1 = Frame(master, bg='#B5B1CE')
        self.frame2 = Frame(master)
        self.frame3 = Frame(self.frame2, bg='#C3C3DD')
        self.frame4 = Frame(self.frame2, bg='#C3C3DD')
        self.frame5 = Frame(self.frame2)
        self.frame1.pack(side=LEFT, fill=BOTH)
        self.frame2.pack(side=LEFT, fill=BOTH, expand=1)
        self.frame3.pack(fill=BOTH, expand=1)
        self.frame4.pack(fill=BOTH, expand=1)
        self.frame5.pack(fill=BOTH, expand=1)

    def centraliza(self, master): # centraliza a janela
        larg = 1000 # largura da janela
        alt = 600 # altura da janela
        master.minsize(1000, 600)

        # Obtém a largura e a altura da tela
        larg_tela = master.winfo_screenwidth()
        alt_tela = master.winfo_screenheight()

        # calcula as coordenadas x e y para a janela
        x = (larg_tela/2) - (larg/2)
        y = (alt_tela/2) - (alt/2)

        # define as dimensões da janela 
        # e onde ela será colocada
        master.geometry('%dx%d+%d+%d' % (larg, alt, x, y))

    def widgets(self):
        self.lbl = Label(self.frame1, text="Insira os dados do\ngráfico ou carregue\na partir de um arquivo", font=('Arial', 11), bg='#B5B1CE')
        self.lbl.pack(fill=BOTH, padx=5, pady=5)
        self.caixa_entrada = Text(self.frame1, width=5, height=40)
        self.caixa_entrada.pack(side=BOTTOM, fill=BOTH, expand=1, padx=5, pady=5)
        self.rb1 = Radiobutton(self.frame3, text="Gráfico de linha", variable=grafico, value="linha", bg='#C3C3DD', highlightbackground='#C3C3DD')
        self.rb1.pack(side=LEFT, fill=X, padx=5, pady=2)
        self.rb1.select()
        self.rb2 = Radiobutton(self.frame3, text="Gráfico de pizza", variable=grafico, value="pizza", bg='#C3C3DD', highlightbackground='#C3C3DD')
        self.rb2.pack(side=LEFT, fill=X, padx=5, pady=2)
        self.lbl_tema = Label(self.frame3, text="Tema:", bg='#C3C3DD')
        self.lbl_tema.pack(side=LEFT, fill=X, padx=5, pady=2)
        self.opcoes = apply(OptionMenu, (self.frame3, tema) + tuple(estilos))
        self.opcoes.config(highlightbackground='#C3C3DD')
        self.opcoes.pack(side=LEFT, fill=X, expand=1, padx=5, pady=2)
        self.lbl_titulo = Label(self.frame3, text="Título:", bg='#C3C3DD')
        self.lbl_titulo.pack(side=LEFT, padx=5, pady=2)
        self.ent = Entry(self.frame3, highlightbackground='#C3C3DD')
        self.ent.pack(side=LEFT, padx=5, pady=2)
        self.btnGerarGrafico = Button(self.frame4, text="Gerar gráfico", command=lambda:gera_grafico(self.caixa_entrada, self.ent), highlightbackground='#C3C3DD')
        self.btnGerarGrafico.pack(padx=5, pady=5)

    def menu(self, master):
        menu = Menu(self, tearoff=0)
        menu_arquivo = Menu(menu)
        menu_arquivo.add_command(label="Abrir arquivo", command=lambda:abre_arquivo(self.caixa_entrada))
        menu_arquivo.add_command(label="Salvar arquivo", command=salva_arquivo)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=lambda:sair(master))
        menu.add_cascade(menu=menu_arquivo, label="Arquivo")
        menu_ajuda = Menu(menu)
        menu_ajuda.add_command(label="Como utilizar", command=exibe_ajuda)
        menu.add_cascade(menu=menu_ajuda, label="Ajuda")
        master.configure(menu=menu)

    def canvas_grafico(self):
        self.canvas = FigureCanvasTkAgg(fig, self.frame5)
        self.canvas.get_tk_widget().pack(fill=BOTH, padx=5, pady=5)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.frame4)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(fill=BOTH, expand=1, padx=5, pady=5)