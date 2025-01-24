import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

tabela = pd.read_excel("pd_sla_list.xlsx")

# Configura as opções do navegador
options = Options()
options.add_argument("--start-maximized") 

# Configura o ChromeDriver usando o WebDriver Manager
service = Service(ChromeDriverManager().install())

# Inicializa o WebDriver com o serviço e as opções
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)

# Abre a URL desejada
driver.get("https://servicedesk.colibri.capital/front/slm.form.php?id=1")

# Inputando usuário
usuario = driver.find_element(By.XPATH, "//input[@id='login_name']")
usuario.send_keys("bot.colibri24")

# Inputando a senha
senha = driver.find_element(By.XPATH, "//input[@id='login_password']")
senha.send_keys("Botcolibr!@DESK24scripts")

# Pressionando Enter após preencher ambos
senha.send_keys(Keys.ENTER)

# Navegando para o link desejado

slas = driver.find_element(By.XPATH, "//a[@id='ui-id-4']") #lendo pela id do elemento
time.sleep(3)
slas.click()

btnaddd_sla = driver.find_element(By.XPATH, "//a[text()='Adicionar um novo item']") # lendo pelo conteudo do elemento (texto)
btnaddd_sla.click()

campo_texto = driver.find_element(By.CSS_SELECTOR,"input[name='name']")
campo_texto.send_keys('Seu Texto Aqui')

input()

# for para ler a planilha
# for index, row in tabela.iterrows():
#     btnaddd_sla = driver.find_element(By.XPATH, "//a[text()='Adicionar um novo item']") # lendo pelo conteudo do elemento (texto)
#     btnaddd_sla.click()
#     #name_sla = driver.find_element(By.XPATH, "//input[@type='text']")
#     #name_sla = driver.find_element(By.CSS_SELECTOR, "textfield_name")
#     name_sla = driver.find_element(By.TAG_NAME, "name")
#     name_sla.send_keys("oiiiiiiiiiiii")
#     name_sla.clear()
#     time.sleep(2)
    

# Aguarda para evitar o fechamento do navegador
input("Pressione Enter para encerrar...")

