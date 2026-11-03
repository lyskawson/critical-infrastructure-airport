# A — domknięcie usytuowania czytników G01 po R1

Kontynuujesz jako ten sam wykonawca A w repozytorium `/Users/aleklyskawa/Desktop/airport-project` (cytuj pełną ścieżkę ze spacją po `critical_project`). Model R1 został sprawdzony: A2 (D01), A3 (optyka/PATH1/AI) i A4 (kaskadowe zasilanie G01) są zamknięte w przyjętym modelu. Nie wracaj do tych rozwiązań ani do SSP/UPS bez bezpośredniej zależności. Nie uruchamiaj agentów, nowych czatów, commitów, pushy ani publikacji.

Przeczytaj bieżący status w `/Users/aleklyskawa/Desktop/airport-project/docs/ustalenia-projektowe.md` i końcową sekcję `/Users/aleklyskawa/Desktop/airport-project/docs/odbior-a.md`. Sprawdź właściwe AGENTS.md i zachowaj obecne zmiany użytkownika.

**Pozostała jedna kolizja w A1:** RD-G01-IN ma punkt SITE `[64.5,9,1.1]`, RD-G01-OUT `[64.5,11,1.1]`. Tor tylnej osi auta biegnie po x=65, y=5..28. Nadwozie szerokości 1,8 m zajmuje x=64,1..65,9, a z marginesem 0,2 m x=63,9..66,1. Oba czytniki są wewnątrz tej obwiedni. Przy osi `[65,9]` rzut samochodu obejmuje również oba ich współrzędne y. `parking_results` pomija czytniki i ich podpory w liście przeszkód.

Wdróż fizycznie spójne ustawienie i mocowanie czytników albo skoryguj tor samochodu. Określ obrysy podpór/paneli i sposób przedstawienia karty przy postoju; ręczna obsługa patrolu może pozostać. Zachowaj wolny przejazd, otwarcie bramy, pas pieszy i poprawione miejsca postojowe. Jeśli urządzenie miałoby być na elemencie ruchomym, model musi jednoznacznie określać jego pozycje i prowadzenie przewodów w stanach roboczych. B nie może sam rozstrzygać mocowania ani przesuwać symboli względem rzeczywistych punktów.

Edytuj `/Users/aleklyskawa/Desktop/airport-project/data/design.json`, `/Users/aleklyskawa/Desktop/airport-project/tools/design_geometry.py` i `/Users/aleklyskawa/Desktop/airport-project/tools/validate_design.py` oraz niezbędne zależności eksportu, rozdziału 08 i opisu KD. Po zmianie punktów/mocowania sprawdź końce kabli, przebiegi, zapasy, BOM i kaskadę napięć G01; po zmianie toru sprawdź pełną obwiednię w obu kierunkach. W danych pozostał też drobny stary tekst `areas.A03.scope` o C08 przy x=68 — uzgodnij go z aktualną kamerą `[63,20,3]`.

Rozszerz kontrolę manewru o fizyczne czytniki i ich mocowania. Dodaj jedną celowaną regresję odrzucającą dotychczasowe ustawienie lub równoważną kolizję; zachowaj wcześniejsze 20 prób. Nie dodawaj całego nowego systemu ani nie przebudowuj składu C i rysunków B.

Nadaj modelowi kolejną rewizję. Odtwórz rejestr i tabele (`make data`), uruchom walidator z próbami negatywnymi, kompilację i pakowanie wraz z kompilacją świeżego ZIP-u. Sprawdź odpowiednie strony PDF i diff. Zaktualizuj krótko ustalenia; nie edytuj historycznych raportów odbioru ani promptów. Zwróć położenia i mocowania czytników lub nowy tor, wynik kontroli przejazdu, wpływ na kable/napięcia/materiały oraz ścieżkę PDF. To wąskie domknięcie A1, nie ponowne wykonanie pakietu A. Przyjęcie do B należy do orkiestratora.
