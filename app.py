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

# criando planilha
list = openpyxl.Workbook()
list.create_sheet('produtos')
sheet_produtos = list['produtos']
sheet_produtos['A1'].value = 'Produtos(Computadores)'
sheet_produtos['B1'].value = 'Preços'

# inserir dados em uma planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text, preco.text])

# salvando a planilha
list.save('computadores.xlsx')
