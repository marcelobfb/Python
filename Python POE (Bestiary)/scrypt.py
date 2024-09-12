import sys

import pyautogui
import cv2
import numpy as np
import time
import threading
from pynput import keyboard

thread_result = None

time.sleep(2)
orb_da_bestiary = cv2.imread('orbdabestiary.png')
espaco_vazio = cv2.imread('espacovazio.PNG')
imagens_das_bestas = [cv2.imread(f'besta{i}.png') for i in range(1, 10)]


def tira_print():
    screen = pyautogui.screenshot()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen


def encontrar_imagem(screen, imagem_alvo, lado='esquerdo'):
    global thread_result
    if lado == 'esquerdo':
        screen = screen[0:1080, 0:960]
    elif lado == 'direito':
        screen = screen[0:1080, 960:1920]

    resultado = cv2.matchTemplate(screen, imagem_alvo, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    if max_val > 0.8:
        thread_result = max_loc
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


def encontra_imagem_com_multiplos_templates(screen, imagens, lado='esquerdo'):
    global thread_result
    thread_result = None
    threads = []
    for imagem in imagens:
        t = threading.Thread(target=encontrar_imagem, args=[screen, imagem, lado])
        t.start()
        threads.append(t)

    while True:
        completed_threads = 0
        for th in threads:
            if not th.is_alive():
                completed_threads += 1
        
        if completed_threads == len(threads):
            break

    return thread_result


x = threading.Thread(target=thread_function)
x.start()

while True:
    if parado:
        break
    printola = tira_print()
    orb_location = encontrar_imagem(printola, orb_da_bestiary, 'direito')
    if orb_location:
        x, y = orb_location
        pyautogui.moveTo(x + 980, y + 20, 0.1)
        pyautogui.rightClick()
        besta_location = encontra_imagem_com_multiplos_templates(printola, imagens_das_bestas)
        if besta_location:
            x, y = besta_location
            pyautogui.moveTo(x + 20, y + 20, 0.1)
            pyautogui.leftClick()

            espaco_vazio_location = encontrar_imagem(printola, espaco_vazio, 'direito')

            if espaco_vazio_location:
                x, y = espaco_vazio_location
                pyautogui.moveTo(x + 980, y + 20, 0.1)
                pyautogui.leftClick()
                pyautogui.moveTo(900, 500)
        else:
            rolar_roleta()

    else:
        break
