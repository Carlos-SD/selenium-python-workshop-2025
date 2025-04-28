from behave import given, when, then
from selenium import webdriver
from pages.wikipedia_article_page import SearchArticle

@given('el usuario se encuentra en la seccion de busqueda de wikipedia')
def step_given_wikipedia_search(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://es.wikipedia.org/wiki/Wikipedia:Portada')
    context.wikipedia_article_page = SearchArticle(context.driver)

@when('el usuario escribe Python')
def step_when_wikipedia_search(context):
    context.wikipedia_article_page.search_item("Python (lenguaje de programación)")

@then('aparece un articulo con el titulo Python')
def step_then_wikipedia_search(context):
    assert "Python" == context.wikipedia_article_page.isElementPresent()