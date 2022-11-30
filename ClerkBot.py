import PySimpleGUI as sg
from backChatBot import sendMessage
from time import sleep
from tkinter import *
from tkinter.ttk import *
import tkVideoPlayer

# Dados da aplicação 
listContato = []
listImages = []
listDocs = []

# Criar janela e layouts
def janelaInicial():
    sg.theme('Reddit')
    layout = [
        [sg.Image(source="logo_def.png")],
        [sg.Button("Bot", size=(15,20), font="arial 16 ", button_color='#5271FF'), sg.Button("Como funciona?", font="arial 16 ", size=(15,20))]
    ]
    return sg.Window('ClerkBot', layout=layout, element_justification="center", finalize=True, size=(720, 500), background_color='#03989E', icon='logo_robot.ico')
    
def janelaEnviar():
    sg.theme('Reddit')
    layout =[
        [sg.Text("Enviar mensagens", font="arial 24", justification="center")],
        [sg.Text("Digite o nome do contato e/ou grupo", font="arial 10")],
        [sg.Text("Contato:", font="arial 12"),sg.Input(key="contato", size=(25,2), font="arial 12"),sg.Button("Adicionar"),sg.Button("Remover")],
        [sg.Text("Contatos:",font="arial 12"),sg.Text(f"{'' if len(listContato) < 0 else listContato}", key="contatos", font="arial 12", size=(30,2))],
        [sg.Text("Imagem ou Vídeo:", font="arial 12"),sg.Input(key="img", size=(25,2),font="arial 12"), sg.FileBrowse(),sg.Button("Adicionar Imagem"), sg.Button("Remover imagem",)],
        [sg.Text("Quantidade de imagem:",font="arial 12"),sg.Text(f"{len(listImages)}",font="arial 12",key="imgs",size=(30,2))],
        [sg.Text("Documento:", font="arial 12"),sg.Input(key="doc", size=(25,2),font="arial 12"), sg.FileBrowse(),sg.Button("Adicionar documento"), sg.Button("Remover documento")],
        [sg.Text("Quantidade de documentos:",font="arial 12"),sg.Text(f"{len(listDocs)}",font="arial 12",key="documentos", size=(30,2))],
        [sg.Text("Digite sua mensagem:", font="arial 12")],
        [sg.Multiline(key="newMessage", size=(80,5))],
        [sg.Button("Voltar",font="arial 13"), sg.Button("Enviar", font="arial 13")],
    ]
    
    return sg.Window('ClerkBot', layout=layout, element_justification="center", finalize=True, icon='logo_robot.ico')

def Remover():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Digite o nome do contato para remover")],
        [sg.Input(key="valueRemove")],
        [sg.Text("Contatos:"),sg.Text(f"{listContato}" , key="valueContato", size=(30,2))],
        [sg.Button("Voltar"), sg.Button("Remover"), sg.Button("Remover tudo")]
    ]
    return sg.Window("ClerkBot",layout= layout,element_justification="center", finalize=True, icon='logo_robot.ico')

def help1():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Ajuda 1")],
        [sg.Button("Voltar", size=(15,20), font="arial 16 ", button_color='#5271FF'),sg.Button("Continuar", size=(15,20), font="arial 16 ", button_color='#5271FF')]
    ]
    return sg.Window('ClerkBot', layout=layout, element_justification="center", finalize=True, size=(720, 500), background_color='#03989E', icon='logo_robot.ico')
def help2():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Ajuda 2")],
        [sg.Button("Voltar", size=(15,20), font="arial 16 ", button_color='#5271FF'),sg.Button("Continuar", size=(15,20), font="arial 16 ", button_color='#5271FF')]
    ]
    return sg.Window('ClerkBot', layout=layout, element_justification="center", finalize=True, size=(720, 500), background_color='#03989E', icon='logo_robot.ico')
def help3():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Ajuda 3")],
        [sg.Button("Voltar", size=(15,20), font="arial 16 ", button_color='#5271FF'),sg.Button("Tela Inicial", size=(15,20), font="arial 16 ", button_color='#5271FF')]
    ]
    return sg.Window('ClerkBot', layout=layout, element_justification="center", finalize=True, size=(720, 500), background_color='#03989E', icon='logo_robot.ico')

# Video de abertura
Tela = Tk()

photo = PhotoImage(file="logo.png")

Tela.iconphoto(False, photo)

Tela.title("ClerkBot")
Tela.geometry("720x500+600+200")
Tela.config(background="gray")
video = tkVideoPlayer.TkinterVideo(Tela, scaled=True)
video.load("clerkbot.mp4")
video.pack(expand=True, fill="both")
video.play()
Tela.after(8000, Tela.destroy)
Tela.mainloop()

inicial,enviar,remover,ajuda1, ajuda2, ajuda3 = janelaInicial(),None, None, None, None, None

# Leitura de eventos
while True:
    window,event,values = sg.read_all_windows()

    # Fechamento das janelas
    if window == inicial and event == sg.WIN_CLOSED:
        break
    if window == enviar and event == sg.WIN_CLOSED:
        break
    if window == remover and event == sg.WIN_CLOSED:
        break
    if window == ajuda1 and event == sg.WIN_CLOSED:
        break
    if window == ajuda2 and event == sg.WIN_CLOSED:
        break
    if window == ajuda3 and event == sg.WIN_CLOSED:
        break

    # Eventos do botão
    if window == inicial and event == "Bot":
        enviar = janelaEnviar()
        inicial.close()
        inicial = None
    if window == inicial and event == "Como funciona?":
        ajuda1 = help1()
        inicial.close()
        inicial = None

    # Como funciona primeira tela
    if window == ajuda1 and event == "Voltar":
        inicial = janelaInicial()
        ajuda1.close()
        ajuda1 = None
        
    if window == ajuda1 and event == "Continuar":
        ajuda2 = help2()
        ajuda1.close()
        ajuda1 = None

    # Como funciona segunda tela
    if window == ajuda2 and event == "Voltar":
        ajuda1 = help1()
        ajuda2.close()
        ajuda2 = None

    if window == ajuda2 and event == "Continuar":
        ajuda3 = help3()
        ajuda2.close()
        ajuda2 = None

    # Como funciona terceira tela
    if window == ajuda3 and event == "Voltar":
        ajuda2 = help2()
        ajuda3.close()
        ajuda3 = None

    if window == ajuda3 and event == "Tela Inicial":
        inicial = janelaInicial()
        ajuda3.close()
        ajuda3 = None

        
    # Adicionar e remover contato
    if window == enviar and event == "Voltar":
        inicial = janelaInicial()
        enviar.close()
        enviar = None
    if window == enviar and event == "Adicionar":
        contato = values['contato']
        if contato != "":
            listContato.append(contato)
            window['contatos'].update(listContato)
            window['contato'].update("")
        else:
            sg.popup_auto_close("Digite o contato")
            
    if window == enviar and event == "Remover":
        if len(listContato) > 0:
            remover = Remover()
            enviar.close()
            enviar = None
        else:
            sg.popup_auto_close("Você não pode excluir sem ter um contato")     

    # Adicionar e remover imagem
    if window == enviar and event == "Adicionar Imagem":
        imagem = str(values['img'])
        if imagem != "":
            newMsg = imagem.replace("/", "\\")
            listImages.append(newMsg)
            window['imgs'].update(len(listImages))
            window['img'].update("")
        else:
            sg.popup_auto_close("Selecione uma imagem para adicionar")
        
    if window == enviar and event == "Remover imagem":
        if len(listImages) > 0:
            listImages.pop()
            window['imgs'].update(len(listImages))
        else:
            sg.popup_auto_close("Não é possível remover sem ter adicionado uma imagem")
            
    # Adicionar e remover documento
    if window == enviar and event == "Adicionar documento":
        documento = str(values['doc'])
        if documento != "":
            newDoc = documento.replace("/", "\\")
            listDocs.append(newDoc)
            window['documentos'].update(len(listDocs))
            window['doc'].update("")
        else:
            sg.popup_auto_close("Selecione um documento para adicionar")
        
    if window == enviar and event == "Remover documento":
        if len(listDocs) > 0:
            listDocs.pop()
            window['documentos'].update(len(listDocs))
        else:
            sg.popup_auto_close("Não é possível remover sem ter adicionado um documento")
    
    # Começar a automatização   
    if window == enviar and event == "Enviar":
        mensagem = values['newMessage']
        documento = str(values['doc'])
        imagem = str(values['img'])
        if len(listContato) > 0 and (len(listDocs) > 0 or len(listImages) > 0 or mensagem != ""):
            sendMessage(mensagem, listContato, listImages, listDocs)
        else:
            sg.popup_auto_close("Adicione um contato e/ou digite uma mensagem")
            
    # Janela de remover contato 
    if window == remover and event == "Voltar":
        remover.close()
        remover = None
        enviar = janelaEnviar()
        
    if window == remover and event == "Remover":
        value = values['valueRemove']
        if value != "":   
            listContato.remove(value)
            window['valueContato'].update(listContato)
            window['valueRemove'].update("")
            loading = False
        else:
           sg.popup_auto_close("Digite o contato que deseja apagar") 
    if window == remover and event == "Remover tudo":
        listContato.clear()
        window['valueContato'].update(listContato)