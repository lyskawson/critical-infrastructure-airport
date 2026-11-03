# Odbiór pakietu A-2026-10-24

Data przeglądu: 24.10.2026. **Wynik: jedna runda poprawek A przed przyjęciem modelu do B.** Nie zmieniono modelu technicznego ani plików LaTeX. Zachowujemy zakres małego terminalu i pracę wykonaną przez A; nie wracamy do dawnego modelu czterech budynków.

## Sprawdzenia i zakres przeglądu

Przeczytano bieżący JSON, wszystkie rozdziały techniczne 01–18, rejestr, eksport, walidator, Makefile, pakowanie ZIP, README i ustalenia. Sprawdzono diff i stan plików; nie znaleziono właściwego AGENTS.md. Nie uruchamiano agentów, nowych czatów ani komunikacji z wykonawcą.

- `python3 tools/validate_design.py --self-test --report tmp/odbior-a-2026-10-24/validation.json`: OK, 15/15 uszkodzonych wariantów odrzuconych.
- `python3 tools/export_design.py --check`: eksport aktualny. `git diff --check`: bez błędów.
- Niezależna kompilacja do `tmp/pdfs/odbior-a-2026-10-24/build/`: 34 strony, końcowy log bez ostrzeżeń, niezdefiniowanych odsyłaczy i overfull/underfull.
- Zastany ZIP: 37 wpisów, poprawne CRC, wszystkie dołączone pliki odpowiadały plikom lokalnym w chwili kontroli. Świeżo rozpakowano go do `tmp/pdfs/odbior-a-2026-10-24/overleaf-unpacked/` i skompilowano do `build-review/`: 34 strony, końcowy log bez ostrzeżeń. Nie jest to import do usługi Overleaf. Po poprawkach i aktualizacji ustaleń trzeba zbudować nowy ZIP.
- Wykonano świeży render wszystkich 34 stron. Obejrzano komplet sześciu arkuszy miniatur i osobno strony fizyczne 16, 20 i 24 w większej rozdzielczości. Czytelność tych tabel i tekstu jest wystarczająca do przeglądu A; nie jest to odbiór składu końcowego C.
- Niezależne przeliczenie łamanych i cięć potwierdza 1658,843 m instalowanego kabla oraz 1873 m zakupu, po wyłączeniu przewodów fabrycznych i patchcordów zawartych w osprzęcie. Zapis: 3,6288 TB surowo i 4,536 TB z rezerwą. PoE: 273,2 W alokacji i 341,5 W z rezerwą. Obwiednia UPS: 861,1 W, po rezerwie 1076,375 W.
- Odczytano źródłowy szereg `ebm2` z [krzywej Eaton](https://eg.eaton.com/ups-battery-runtime/en-gb/5PX1500IRT2UG2): odpowiada wszystkim punktom zapisanym w JSON. Punkt 1100 W / 67 min daje po współczynnikach 0,85 i 0,8 wynik 45,56 min. To obliczony dobór, nie wykonana próba autonomii.

Dokumenty pierwotne sprawdzano wybiórczo dla parametrów i twierdzeń istotnych w odbiorze: karta kamery i instrukcje Axis, krzywa UPS, opis rodziny ACSP, wskazane akty ppoż. i nowe wydanie Kodeksu pracy. Nie oznacza to pełnego audytu wszystkich przepisów i instrukcji ani zgodności wykonawczej. Jawne założenia promieni detekcji SSP i przyszłe próby rzeczywistej instalacji nie są tutaj traktowane jako rzekome pomiary lub certyfikaty.

## A1. Wjazd koliduje z miejscami postojowymi

Źródło: `data/design.json`, `site.parking_layout.stalls`, opis G01 i `sections/08-site.tex`.

Wyznaczony pas G01 ma x=63..67, y=10..20. Alejka manewrowa zaczyna się dopiero na y=25. Pomiędzy nimi występują miejsca:

- P04: x=62..64,5, y=20..25;
- P05: x=66..68,5, y=20..25.

Pas szerokości 4 m nakłada się na te miejsca; między ich obrysami pozostaje jedynie 1,5 m na x=64,5..66. Nie zdefiniowano wolnego połączenia wjazdu z alejką dostępnego również przy zajętych miejscach. A ma poprawić geometrię i sprawdzić przejazd/manewr przy zadanym pojeździe, zamiast zostawiać naprawę rysownikowi. Liczba 12 miejsc nie jest ograniczeniem wymagającym zachowania kosztem przejazdu.

W tej samej korekcie: pozycja B-CHAMBER opisuje studzienki na terenie bez ruchu kołowego, ale trzeci punkt (65,11) leży w pasie G01 i rzucie otwierania bramy. Sam środek między śladami kół nie wyłącza obciążeń pojazdami. Trzeba zmienić lokalizację lub jednoznacznie dobrać właściwy osprzęt i zaktualizować trasy/przedmiar.

## A2. Żadna z przypisanych kamer nie obejmuje D01 w zapisanych granicach kadru

Źródło: `devices.C01/C02`, `access_points.D01`, `openings.D01`, `tools/validate_design.py:117`.

D01 ma punkt lokalny w rzucie `[20, 0]`. C01 leży na `[20, 9.5, 2.4]`, patrzy na południe, ale ma `far_clip_m=8`; odległość pozioma do drzwi wynosi 9,5 m. C02 na `[20, 0.5, 2.4]` patrzy na północ, więc drzwi leżą za jej kierunkiem obserwacji. Obie są przypisane do weryfikacji D01, a opis C01 wymienia D01 jako zadanie. Walidator kontroluje rzeczywiste punkty tylko dla D02–D04 i nie wykrywa tej rozbieżności.

Trzeba wybrać i udokumentować kadr dla zdarzenia przy D01, z podaniem celu oraz gęstości obrazu przy tym przejściu. Nie wystarczy zmienić podpisu sektora albo dopisać próbę terenową. Kontrola powinna obejmować każdy deklarowany punkt weryfikacji, we właściwym układzie współrzędnych, wraz z near/far i wysokością celu.

## A3. Brakuje pionowego sprawdzenia kadru C08 i ujęć PATH1

Źródło: `devices.C08.view`, `ai.line_site_m`, `path_observation.views`, `tools/validate_design.py:89`, `sections/11-ai.tex:2`.

Kontrola AI sprawdza azymut, HFOV i promień w rzucie. Nie korzysta z wysokości kamery, pochylenia ani VFOV, mimo że tekst deklaruje widoczność całej linii. W [instrukcji AXIS Object Analytics](https://help.axis.com/en-us/axis-object-analytics) punkt detekcji człowieka jest przy stopach; widoczność górnej części ciała również ma znaczenie. Estymacja zasłoniętego punktu nie jest dowodem pełnego pokrycia geometrycznego.

Niezależne sprawdzenie idealną projekcją prostoliniową 1920×1080 daje dla C08, HFOV=51,699 stopnia i tilt=16,602 stopnia, VFOV około 30,488 stopnia. Po przeliczeniu punktów podłoża do obrazu, przy pionowym zakresie znormalizowanym -1..1:

| Punkt SITE, z=0 | Pionowa współrzędna obrazu |
|---|---:|
| (65,15,0) | -0,968 |
| (66,15,0) | -1,140 |
| (67,15,0) | -1,343 |

Dwa wschodnie punkty wypadają poniżej kadru tego modelu kontrolnego. Jest to wynik obliczenia przy podanych założeniach optycznych, **nie pomiar obrazu ani dowód dokładnego odwzorowania konkretnego obiektywu**. [Karta P3265-LVE](https://www.axis.com/dam/public/ac/8e/70/datasheet-axis-p3265-lve-dome-camera-en-US-437931.pdf) podaje zakresy HFOV i VFOV, ale model nie określa wybranego VFOV, projekcji ani ustawienia korygowania zniekształceń.

A ma zamknąć ten model optyczny, uzasadnić parametry i skorygować ustawienie, linię lub obszar AI, jeśli potrzeba. Sprawdzić należy również wysokości celów na zadeklarowanych odcinkach PATH1 i gęstość obrazu w ich skrajnych punktach. Nie narzuca się obserwacji całej sylwetki w każdym kadrze, ale trzeba określić, jakie części osoby mają być widoczne i na jakim odcinku; wymagania AI trzeba odróżnić od ujęcia przodu/profilu do weryfikacji operatora. B ma dostać dane wystarczające do narysowania rzeczywistych sektorów, bez samodzielnego zmieniania optyki.

## A4. Sprzeczny opis zasilania czytników G01

`network.external_gate_bus` (`data/design.json:10688`) podaje 240 mA i wspólną parę 2,5 mm2. Model przewodu `DC-READER-O`, połączenie `DC-RD-G01-IN` oraz `sections/09-routes.tex:17` przyjmują 0,5 A i 6 mm2. Obliczenie spadku i tabela odnoszą się do drugiego zestawu. Usunąć nieaktualny opis lub wyprowadzać go z parametrów, żeby pojedynczy JSON nie zawierał sprzecznych wersji tej samej decyzji. Po korekcie geometrii przeliczyć również aktualne długości i napięcie dalszego czytnika.

## Warunek przejścia do B

A poprawia wskazane kwestie i ich zależności w tym samym modelu, eksporcie, tekście i pakiecie. Walidator ma odrzucać co najmniej kolizję przejazdu, przypisanie punktu poza kadrem i błędne pokrycie pionowe scenariusza AI. Uzupełnienie kontroli ma odpowiadać rzeczywistym zależnościom, nie nowym stałym sumom. Po kontroli poprawionych plików i odpowiednich stron PDF orkiestrator podejmie odbiór A. Etapy B i C nie zostały uruchomione.

## Powtórny odbiór R1 — 26.10.2026

Sprawdzono model `A-2026-10-24-R1`, różnice względem zachowanej kopii A0, nowy `tools/design_geometry.py`, zmiany eksportu i walidatora oraz odpowiednie rozdziały. **A2, A3 i A4 zamknięto w zadanym modelu akademickim. A1 pozostaje do wąskiej korekty mocowania czytników lub toru auta.** Nie zmieniono technicznych plików A; aktualizowano tylko wynik odbioru, ustalenia i prompt.

Potwierdzone sprawdzenia:

- Walidator: 20/20 prób negatywnych odrzuconych; pięć nowych przypadków kontroluje także właściwy powód odrzucenia. Eksport aktualny, `git diff --check` bez błędów.
- Niezależna kompilacja źródeł: 36 stron, końcowy log bez ostrzeżeń i błędów. ZIP: 38 wpisów, poprawne CRC i zgodne pliki w chwili kontroli; kompilacja nowego rozpakowania także bez ostrzeżeń. Po zmianie ustaleń lub modelu ZIP wymaga odtworzenia.
- Świeży render wszystkich 36 stron, przegląd sześciu arkuszy miniatur, szczegółowo strony fizyczne 6 i 22. Pozostawiony dawny skład należy do C.
- D01: niezależna projekcja narożników otworu w prawidłowo przeliczonym układzie SITE daje maksymalne wartości bezwzględne obrazu x=0,1742, y=0,4780 i odległości poziome 9,500–9,519 m; mieści się w C01 z granicą 10,5 m.
- PATH1: niezależne sprawdzenie narożników obwiedni na krańcach każdego przyjętego odcinka potwierdza zakresy pionowe i poziome. C01/C02 oraz oba profile mieszczą się w zadanym kadrze z rezerwą. Zakres wysokości 1,2–2,0 m jest jawnie ograniczony do określonych części osoby.
- AI: narożniki obwiedni całej osoby nad ROI dają maks. |x|=0,7729 i |y|=0,9060, a nad linią |x|=0,5554 i |y|=0,6766. Wyniki mieszczą się w limicie 0,96. Potwierdza to podany idealny model projekcji, bez deklarowania pomiarów rzeczywistego obiektywu.
- G01: niezależnie otrzymano 0,5 A, 6 mm2, napięcie IN 11,66534 V i OUT 11,57784 V; wynik drugiego odcinka pochodzi z pierwszego, nie z odrębnej korzystniejszej stałej.
- Aktualne wielkości wynikające z modelu: 10 miejsc parkingowych, 100 urządzeń/zespołów, 121 połączeń, 1882 m zakupu kabli i najdłuższy kanał 91,3 m. Podstawowe bilanse SSP, UPS, zapisu i PoE nie zostały zmienione przez korektę.

Pliki sprawdzeń: `tmp/odbior-a-r1-2026-10-26/validation.json`, `independent-checks.json` oraz `tmp/pdfs/odbior-a-r1-2026-10-26/`.

### Pozostałość A1: czytniki nie zostały uwzględnione w obwiedni przejazdu

Źródła: `data/design.json:2648` (RD-G01-IN), `data/design.json:2672` (RD-G01-OUT), `site.parking_layout.sweep`, `tools/design_geometry.py:162`.

Pozycje SITE czytników wynoszą `[64.5,9,1.1]` i `[64.5,11,1.1]`. Prosty odcinek toru tylnej osi biegnie po x=65 od y=5 do y=28. Samochód ma szerokość 1,8 m, więc jego rzut podczas jazdy na północ zajmuje x=64,1..65,9; z przyjętym marginesem 0,2 m jest to x=63,9..66,1. Oba punkty czytników leżą wewnątrz obu przedziałów. Przykładowo przy tylnej osi `[65,9]` nadwozie w rzucie obejmuje x=64,1..65,9 i y=8,1..12,6, zawierając oba punkty.

`parking_results` sprawdza miejsca postojowe, pas pieszy, podporę kamery, otwarte skrzydła bramy i studzienki. Nie uwzględnia paneli czytników i ich podpór. Dlatego zwraca brak kolizji mimo nieuzgodnionego fizycznego usytuowania urządzeń. Nie wystarczy później przesunąć ich symboli na rysunku B.

A ma dopasować rzeczywiste położenie i mocowanie czytników do toru pojazdu lub zmienić tor z ponownym sprawdzeniem manewru. Należy wskazać także sposób użycia karty przy postoju; przyjęta ręczna obsługa przez patrol może pozostać. Zmiana wymaga aktualizacji końców i przebiegu kabli, długości, napięć, osprzętu i tekstu wyłącznie w zakresie, na który wpływa. Kontrola ma uwzględniać fizyczne urządzenia i ich podpory, a nie tylko wcześniej wybrane obrysy. Dodatkowo uporządkować stary tekst `areas.A03.scope` o podporze C08 przy x=68.

Jedyny aktywny prompt to `docs/prompt-poprawka-a-r2.md`. Nie uruchomiono B ani C.
