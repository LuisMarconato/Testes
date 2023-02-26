from tkinter import *
from tkinter import ttk
import os as os
import shutil
import __pycache__ as fun
#ESTRUTURA PRINCIPAL
#1- ESTRUTURA DA JANELA:
janela = Tk()
janela.title("Gdoor - Sistemas")
janela["background"]= "orange red"

#1.1- Dimensões da janela
largura = 500
altura = 300            

#1.2- RESOLUÇÃO DO NOSSO SISTEMA
largura_janela = janela.winfo_screenwidth()
altura_janela = janela.winfo_screenheight()

#1.3- POSIÇÃO DA JANELA
posx = largura_janela/2 - largura/2
posy = altura_janela/2 - altura/2

#1.4- DEFINIR A GEOMETRY
janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

#1.5- DEFINIR ESPAÇO DO STATUS
LabelFrame  = LabelFrame(janela,text="STATUS:",font=("Arial",16,"bold"), background="orange red", labelanchor=N)
LabelFrame.pack(fill="both", expand="yes")

#1.6- DEFINIR ESPAÇO DA INSERÇAO DE SENHA
Label_senha = Label(janela,text="DEFINA A SENHA:",font=("Arial",12,"bold"), background="orange red")
Label_senha.pack(fill="both",expand="yes")
Label_senha = Entry(janela,bd=4,justify=CENTER,state=NORMAL, background="orange red")
Label_senha.pack(fill="both",expand="yes")



#1.7- BOTÃO SALVAR SENHA ***(não defini se vai ficar aqui ou junto com os botões!) 
salva_senha = Button(text='SALVAR SENHA',height=1,width=15,command= fun.SALVAR_SENHA  )
salva_senha.pack(fill="both", expand="yes")

#1.8- TEXTO STATUS
texto_status = Label(LabelFrame,text="",font=("Arial",12),background="orange red")
texto_status.pack(anchor=N, fill=BOTH, expand="yes")

#1.9- BARRA DE PRROGRESSO ****(não esta funcionando direito, revisar!)
#barra_progresso= Progressbar(janela, orient= HORIZONTAL, mode= 'determinate',maximum=10,value=0)
#barra_progresso.pack(anchor=CENTER, fill=BOTH,expand="yes",side=BOTTOM)

#1.10- TEXTO EXECUÇÃO TROCA DE SENHA 
texto_senha = Label(LabelFrame, text="",font=("Arial",12),background="orange red")
texto_senha.pack(anchor=CENTER, fill=Y, expand="yes")

#1.11- TEXTO SELEÇÃO COMBOBOX
seleciona_modulo = Label(janela,text='SELECIONA O MÓDULO GDOOR:',font=("Arial",12,"bold"),background="orange red")
seleciona_modulo.pack( expand="yes")

#1.12- VARIAVEL GLOBAL DOS MÓDULOS
lista_modulos = ["PRO", "SLIM","MEI"]
caminho_pro='C:/GDOOR Sistemas/GDOOR PRO/'
caminho_slim='C:/GDOOR Sistemas/GDOOR SLIM/'
caminho_mei='C:/GDOOR Sistemas/GDOOR MEI/'

#1.13- CRIAÇÃO COMBOBOX
cb_modulos = ttk.Combobox(janela,values=lista_modulos,state='readonly')
cb_modulos.set(lista_modulos[0])
cb_modulos.pack(fill="both", expand="yes")
combo = 0

#2- VERIFICA SE O DIRETORIO JA ESTA CRIADO, SE NÃO TIVER SERÁ CRIADO
#GDOORPRO
if os.path.exists(f'{caminho_pro}'):
    if not os.path.exists(f'{caminho_pro}/Backup Tecnico')and not os.path.exists(f'{caminho_pro}/Base Cliente'):
            os.makedirs(f'{caminho_pro}/Base Cliente')
            os.makedirs(f'{caminho_pro}/Backup Tecnico')
#GDOORSLIM            
if os.path.exists(f'{caminho_slim}'):
    if not os.path.exists(f'{caminho_slim}/Backup Tecnico')and not os.path.exists(f'{caminho_slim}/Base Cliente'):
            os.makedirs(f'{caminho_slim}/Base Cliente')
            os.makedirs(f'{caminho_slim}/Backup Tecnico')
#GDOORMEI
if os.path.exists(f'{caminho_mei}'):
    if not os.path.exists(f'{caminho_mei}/Backup Tecnico')and not os.path.exists(f'{caminho_mei}/Base Cliente'):
            os.makedirs(f'{caminho_mei}/Base Cliente')
            os.makedirs(f'{caminho_mei}/Backup Tecnico')

#3- BOTÕES
#3.1- BOTÃO DELETE
DELETE_button = Button(text='DELETE VERSÃO',height=1,width=15, command=fun.DELETE_VERSAO)
DELETE_button.pack(fill="both", expand="yes")

#3.2- BOTÃO TROCAR
TROCA_button = Button(text='TROCAR BASE',height=1,width=15, command=fun.TROCA)
TROCA_button.pack(fill="both", expand="yes")

#3.3- BOTÃO REVERTER
REVERTE_button = Button(text='REVERTER BASE',height=1,width=15,command=fun.REVERTER)
REVERTE_button.pack(fill="both", expand="yes")

#3.4- BOTÃO SALVAR SENHA ***(não defini a posição ainda!)
#salva_senha = Button(text='SALVAR SENHA',height=1,width=15,command=SALVAR_SENHA)
#salva_senha.pack(fill="both", expand="yes")

#4- VALIDAÇÃO DO BOTÃO REVERTER (APRIMORAR VARREDURA PARA HABILITAR BOTÕES DE AÇÕES)
if combo == 0:
    if len(os.listdir(f'{caminho_pro}Backup Tecnico')) == 0:
        REVERTE_button.configure(state='disable')
    
    if len (os.listdir(f'{caminho_slim}Backup Tecnico')) == 0:
        REVERTE_button.configure(state='disable')
    
    if len (os.listdir(f'{caminho_mei}Backup Tecnico')) ==0:
        REVERTE_button.configure(state='disable')

janela.mainloop()