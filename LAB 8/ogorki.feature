Feature: Sklep z ogórkami

  Scenario: Dodawanie ogórków do koszyka
    Given Otwieram stronę główną sklepu z ogórkami
    When Wybieram pierwszy ogórek z listy dostępnych produktów
    And Dodaję ogórek do koszyka
    Then Ogórek zostaje dodany do koszyka

  Scenario: Wyszukiwanie ogórków
    Given Otwieram stronę główną sklepu z ogórkami
    When Wpisuję "ogórek" w pole wyszukiwania
    And Klikam przycisk "Szukaj"
    Then Wyświetlają się wyniki wyszukiwania zawierające ogórki

  Scenario: Sprawdzanie szczegółów ogórka
    Given Otwieram stronę główną sklepu z ogórkami
    When Wybieram pierwszy ogórek z listy dostępnych produktów
    And Klikam na link ze szczegółami ogórka
    Then Wyświetlają się szczegóły wybranego ogórka

  Scenario: Złożenie zamówienia na ogórki
    Given Otwieram stronę główną sklepu z ogórkami
    When Wybieram pierwszy ogórek z listy dostępnych produktów
    And Dodaję ogórek do koszyka
    And Przechodzę do koszyka
    And Klikam przycisk "Zamów teraz"
    And Wprowadzam wymagane dane do złożenia zamówienia
    And Potwierdzam zamówienie
    Then Zamówienie zostaje pomyślnie złożone
