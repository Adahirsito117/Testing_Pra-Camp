from selenium import webdriver

#A - Preparar
driver = webdriver.Chrome()

#A - Ejecutar
driver.get("https://alexanderggfi.github.io/IS2026-2-Sistema-de-Practicas-de-Campo/")

#A - Verificar
assert driver.title=="Login"
print("El sistema cargó correctamente")
print("Título:", driver.title)

#limpiar
driver.quit()