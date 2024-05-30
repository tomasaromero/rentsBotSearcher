import pyautogui, time

# Considero las siguientes ventanas abiertas: wpp web y https://www.zonaprop.com.ar 
# print(pyautogui.position()), donde esta el mouse
# para saber tamaño de su pantalla ==> print(pyautogui.size())
time.sleep(3)
# Mouse Functions
#print(pyautogui.size())
print(pyautogui.position())
print(pyautogui.size())
#Move the mouse over time(3 secs)
#pyautogui.moveTo(100,100,3)

#Move the mouse relative to its currents position
#pyautogui.moveRel(100,100,3)

#Click
#pyautogui.click(500,500,3,3,button="left")
#pyautogui.doubleClick(500,500,3,3,button="left")
#pyautogui.rightClick(100,100,3,3)

#Scroll up||down
#pyautogui.scroll(-500)
#pyautogui.scroll(500)
#pyautogui.doubleClick(3044,295,button="left")
#----------------------------------------------------------------------------------------------------
#comprar
#pyautogui.click(2647, 415,3,button="left")
#capital federal
time.sleep(1)
pyautogui.click(2793, 465,3,button="left")
time.sleep(1.5)
pyautogui.typewrite("cap")
time.sleep(1)
pyautogui.click(2686, 513,3,button="left")
#buscar
time.sleep(1)
pyautogui.click(3244,463,3,button="left")
time.sleep(5)
#mas filtros
time.sleep(1)
pyautogui.click( 3025,184,3,button="left")
time.sleep(1)
#supCubierta
pyautogui.click(2769, 453,3,button="left")
pyautogui.typewrite("32")
time.sleep(1)
pyautogui.click(2918, 449,3,button="left")
pyautogui.typewrite("75")
#fechaPublicacion
time.sleep(1)
pyautogui.scroll(-200)
time.sleep(1)
pyautogui.click(2656,831,3,button="left")#(hoy)
#luminoso
time.sleep(1)
pyautogui.scroll(230)
pyautogui.click(2731, 293,3,button="left")
time.sleep(1)
pyautogui.typewrite("luminoso")
time.sleep(1)
pyautogui.click(2686, 333,3,button="left")
pyautogui.click(2990,922,3,button="left")#verRES
#ambientes
time.sleep(2)
pyautogui.click(2783,187,3,button="left")
time.sleep(0.5)
pyautogui.click(2767,289,3,button="left")
time.sleep(0.5)
pyautogui.click(2782,426,3,button="left")#2
#precio
time.sleep(1)
pyautogui.click(2888,181,3,button="left")
time.sleep(0.5)
#pyautogui.click(2944,287,3,button="left")#usd
pyautogui.click(2901,348,3,button="left")
time.sleep(0.5)
pyautogui.typewrite("30000")
time.sleep(0.8)
pyautogui.click(3044,335,3,button="left")
pyautogui.typewrite("70000")
pyautogui.click(3049,663,3,button="left")
#masVistos
time.sleep(2)
pyautogui.click(3540,285,3,button="left")
pyautogui.click(3502,328,3,button="left")
#mapa
time.sleep(5)
pyautogui.click(3336,275,3,button="left")
time.sleep(3)
pyautogui.moveTo(2871,707)#cerca de este punto al mapa mostrarte CABA,zoom
pyautogui.scroll(6000)
time.sleep(1)
pyautogui.scroll(6000)
time.sleep(1)
pyautogui.scroll(6000)
time.sleep(1)
pyautogui.scroll(6000)
time.sleep(1)
pyautogui.scroll(6000)
pyautogui.click(2971, 1001,3,button="left")
time.sleep(1)
pyautogui.click(3655,289,3,button="left")
#links


i=0
while i< 5 :
    pyautogui.moveTo(2656, 428, 1)
    time.sleep(1)
    pyautogui.click(2656, 428, 3, button="left")
    time.sleep(1)
    pyautogui.tripleClick(2557, 52, button="left")
    pyautogui.click(button="right")
    pyautogui.moveRel(50, 215, 1)
    pyautogui.click(button="left")#copioLinkPublicacion
    pyautogui.click(2058,10,3,button="left")#cambio pestaña a wpp
    pyautogui.click(2264, 260, 3, button="left")  # buscoDondeMandarlo
    pyautogui.typewrite("Dptos caballito")
    time.sleep(1)
    pyautogui.press("Enter")
    pyautogui.click(2855, 976, 3, button="left")  # pegoLink
    pyautogui.click(button="right")
    pyautogui.moveRel(50, -335, 1)
    pyautogui.click(button="left")
    pyautogui.press("Enter")#envio
    pyautogui.click(2665, 14, 3, button="left")  # cierroPestaña,sino modifica tamaño de labels
    time.sleep(1)
    pyautogui.click(2365, 8, 3, button="left")  # cambio pestaña a ZonaProp
    pyautogui.moveTo(2656, 428,3)
    pyautogui.scroll(-227)
    time.sleep(1)
    i+=1








