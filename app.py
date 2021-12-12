import pyshorteners, clipboard, webbrowser
import PySimpleGUI as sg
from time import sleep

#      _     _       _      ____  _                _                       
#     | |   (_)_ __ | | __ / ___|| |__   ___  _ __| |_ ___ _ __   ___ _ __ 
#     | |   | | '_ \| |/ / \___ \| '_ \ / _ \| '__| __/ _ \ '_ \ / _ \ '__|
#     | |___| | | | |   <   ___) | | | | (_) | |  | ||  __/ | | |  __/ |   
#     |_____|_|_| |_|_|\_\ |____/|_| |_|\___/|_|   \__\___|_| |_|\___|_|   
#                                                                          

#     Software desenvolvido por Elizeu Barbosa Abreu
 
sg.theme('DarkTanBlue')

def clear():
    window['-output-'].update(short_link)
    window['-b-'].update(visible=True) 

def error():
    sg.popup_timed('Serviço temporariamente indisponível! \nEscolha outro encurtador ou confira sua conexão à internet!!!')

def sobre():
    return sg.popup(
        'Sobre o Software',
        '''PyShortenerURL é um encurtador de links desenvolvido 100% em Python por Elizeu Barbosa Abreu...

Conheça outros projeto do autor navegando pelo menu: Ajuda->Autor-> GitHub...
Visite e siga meu perfil no LInkedin: Ajuda->Autor-> Linkedin...

Obrigado por usar nossos softwares s2
'''
        )

menu = [
    ['&Arquivo', ['&Colar', '---', '&Sair']],
    ['&Ajuda',['&Sobre', '---', '&Autor',['&GitHub', '&Linkedin']]]
    ]

layout = [
    [sg.Menu(menu)],
    [sg.Text(size=(1, 3))],
    [sg.Stretch(),
     sg.Text('Digite ou cole o link a ser encurtado: ', size=(40,1)),
     sg.Stretch()],
     [sg.Stretch(),
      sg.Input(key='-url-', size=(40, 1)),
      sg.Stretch()],
     [sg.Stretch(), sg.Text('Serviço:'),
      sg.Combo(['isgd', 'tinyurl', 'dagd', '0x0.st', 'ttm.sh', 'osdb', 'owly', 'qpsru'], default_value='ttm.sh', key='-service-'),
     sg.Button('Encurtar Link'),
     sg.Stretch()],
    [sg.Stretch(),
     sg.Text(key='-output-'),
     sg.Button('Copiar o link Gerado', visible=False, key='-b-'),
     sg.Stretch()],
    [sg.Text(size=(1, 4))],
    ]

window = sg.Window('PyShortenerURL', layout, size=(480, 220))
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event in ('Sair'):
        break
    
    elif event in ('Colar'):
        window['-url-'].update(clipboard.paste())
        
    elif event in ('Sobre'):
        sobre()
        
    elif event in ('GitHub'):
        webbrowser.open_new_tab('https://github.com/elizeubarbosaabreu')
    
    elif event in ('Linkedin'):
        webbrowser.open_new_tab('https://www.linkedin.com/in/elizeu-barbosa-abreu-69965b218/')
    
    elif event in ('Encurtar Link'):
        url = values['-url-']
        
        if url == '':
            sg.popup_timed('Entre com um link válido!!!')
        else:
            if values['-service-'] == 'tinyurl':
                try:
                    s = pyshorteners.Shortener()
                    short_link = s.tinyurl.short(url)
                    clear()                         
                     
                except:
                    error()
            
            if values['-service-'] == 'isgd':
                try:
                    s = pyshorteners.Shortener()
                    short_link = s.isgd.short(url)
                    clear()                          
                     
                except:
                    error()
                    
            if values['-service-'] == 'dagd':
                try:
                    s = pyshorteners.Shortener()
                    short_link = s.dagd.short(url)
                    clear()                          
                     
                except:
                    error()
                    
            if values['-service-'] == '0x0.st':
                try:
                    s = pyshorteners.Shortener(domain='https://0x0.st')
                    short_link = s.nullpointer.short(url)
                    clear()                          
                     
                except:
                    error()
                        
            if values['-service-'] == 'ttm.sh':
                try:
                    s = pyshorteners.Shortener(domain='https://ttm.sh')
                    short_link = s.nullpointer.short(url)
                    clear()                          
                     
                except:
                    error()
                        
            if values['-service-'] == 'osdb':
                try:
                    s = pyshorteners.Shortener()
                    short_link = s.osdb.short(url)
                    clear()                          
                     
                except:
                    error()
                        
            if values['-service-'] == 'owly':
                try:
                    s = pyshorteners.Shortener()
                    short_link = s.owly.short(url)
                    clear()                          
                     
                except:
                    error()
                    
            if values['-service-'] == 'qpsru':
                try:
                    s = pyshorteners.Shortener()
                    short_link = s.qpsru.short(url)
                    clear()                          
                     
                except:
                    error()
                  
    elif event in ('-b-'): 
        clipboard.copy(short_link)
        sg.popup_timed('Link copiado para a área de transferência')
        sleep(0.3)
        
        window['-b-'].update(visible=False)
        window['-output-'].update('')

window.close()
