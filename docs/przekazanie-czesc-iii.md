# Przekazanie: część II → część III (rozdz. 13–17)

Część II przechodzi na nowy plan lotniska (`docs/plan-czesc-ii.md`, rysunki F1 `figures/fig-site.pdf` i F2 `figures/fig-terminal.pdf`). Rozdziały 13–17 odwołują się do urządzeń R1 (C01–C08, G01, AI1), które w części II mają nowe odpowiedniki.

## Mapa identyfikatorów

| R1 | Część II | Uwagi |
|---|---|---|
| C01–C04 (PATH1) | `KT03`–`KT06` | PATH1 na wyjściu z `PK1` do holu `Z-AS` |
| C05 | `KT01`, `KT02` | hol landside |
| C06, C07 | brak | poza zakresem |
| C08 + AI1 | `KP03` + S5 | linia `L3` przy `B1` |
| G01 | `B1` | brama przesuwna z napędem i furtka, ok. 120 m od terminalu |
| AI1 | S1–S5 | karty scenariuszy w rozdz. 11 |
| brak | `KT07`, `KT08`, `KP01`, `KP02`, `PTZ1` | `DT1`, hol airside, termowizja `OG1`, PTZ przy `B1` |
| brak | `N0`, `SP1`, `SP2` | rdzeń w IT, szafy polowe przy `B1` i na końcu `OG1` |

## Zasilanie (rozdz. 13)

- Rozdz. 12 podaje bilans mocy bez czasu podtrzymania. Czas podtrzymania liczy rozdz. 13.
- Odbiory centralnego UPS: `N0`, NAS, SOC, kamery terminalu `KT01`–`KT08` i `KP01` przez PoE z `N0` (`KP01` stoi 4 m od terminalu, ok. 35 m miedzi).
- `SP1`, `SP2`: zasilanie 230 V z lokalnym UPS na szynie DIN. `SP1` zasila `KP03`, `PTZ1`, kontroler `B1` i napęd `B1`, `SP2` zasila `KP02`.
- Napęd `B1` (przykład FAAC 741, 500 W) ma osobny wyłącznik w `SP1` przed UPS DIN. Przy zaniku sieci bramę otwiera się ręcznie, furtka działa z PoE kontrolera.
- Moc do pokrycia (rozdz. 12): centralny UPS 1076 W z zapasem 25%, UPS DIN co najmniej 195 W (ten sam model w `SP1` i `SP2`).
- Obwody 230 V do szaf: `SP1` kabel ziemny 3 × 4 mm², `SP2` 3 × 2,5 mm², każdy z RCD 30 mA.
- Klasy PoE: Q1972-E klasa 3 (maks. 12,95 W), Q6355-LE 802.3bt klasa 6 (51 W). Dokładne liczby w rozdz. 12.
- Długi przewód DC do `G01` znika. `B1` zasila `SP1`.

## Materiały (rozdz. 14)

- 12 kamer zamiast 8. Licencje ACS Pro dla 12 kamer i kontrolera `B1`.
- Dochodzi światłowód SM w gwieździe `N0` → `SP1`/`SP2`, moduły SFP, przełączniki polowe (przykład AXIS T8504-R), szafy polowe z UPS DIN i zasilaczem DIN PS56, napęd bramy `B1`, furtka. Zgodność `PTZ1` (802.3bt klasa 6) z portem AXIS High PoE do potwierdzenia przed zakupem. W R1 zakup światłowodu był wykluczony.
- Długości tras po zapasie: rozdz. 9.

## Procedury (rozdz. 15)

- Reguła AI1 → reguły S1–S5. Wyłączenie reguły dotyczy konkretnego scenariusza.
- S4 (naruszenie `OG1`) ma tory: czujnik, VMS, SOC, patrol, służba operacyjna (rysunek F7 w rozdz. 11).
- `PTZ1` prowadzi automatycznie obiekt z `KP01`. Dla `KP02` VMS ustawia preset.

## Cyberbezpieczeństwo i prywatność (rozdz. 16)

- C08 → `KP03` i kamery terminalu.
- Wyszukiwanie po wyglądzie (AXIS Camera Station Pro Smart search 2, scenariusz S3) działa na nagraniach, bez biometrii. Warto ująć w ocenie DPIA.
- Termowizja `KP01`, `KP02` obserwuje granicę, nie identyfikuje osób.

## Walidacja (rozdz. 17)

- Próby PATH1: C01–C04 → `KT03`–`KT06`.
- Próby AI1 → osobne kryteria dla S1–S5.
- Nowe próby: zasięg wykrycia `KP01`, `KP02` wzdłuż `OG1`, przejęcie obiektu przez `PTZ1` (parowanie do sprawdzenia), linia `L3` przy `B1`.
- Wnętrze `PK1` (stanowiska CT, kamery nad nimi) należy do części III. Część II podaje tylko obrys.

## Nowe źródła (lista `sources` w `data/design.json`)

`S-AOA2`, `S-SS2`, `S-PD`, `S-PDPTZ`, `S-Q1972`, `S-Q6355`, `S-D2210`, `S-T8504`, `S-RWSL`, `S-PXD`, `S-GATE`. Dopisuje część II.
