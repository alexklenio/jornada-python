import pyautogui
from time import sleep

#https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.press("win")
sleep(1)
pyautogui.write("chrome")