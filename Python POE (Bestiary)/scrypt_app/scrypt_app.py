import sys
import pyautogui
import cv2
import numpy as np
import time
import threading
from pynput import keyboard


time.sleep(2)
orb_da_bestiary = cv2.imread('orbdabestiary.png')
espaco_vazio = cv2.imread('espacovazio.PNG')
imagens_das_bestas = [cv2.imread(f'besta{i}.png') for i in range(1, 8)]


def encontrar_imagem(imagem_alvo):
    screen = pyautogui.screenshot()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    resultado = cv2.matchTemplate(screen, imagem_alvo, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    if max_val > 0.8:
        return max_loc
    else:
        return None


def rolar_roleta():
    pyautogui.scroll(-1)


parado = False


def parar(key):
    global parado
    if key == keyboard.Key.esc:
        parado = True
        sys.exit()


def thread_function():
    listener = keyboard.Listener(on_press=parar)
    listener.start()
    listener.join()


x = threading.Thread(target=thread_function)
x.start()

while True:
    if parado:
        print(parado)
        break
    orb_location = encontrar_imagem(orb_da_bestiary)
    if orb_location:
        x, y = orb_location
        pyautogui.moveTo(x + 20, y + 20, 0.2)
        pyautogui.rightClick()
        for imagem_da_besta in imagens_das_bestas:
            besta_location = encontrar_imagem(imagem_da_besta)
            if besta_location:
                x, y = besta_location
                pyautogui.moveTo(x + 20, y + 20, 0.2)
                pyautogui.leftClick()

                espaco_vazio_location = encontrar_imagem(espaco_vazio)

                if espaco_vazio_location:
                    x, y = espaco_vazio_location
                    pyautogui.moveTo(x + 20, y + 20, 0.2)
                    pyautogui.leftClick()
                    pyautogui.moveTo(900, 500)
                    break
            else:
                rolar_roleta()

    else:
        break
    