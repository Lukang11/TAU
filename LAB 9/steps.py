from behave import given, when, then

@given('Jestem na stronie logowania')
def step_given_jestem_na_stronie_logowania(context):
    context.driver.visit("https://example.com/login")

@when('Wprowadzam poprawne dane logowania')
def step_when_wprowadzam_poprawne_dane_logowania(context):
    context.driver.fill("input[name='username']", "moj_login")
    context.driver.fill("input[name='password']", "moje_haslo")

@when('Klikam przycisk "Zaloguj"')
def step_when_klikam_przycisk_zaloguj(context):
    context.driver.click("button[type='submit']")

@then('Powinienem zostać zalogowany i widzieć stronę główną')
def step_then_powinienem_zostac_zalogowany_i_widziec_strone_glowna(context):
    assert context.driver.url == "https://example.com/home"
    assert "Witaj" in context.driver.text

@given('Jestem zalogowany na stronie')
def step_given_jestem_zalogowany_na_stronie(context):
    context.driver.visit("https://example.com/home")

@when('Wybieram produkt z listy dostępnych')
def step_when_wybieram_produkt_z_listy_dostepnych(context):
    context.driver.click("a.produkt")

@when('Dodaję produkt do koszyka')
def step_when_dodaje_produkt_do_koszyka(context):
    context.driver.click("button.dodaj-do-koszyka")

@then('Powinienem zobaczyć komunikat o dodaniu do koszyka')
def step_then_powinienem_zobaczyc_komunikat_o_dodaniu_do_koszyka(context):
    assert "Produkt został dodany do koszyka" in context.driver.text

@then('Koszyk powinien zawierać dodany produkt')
def step_then_koszyk_powinien_zawierac_dodany_produkt(context):
    context.driver.visit("https://example.com/koszyk")
    assert "Produkt" in context.driver.text

@given('Jestem na stronie głównej')
def step_given_jestem_na_stronie_glownej(context):
    context.driver.visit("https://example.com")

@when('Wpisuję "{produkt}" w pole wyszukiwania')
def step_when_wpisuje_produkt_w_pole_wyszukiwania(context, produkt):
    context.driver.fill("input[name='search']", produkt)

@when('Klikam przycisk "Szukaj"')
def step_when_klikam_przycisk_szukaj(context):
    context.driver.click("button.szukaj")

@then('Powinienem zobaczyć wyniki wyszukiwania zawierające "{produkt}"')
def step_then_powinienem_zobaczyc_wyniki_wyszukiwania_zawierajace_produkt(context, produkt):
    assert produkt in context.driver.text
