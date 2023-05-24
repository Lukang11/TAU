Feature: Logowanie do aplikacji

  Scenario: Poprawne logowanie
    Given Jestem na stronie logowania
    When Wprowadzam poprawne dane logowania
    And Klikam przycisk "Zaloguj"
    Then Powinienem zostać zalogowany i widzieć stronę główną
