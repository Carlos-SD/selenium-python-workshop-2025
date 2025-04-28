from behave import given, when, then
from selenium import webdriver
from pages.mercadolibre_search_page import SearchItem

@given('el usuario se encuentra en la seccion de busqueda de mercadolibre')
def step_given_mercadolibre_search(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co/')
    context.search_page = SearchItem(context.driver)

@when('el usuario escribe Iphone 13')
def step_when_mercadolibre_search(context):
    context.search_page.search_item("Iphone 13")

@then('aparecen resultados que contienen el texto Iphone')
def step_then_mercadolibre_search(context):
    assert "Iphone"  ==  context.search_page.isElementPresent()