from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#A - Preparar
driver = webdriver.Chrome()
driver.get("https://alexanderggfi.github.io/IS2026-2-Sistema-de-Practicas-de-Campo/")

#A - Ejecutar
campos = driver.find_elements(By.CLASS_NAME,"entradaTexto")

campos[0].send_keys("no_existe@gmail.com")
campos[1].send_keys("no_123")

driver.find_element(By.ID,"btnIngresar").click()

time.sleep(5)

mensaje = driver.find_element(By.ID,"mensaje").text

#A - Verificar
assert mensaje == "Credenciales incorrectas"
print("El login si funciono correctamente macho tio oztia")
driver.save_screenshot("evidencias/testLoginFallido.png")
print("La captura se guardó correctamente")

#limpiar
driver.quit()