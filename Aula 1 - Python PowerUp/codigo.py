import pyautogui
from time import sleep
import pandas as pd

#https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas


pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")  

pyautogui.press("enter")
sleep(3)
pyautogui.click(x=765, y=377)
sleep(2)

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
sleep(1)
pyautogui.press("enter")
sleep(1)

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=660, y=410, clicks=2)

sleep(1)

# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
sleep(1)
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")
sleep(3)
pyautogui.click(x=850, y=362)
sleep(1)

tabela = pd.read_csv("produtos.csv")
print(tabela)



for linha in tabela.index:
    pyautogui.click(x=640, y=294)

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    pyautogui.scroll(5000)