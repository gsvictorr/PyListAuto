from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# Acessar a página abaixo e buscar os títulos e preços dos computadores
# página
# https://www.kabum.com.br/computadores/pc/all-in-one
web = webdriver.Chrome()
web.get('https://www.kabum.com.br/computadores/pc/all-in-one')

# título
# tag span atributo class="sc-d79c9c3f-0 nlmfp sc-cdc9b13f-16 eHyEuD nameCard"

titulos = web.find_elements(
    By.XPATH, "//span[@class='sc-d79c9c3f-0 nlmfp sc-cdc9b13f-16 eHyEuD nameCard']")

# preço
# tag span atributo class="sc-620f2d27-2 bMHwXA priceCard"
precos = web.find_elements(
    By.XPATH, "//span[@class='sc-620f2d27-2 bMHwXA priceCard']")


# inserir dados em uma planilha
