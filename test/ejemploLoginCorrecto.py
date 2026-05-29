from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#A - Preparar
driver = webdriver.Chrome()
driver.get("https://alexanderggfi.github.io/IS2026-2-Sistema-de-Practicas-de-Campo/")

#A - Ejecutar
campos = driver.find_elements(By.CLASS_NAME,"entradaTexto")

campos[0].send_keys("hormigaglez@gmail.com")
campos[1].send_keys("armandoalba")

driver.find_element(By.ID,"btnIngresar").click()

time.sleep(5)

#A - Verificar
assert "principal.html" in driver.current_url
print("El login si funciono correctamente macho tio oztia")

#limpiar
driver.quit()