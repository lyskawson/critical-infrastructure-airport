# Plan części II: rozdziały 6–12

Ustalone 22 listopada 2026. Rozwija `docs/praca-zespolowa.md` dla części II. Gałąź robocza `part-2`.

## Zasady

- Nowy plan funkcjonalny lotniska zamiast działki 80 × 60 m z R1. Obwiednia samochodu, G01 i parking pracowników nie wchodzą do części II.
- `data/design.json` pozostaje materiałem pomocniczym R1. Rozdziały 6–12 nie używają makr R1 (`\RouteTable`, `\UPSLoad` itd.). Nowe liczby i krótkie tabele są w tekście. Wyjątek: nowe źródła dopisuje się do listy `sources`, bo z niej powstaje wspólna bibliografia.
- Rozdziałów spoza 6–12 nie zmieniamy. Zmiany dla części I i III trafiają do dwóch krótkich notatek: `docs/przekazanie-czesc-i.md`, `docs/przekazanie-czesc-iii.md`.
- Urządzenia Axis są przykładem potwierdzającym wykonalność funkcji, nie wymaganiem.
- Rysunki w TikZ: `figures/src/*.tex` w klasie `standalone`, wspólny styl `figures/src/style.tex` z paletą preambuły. PDF-y wstawiane przez `\includegraphics`, bez zmian preambuły. Stary generator reportlab i archiwalne PDF-y usunięte. `make figures` kompiluje `figures/src/fig-*.tex` do `figures/`.
- Tekst bez średników i półpauz.

## Identyfikatory

| Grupa | ID |
|---|---|
| Strefy | `Z-LS` landside, `Z-KB` kontrola, `Z-AS` airside, `Z-OP` strefa operacyjna |
| Kamery | `KT01–KT08` terminal, `KP01–KP03` teren, `PTZ1`, `RD1` (radar tylko jako wariant) |
| Obiekty | `DT1` drzwi techniczne, `B1` brama służbowa, `OG1` odcinek ogrodzenia, `PK1` punkt kontroli |
| Analityka | `L1` strefa ostrzegawcza, `L2` granica chroniona, `L3` wejście do obszaru krytycznego, `S1–S5` scenariusze |
| Sieć | `N0` rdzeń, `SP1`, `SP2` szafy polowe |

## Układ lotniska (skala metryczna)

- Terminal 60 × 30 m przy drodze dojazdowej, płyta postojowa ok. 150 × 80 m od strony airside.
- Droga kołowania do pasa, pas 45 m szerokości jako fragment z symbolem przerwania.
- `OG1` 300 m między terenem landside a płytą. `B1` w `OG1` na drodze serwisowej ok. 120 m od wschodniej ściany terminalu.
- `SP1` przy `B1`, `SP2` na drugim końcu `OG1`.
- Rów kablowy 4 m za `OG1` po stronie `Z-AS`, światłowody SM `N0` → `SP1`/`SP2` i kable 230 V w osobnych rurach.
- `KP01` stoi 4 m od terminalu i ma PoE z `N0` (ok. 35 m miedzi z ogranicznikami przepięć).
- Terminal: hol `Z-LS`, `PK1` (obrys dla części III), hol `Z-AS`, SOC, IT z `N0`, korytarz techniczny z `DT1`.

## Urządzenia części II

- `KT01–KT02` hol landside, `KT03–KT06` wyjście z `PK1` (PATH1, 4 kierunki, `KT03` z linią kierunkową S2), `KT07` przy `DT1` (S1), `KT08` hol airside.
- `KP01`, `KP02`: AXIS Q1972-E z obiektywem 19 mm na końcach `OG1`, skierowane wzdłuż ogrodzenia, Perimeter Defender.
- `PTZ1`: AXIS Q6355-LE przy `B1`, PTZ Autotracking z `KP01`, preset z reguły VMS dla `KP02`.
- `B1`: brama przesuwna z napędem, furtka, czytnik karty z PIN po obu stronach, `KP03` z linią `L3`. Bez interkomu i LPR.
- Radar D2210-VE tylko w porównaniu czujników.
- Kamery nad stanowiskami CT należą do części III.

## Rozdziały

| Rozdz. | Treść | Rysunki |
|---|---|---|
| 6 Architektura | warstwy, role (SOC, operator bagażu, patrol, służba operacyjna), macierz zdarzeń ok. 8 wierszy, SSP i swobodne wyjście niezależne od analityki, bagaż bez założonego API | F3 |
| 7 Sieć | gwiazda SM z `N0` do `SP1`/`SP2`, VLAN skrótem, pasmo 12 kamer, bilans PoE `SP1` | F4 |
| 8 Plan | układ, strefy, przepływ przed/po kontroli, obrys `PK1` | F1, F2 |
| 9 Trasy | 7 tras głównych: medium, długość z planu, $L_{zak}=\lceil L(1+f)\rceil$ | F8 |
| 10 Osoba | PATH1 na wyjściu z `PK1`, jedno obliczenie px/m, S3: śledzenie w jednej kamerze, Smart search 2, śledzenie na żywo tylko jako wariant | F2b |
| 11 Analityka | karty S1–S5 (miejsce → obserwacja → warunek → informacja → reakcja → ograniczenie), potok ML, kamizelka jako akapit (PPE monitoring beta), RWSL jako odrębna technologia, ocena skrócona | F5, F6, F7, F9a |
| 12 Zasilanie | bilans centralnego UPS i szaf polowych (230 V + UPS DIN), obwody 230 V do szaf ze spadkiem napięcia, bez czasu podtrzymania | F9b |

Scenariusze: S1 pozostawanie >120 s przy `DT1`, S2 ruch pod prąd z `Z-AS` do `PK1`, S3 wyszukiwanie oznaczonej osoby, S4 naruszenie `OG1` (`L1` → `L2`), S5 nieuprawniony ruch przez `B1` (`L3`).

## Rysunki

| ID | Plik | Treść |
|---|---|---|
| F1 | `fig-site.tex` | plan sytuacyjny, strefy, `OG1`, `B1`, legenda |
| F2 | `fig-terminal.tex` | terminal, przepływ przed/po kontroli, kamery z polami widzenia |
| F3 | `fig-architecture.tex` | sensory → analityka w kamerze → sieć → VMS → role |
| F4 | `fig-network.tex` | `N0`, światłowód do `SP1`/`SP2`, VLAN |
| F2b | `fig-path1.tex` | PATH1: wymagane 250 px/m i gęstość pikseli `KT03`–`KT06` |
| F5 | `fig-perimeter.tex` | `OG1` + `B1`, `L1–L3`, pokrycie termowizji, PTZ i radaru jako pasy wzdłuż ogrodzenia |
| F6 | `fig-ml-pipeline.tex` | detektor → śledzenie → reguła → zdarzenie → operator |
| F7 | `fig-s4-swimlane.tex` | tory S4: czujnik, VMS, SOC, patrol, służba operacyjna |
| F8 | `fig-routes.tex` | a: rów kablowy wzdłuż `OG1`, b: koryta w terminalu |
| F9a | `fig-chart-pixels.tex` | piksele na człowieka od odległości |
| F9b | `fig-chart-power.tex` | bilans mocy centralnego UPS i zasilaczy szaf polowych |

Geometria terenu jest jedna (`figures/src/site.tex`), a F1, F2, F5 i F8 są jej widokami.

## Obliczenia w głównym tekście

1. px/m dla jednej kamery PATH1.
2. Piksele na człowieka od odległości dla Q1972-E wobec minimum analityki.
3. Pasmo 12 kamer, łącza `SP1`/`SP2`, port NAS.
4. Bilans PoE `SP1`.
5. Bilans mocy centralnego UPS i szaf polowych.

Retencja (rozdz. 3) i czas podtrzymania (rozdz. 13) pozostają w częściach I i III.

## Źródła

Nowe klucze w `sources`: `S-AOA2`, `S-SS2`, `S-PD`, `S-PDPTZ`, `S-Q1972`, `S-Q6355`, `S-D2210`, `S-T8504`, `S-RWSL`, `S-PXD`, `S-GATE`.

## Kolejność

1. `style.tex`, `site.tex`, F1, F2. Przegląd planu przez użytkownika.
2. Notatki dla części I i III.
3. Rozdziały 8 → 11 → 10 → 6 → 7 → 9 → 12, kompilacja po każdym.
4. Commit tylko na polecenie użytkownika, bez push.
