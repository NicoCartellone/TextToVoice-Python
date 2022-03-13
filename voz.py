from typing import Text
import pyttsx3
import msvcrt

menu = """
Menu
1-Ejecutar programa
2-Salir

"""

pop = True
while pop == True:
    print(menu)
    op = int(input("Elija la opcion deseada: "))
    if op == 1:
        engine = pyttsx3.init()

        engine.setProperty("rate", 140)
        Text = (input("Ingrese el texto: "))
        engine.say(Text)

        engine.runAndWait()

    elif op == 2:
        exit()
    else:
        print("opcion invalida")

msvcrt.getch()
