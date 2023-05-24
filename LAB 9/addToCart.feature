Feature: Dodawanie produktu do koszyka

  Scenario: Dodawanie produktu do koszyka
    Given Jestem zalogowany na stronie
    When Wybieram produkt z listy dostępnych
    And Dodaję produkt do koszyka
    Then Powinienem zobaczyć komunikat o dodaniu do koszyka
    And Koszyk powinien zawierać dodany produkt
