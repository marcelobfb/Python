import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import keyboard
from time import sleep

options=Options()
options.add_argument('window-size=800,800')
navegador=webdriver.Chrome(options=options)
navegador.get('https://www.youtube.com.br')
sleep(2)
input_place=navegador.find_elements_by_tag_name('input')
input_place.send_key('São Paulo')
input_place.submit()



while True:
    if keyboard.is_pressed('-'):
        break