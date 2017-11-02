# -*- coding: utf-8 -*-
from __future__ import unicode_literals # permite incluir acentos nos gráficos (legendas)
from Tkinter import *
from tkFileDialog import *
import tkMessageBox
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

root = Tk()

#Variaveis
tema = StringVar(master=root)
tema.set("fivethirtyeight")
grafico = StringVar(master=root)
grafico.set("linha")
estilos = plt.style.available
fig = plt.figure(dpi=150, figsize=(4, 4)) # Cria uma figura, onde ficará o gráfico
plt.ion() #Habilita o modo interativo

def exibe_ajuda():
    texto = """
1. Insira os dados do gráfico diretamente na caixa de texto ou através do menu "Arquivo>Abrir arquivo".
Atenção: Os dados devem respeitar o formato "x,y" para gráficos do tipo linha e "identificador,porcentagem" ou "identificador,quantidade" para gráficos do tipo pizza. Cada par de dados deve ser separado por uma quebra de linha.
Exemplos: linha:
"1,1
3,5
6,2", 
pizza:
"Sim,30
Não,40
Talvez,30".
2. Escolha o tipo de gráfico: linha ou pizza.
3. Insira o nome do gráfico no local especificado.
4. Se desejar, escolha a aparência do gráfico através do menu "Tema".
5. Clique em "Gerar gráfico" para gerar e visualizar o gráfico.
6. Se desejar, exporte o gráfico para uma imagem através do menu "Arquivo>Salvar arquivo" ou pelo botão na barra de ferramentas acima do gráfico.
"""
    tkMessageBox.showinfo("Como utilizar", texto)

def sair(master): # Fecha o programa
    if tkMessageBox.askyesno("Fechar", "Deseja fechar o programa?"):
        #master.destroy()
        quit()

def abre_arquivo(caixa_entrada):
    caminho = askopenfilename(initialdir = "~/Documentos", filetypes = (('Arquivos de Texto','*.txt *.doc *.docx *.odt'),("Todos os Arquivos","*.*"))) #Linux
    #caminho = askopenfilename(initialdir = "C:/", title="Abrir arquivo", filetypes = (('Arquivos de Texto','*.txt *.doc *.docx *.odt'),("Todos os Arquivos","*.*"))) #Windows
    if not caminho: # se o diálogo for cancelado, sai da função
        return
    with open(caminho) as arq:
        conteudo = arq.read()
    caixa_entrada.delete(1.0, END)
    caixa_entrada.insert(INSERT, conteudo)

def salva_arquivo():
    caminho = asksaveasfilename(initialdir = "~/Imagens", defaultextension=".png", filetypes=(("Arquivos de imagem", "*.png *.jpeg"),("Todos os arquivos", "*.*")))
    #caminho = asksaveasfilename(initialdir = "C:/", defaultextension=".png", filetypes=(("Arquivos de imagem", "*.png *.jpeg"),("Todos os arquivos", "*.*"))) #Windows
    if not caminho: # se o diálogo for cancelado, sai da função
        return
    plt.savefig(caminho)

def gera_grafico(caixa_entrada, ent):
    try: # Verifica se os dados estão em formato correto
        # Separa os dados em uma lista, por quebra de linha
        dados = []
        dados = caixa_entrada.get(1.0, END).split("\n")
        x = []
        y = []

        for i in dados:
            if i != '':
                if grafico.get() == 'linha':
                    x.append(float(i.split(',')[0]))
                else:
                    x.append(i.split(',')[0])
                
                y.append(float(i.split(',')[1]))

                if len(i.split(',')) > 2:
                    raise IndexError

    except:
        tkMessageBox.showwarning(
        "Atenção",
        "Os dados estão em formato inesperado.")
        return

    if tema.get() == 'dark_background':
        estilo = ['dark_background', 'seaborn-dark-palette']
        fig.set(facecolor="black")
        plt.rcParams['savefig.facecolor']='black'
    else:
        estilo = tema.get()
        fig.set(facecolor="whitesmoke")
        plt.rcParams['savefig.facecolor']='whitesmoke'
    
    with plt.style.context(estilo):

        fig.clear() # Limpa o que estiver na figura

        if grafico.get() == "linha":
            # Gera gráfico de linha
            plt.plot(x,y, marker='o')
        else:
            # Gera gráfico de pizza
            patches, texts = plt.pie(y, startangle=90, radius=1.2)
            # Formata a legenda do gráfico
            labels = ['{0} - {1:1.2f} %'.format(i,100.0*j/sum(y)) for i,j in zip(x, y)]
            plt.legend(patches, labels, fontsize=6, loc='lower left')
            plt.axis('equal')  # Define o aspecto da pizza como um circulo

        titulo = ent.get()
        plt.title(titulo)
        fig.canvas.draw() # Desenha o gráfico no canvas