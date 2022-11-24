import PySimpleGUI as sg
from backChatBot import sendMessage
from time import sleep

listContato = []
loading = True
# Criar janela e layouts
def janelaEnviar():
    sg.theme('Reddit')
    layout =[
        [sg.Text("Enviar mensagens", font="arial 24", justification="center")],
        [sg.Text("Digite o nome do contato e/ou grupo", font="arial 10")],
        [sg.Text("Contato:", font="arial 12"),sg.Input(key="contato", size=(25,2), font="arial 12"),sg.Button("Adicionar")],
        [sg.Text("Contatos:",font="arial 12"),sg.Text("", key="contatos", font="arial 12", size=(25,2)),sg.Button("Remover")],
        [sg.Text("Digite sua mensagem:", font="arial 12")],
        [sg.Multiline(key="newMessage", size=(45,5))],
        [sg.Button("Enviar", font="arial 13")],
    ]
    
    return sg.Window('ClerkBot', layout=layout, element_justification="center", finalize=True)

def Remover():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Digite o nome do contato para remover")],
        [sg.Input(key="valueRemove")],
        [sg.Text("Contatos:"),sg.Text(f"{listContato}" , key="valueContato", size=(30,2))],
        [sg.Button("Voltar"), sg.Button("Remover")]
    ]
    return sg.Window("ClerkBot",layout= layout,element_justification="center", finalize=True)

# Criar janelas 
enviar,remover = janelaEnviar(), None
# Leitura de eventos
while True:
    window,event,values = sg.read_all_windows()
    # Fechar a janela
    if window == enviar and event == sg.WIN_CLOSED:
        break
    if window == remover and event == sg.WIN_CLOSED:
        break
    # Eventos do botão
    if window == enviar and event == "Remover":
        if len(listContato) > 0:
            remover = Remover()
            enviar.close()
            enviar = None
        else:
            sg.popup_auto_close("Você não pode excluir sem ter um contato")
     
    if window == enviar and event == "Adicionar":
        contato = values['contato']
        if contato != "":
            listContato.append(contato)
            window['contatos'].update(listContato)
            window['contato'].update("")
        else:
            sg.popup_auto_close("Digite o contato")
         
    if window == enviar and event == "Enviar":
        mensagem = values['newMessage']
        if mensagem != "" and len(listContato) > 0:
            sendMessage(mensagem, listContato)
        else:
            sg.popup_auto_close("Adicione um contato e/ou digite uma mensagem")
        
    if window == remover and event == "Voltar":
        remover.close()
        remover = None
        enviar = janelaEnviar()
        
    if window == remover and event == "Remover":
        value = values['valueRemove']
        if value != "":   
            listContato.remove(value)
            window['valueContato'].update("" if len(listContato) < 0 else listContato)
            window['valueRemove'].update("")
            loading = False
        else:
           sg.popup_auto_close("Digite o contato que deseja apagar") 
