# Audyt początkowy i struktura dokumentu

Data: 19.10.2026. Przegląd dotyczy lokalnej wersji przy HEAD `8112694`, bez zmiany projektu technicznego.

## Podstawa i wykonane sprawdzenia

Przeczytano wszystkie pliki `sections/*.tex`, `main.tex`, `preamble.tex`, `metadata.tex`, `data/design.json`, trzy skrypty w `tools/`, Makefile, workflow i dokumentację projektu. W projekcie i sprawdzonych katalogach nadrzędnych nie znaleziono `AGENTS.md`. We wzorcu przeczytano `AGENTS.md`, wskazany `CLAUDE.md`, `main.tex`, `latex-settings.tex` i README; obejrzano stronę tytułową. Wzorca nie zmieniano ani nie przenoszono jego danych formalnych.

Aktualny `output/pdf/lotnisko-polnoc.pdf` ma 21 stron. Wykonano świeży render wszystkich stron, przegląd ich miniatur oraz szczegółowe oględziny stron 10 i 12. Nie jest to końcowy odbiór każdej strony w docelowej skali. Materiał roboczy: `tmp/pdfs/audyt-start-2026-10-19/`.

- `python3 tools/validate_design.py`: wynik OK dla dotychczasowych założeń. Niezależne przeliczenie potwierdza 1520 m tras oraz 7,2576 TB zapisu / 9,072 TB z zapasem 25%; to nie potwierdza doboru kamer ani przedmiaru instalacji lokalnych.
- Kompilacja bazowa przez `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=tmp/pdfs/audyt-start-2026-10-19/build main.tex`: powodzenie, 21 stron. Końcowy `main.log` nie zawiera ostrzeżeń, niezdefiniowanych odsyłaczy ani komunikatów overfull/underfull. Ostrzeżenia pierwszego przebiegu o odsyłaczach zniknęły po automatycznym ponowieniu.
- Istniejący ZIP Overleafa: poprawny CRC, `main.tex` w katalogu głównym, 32 wpisy. Zawiera PDF-y rysunków, ale nie `data/design.json`, generatora ani jego zależności. Nie spełnia więc wymagania dostarczenia także źródeł odtwarzających rysunki. Nie wykonano tutaj nowego importu do usługi Overleaf.

## Najważniejsze braki

1. **Nie zamknięto modelu obiektu.** JSON zawiera głównie cztery agregaty węzłów; funkcje sześciu części terminalu i położenia D01–D06 zapisano osobno w generatorze (`tools/generate_figures.py:179`). Brakuje wysokości i warunków pomieszczeń, pełnych wejść oraz wyjść. Wszystkie sześć przejść na rzucie terminalu jest wewnętrznych; nie zaznaczono drzwi zewnętrznych. Rejestr opisuje zespoły, nie pojedyncze elementy (`docs/rejestr-urzadzen.md`). Najpierw A ma określić geometrię i identyfikatory, potem B ją narysuje.

2. **SSP pozostaje rezerwą ilościową.** `sections/05-fire.tex:13` wprost nazywa 20 czujek hangaru rezerwą, a osiem modułów I/O nie stanowi doboru sterowań. Generator terminalu tworzy 48 punktów pętlami `range(6)` i `range(8)` (`tools/generate_figures.py:198`), niezależnie od funkcji pomieszczeń. Brakuje listy elementów/adresów, rzeczywistych połączeń, uzasadnienia typu i zasięgu detekcji, rozdziału izolatorów, obwodów alarmowania oraz macierzy przyczyna–skutek. Nie rozstrzygnięto dla modelu DSO i transmisji pożarowej. To problem A; B nie może naprawić go samym rysunkiem.

3. **CCTV, KD i SSWiN nie są rozpisane na konkretne zadania i obwody.** Przykład 2688 px / 10 m jest rachunkowo użyteczny, ale nie przypisano go do C01–C24. Brakuje wysokości, kierunków, obszarów celu i szerokości kadrów. Dokument słusznie nie deklaruje pełnego pokrycia 24 ha; zarzutem jest brak projektu wybranych kadrów. Dla drzwi brakuje indywidualnych typów zamknięć, połączeń zwolnienia i stanów po zaniku napięcia. SSWiN nie ma przypisania czujek do pomieszczeń, wejść i stref uzbrojenia.

4. **Przedmiar i bilans zasilania nie wynikają z rejestru.** Odcinki R1–R4 mają weryfikowalną geometrię, ale 1800 m kat. 6A, 2200 m KD/SSWiN, lokalne długości SSP i 1700 m energii pozostają szacunkami (`sections/10-terminal.tex:5`, `sections/14-materials-b.tex:32`). Nie ma listy połączeń, tras zasilających ani spadków napięć. 1335 W i rozdział UPS sumują się poprawnie, lecz prądy central przyjęto jednakowe mimo różnych zespołów, a 400 W na DC i ładowanie jest ogólną rezerwą. Sam tekst uczciwie zastrzega, że 0,927 kWh nie potwierdza 30 min; A ma doprowadzić dobór do sprawdzalnego modelu i krzywych producenta, rozdzielając to od późniejszej próby odbiorowej.

5. **Spójność danych i interfejsów jest częściowa.** Walidator ma na sztywno sumy urządzeń, moc i 1520 m (`tools/validate_design.py:10`), a sprawdzenie rysunku ogranicza do istnienia pliku. Nie kontroluje identyfikatorów, pomieszczeń, długości przyłączy, map portów, obwodów SSP i materiałów. Rysunki zawierają także liczby wpisane poza JSON. Nie podano referencyjnej kompatybilnej rodziny SSP ani parametrów optycznych jej magistrali. A powinien przyjąć sprawdzalne rozwiązanie i dane do obliczeń; B odwzoruje jego topologię i powiązania.

6. **AI i procedury wymagają domknięcia.** Są opis przetwarzania lokalnego i sensowna propozycja walidacji bez fikcyjnych wyników. Brakuje jednak wskazania konkretnych kamer, strefy i jednego rozstrzygniętego scenariusza (`sections/11-ai.tex`). Procedury mają role i działania, ale warunki przywrócenia pracy są głównie wspólną uwagą, a nie warunkiem każdego scenariusza (`sections/15-procedures.tex`). Można to uzupełnić bez rozbudowywania podręcznika eksploatacji.

7. **Forma PDF jest sprzeczna z zamówieniem.** Dokument używa 11 pt, wymuszonego kroju bezszeryfowego, marginesów 20–22 mm, barwnych nagłówków, ramek i stałych oznaczeń roboczych w nagłówkach/stopkach (`preamble.tex`). Tytuł zawiera render i podpis o AI, spis treści panel „Pokrycie wymagań”, a rozdział odbiorowy instrukcje podziału pracy. `main.tex` wymusza `clearpage` przed każdym kolejnym plikiem, co zostawia rozległe puste części stron. Wzorcem są Latin Modern 12 pt i około 25 mm; nie należy kopiować klasy book, nagłówków uczelnianych ani danych wzorca. Właściwy etap przebudowy składu: C.

## Osiem wymagań a stan obecny

Wszystkie osiem tematów ma odpowiednik w źródłach, ale sama obecność rozdziałów nie oznacza spełnienia zadania. Tytuł wymaga nowego składu i danych formalnych (C/użytkownik), spis treści oczyszczenia i automatycznych odsyłaczy (C), opis techniczny z AI oraz materiały zamknięcia modelu i doborów (A), lokalizacje i trasy kompletnego modelu połączeń (A), a następnie właściwych rysunków (B). Schemat ideowy wymaga konkretnych interfejsów (A/B), energia doboru z odbiorników i źródeł producentów (A/B), procedury jednoznacznych warunków reakcji i przywrócenia (A). Na końcu C składa wszystkie części i weryfikuje PDF.

## Proponowana struktura końcowa

Przed treścią: klasyczna strona tytułowa i spis treści. Następnie:

1. **Przedmiot, zakres i model obiektu** — funkcje i geometria, przyjęte warunki, strefy oraz istotne zagrożenia; założenia opisane raz.
2. **Rozwiązania techniczne systemów ochrony** — CCTV, KD/SSWiN, SSP/SAP; dobór, zadania, stany awaryjne i macierz przyczyna–skutek.
3. **Sieć, integracja i analityka ML/AI** — topologia, interfejsy, porty i włókna, jeden przypadek AI, wymagania dostępu i danych.
4. **Rozmieszczenie i trasy instalacji** — plan oraz potrzebne rzuty, identyfikatory, obwody, długości i odwołania do rejestru.
5. **Zasilanie i obliczenia projektowe** — bilanse zapisu, transmisji, PoE, mocy, napięć, baterii i źródła rezerwowego; obliczenia można umieścić bliżej odpowiednich doborów, jeśli poprawia to wywód.
6. **Zestawienie materiałów podstawowych** — oddzielnie urządzenia/licencje, przewody, osprzęt i jawne zapasy; ilości wyprowadzone z modelu.
7. **Procedury bezpieczeństwa oraz weryfikacja działania** — wyzwalacz, odpowiedzialny, działanie, warunek przywrócenia, rzeczywiste kryteria prób. Bez organizacji pracy zespołu.
8. **Bibliografia** — źródła pierwotne powiązane z konkretnymi parametrami i twierdzeniami.

Pełny rejestr i większe rysunki mogą być załącznikami tego samego PDF. Nie narzuca się liczby stron, liczby rysunków ani osobnych stron dla każdego pliku. Numeracja powyżej jest propozycją redakcyjną, nie pretekstem do zmiany wielkości technicznych przez C.

## Ograniczony przegląd źródeł pierwotnych

Sprawdzono dostępne strony [RCB](https://www.gov.pl/web/rcb/infrastruktura-krytyczna), [ELI — Dz.U. 2023 poz. 822](https://eli.gov.pl/eli/DU/2023/822/ogl) i [komunikatu PKN](https://www.pkn.pl/komunikat-online). RCB podtrzymuje rozróżnienie między znaczeniem strategicznym a formalną kwalifikacją IK. PKN wskazuje zastąpienie PN-EN 62676-4:2015-06 przez PN-EN IEC 62676-4:2026-01; jest to potwierdzenie oznaczenia, nie treści normy.

W [odczytanym tekście ELI z 2023 r.](https://eli.gov.pl/api/acts/DU/2023/822/text.html) § 28 ust. 1 pkt 19 i § 29 ust. 1 pkt 8 odnoszą się do dworców i portów o obsadzie ponad 500 osób. Obecne założenie 300 osób w terminalu nie zamyka jeszcze oceny całego przyjętego obiektu ani pozostałych przesłanek. Strona ELI wskazuje dwie późniejsze zmiany; ich pełnej analizy nie wykonano w tym audycie. Weryfikacja stanu prawnego na datę projektu, zastosowania do wybranego modelu oraz kart i kompatybilności urządzeń należy do A. Nie przyjęto tutaj wniosku o obowiązku lub braku obowiązku DSO ani transmisji do PSP.
