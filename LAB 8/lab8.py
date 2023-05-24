from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

@given('Otwieram stronę główną sklepu z ogórkami')
def step_impl(context):
    driver.get("https://example.com/sklep")  # Zastąp URL adresem strony z ogórkami

@when('Wybieram pierwszy ogórek z listy dostępnych produktów')
def step_impl(context):
    pierwszy_ogorek = driver.find_element_by_css_selector("div.produkt:nth-child(1)")
    pierwszy_ogorek.click()

@when('Dodaję ogórek do koszyka')
def step_impl(context):
    dodaj_do_koszyka_btn = driver.find_element_by_css_selector("button.dodaj-do-koszyka")
    dodaj_do_koszyka_btn.click()

@when('Wpisuję "{tekst}" w pole wyszukiwania')
def step_impl(context, tekst):
    pole_wyszukiwania = driver.find_element_by_css_selector("input#search-input")
    pole_wyszukiwania.send_keys(tekst)

@when('Klikam przycisk "Szukaj"')
def step_impl(context):
    przycisk_szukaj = driver.find_element_by_css_selector("button.szukaj-btn")
    przycisk_szukaj.click()

@when('Klikam na link ze szczegółami ogórka')
def step_impl(context):
    link_szczegoly = driver.find_element_by_css_selector("a.szczegoly-link")
    link_szczegoly.click()

@when('Przechodzę do koszyka')
def step_impl(context):
    koszyk_btn = driver.find_element_by_css_selector("a.koszyk-btn")
    koszyk_btn.click()

@when('Klikam przycisk "Zamów teraz"')
def step_impl(context):
    zamow_teraz_btn = driver.find_element_by_css_selector("button.zamow-teraz")
    zamow_teraz_btn.click()

@when('Wprowadzam wymagane dane do złożenia zamówienia')
def step_impl(context):
    # Wprowadź odpowiednie dane do formularza
    pass

@when('Potwierdzam zamówienie')
def step_impl(context):
    potwierdz_btn = driver.find_element_by_css_selector("button.potwierdz")
    potwierdz_btn.click()

@then('Ogórek zostaje dodany do koszyka')
def step_impl(context):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.koszyk")))
    assert "Produkt dodany do koszyka" in driver.page_source

@then('Wyświetlają się wyniki wyszukiwania zawierające ogórki')
def step_impl(context):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.wyniki-wyszukiwania")))
    assert "ogórek" in driver.page_source

@then('Wyświetlają się szczegóły wybranego ogórka')
def step_impl(context):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.szczegoly-ogorka")))
    assert "Szczegóły ogórka" in driver.page_source

@then('Zamówienie zostaje pomyślnie złożone')
def step_impl(context):
    # Dodaj asercję sprawdzającą, czy zamówienie zostało złożone pomyślnie
    pass
