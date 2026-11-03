# Ustalenia projektowe

Pakiet A, model **A-2026-10-24-R1**, baza HEAD `8112694`. Dane techniczne przygotowano do przeglądu i wykonania rysunków B; nie jest to zatwierdzenie wykonawcze. Praca bez agentów, nowych czatów, commitów, pushy i publikacji. Nie znaleziono właściwego AGENTS.md w repo ani sprawdzonych katalogach nadrzędnych. Audyt i prompty wejściowe pozostają bez zmian.

## Aktualny odbiór orkiestratora 26.10.2026

**R1: A2, A3 i A4 zamknięte w przyjętym modelu obliczeniowym. A1 ma jedną pozostałą kolizję do poprawienia przed B.** Usunięcie P04/P05 i przeniesienie JC03 przyjęto. Czytniki RD-G01-IN `[64.5,9,1.1]` i RD-G01-OUT `[64.5,11,1.1]` nadal leżą wewnątrz obwiedni samochodu jadącego po x=65; ich mocowań nie uwzględnia sprawdzenie manewru. A ma uzgodnić fizyczne mocowanie czytników z torem pojazdu i przeliczyć bezpośrednie zależności. Drobny opis `areas.A03.scope` również zachował poprzednie położenie C08 x=68 zamiast aktualnego (63,20).

Kontrole powtórnego odbioru: 20/20 prób negatywnych, aktualny eksport, kompilacje projektu i świeżego ZIP-u bez ostrzeżeń, niezależne sprawdzenie projekcji D01/PATH1/AI i napięcia G01. PDF 36 stron: świeży render i przegląd miniatur całości, szczegółowo strony fizyczne 6 i 22. Wyniki i dowód kolizji dopisano do `docs/odbior-a.md`.

**Jedyny aktualny pakiet wykonawczy: `docs/prompt-poprawka-a-r2.md`, do tego samego A.** Użytkownik przekazuje go ręcznie. B i C pozostają nieuruchomione; nie wracamy do poprawionych kadrów, SSP, UPS ani starego zakresu bez nowego powodu. Poniższe sekcje odbioru 24.10 oraz wykonania R1 są historią, nie bieżącą zgodą na B.

## Odbiór orkiestratora 24.10.2026 - historia wersji A-2026-10-24

**Status: A wymaga jednej rundy poprawek przed przyjęciem do B.** Kompilacja lokalna i świeżo rozpakowanego ZIP-u, aktualność eksportu oraz 15 prób negatywnych przeszły; niezależnie potwierdzono podstawowe sumy kabla, zapisu, PoE i krzywą UPS. Szczegóły: `docs/odbior-a.md`; jedyny aktualny pakiet wykonawczy: `docs/prompt-poprawka-a.md`, do tego samego wykonawcy A, przekazywany ręcznie przez użytkownika.

- A1: wjazd x=63..67 kończy się na rzędzie miejsc P04/P05; trzeba zaprojektować wolne połączenie z alejką, sprawdzić manewr i położenie studzienki (65,11) w pasie ruchu.
- A2: D01 jest 9,5 m od C01 przy `far_clip_m=8`; C02 patrzy w przeciwną stronę. Trzeba uzgodnić zadanie, rzeczywisty kadr i gęstość obrazu przy przejściu.
- A3: dotychczasowa walidacja linii AI i PATH1 obejmuje głównie azymut/HFOV. Trzeba zamknąć pionowy model kadru oraz widoczność celu; dla C08 projekcja kontrolna 16:9 wskazuje problem z podłożem na wschodnim końcu linii. To wynik modelu kontrolnego, nie pomiar obrazu kamery.
- A4: `network.external_gate_bus` nadal podaje 240 mA i 2,5 mm2, gdy połączenia i opis przyjmują 0,5 A i 6 mm2. Należy usunąć tę sprzeczność oraz zaktualizować wszystkie zależności po korektach.

Nie zmieniono tutaj modelu ani doborów A. B i C nie są uruchomione; skład, większe załączniki tabelaryczne i końcowe oględziny wszystkich stron pozostają etapem C. Powyższy zapis opisuje wynik odbioru poprzedniej wersji. Stan wykonanej korekty R1 podano poniżej; nie zmienia on decyzji orkiestratora o odbiorze.

## Wykonanie korekty R1 - do ponownego odbioru

- **A1:** usunięto P04/P05, pozostawiono10 miejsc i P01 dostępne. Korytarz x63..67 dochodzi do alejki; tor tylnej osi (65,5)-(65,28), łukR6 o środku(59,28) do(59,34), następnie(55,34). Samochód własnego modelu4,5x1,8m, osie2,7m, zwisy0,9m; sprawdzenie368 położeń w każdym kierunku z marginesem0,2m przy wszystkich miejscach zajętych. JC03 przeniesiono na(62,11), na tej samej trasie R5 poza ruchem i otwarciem bramy.
- **A2:** D01 weryfikuje C01: HFOV40°, tilt8°, far10,5m, całe światło1,2m na wysokości1,2..2m, minimum275,5px/m. C02 wyłącznie dla PATH1. Kontrola obejmuje każdą deklarowaną kamerę D01-D04/G01, pełną szerokość otworu, wysokość, near/far i transformację SITE. C05 skorygowano do az49°/HFOV72°/far13m dla D03/D04; są to ujęcia przeglądowe, bez identyfikacji twarzy.
- **A3:** wspólny model projekcji prostoliniowej16:9, kwadratowe piksele, roll0°, korekcja dystorsji ON i jawne założenie zerowej reszty z rezerwą2% całego wymiaru obrazu po każdej stronie. C08 przeniesiono do(63,20,3), az292°/tilt25°/HFOV72°/VFOV44,4577°. Promienie AI pozostają wewnątrz bocznego ogrodzenia i nie przecinają G01. ROI stóp x63,3..66,7/y12,5..16,5; linia y15,5. Obwiednia omija również otwarte skrzydła do y12. Skrajne pasy0,3m wyłączono z AI. Osoba0..2m i0,6x0,6m mieści się w kadrze; minimum obrazu osoby1,4m to212,3px wobec86,4px. PATH1: zakres wysokości1,2..2m, środek±0,6m od osi, obwiednia0,6x0,6m; odcinki y1..5,5 (C01),3,5..7 (C02),4,2..5,8 (C03/C04). Minima297/309/430/430px/m. Nie deklaruje się całej sylwetki w czterech kadrach PATH1.
- **A4:** usunięto tekst240mA/2,5mm². Parametry G01 wynikają z modeli czytników i kabli: wspólny prąd0,5A, przekrój6mm², napięcie IN11,665V. OUT pobiera wejście bezpośrednio z poprzedniego wyniku i ma11,578V wobec własnego minimum11,4V. Długość zasilania G01 bez zmiany.

Nowa trasa C08: R8 od(63,11) do(63,20); kanał maksymalny91,263m, tory stałe do86,263m; kanalizacja85m/zakup95m, kabel instalowany1666,843m/zakup1882m. Dodano w BOM słup C08 3m z podstawą poza pasem i uchwytem0,2m. Urządzenia/zespoły100, połączenia121 i przepusty30 bez zmiany. SSP, UPS, PoE i zapis zachowano. Nowy `tools/design_geometry.py` służy wspólnym obliczeniom i eksportowi; nie jest generatorem rysunków B.

Kontrole:20/20 prób negatywnych (15 zachowanych +5 celowanych), aktualny eksport, PDF36 stron wyrenderowany i przejrzany, powiększone strony optyki/manewru/PATH1/AI/napięć/BOM bez ucięć; log bez ostrzeżeń. Świeżo rozpakowany ZIP skompilowano lokalnie bez ostrzeżeń; nie wykonano importu do usługi Overleaf. Niezależnie przeliczono kabel, napięcie G01 oraz projekcję D01 i końców linii AI; roboczy wykres manewru i kadru pozostaje w tmp. Obliczenia idealnego modelu i manewru nie są próbami instalacji. **Status: korekta wykonana przez A, przekazana do ponownego odbioru; nie deklaruje się przyjęcia do B.** Raportu odbioru, promptów, danych formalnych i składu C nie zmieniono.

## Zamknięte decyzje

- Fikcyjny obszar 80 × 60 m (0,48 ha), jeden terminal T0 24 × 16 m, siedem pomieszczeń R101-R107, płaski strop 3 m, bez pustek. Wnętrza 15-30°C, teren -25..40°C. Terminal do60 osób, hol do40, cały port do150; dwie osoby ochrony na zmianie. Parking10 miejsc, w tym dostępne3,6 ×5 m. Wymiary są założeniami, nie pomiarami.
- Osiem stałych kamer1920×1080, bez PTZ. PATH1 jest prostą drogą w R102; C01/C02 dają przód/tył, C03/C04 przeciwne profile na zapisanych odcinkach. Przebieg załamany odrzucono po porównaniu ujęć i ruchu. Nie obiecuje się widoczności każdej strony przy zasłonięciu inną osobą. Wyjście nie wymaga postoju dla kamery.
- KD: D01-D04 i G01, pięć A1210, sześć HID Signo40K, karty Seos5006 SIO/AES128 i OSDP Secure Channel. D03/D04 także PIN. Biometrię odrzucono wobec braku wykazanej niezbędności; porównanie i aktualny art.22¹b KP w treści. Drzwi mają mechaniczne wyjście; nie ma elektromagnesów ani elektrycznego toru blokującego ewakuację. G01 jest ręczny, z dwoma czytnikami, kontaktronem i obsługą patrolu, bez napędu/zasilanego zamka.
- Parking ma założone istniejące ogrodzenie architektoniczne, otwartą przerwę pieszą1,5 m na zachodzie i oddzielony pas pieszy. Dojście do D01 nie przecina kontrolowanego pasa G01. E02/E03 wychodzą na otwarte A06/A05. Ochrona nie obejmuje całego ogrodzenia lotniska.
- SSWiN: jedna VERSA15, sześć PIR, cztery odrębne kontaktrony obwodu, 15 przypisanych wejść, dwie strefy, napad i sabotaż. ETHM jest lokalnym interfejsem serwisowym; nie obiecuje się nieudokumentowanej integracji VERSA z VMS. Operator korzysta z manipulatora w SOC. Kontaktrony KD i SSWiN przy D01 są fizycznie odrębne.
- SSP: jedna ACSP402, dziesięć DMP400 i jedna DCP400 w WC, trzy ROP, osiem SPP400. L1 ma22 adresy i23 odcinki; izolator w każdym elemencie. Dwa styki informacyjne OUT1/OUT8 do SSWiN, bez MIO i magistrali optycznej. Alarm jednostopniowy bez zwłoki. Własne promienie kontrolne5/4 m, warunki stropu i ograniczenia źródeł opisano jawnie. SSP jest dobrowolny dla przyjętego modelu poniżej przesłanek obowiązku; DSO i automatyczna transmisja do PSP nie są instalowane. Powiadomienie112 przez dyżurnego. Uwzględniono zmiany prawa2024/1716,2026/1276 i2026/815 oraz KP2026/1245.
- LAN: jedna gwiazda17 łączy, PoE273,2 W alokacji /341,5 W z rezerwą wobec384 W; najdłuższy kanał91,3 m. Brak pierścienia, włókien i SFP. NAS4×8TB RAID6; potrzeba4,536TB z rezerwą, dostępne14,4TB; SD128GB daje37,9 h przy6Mb/s. Jeden AI1 na C08: osoba przekracza linię w pasie pojazdów. Częstość wejścia25kl/s nie jest fikcyjną gwarancją inferencji25Hz. Cele TP/FP/FN i opóźnienia są do pomiaru.
- UPS861,1 W obwiedni AC,1076,375 W z rezerwą. Eaton5PX1500IRT2UG2 +2EBM48: krzywa67min przy1100W, po0,85×0,8:45,56min wobec celu30min. SSP i SSWiN mają po jednej baterii12V17Ah; bilanse, ładowanie i niskie napięcia są przeliczone. SSP przed PWP, UPS po PWP z fizycznym RPO oraz odłączeniem wejścia AC. Brak agregatu/SZR. Wyjście pozostaje mechaniczne po wyczerpaniu baterii.
- Nowe ilości:24→8 kamer,14→5 punktów KD,80→11 czujek SSP,4→1 CSP i4→1 SSWiN,24→6 PIR. Dawne1520m pierścienia zastąpiono85m drzewa kanalizacji;1882m oznacza sumę zakupu wszystkich typów kabla z indywidualnych cięć, a nie jedną trasę. Rejestr obejmuje100 urządzeń/zespołów i121 połączeń; elementy fabryczne nie są liczone ponownie do mocy lub metrów kabla.

## Identyfikatory i dane dla B

Jedynym modelem jest `data/design.json`; `make data` odtwarza rejestr i tabele `generated/`. SITE w metrach: x wschód, y północ; lokalne T0 przelicza się przez dodanie(20,25,0). Ściany, otwory, grubości, kierunki skrzydeł, przeszkody, parking, droga osoby, sektory kamer i wszystkie łamane kabli3D są w danych. `penetrations` wskazuje30 rzeczywistych przecięć przegród wraz z kablami. Kolejność L1 i końce portów są wiążące. B nie dobiera liczby urządzeń, adresów, kanałów ani długości.

- N0 pozostaje jedyną szafą; N1-N3 usunięto. CSP-0 i SSWiN-0 zachowano; jednostki1-3 usunięto.
- C01-C08 mają nowe role/pozycje; C09-C24 wycofano. D01-D04 to nowe przejścia KD; D05-D07 są zwykłymi drzwiami, D08-D12 wycofano. G01 jest ręczny, G02 wyłączono. Nowe E01-E03 są wyjściami bez KD.
- R1-R4 ponownie oznaczają trasy wewnętrzne, a nie stary pierścień. R5-R8 to kanalizacja terenowa. Każdy kabel ma dodatkowo pełną łamaną, rzut, pion, zapas i zakup; ta łamana rozstrzyga przebieg odgałęzienia.
- Do narysowania: plan terenu z otwartymi dojściami, rzut wszystkich pomieszczeń i punktów, PATH1 i uzasadnione kadry, trasy/obwody L1 oraz KD/SSWiN/IP, ideowy podział funkcji i zasilanie z Q0/Q1/Q2 oraz RPO. B wybiera sposób prezentacji i źródła wektorowe.

Dawne rysunki i ich źródła zachowano, lecz wyłączono z PDF. Generator v1 odmawia pracy na schemacie2 przed zapisem plików, więc nie nadpisuje rejestru. Pakiet ZIP po A zawiera dane i eksport; po B trzeba dodać nowe rysunki/źródła. C kończy skład LatinModern12pt, marginesy~25mm, czarne odsyłacze, numer strony i redakcję; zasadniczy stary skład celowo nie jest przebudowany w A.

## Rzeczywiste kwestie pozostałe

Dane formalne i wymagany przez uczelnię sposób ujawnienia AI -- użytkownik/C. Przed rzeczywistą realizacją: pomiary geometrii/gruntu/PE/SWZ/RCD, próby kadrów, sygnalizacji i dostępności, zadymienie/test temperatury, napięcia przy niskiej baterii, próba autonomii i RPO oraz dostarczone wersje i dokumenty urządzeń. Próg20,4V regulowanej pętli, minima sprawności i promienie rozmieszczenia są własnymi założeniami kontroli, nie zmyślonymi parametrami katalogowymi ani wynikiem badań. Brak pełnych tekstów norm i nowej ograniczonej instrukcji instalatora03/26 został ujawniony. Nie stanowi to deklaracji pełnej zgodności wykonawczej. Niezaliczenie próby wymaga aktualizacji modelu przed realizacją, nie dowolnego przerysowania przez B.
