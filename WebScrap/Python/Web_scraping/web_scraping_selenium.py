from selenium import webdriver
import keyboard


navegador = webdriver.Chrome()
navegador.get('https://www.amazon.com.br')
while True:
    if keyboard.is_pressed('-'):
        break