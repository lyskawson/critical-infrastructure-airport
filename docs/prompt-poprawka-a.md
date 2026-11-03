# Poprawka do pakietu A-2026-10-24

Kontynuujesz jako ten sam wykonawca A. Wdrożono istotną część projektu, a kompilacja, eksport i 15 prób negatywnych przeszły także w niezależnym odbiorze. Nie zaczynaj od nowa i nie przywracaj modelu czterech budynków. Przed przyjęciem do B popraw cztery konkretne kwestie poniżej oraz ich bezpośrednie zależności. Nie uruchamiaj agentów ani nowych czatów, nie wykonuj commitów/pushy/publikacji.

Repozytorium: `/Users/aleklyskawa/Desktop/airport-project` — cytuj całą ścieżkę, ze spacją po `critical_project`.

Najpierw sprawdź stan plików i właściwe AGENTS.md. Przeczytaj:

- `/Users/aleklyskawa/Desktop/airport-project/docs/odbior-a.md` — dowody i wyniki kontroli;
- `/Users/aleklyskawa/Desktop/airport-project/docs/ustalenia-projektowe.md` — aktualny status;
- `/Users/aleklyskawa/Desktop/airport-project/data/design.json`;
- `/Users/aleklyskawa/Desktop/airport-project/tools/validate_design.py` i `/Users/aleklyskawa/Desktop/airport-project/tools/export_design.py`;
- rozdziały 03, 04, 07–11 i 13–14 w `/Users/aleklyskawa/Desktop/airport-project/sections/` oraz zależny opis obiektu.

Edytuj model, walidator, eksport, odpowiednie rozdziały, README w razie zmiany poleceń i krótkie ustalenia. Rejestr oraz `generated/` odtwórz z danych. Nie edytuj historycznego audytu, promptów ani raportu odbioru; status wykonania poprawek dopisz w ustaleniach i odpowiedzi. Nie przebudowuj rysunków B ani składu C. Zachowaj wszystkie dotychczasowe zmiany użytkownika i dane formalne bez zgadywania.

1. **Połącz wjazd z alejką parkingu.** Pas x=63..67, y=10..20 kończy się przed miejscami P04 (62..64,5 × 20..25) i P05 (66..68,5 × 20..25). Między obrysami tych miejsc zostaje tylko 1,5 m, a alejka zaczyna się na y=25. Przyjmij wolny korytarz przejazdu i sprawdź manewr zadanym pojazdem także przy zajętych miejscach. Możesz zmienić położenie lub liczbę miejsc; nie utrzymuj 12 kosztem przejezdności. Zachowaj dostępne dojście i rozdział pieszego ruchu. Zweryfikuj studzienkę (65,11): leży w pasie bramy, choć B-CHAMBER opisuje teren bez ruchu kołowego. Zmień lokalizację albo dobierz właściwe obciążenia osprzętu. Każdą zmianę przeprowadź przez kamery, AI, trasy, przepusty, długości, napięcia i BOM, jeśli na nie wpływa.

2. **Zapewnij rzeczywisty kadr weryfikacji D01.** C01 ma punkt lokalny `[20, 9.5, 2.4]`, a D01 punkt w rzucie `[20, 0]`: odległość pozioma 9,5 m przekracza `far_clip_m=8`. C02 na `[20, 0.5, 2.4]` patrzy na północ, więc D01 leży za nią. Obie przypisano do D01. Uzgodnij zadanie, ustawienie i granice kadru oraz gęstość obrazu w miejscu przejścia. Rozszerz kontrolę z obecnego wyjątku D02–D04 na wszystkie deklarowane punkty weryfikacji, z near/far, kątem, wysokością celu i właściwym układem współrzędnych. Nie koryguj wyłącznie podpisu lub zasięgu bez ponownego sprawdzenia zadania i rozdzielczości.

3. **Sprawdź pionowy kadr C08 oraz zadeklarowane ujęcia PATH1.** Obecna kontrola AI sprawdza tylko rzut poziomy. Dla C08 (68,11,3), tilt=16,602 stopnia i HFOV=51,699 stopnia kontrolna prostoliniowa projekcja 16:9 daje VFOV około 30,488 stopnia; podłoże w (66,15,0) i (67,15,0) wypada poniżej kadru. To obliczenie kontrolne, nie pomiar konkretnej kamery. Wybierz i opisz model optyczny, VFOV/format obrazu oraz założenia zniekształceń, sprawdź widoczność punktu detekcji człowieka przy stopach i potrzebnej części sylwetki, całą linię oraz obszar analizy. Skoryguj ustawienie lub geometrię, gdy to potrzebne. Dla PATH1 określ wymagane części osoby, wysokości i widoczne odcinki dla przodu, tyłu oraz obu profili, sprawdzając także krańce odcinków i gęstość obrazu. Nie obiecuj pełnej sylwetki w każdym kadrze bez obliczenia i nie zastępuj brakującego projektu zapowiedzią próby terenowej. Źródła: [instrukcja Object Analytics](https://help.axis.com/en-us/axis-object-analytics) oraz [karta P3265-LVE](https://www.axis.com/dam/public/ac/8e/70/datasheet-axis-p3265-lve-dome-camera-en-US-437931.pdf). B ma dostać zamknięte parametry i czytelną definicję sektora.

4. **Usuń sprzeczną wersję zasilania G01.** `network.external_gate_bus` nadal podaje 240 mA / 2,5 mm2, a przewody, bilans i tekst przyjmują 0,5 A / 6 mm2. Usuń nieaktualną wersję lub generuj opis z parametrów. Po ewentualnej zmianie trasy przelicz wspólne obciążenie i napięcie ostatniego czytnika; wyprowadź jego napięcie wejściowe z poprzedniego odcinka albo sprawdzaj, czy przyjęta granica konserwatywna nie przewyższa napięcia faktycznie dostępnego według obliczeń.

Dodaj celowane kontrole i próby negatywne dla kolizji wjazdu/miejsc, punktu KD poza kadrem oraz pionowej widoczności linii AI. Nie zwiększaj liczby testów tylko dla samej liczby. Zachowaj dotychczasowe kontrole. Nie zmieniaj założeń SSP ani poprawnie sprawdzonego UPS bez związku z korektą.

Nadaj korekcie nowy identyfikator wersji i krótko opisz zmiany. Uruchom eksport, walidator z próbami negatywnymi, kompilację, pakowanie i kompilację świeżego ZIP-u. Obejrzyj odpowiednie wyrenderowane strony. Dla przeglądu geometrii możesz przygotować roboczy wykres z danych w `tmp/`; nie zastępuje on docelowych rysunków B. Przed zakończeniem sprawdź diff i aktualność eksportu.

Kryterium odbioru: wolny przejazd do alejki; spójny kadr D01 i ujęcia PATH1; widoczna linia AI w określonym modelu 3D; jedna wersja parametrów G01; brak nowych sprzeczności w połączeniach i obliczeniach. Nie deklaruj samodzielnie przyjęcia A przez orkiestratora. Zwróć zwięźle zmienione pliki, rozwiązanie każdego z punktów A1–A4, aktualne wielkości, wykonane sprawdzenia i ścieżkę PDF. Prompt B powstanie dopiero po odbiorze tych poprawek.
