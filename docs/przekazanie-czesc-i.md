# Przekazanie: część II → część I (rozdz. 1–5)

Część II przechodzi na nowy plan lotniska (`docs/plan-czesc-ii.md`, rysunki F1 `figures/fig-site.pdf` i F2 `figures/fig-terminal.pdf`). Rozdziały 1–5 opierają się na geometrii R1, która przestaje pasować do rozdz. 6–12.

## Co się zmienia

- Teren: zamiast działki 80 × 60 m terminal 60 × 30 m, płyta postojowa, droga kołowania, fragment pasa, ogrodzenie `OG1` 300 m.
- Strefy: `Z-LS` landside, `Z-KB` kontrola (`PK1`), `Z-AS` airside, `Z-OP` strefa operacyjna.
- Terminal: hol `Z-LS`, pas `PK1`, hol `Z-AS`, część techniczna (korytarz z `DT1`, IT z `N0`, SOC, zaplecze, wejście pracowników). Pomieszczenia R101–R107 i obrys T0 24 × 16 m nie występują w części II.
- `G01` i parking pracowników (A02) nie wchodzą do części II. Funkcję wjazdu służbowego przejmuje `B1` w `OG1`.

## Mapa identyfikatorów

| R1 (rozdz. 1–5) | Część II | Uwagi |
|---|---|---|
| C01–C04 (PATH1 w R102) | `KT03`–`KT06` | PATH1 na wyjściu z `PK1` do holu `Z-AS`, 4 kierunki |
| C05 (hol R101) | `KT01`, `KT02` | hol landside, dwa narożniki |
| C06 (plac A01), C07 (parking) | brak | poza zakresem części II |
| C08 + AI1 (pas wjazdu G01) | `KP03` + S5 | linia `L3` przy `B1` |
| brak | `KT07` | drzwi `DT1`, scenariusz S1 |
| brak | `KT08` | hol airside |
| brak | `KP01`, `KP02` | termowizja AXIS Q1972-E na końcach `OG1`, S4 |
| brak | `PTZ1` | AXIS Q6355-LE przy `B1` |
| G01 | `B1` | brama przesuwna z napędem i furtka, czytnik karty z PIN po obu stronach, bez interkomu i LPR |
| D01–D04 | do ponumerowania w części I | F2 pokazuje przejścia z KD: wejście pracowników, wejście do korytarza, SOC, IT, zaplecze, `DT1` |
| AI1 | S1–S5 | karty scenariuszy w rozdz. 11 |

## Do poprawy w rozdziałach

- **Rozdz. 1:** opis terenu, strefy, `B1` zamiast `G01`, bez parkingu. Makra `\ParkingCount`, `\ModelRooms` opisują R1.
- **Rozdz. 2:** scenariusze S1–S5 jako zagrożenia do macierzy ryzyka (pozostawanie przy `DT1`, ruch pod prąd do `PK1`, wyszukiwanie osoby, naruszenie `OG1`, nieuprawniony ruch przez `B1`).
- **Rozdz. 3:** 12 kamer (`KT01`–`KT08`, `KP01`–`KP03`, `PTZ1`). Retencję (`\StorageNeed`) liczyć dla 12 kamer. Tabele `\CameraTable`, `\OpticsTable` dotyczą R1. Kamery nad stanowiskami CT należą do części III.
- **Rozdz. 4:** nowa lista drzwi z KD według F2. `B1`: brama z napędem, czytniki z PIN w obu kierunkach, furtka z tym samym czytnikiem. SSWiN do nowych pomieszczeń.
- **Rozdz. 5:** lista drzwi z mechanicznym wyjściem (D01–D04) według nowej numeracji. Rozdz. 6 zakłada, że SSP i swobodne wyjście nie zależą od analityki ani sieci.

## Nowe źródła (lista `sources` w `data/design.json`)

`S-AOA2`, `S-SS2`, `S-PD`, `S-PDPTZ`, `S-Q1972`, `S-Q6355`, `S-D2210`, `S-T8504`, `S-RWSL`, `S-PXD`, `S-GATE`. Dopisuje część II.
