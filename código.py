import pyautogui
import time

def function1():
    
    #SITE DA PREFEITURA -----------------------------------------------------------------------
    
    boletimDia = str(input( "Boletim do dia: "))
    pyautogui.alert("Aperte no OK ou feche essa janela para o programa começar", "Prefeitura", "OK")
    time.sleep(1)
    # Entra na aba covid
    pyautogui.moveTo(433, 128)
    pyautogui.moveTo(389, 395)
    pyautogui.click(627, 396)
    time.sleep(1)
    ## Cadastrar
    pyautogui.click(944, 628)
    time.sleep(2)
    #Selecionar Informações gerais e evolução de casos
    pyautogui.click(547, 212)
    time.sleep(1)
    pyautogui.click(477, 209)
    time.sleep(1)
    pyautogui.click(551, 243)
    time.sleep(1)
    pyautogui.click(488, 189)
    time.sleep(1)
    #Anexar foto
    pyautogui.click(412, 168)
    time.sleep(1)
    pyautogui.click(1046, 236)
    time.sleep(1)
    pyautogui.moveTo(128, 702)
    time.sleep(1)
    pyautogui.mouseDown(128, 702, button='left')
    pyautogui.moveTo(436, 301, duration=0.5)
    time.sleep(1)
    pyautogui.mouseUp(436, 301)
    time.sleep(1)
    #Escrever Boletim do dia no anexo
    pyautogui.click(442, 274)
    pyautogui.write("boletim " + boletimDia)
    #Colar texto
    pyautogui.click(293, 173)
    time.sleep(1)
    pyautogui.click(1149, 656, clicks= 30)
    time.sleep(1)
    pyautogui.click(587, 476)
    pyautogui.hotkey('ctrl', 'v')
    #Escrever boletim do dia nos dados gerais
    pyautogui.click(691, 250)
    pyautogui.write("Boletim " + boletimDia)
    #Salvar
    time.sleep(1)
    pyautogui.click(936, 641)
    time.sleep(1)

    ##INSTAGRAM --------------------------------------------------------------------------
    
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(1)
    pyautogui.click(991, 130)
    pyautogui.mouseDown(128, 702, button='left')
    pyautogui.moveTo(681, 417, duration=0.5)
    time.sleep(1)
    pyautogui.mouseUp(681, 417)
    time.sleep(1)
    pyautogui.click(539, 554)
    time.sleep(1)
    pyautogui.click(583, 348)
    time.sleep(1)
    pyautogui.click(817, 214)
    time.sleep(1)
    pyautogui.click(858, 349)
    time.sleep(1)
    pyautogui.click(978, 210)
    time.sleep(1)
    pyautogui.click(816, 311)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(952, 210)

    #FACEBOOK ------------------------------------------------------------------------------
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(1)
    pyautogui.click(1355, 111, clicks= 30)
    time.sleep(1)
    pyautogui.click(1355, 663, clicks= 10)
    time.sleep(1)
    pyautogui.click(1052, 454)
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.moveTo(128, 702)
    time.sleep(1)
    pyautogui.mouseDown(128, 702, button='left')
    pyautogui.moveTo(634, 391, duration=0.5)
    time.sleep(1)
    pyautogui.mouseUp(634, 391)
    time.sleep(4)
    pyautogui.click(661, 634)
    return 0

def switch(case):
    if case == "1":
        return function1
    else:
        return 0

case = ''
while (case != '1'):
    
    case = str(input('Digite qual opção você quer: '))
    
    if case != '1':
        print("Opção inválida.")

function = switch(case)
function()
