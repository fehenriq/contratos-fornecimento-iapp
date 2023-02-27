from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

email = ""
senha = ""
cliente = "GIMI INSTITUTO DE RADIOL. E ULTRASSONOGRAFIA LTDA"
nome_contato = "NOME CONTATO PROPOSTA"

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
actions = ActionChains(browser)

browser.get("https://ia1.iapp03.iniciativaaplicativos.com.br/home")

browser.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(senha)

captcha = browser.find_element(By.XPATH, "//div[@class='g-recaptcha']")
ActionChains(browser).move_to_element(captcha).click().perform()
sleep(10)

browser.find_element(By.XPATH, '//*[@id="form_login"]/button').click()

browser.maximize_window()

for i in range(261):
  sleep(2)
  
  browser.find_element(By.XPATH, '/html/body/aside/div/div[2]/ul/li[7]/a').click()
  sleep(1)
  browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[3]/div/div/div/div[1]/div/a').click()
  sleep(1)
  browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div/div[2]/div/a').click()
  sleep(1)
  
  browser.find_element(By.XPATH, '//*[@id="select2-cliente-container"]').click()
  campo_cliente = browser.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
  campo_cliente.send_keys(cliente)
  sleep(15)
  campo_cliente.send_keys(Keys.ENTER)
  
  browser.find_element(By.XPATH, '//*[@id="form_contrato"]/div[3]/div/div/div[2]/div/div/button').click()
  browser.find_element(By.XPATH, '//*[@id="bs-select-1-137"]').click()
  
  browser.find_element(By.XPATH, '//*[@id="form_contrato"]/div[3]/div/div/div[3]/div/input').send_keys(nome_contato)
  
  browser.find_element(By.XPATH, '//*[@id="form_contrato"]/div[3]/div/div/div[5]/div/div/button').click()
  browser.find_element(By.XPATH, '//*[@id="bs-select-2-3"]').click()
  
  browser.find_element(By.XPATH, '//*[@id="form_contrato"]/div[3]/div/div/div[6]/div/div/button').click()
  browser.find_element(By.XPATH, '//*[@id="bs-select-3-1"]').click()
  
  browser.find_element(By.XPATH, '//*[@id="form_contrato"]/div[3]/div/div/div[8]/div/div/button').click()
  browser.find_element(By.XPATH, '//*[@id="bs-select-4"]/ul/li[17]').click()
  
  browser.find_element(By.XPATH, '//*[@id="form_contrato"]/div[3]/div/div/div[9]/div/div/button').click()
  browser.find_element(By.XPATH, '//*[@id="bs-select-5-1"]').click()
  
  browser.find_element(By.XPATH, '//*[@id="form_contrato"]/div[3]/div/div/div[10]/div/div/button').click()
  browser.find_element(By.XPATH, '//*[@id="bs-select-6-1"]').click()
  
  browser.find_element(By.XPATH, '//*[@id="salvar_rascunho"]').click()
  
  sleep(3)
  