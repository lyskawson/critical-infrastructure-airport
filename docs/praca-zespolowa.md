# Zakres technologiczny i podział projektu na trzy osoby

Aktualizacja: 3 listopada 2026, po kolejnych zajęciach z prowadzącym. Jest to wspólny plan opracowania. PDF i źródła rozdziałów nie zostały jeszcze przebudowane według tego planu. Użytkownik wybrał podział według stron obecnego PDF-u: jego część to strony 1–12, a nie proponowany wcześniej podział tematyczny.

## Charakter opracowania

Projekt przedstawia przemyślaną koncepcję systemów bezpieczeństwa fikcyjnego „Lotniska Północ”: jakie zdarzenia wykrywamy, jakich technologii używamy i co robi operator. Nacisk pada na obserwację osób, analitykę obrazu, ochronę terenu przy pasie i kontrolę bagażu. Pozostają opis obiektu, schematy, zestawienie głównych urządzeń, podstawowe obliczenia zasilania oraz krótkie procedury wymagane w zadaniu.

Dla każdego rozwiązania wystarczają: cel, miejsce zastosowania, zasada działania, przykładowy sprzęt i oprogramowanie, powiązanie z innymi systemami, reakcja oraz najważniejsze ograniczenia. Przykład produktu uzasadnia wykonalność funkcji; nie oznacza kompletnej konfiguracji zakupowej ani gotowej integracji.

Notatki prowadzącego wskazują kierunek, nie nakaz zastosowania każdego wariantu. Nie rozbudowujemy projektu o pełny system sterowania ruchem lotniczym, projekt wszystkich instalacji lotniska ani własne badania naukowe ML.

## Uzgodniony podział według stron obecnego PDF-u

Podstawą jest obecny, 36-stronicowy plik `output/pdf/lotnisko-polnoc.pdf`, model `A-2026-10-24-R1`. Liczymy fizyczne strony pliku od strony tytułowej, zgodnie z licznikiem przeglądarki PDF, a nie numeracją w stopce. Użytkownik potwierdził strony 1–12 jako swój zakres. Pozostałe dwie części przypisujemy odpowiednio do obecnych stron 13–24 i 25–36.

| Część i obecne strony | Zawartość wyznaczająca granice | Kierunek zmian technologicznych |
|---|---|---|
| I — użytkownik, 1–12 | Tytuł, spis treści oraz rozdziały 1–5: założenia, ryzyka, CCTV, KD/SSWiN i SSP | Skrócenie opisu obiektu i SSP, mocniejszy opis technologii kamer i kontroli dostępu; krótkie wprowadzenie do analityki |
| II — osoba 2, 13–24 | Rozdziały 6–12: architektura, sieć, teren, trasy, obserwacja przejścia, AI i zasilanie podstawowe | Rozwinięcie analityki osób, wirtualnych linii oraz ochrony terenu i dostępu w kierunku pasa; spójna architektura i plan |
| III — osoba 3, 25–36 | Rozdziały 13–18: autonomia, materiały, procedury, cyberbezpieczeństwo, weryfikacja i źródła | Dodanie kontroli bagażu podręcznego przy skróceniu szczegółowych tabel; dostosowanie podtrzymania, wyposażenia, procedur i oceny |

Granice są zakotwiczone w powyższej zawartości obecnego PDF-u. Jeżeli po skróceniu tekstu rozdziały przesuną się na inne strony, nie przydzielamy autorom automatycznie kolejnych fragmentów, aby ponownie uzyskać po 12 stron. W szczególności orkiestrator nie zaczyna poprawiać rozdziału 6 tylko dlatego, że po redakcji znalazł się on na stronie 12. Przeniesienie rozdziału między autorami wymaga osobnego ustalenia.

Zakres źródeł do redakcji stylu użytkownika: `sections/01-assumptions.tex`, `02-risk.tex`, `03-cctv.tex`, `04-access-intrusion.tex` i `05-fire.tex`. Tytuł i spis w `main.tex` należą do początku dokumentu; nie daje to uprawnienia do redakcji pozostałych włączeń. Automatyczne przeliczenie numerów stron i spisu treści nie zmienia autorstwa fragmentów. Rozdziały `06-architecture.tex` do `12-power.tex` pozostają osobie 2, a `13-autonomy.tex` do `18-references.tex`, w tym obie części materiałów, osobie 3.

Orkiestrator użytkownika ustala zakres i sprawdza spójność całego projektu, ale redaguje styl wyłącznie pierwszego zakresu. Nie zmienia globalnej preambuły, fontów, nagłówków ani odstępów w sposób, który narzucałby skład pozostałym autorom. Strona tytułowa i spis są w części I, bibliografia w III; każdy autor dostarcza własne źródła. Opracowanie pozostaje koncepcją technologiczną zgodnie ze wskazówkami prowadzącego.

Ten podział dotyczy trzech autorów. Nie należy utożsamiać go z dawnymi pakietami wykonawców AI A/B/C: model techniczny, rysunki, skład. Nie uruchamiać automatycznie agentów ani nowych czatów.

## Część I — strony 1–12: wprowadzenie i podstawowe systemy

Zakres użytkownika obejmuje:

1. Tytuł i spis treści oraz zwięzłe założenia fikcyjnego lotniska, uwzględniające nowe obszary dalszej pracy.
2. Najważniejsze zagrożenia i cel ochrony, bez rozbudowanej analizy wykonawczej.
3. CCTV: rodzaje i zadania kamer, jakość obrazu, kilka kierunków obserwacji oraz krótkie wyjaśnienie roli ML. Szczegółowe scenariusze z obecnego rozdziału 11 pozostają w części II.
4. Dostęp pracowników: karta kryptograficzna, PIN w wybranych strefach, powiązanie zdarzenia z kamerą i swobodne wyjście. SSWiN jako uzupełnienie ochrony po zamknięciu.
5. SSP: cel, najważniejsze urządzenia, zasada alarmowania i niezależność od IT. Skrócić nadmiar szczegółów; nie usuwać tematu tylko dlatego, że nacisk przesuwa się na analitykę.

## Część II — strony 13–24: architektura, analityka i teren

To tutaj rozwijamy obecne rozdziały o AI, obserwacji przejścia, planie terenu i współpracy systemów. Osoba 2 odpowiada także za zwięzły opis sieci, tras głównych i zasilania podstawowego. Szczegółowe listy kabli można skrócić, aby zrobić miejsce na scenariusze technologiczne.

### Jak wykorzystać notatki prowadzącego

- **„Szwędanie się”** opisać jako przekroczenie czasu przebywania w konkretnej strefie i kontekście. Przykład własny: osoba pozostaje ponad 120 s przy zamkniętych drzwiach technicznych. Jest to parametr przykładu, nie wymaganie normy ani wynik pomiaru. Poczekalnia i kolejka nie mogą automatycznie podlegać tej samej regule. Detektor osoby dostarcza obserwacji, a reguła czasu nadaje zdarzeniu znaczenie. AXIS Object Analytics dokumentuje scenariusz Time in area [1].
- **„Podejrzane zachowanie”** zamienić na obserwowalne zdarzenie wymagające sprawdzenia. Nie obiecywać odczytywania zamiarów lub automatycznej oceny winy. Wystarczy dobrze opisany scenariusz czasu oraz drugi przykład, np. ruch przeciwny do wyznaczonego kierunku.
- **Ubiór** wykorzystać przede wszystkim jako atrybut wyszukiwania, np. kolor kurtki wskazany przez operatora. Osobny wariant to brak wymaganego elementu odzieży ochronnej w strefie technicznej. Ten wariant wymaga właściwego modułu klasyfikacji i sprawdzenia jego obsługi; nie przypisywać standardowej aplikacji funkcji wykrywania kamizelek bez źródła. Nietypowy strój sam w sobie nie jest rozpoznaniem zagrożenia.
- **Oznaczona osoba**: operator wybiera zdarzenie lub osobę i przegląda kolejne powiązane ujęcia. Oddzielić śledzenie obiektu w jednej kamerze, wyszukiwanie podobnego wyglądu w nagraniach oraz automatyczne śledzenie między kamerami na żywo. To różne funkcje. Smart search 2 dokumentuje filtry ubioru i podobieństwa wizualnego, ale podobieństwo nie potwierdza tożsamości i nie jest gotowym automatycznym śledzeniem na żywo [2].

Rozwinięcie automatycznego śledzenia między kamerami można krótko porównać jako wariant. W podstawowej koncepcji wystarcza wspomagane przez operatora odtwarzanie drogi z wybranych ujęć. Nie dodawać rozpoznawania twarzy, bazy biometrycznej ani samodzielnego treningu modelu jako domyślnego zakresu.

### Teren, ogrodzenie i dostęp w kierunku pasa

Proponowany układ:

1. Funkcjonalny plan fikcyjnego lotniska: terminal, punkt kontroli, dojścia i wjazdy, granica terenu, wybrany fragment części operacyjnej i pas.
2. Warstwy detekcji: zbliżenie do chronionego obszaru, przekroczenie granicy, dalszy ruch do obszaru krytycznego. Każda linia ma miejsce, kierunek, obiekt i reakcję.
3. Przykładowy dobór: kamera termowizyjna lub inny czujnik do wykrycia, kamera obrazu widzialnego do weryfikacji; radar jako wariant porównawczy. Uzasadnić, co wnosi drugi rodzaj sensora. Nie instalować wszystkich technologii bez potrzeby [3].
4. Dwa scenariusze: naruszenie wybranego odcinka ogrodzenia oraz nieuprawniony ruch przez wybrany dostęp w kierunku strefy pasa. Ująć pracę nocną, pogodę, zasłonięcia i przejazdy obsługi.

Na planie oznaczyć linie koncepcyjne, np. L1 — strefa ostrzegawcza, L2 — granica chroniona, L3 — wejście do obszaru krytycznego. Są to linie analityki na planie i w obrazie, a nie nowe oznakowanie drogi startowej. „Próg zadziałania” odróżnić od lotniczego pojęcia progu pasa.

Ochronę pasa pokazać przez jeden dobrze opisany dostęp i sąsiadujący fragment terenu. Nie deklarować pełnej obserwacji całego pasa kilkoma kamerami ani zastąpienia kontroli ruchu lotniczego. Zdarzenie przekazuje się odpowiedniej służbie operacyjnej; obraz CCTV nie udziela zezwolenia na wjazd. RWSL można pokazać jako przykład odrębnej technologii bezpieczeństwa ruchu, nie jako zaprojektowany element tej instalacji [4].

Osoba 2 przygotowuje wspólny plan sytuacyjny w edytowalnym formacie wektorowym. Wszyscy korzystają z tego samego układu stref i przejść; inne części mogą zawierać jego zbliżenia.

## Część III — strony 25–36: bagaż, podtrzymanie i procedury

Osoba 3 rozwija swoją dotychczasową część o jeden punkt kontroli **bagażu podręcznego** z kontrolą dodatkową, wykorzystując miejsce po skróceniu szczegółowych tabel. Zachowuje odpowiedzialność za autonomię, materiały, procedury, cyberbezpieczeństwo, ocenę działania i bibliografię. Pełny system bagażu rejestrowanego i sortownia pozostają poza zakresem.

Proponowany układ:

1. Obieg bagażu: podanie tacy, badanie, decyzja operatora, odbiór albo przekazanie do kontroli dodatkowej. Na rzucie oddzielić ruch przed kontrolą i po niej.
2. Krótkie porównanie klasycznego prześwietlania RTG i CT; wybór CT jako głównego przykładu technologicznego, z uzasadnieniem korzyści i kosztu złożoności.
3. Rozdzielenie metod: obrazowanie i wykrywanie przedmiotów, algorytmy alarmujące o określonych zagrożeniach, detekcja śladowa pobranej próbki. Przykład zestawu: HI-SCAN 6040 CTiX z odpowiednią opcją rozpoznawania obiektów oraz stanowisko ETD, np. IONSCAN 600. Pierwszy producent dokumentuje obrazy 3D, detekcję materiałów wybuchowych i opcjonalny iCMORE [5]; drugi — detekcję śladów metodą IMS z użyciem wymazówek [6]. Nie przedstawiać zwykłej kamery CCTV jako analizatora substancji ani ETD jako identyfikatora dowolnej zawartości walizki.
4. Integracja: operator bagażowy korzysta ze specjalistycznego stanowiska, SOC z obrazu sytuacyjnego i informacji o zdarzeniu. Opisać funkcjonalny przepływ informacji; nie zakładać gotowego API pomiędzy dowolnym skanerem i VMS. Brak integracji nie odbiera operatorowi lokalnego interfejsu kontroli.
5. Podtrzymanie zasilania, główne urządzenia, procedury, bezpieczeństwo danych, podstawowa ocena działania i źródła. Osoba 3 przekazuje wymagania punktu bagażowego do architektury i sieci osoby 2; korzysta z opisu SSP z części I zamiast go powielać.

Zasilanie opisać osobno dla IT/CCTV/KD i dla punktu kontroli bagażu. Nie dopisywać CT do dawnego bilansu UPS bez sprawdzenia jego zapotrzebowania. Na poziomie koncepcji wystarczy świadoma decyzja o podtrzymaniu nadzoru oraz bezpiecznym przerwaniu kontroli po utracie zasilania; nie trzeba projektować szczegółowych obwodów całej linii.

Każdy autor dostarcza własne główne urządzenia i źródła do wspólnego zestawienia. Osoba 3 je zestawia i wskazuje zależności. Nie odpowiada za redakcję całej pracy innych autorów.

## Poziom szczegółowości i spójność

- Zachować osiem tematów zadania: tytuł, spis, opis technologii z AI, materiały, lokalizacje/trasy, schemat, energię i procedury. Skrócić ich opis do poziomu koncepcji.
- Szczegółowe adresy pętli, pełne listy portów, wszystkie cięcia kabli, obwiednie każdej pozycji samochodu, pełne tabele spadków napięć i instrukcje konfiguracji nie muszą zajmować głównego PDF-u. Dotychczasowe dane mogą pozostać materiałem pomocniczym.
- W głównej treści zostawić obliczenia pomagające w decyzji: przykładową czytelność obrazu, retencję, podstawowy bilans mocy/podtrzymania i ewentualnie przepustowość punktu kontroli. Nie przenosić starych wyników na nowe urządzenia.
- Każdy autor opisuje swoje scenariusze według wspólnego schematu: **miejsce → obserwacja → warunek zdarzenia → informacja dla operatora → reakcja → ograniczenie**. Wystarczą krótkie opisy, bez rozbudowanych instrukcji serwisowych.
- Ujednolicić nazwy stref i zdarzeń na planie. Wystarczą identyfikatory potrzebne do powiązania rysunku z opisem; nie tworzyć nowych, rozbudowanych rejestrów.
- Rozdzielić operatora SOC, operatora kontroli bagażu i służbę operacyjną lotniska. Nie przypisywać jednej osobie wszystkich zadań równocześnie ani traktować alarmu kamery jak decyzji o ruchu lotniczym.
- SSP i swobodne wyjście pozostają niezależne od analityki. Ich opis ma być krótki i rzeczowy. Prywatność, bezpieczeństwo danych i zawodność analityki uwzględnić przy właściwej funkcji, bez powielania długich zastrzeżeń.
- Każdy autor dodaje źródła swoich twierdzeń. Własne progi są założeniami; planowana ocena nie jest przeprowadzonym testem. Przykłady modeli urządzeń wymagają sprawdzenia funkcji, opcji i obsługiwanej wersji.

## Relacja do obecnego modelu

Model `A-2026-10-24-R1` opisuje terminal z parkingiem i jeden scenariusz AI, a nie powyższy rozszerzony projekt. Jego osiem kamer i dotychczasowe bilanse nie stanowią doboru dla ochrony pasa ani kontroli bagażu. Trzeba uzgodnić nowy plan funkcjonalny, w tym miejsce kontroli pasażerów i rozdzielenie strumieni przed/po kontroli. Rozszerzenia nie wolno jedynie dopisać do opisu przy niezmienionym rzucie.

Otwarta kolizja czytników G01 z torem pojazdu pozostaje zapisana w odbiorze. Jeżeli obecny wjazd zostanie zachowany, trzeba ją rozwiązać przy aktualizacji jego układu. Dawny prompt R2 nie jest już jedynym następnym zadaniem: najpierw obowiązuje nowy zakres koncepcyjny i podział autorów. Nie ogłaszać rozwiązania kolizji ani przyjęcia rozszerzonego modelu bez sprawdzenia.

## Źródła do rozwinięcia części

Odczyt: 3 listopada 2026. Dokumentacja potwierdza wskazane funkcje produktów, nie skuteczność całej projektowanej instalacji.

1. [AXIS Object Analytics — Time in area i pozostałe scenariusze](https://help.axis.com/en-us/axis-object-analytics).
2. [AXIS Camera Station Pro — Smart search 2 i wyszukiwanie podobieństwa](https://help.axis.com/en-us/axis-camera-station-pro).
3. [AXIS Perimeter Defender — scenariusze i współpraca kamer](https://help.axis.com/en-US/axis-perimeter-defender).
4. [FAA — Runway Status Lights Pilot Reference Guide](https://www.faa.gov/air_traffic/technology/rwsl/pet). Źródło porównania funkcji, nie podstawa polskich wymagań prawnych.
5. [Smiths Detection — HI-SCAN 6040 CTiX, karta rozwiązania](https://www.smithsdetection.com/media/m5imgzeg/hi-scan-6040-ctix.pdf), s. 1–2. Karta opisuje przykład technologii; nie ustala się na jej podstawie bieżących zasad przewozu płynów ani aktualnych dopuszczeń.
6. [Smiths Detection — IONSCAN 600, zasada IMS i pobieranie próbki](https://www.smithsdetection.com/products/ionscan-600/).
