import sys
import pandas as pd
import os
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
load_dotenv()



tabela = pd.read_excel("pd_sla_list 1.xlsx")

driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = str(os.getenv("ServiceDeskUrl"))
driver.get(url)

pyautogui.press("f11")
_usuario = os.getenv("User")
_senha = os.getenv("Pass")

usuario = driver.find_element(By.XPATH, "//input[@id='login_name']")
senha = driver.find_element(By.XPATH, "//input[@id='login_password']")

usuario.send_keys(_usuario)
senha.send_keys(_senha)
time.sleep(1)
senha.send_keys(Keys.RETURN)
time.sleep(2)




for index, row in tabela.iterrows():    
    driver.get(os.getenv("ServiceLevelUrl"))
    time.sleep(3)
    SLAs_barra_lateral = driver.find_element(By.XPATH, "//a[@id='ui-id-4']")
    SLAs_barra_lateral.click()
    
    adicionar_novo_sla = driver.find_element(By.XPATH, "//a[text()='Adicionar um novo item']")
    adicionar_novo_sla.click()

    time.sleep(5)
    pyautogui.click(x=697, y=347)
    time.sleep(2)
    adicionar_novo_sla = driver.switch_to.active_element
    adicionar_novo_sla.send_keys(row["SLAS"])
    
    tempo = driver.find_element(By.XPATH, "//span[text()='4']")
    tempo.click()
    
    time.sleep(1)
    tempo = driver.switch_to.active_element
    tempo.send_keys("16")
    time.sleep(1)
    tempo.send_keys(Keys.ENTER)
    time.sleep(2)

    tipo = driver.find_element(By.XPATH, "//span[text()='Tempo para atendimento']")
    tipo.click()
    trocar_para_solucao = driver.find_element(By.XPATH, "//span[text()='Tempo para solução']")
    trocar_para_solucao.click()
    time.sleep(3)
    
    adicionar_definitivo =  driver.find_element(By.XPATH, "//button[@name='add']")
    adicionar_definitivo.click()
    time.sleep(3)
    print(f"Adicionado: {row["SLAS"]}")

# time.sleep(5)
# print(pyautogui.position())


input()