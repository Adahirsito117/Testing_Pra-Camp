import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

URL="https://alexanderggfi.github.io/IS2026-2-Sistema-de-Practicas-de-Campo/"

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()

def testCargaPagina(driver):
    driver.get(URL)
    assert driver.title=="Login"

def testLoginCorrecto(driver):
    driver.get(URL)
    campos = driver.find_elements(By.CLASS_NAME,"entradaTexto")
    campos[0].send_keys("hormigaglez@gmail.com")
    campos[1].send_keys("armandoalba")
    driver.find_element(By.ID,"btnIngresar").click()
    time.sleep(2)
    try:
        assert "principal.html" in driver.current_url
    except:
        os.makedirs("evidencias",exist_ok=True)
        driver.save_screenshot("evidencias/test_fallido.png")
        raise

def testLoginIncorrecto(driver):
    driver.get(URL)
    campos = driver.find_elements(By.CLASS_NAME,"entradaTexto")
    campos[0].send_keys("no_esta@gmail.com")
    campos[1].send_keys("no_123")
    driver.find_element(By.ID,"btnIngresar").click()
    time.sleep(2)
    try:
        assert driver.find_element(By.ID,"mensaje").text=="Credenciales incorrectas"
    except:
        os.makedirs("evidencias",exist_ok=True)
        driver.save_screenshot("evidencias/test_fallido.png")
        raise