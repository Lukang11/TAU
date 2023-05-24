Feature: Wyszukiwanie produktu

  Scenario: Wyszukiwanie produktu
    Given Jestem na stronie głównej
    When Wpisuję "telewizor" w pole wyszukiwania
    And Klikam przycisk "Szukaj"
    Then Powinienem zobaczyć wyniki wyszukiwania zawierające "telewizor"
