# Rejestr urządzeń i połączeń - pakiet A

Eksport z `data/design.json`, wersja `A-2026-10-24-R1`, SHA256 `3a0e29eaecfa59554c566d141468290e8ebef0ea96979d5b729f6c0f4bed4286`.
Nie edytować niezależnie; regeneracja: `make data`. Jednostki: m, W, A; punkty nie są pomiarem.

## Urządzenia

| ID | Model | Miejsce; układ; (x,y,z) | Zasilanie | Port/obwód |
|---|---|---|---|---|
| C01 | AXIS P3265-LVE 9 mm | R102; T0; [20, 9.5, 2.4] | SW-0 | IP-C01:ETH, INT-SD-C01:SD |
| SD-C01 | AXIS Surveillance Card 128GB | R102; T0; [20, 9.5, 2.4] | C01 | INT-SD-C01:CARD |
| C02 | AXIS P3265-LVE 9 mm | R102; T0; [20, 0.5, 2.4] | SW-0 | IP-C02:ETH, INT-SD-C02:SD |
| SD-C02 | AXIS Surveillance Card 128GB | R102; T0; [20, 0.5, 2.4] | C02 | INT-SD-C02:CARD |
| C03 | AXIS P3265-LVE 9 mm | R102; T0; [16.2, 5, 2.4] | SW-0 | IP-C03:ETH, INT-SD-C03:SD |
| SD-C03 | AXIS Surveillance Card 128GB | R102; T0; [16.2, 5, 2.4] | C03 | INT-SD-C03:CARD |
| C04 | AXIS P3265-LVE 9 mm | R102; T0; [23.8, 5, 2.4] | SW-0 | IP-C04:ETH, INT-SD-C04:SD |
| SD-C04 | AXIS Surveillance Card 128GB | R102; T0; [23.8, 5, 2.4] | C04 | INT-SD-C04:CARD |
| C05 | AXIS P3265-LVE 9 mm | R101; T0; [0.5, 0.5, 2.8] | SW-0 | IP-C05:ETH, INT-SD-C05:SD |
| SD-C05 | AXIS Surveillance Card 128GB | R101; T0; [0.5, 0.5, 2.8] | C05 | INT-SD-C05:CARD |
| C06 | AXIS P3265-LVE 9 mm | A01; SITE; [24, 24.7, 2.8] | SW-0 | IP-C06:ETH, INT-SD-C06:SD |
| SD-C06 | AXIS Surveillance Card 128GB | A01; SITE; [24, 24.7, 2.8] | C06 | INT-SD-C06:CARD |
| C07 | AXIS P3265-LVE 9 mm | A02; SITE; [60, 49, 4] | SW-0 | INT-SD-C07:SD, IP-C07-C:ETH |
| SD-C07 | AXIS Surveillance Card 128GB | A02; SITE; [60, 49, 4] | C07 | INT-SD-C07:CARD |
| C08 | AXIS P3265-LVE 9 mm | A03; SITE; [63, 20, 3] | SW-0 | INT-SD-C08:SD, IP-C08-C:ETH |
| SD-C08 | AXIS Surveillance Card 128GB | A03; SITE; [63, 20, 3] | C08 | INT-SD-C08:CARD |
| KD-01 | AXIS A1210 | R102; T0; [20, 0.4, 2.4] | SW-0 | IP-KD-01:ETH, BUS-RD-D01-IN:READER, PWR-D01:LOCK, DPS-D01:DPS, REX-D01:REX, DC-RD-D01-IN:READER-12V |
| RD-D01-IN | HID Signo 40K Standard, profil Seos/SIO (HID Elite) | A01; SITE; [39.2, 24.8, 1.1] | KD-01 | BUS-RD-D01-IN:BUS, DC-RD-D01-IN:DC |
| LK-D01 | effeff 118.13 A71 + zamek z klamką wewnętrzną | R102; T0; [20, 0, 1] | KD-01 | PWR-D01:DC |
| DC-D01 | SATEL S-4 NC z sabotażem | R102; T0; [20, 0, 2.05] | passive | DPS-D01:LINE |
| RX-D01 | Styk klamki mechanicznej NC | R102; T0; [20, 0, 1] | passive | REX-D01:LINE |
| KD-02 | AXIS A1210 | R102; T0; [16.3, 5, 2.4] | SW-0 | IP-KD-02:ETH, BUS-RD-D02-IN:READER, PWR-D02:LOCK, DPS-D02:DPS, REX-D02:REX, DC-RD-D02-IN:READER-12V |
| RD-D02-IN | HID Signo 40K Standard, profil Seos/SIO (HID Elite) | R101; T0; [15.8, 4.3, 1.1] | KD-02 | BUS-RD-D02-IN:BUS, DC-RD-D02-IN:DC |
| LK-D02 | effeff 118.13 A71 + zamek z klamką wewnętrzną | R102; T0; [16, 5, 1] | KD-02 | PWR-D02:DC |
| DC-D02 | SATEL S-4 NC z sabotażem | R102; T0; [16, 5, 2.05] | passive | DPS-D02:LINE |
| RX-D02 | Styk klamki mechanicznej NC | R102; T0; [16, 5, 1] | passive | REX-D02:LINE |
| KD-03 | AXIS A1210 | R103; T0; [3, 10.3, 2.4] | SW-0 | IP-KD-03:ETH, BUS-RD-D03-IN:READER, PWR-D03:LOCK, DPS-D03:DPS, REX-D03:REX, DC-RD-D03-IN:READER-12V |
| RD-D03-IN | HID Signo 40K Standard, profil Seos/SIO (HID Elite) | R101; T0; [2.3, 9.8, 1.1] | KD-03 | BUS-RD-D03-IN:BUS, DC-RD-D03-IN:DC |
| LK-D03 | effeff 118.13 A71 + zamek z klamką wewnętrzną | R103; T0; [3, 10, 1] | KD-03 | PWR-D03:DC |
| DC-D03 | SATEL S-4 NC z sabotażem | R103; T0; [3, 10, 2.05] | passive | DPS-D03:LINE |
| RX-D03 | Styk klamki mechanicznej NC | R103; T0; [3, 10, 1] | passive | REX-D03:LINE |
| KD-04 | AXIS A1210 | R104; T0; [8, 10.3, 2.4] | SW-0 | IP-KD-04:ETH, BUS-RD-D04-IN:READER, PWR-D04:LOCK, DPS-D04:DPS, REX-D04:REX, DC-RD-D04-IN:READER-12V |
| RD-D04-IN | HID Signo 40K Standard, profil Seos/SIO (HID Elite) | R101; T0; [7.3, 9.8, 1.1] | KD-04 | BUS-RD-D04-IN:BUS, DC-RD-D04-IN:DC |
| LK-D04 | effeff 118.13 A71 + zamek z klamką wewnętrzną | R104; T0; [8, 10, 1] | KD-04 | PWR-D04:DC |
| DC-D04 | SATEL S-4 NC z sabotażem | R104; T0; [8, 10, 2.05] | passive | DPS-D04:LINE |
| RX-D04 | Styk klamki mechanicznej NC | R104; T0; [8, 10, 1] | passive | REX-D04:LINE |
| KD-05 | AXIS A1210 | R104; T0; [6.8, 14.8, 1.5] | SW-0 | IP-KD-05:ETH, BUS-RD-G01-IN:READER, DC-RD-G01-IN:READER-12V, DPS-G01:DPS |
| RD-G01-IN | HID Signo 40K Standard, profil Seos/SIO (HID Elite) | A00; SITE; [64.5, 9, 1.1] | KD-05 | BUS-RD-G01-IN:BUS, BUS-RD-G01-OUT:BUS, DC-RD-G01-IN:DC, DC-RD-G01-OUT:DC |
| RD-G01-OUT | HID Signo 40K Standard, profil Seos/SIO (HID Elite) | A03; SITE; [64.5, 11, 1.1] | KD-05 | BUS-RD-G01-OUT:BUS, DC-RD-G01-OUT:DC |
| MECH-G01 | Wyposażenie mechaniczne przejścia | A03; SITE; [65, 10, 1] | none | PE-G01:PE |
| SW-0 | TP-Link SG3428MP (UN) v6.30 | R104; T0; [6.8, 14.8, 1.7] | UPS-0 | IP-C01:P01, IP-C02:P02, IP-C03:P03, IP-C04:P04, IP-C05:P05, IP-C06:P06, IP-KD-01:P09, IP-KD-02:P10, IP-KD-03:P11, IP-KD-04:P12, IP-NAS-0:P14, IP-SOC-0:P15, IP-FW-0:P16, IP-IP-I01:P17, AC-SW-0:AC, IP-C07-A:P07, IP-C08-A:P08, IP-KD-05:P13 |
| NAS-0 | Synology DS923+ (dyski w oddzielnej pozycji) | R104; T0; [6.8, 14.8, 1.2] | UPS-0 | IP-NAS-0:ETH, INT-HDD1:HDD1, INT-HDD2:HDD2, INT-HDD3:HDD3, INT-HDD4:HDD4, AC-NAS-0:AC |
| HDD-01 | Synology HAT3300-8T 8TB | R104; T0; [6.8, 14.8, 1.2] | NAS-0 | INT-HDD1:SATA |
| HDD-02 | Synology HAT3300-8T 8TB | R104; T0; [6.8, 14.8, 1.2] | NAS-0 | INT-HDD2:SATA |
| HDD-03 | Synology HAT3300-8T 8TB | R104; T0; [6.8, 14.8, 1.2] | NAS-0 | INT-HDD3:SATA |
| HDD-04 | Synology HAT3300-8T 8TB | R104; T0; [6.8, 14.8, 1.2] | NAS-0 | INT-HDD4:SATA |
| SOC-0 | Dell OptiPlex Micro 7020 i5-13500T, 32GB, SSD512, Windows11 Pro | R103; T0; [3, 13, 0.8] | UPS-0 | IP-SOC-0:ETH, AC-SOC-0:AC, DP-1:DP1, DP-2:DP2, UPS-USB:USB |
| MON-01 | Dell P2425H, DP | R103; T0; [3, 13, 1.1] | UPS-0 | AC-MON-01:AC, DP-1:VIDEO |
| MON-02 | Dell P2425H, DP | R103; T0; [4, 13, 1.1] | UPS-0 | AC-MON-02:AC, DP-2:VIDEO |
| FW-0 | TP-Link ER605 v2.20; WAN disconnected | R104; T0; [6.8, 14.8, 1.8] | UPS-0 | IP-FW-0:ETH, AC-FW-0:AC |
| UPS-0 | Eaton 5PX1500IRT2UG2 (EBM w oddzielnej pozycji) | R104; T0; [6.8, 14.8, 0.3] | RSEC:Q1 | INT-EBM1:EBM1, AC-SW-0:OUT1, AC-NAS-0:OUT2, AC-SOC-0:OUT3, AC-MON-01:OUT4, AC-MON-02:OUT5, AC-FW-0:OUT6, AC-UPS:AC, UPS-USB:USB, PWP-RPO:RPO |
| EBM-01 | Eaton 5PXEBM48RT2UG2 | R104; T0; [6.8, 14.8, 0.15] | UPS-0 | INT-EBM1:IN, INT-EBM2:OUT |
| EBM-02 | Eaton 5PXEBM48RT2UG2 | R104; T0; [6.8, 14.8, 0.15] | UPS-0 | INT-EBM2:IN |
| RSEC | Rozdzielnica RSEC / PWP / PE | R104; T0; [9, 12, 1.5] | BOUNDARY-230V | AC-UPS:Q1, AC-SSWIN:Q2, AC-SSP:Q0, PWP-RPO:PWP-NC, PE-SPD-01:PE, PE-SPD-02:PE, PE-SPD-03:PE, PE-SPD-04:PE, PE-G01:PE |
| CSP-0 | SATEL ACSP-402 z fabrycznym APS-318 | R103; T0; [1, 11, 1.5] | RSEC:Q0 | INFO-FIRE:OUT1, INFO-FAULT:OUT8, FL1-01:L1A, FL1-23:L1B, INT-BAT-F01:BAT, AC-SSP:AC |
| BAT-F01 | Akumulator VRLA 12V 17Ah (SATEL B-17) | R103; T0; [1, 11, 1.2] | CSP-0 | INT-BAT-F01:DC |
| SSWiN-0 | SATEL VERSA 15 + transformator 40VA / OPU-4 P | R104; T0; [8.5, 13, 1.5] | RSEC:Q2 | AL-I01:Z1, AL-I02:Z2, AL-I03:Z3, AL-I04:Z4, AL-I05:Z5, AL-I06:Z6, AL-IC-E01:Z7, AL-IC-E02:Z8, AL-IC-E03:Z9, AL-IC-D01:Z10, BUS-KP:BUS, BUS-ETHM:BUS, AL-SIREN:OUT1, AL-SIREN-T:Z13, AL-PANIC:Z15, INFO-FIRE:Z11, INFO-FAULT:Z12, INT-BAT-I01:BAT, AC-SSWIN:AC, INT-TAMPER-I:Z14 |
| BAT-I01 | Akumulator VRLA 12V 17Ah (SATEL B-17) | R104; T0; [8.5, 13, 1.2] | SSWiN-0 | INT-BAT-I01:DC |
| IP-I01 | SATEL ETHM-1 Plus | R104; T0; [8.5, 13, 1.5] | SSWiN-0 | IP-IP-I01:ETH, BUS-ETHM:BUS |
| KP-I01 | SATEL VERSA-LCDM-WH | R103; T0; [2.2, 11, 1.4] | SSWiN-0 | BUS-KP:BUS |
| SI-I01 | SATEL SPW-100 | R101; T0; [7.5, 9.8, 2.7] | SSWiN-0 | AL-SIREN:DC, AL-SIREN-T:TAMPER |
| PA-I01 | SATEL PNK-1 napadowy NC z sabotażem | R103; T0; [3, 13, 0.7] | passive | AL-PANIC:LINE |
| I01 | SATEL SLIM-PIR, soczewka standardowa | R101; T0; [0.3, 9.7, 2.4] | SSWiN-0 | AL-I01:LINE |
| I02 | SATEL SLIM-PIR, soczewka standardowa | R101; T0; [15.7, 0.3, 2.4] | SSWiN-0 | AL-I02:LINE |
| I03 | SATEL SLIM-PIR, soczewka standardowa | R102; T0; [23.7, 0.3, 2.4] | SSWiN-0 | AL-I03:LINE |
| I04 | SATEL SLIM-PIR, soczewka standardowa | R104; T0; [9.7, 15.7, 2.4] | SSWiN-0 | AL-I04:LINE |
| I05 | SATEL SLIM-PIR, soczewka standardowa | R105; T0; [10.3, 15.7, 2.4] | SSWiN-0 | AL-I05:LINE |
| I06 | SATEL SLIM-PIR, soczewka standardowa | R107; T0; [20.3, 15.7, 2.4] | SSWiN-0 | AL-I06:LINE |
| IC-E01 | SATEL S-4 NC z sabotażem | R101; T0; [4, 0, 2.05] | passive | AL-IC-E01:LINE |
| IC-E02 | SATEL S-4 NC z sabotażem | R101; T0; [0, 7, 2.05] | passive | AL-IC-E02:LINE |
| IC-E03 | SATEL S-4 NC z sabotażem | R102; T0; [24, 8, 2.05] | passive | AL-IC-E03:LINE |
| IC-D01 | SATEL S-4 NC z sabotażem | R102; T0; [20, 0, 2.05] | passive | AL-IC-D01:LINE |
| F01 | SATEL DMP-400 + DB-400 | R101; T0; [4, 2.5, 3] | CSP-0 | FL1-02:IN, FL1-03:OUT |
| F02 | SATEL DMP-400 + DB-400 | R101; T0; [12, 2.5, 3] | CSP-0 | FL1-07:IN, FL1-08:OUT |
| F03 | SATEL DMP-400 + DB-400 | R101; T0; [4, 7.5, 3] | CSP-0 | FL1-04:IN, FL1-05:OUT |
| F04 | SATEL DMP-400 + DB-400 | R101; T0; [12, 7.5, 3] | CSP-0 | FL1-06:IN, FL1-07:OUT |
| F05 | SATEL DMP-400 + DB-400 | R102; T0; [20, 2.5, 3] | CSP-0 | FL1-09:IN, FL1-10:OUT |
| F06 | SATEL DMP-400 + DB-400 | R102; T0; [20, 7.5, 3] | CSP-0 | FL1-11:IN, FL1-12:OUT |
| F07 | SATEL DMP-400 + DB-400 | R103; T0; [3, 13, 3] | CSP-0 | FL1-21:IN, FL1-22:OUT |
| F08 | SATEL DMP-400 + DB-400 | R104; T0; [8, 13, 3] | CSP-0 | FL1-19:IN, FL1-20:OUT |
| F09 | SATEL DMP-400 + DB-400 | R105; T0; [13, 13, 3] | CSP-0 | FL1-17:IN, FL1-18:OUT |
| F10 | SATEL DCP-400 + DB-400, A1R | R106; T0; [18, 13, 3] | CSP-0 | FL1-15:IN, FL1-16:OUT |
| F11 | SATEL DMP-400 + DB-400 | R107; T0; [22, 13, 3] | CSP-0 | FL1-13:IN, FL1-14:OUT |
| ROP-01 | SATEL ROP-400/PL | R101; T0; [4.8, 0.2, 1.4] | CSP-0 | FL1-01:IN, FL1-02:OUT |
| ROP-02 | SATEL ROP-400/PL | R101; T0; [0.2, 6, 1.4] | CSP-0 | FL1-05:IN, FL1-06:OUT |
| ROP-03 | SATEL ROP-400/PL | R102; T0; [23.8, 7, 1.4] | CSP-0 | FL1-12:IN, FL1-13:OUT |
| SF-01 | SATEL SPP-400 | R101; T0; [4, 5, 2.7] | CSP-0 | FL1-03:IN, FL1-04:OUT |
| SF-02 | SATEL SPP-400 | R101; T0; [12, 5, 2.7] | CSP-0 | FL1-08:IN, FL1-09:OUT |
| SF-03 | SATEL SPP-400 | R102; T0; [20, 5, 2.7] | CSP-0 | FL1-10:IN, FL1-11:OUT |
| SF-04 | SATEL SPP-400 | R103; T0; [3, 12, 2.7] | CSP-0 | FL1-22:IN, FL1-23:OUT |
| SF-05 | SATEL SPP-400 | R104; T0; [8, 12, 2.7] | CSP-0 | FL1-20:IN, FL1-21:OUT |
| SF-06 | SATEL SPP-400 | R105; T0; [13, 12, 2.7] | CSP-0 | FL1-18:IN, FL1-19:OUT |
| SF-07 | SATEL SPP-400 | R106; T0; [18, 12, 2.7] | CSP-0 | FL1-16:IN, FL1-17:OUT |
| SF-08 | SATEL SPP-400 | R107; T0; [22, 12, 2.7] | CSP-0 | FL1-14:IN, FL1-15:OUT |
| SPD-01 | DEHNpatch DPA M CLE RJ45B48 ClassE,929121 | R107; T0; [23.8, 13, 2] | passive | IP-C07-A:IN, IP-C07-B:OUT, PE-SPD-01:PE |
| SPD-02 | DEHNpatch DPA M CLE RJ45B48 ClassE,929121 | A02; SITE; [60, 49, 3.5] | passive | IP-C07-B:IN, IP-C07-C:OUT, PE-SPD-02:PE |
| SPD-03 | DEHNpatch DPA M CLE RJ45B48 ClassE,929121 | R102; T0; [23.8, 2, 2.4] | passive | IP-C08-A:IN, IP-C08-B:OUT, PE-SPD-03:PE |
| SPD-04 | DEHNpatch DPA M CLE RJ45B48 ClassE,929121 | A03; SITE; [63, 20, 2.5] | passive | IP-C08-B:IN, IP-C08-C:OUT, PE-SPD-04:PE |
| TS-I01 | SATEL S-4 NC z sabotażem | R104; T0; [8.5, 13, 1.5] | passive | INT-TAMPER-I:LINE |
| DC-G01 | SATEL S-4 NC z sabotażem | A03; SITE; [65, 10, 1] | passive | DPS-G01:LINE |

Gniazda DB-400 należą do zespołów F01-F11; każdy ma własne gniazdo, ujęte w nazwie i BOM. Uchwyt/okucie nie jest dodatkowym punktem elektrycznym.

## KD i niezależne wyjście

### D01 - A01 -> R102
KD-01, kanał 1; czytniki RD-D01-IN; zamek LK-D01; stan DC-D01; klamka RX-D01.
Normalnie: card. Brak LAN: local cached permissions and 250000 event capacity; lost-card revocation not guaranteed until local update. Brak energii: entry denied, mechanical free egress. Pożar: mechanical egress, no electrical release required. Tor wyjścia: inner lever -> mortise latch retracts -> leaf opens; no powered element in series.

### D02 - R101 -> R102
KD-02, kanał 1; czytniki RD-D02-IN; zamek LK-D02; stan DC-D02; klamka RX-D02.
Normalnie: card. Brak LAN: local cached permissions and 250000 event capacity; lost-card revocation not guaranteed until local update. Brak energii: entry denied, mechanical free egress. Pożar: mechanical egress, no electrical release required. Tor wyjścia: inner lever -> mortise latch retracts -> leaf opens; no powered element in series.

### D03 - R101 -> R103
KD-03, kanał 1; czytniki RD-D03-IN; zamek LK-D03; stan DC-D03; klamka RX-D03.
Normalnie: card+PIN at SOC/IT. Brak LAN: local cached permissions and 250000 event capacity; lost-card revocation not guaranteed until local update. Brak energii: entry denied, mechanical free egress. Pożar: mechanical egress, no electrical release required. Tor wyjścia: inner lever -> mortise latch retracts -> leaf opens; no powered element in series.

### D04 - R101 -> R104
KD-04, kanał 1; czytniki RD-D04-IN; zamek LK-D04; stan DC-D04; klamka RX-D04.
Normalnie: card+PIN at SOC/IT. Brak LAN: local cached permissions and 250000 event capacity; lost-card revocation not guaranteed until local update. Brak energii: entry denied, mechanical free egress. Pożar: mechanical egress, no electrical release required. Tor wyjścia: inner lever -> mortise latch retracts -> leaf opens; no powered element in series.

### G01 - A00 -> A03
KD-05, kanał 1; czytniki RD-G01-IN, RD-G01-OUT; zamek MECH-G01; stan DC-G01; klamka None.
Normalnie: card. Brak LAN: local cached permissions and 250000 event capacity; lost-card revocation not guaranteed until local update. Brak energii: patrol uses mechanical key; card verification by roster. Pożar: patrol opens manually for response; pedestrian egress bypasses gate. Tor wyjścia: separate open pedestrian gap 1.5m at SITE(48,30); path along west parking edge, no crossing of G01 lane.

## CCTV / geometria celów

| ID | Cel i punkt celu | Szerokość / px na m | Azymut / pochylenie / HFOV |
|---|---|---|---|
| C01 | front view; D01 and PATH1; T0 [20.0, 4.5, 1.69729583] | 3.675471781024923 / 522.3819184008532 | 270 / 8 / 40 |
| C02 | rear view; PATH1; T0 [20.0, 5.5, 1.33721719] | 4.600480040755603 / 417.3477513195886 | 90 / 12 / 48.455 |
| C03 | left side view; PATH1; T0 [20.0, 5.0, 1.45255359] | 3.607178458520355 / 532.2719743640224 | 0 / 14 / 49.455 |
| C04 | right side view; PATH1; T0 [20.0, 5.0, 1.45255359] | 3.607178458520355 / 532.2719743640224 | 180 / 14 / 49.455 |
| C05 | hall overview and door event verification D03/D04; no face-identification claim at all hall positions; T0 [6.548565084375258, 7.458078182085377, 1.2000501651096744] | 13.597012406177637 / 141.20749048722433 | 49 / 9.845 / 72 |
| C06 | public entrance E01, face view on approach; SITE [24, 20, 1.2] | 6.338139533204652 / 302.92801064750637 | 270.0 / 18.8 / 65.1 |
| C07 | parking overview; C07 pole, no full identification; SITE [60, 30, 1.2] | 18.19426281137351 / 105.52777102899596 | 270.0 / 8.383 / 50.692 |
| C08 | person crossing into vehicle-only lane; no number-plate recognition; SITE [65.24763956049547, 14.436896872599275, 0.20215405107000795] | 9.619811791059636 / 199.58810439351737 | 292 / 25 / 72 |

## Kadry 3D i dane geometryczne dla B

Model: rectilinear pinhole, square pixels, corrected image. barrel distortion correction ON; zero residual distortion in design calculation, 2% of full image dimension border reserve per side (normalised +/-0.96); not a measured lens calibration.
forward=(cos az cos tilt,sin az cos tilt,-sin tilt); image right=(sin az,-cos az,0); image up=(cos az sin tilt,sin az sin tilt,cos tilt); x=right dot(P-C)/(forward dot(P-C)*tan(HFOV/2)); y=up dot(P-C)/(forward dot(P-C)*tan(VFOV/2)); az from east CCW, tilt positive down. Near/far: horizontal radial distance from camera, metres, in addition to positive optical depth and rectangular 3D frustum.
Promienie narożne poniżej są wektorami w SITE od punktu kamery, bez normalizacji. Sektor: prostokątna piramida między tymi promieniami, dodatnia głębokość optyczna, obcięcie promieniem near/far i nieprzezroczystymi ścianami. Dla kontroli celu obowiązuje dodatkowo |x|,|y| <=0.96. Szerokość kadru w tabeli dotyczy płaszczyzny prostopadłej do osi przez cel, nie rzutu podłoża.

- C01: HFOV/VFOV 40.000000/23.140917 deg; near/far 1/10.5 m; promienie BL,BR,TR,TL: [[0.36397023, -0.96177471, -0.34191391], [-0.36397023, -0.96177471, -0.34191391], [-0.36397023, -1.01876143, 0.06356771], [0.36397023, -1.01876143, 0.06356771]].
- C02: HFOV/VFOV 48.455000/28.408960 deg; near/far 1/8 m; promienie BL,BR,TR,TL: [[-0.44999485, 0.92552056, -0.45550247], [0.44999485, 0.92552056, -0.45550247], [0.44999485, 1.03077465, 0.03967909], [-0.44999485, 1.03077465, 0.03967909]].
- C03: HFOV/VFOV 49.455000/29.046253 deg; near/far 1/6.8 m; promienie BL,BR,TR,TL: [[0.90762628, 0.46053024, -0.49327532], [0.90762628, -0.46053024, -0.49327532], [1.03296517, -0.46053024, 0.00943153], [1.03296517, 0.46053024, 0.00943153]].
- C04: HFOV/VFOV 49.455000/29.046253 deg; near/far 1/7.9 m; promienie BL,BR,TR,TL: [[-0.90762628, -0.46053024, -0.49327532], [-0.90762628, 0.46053024, -0.49327532], [-1.03296517, 0.46053024, 0.00943153], [-1.03296517, -0.46053024, 0.00943153]].
- C05: HFOV/VFOV 72.000000/44.457722 deg; near/far 1/13 m; promienie BL,BR,TR,TL: [[0.05222546, 1.16751321, -0.5736453], [1.14888268, 0.21420364, -0.5736453], [1.24057023, 0.31967811, 0.23167853], [0.14391302, 1.27298768, 0.23167853]].
- C06: HFOV/VFOV 65.100000/39.500591 deg; near/far 1/7.7 m; promienie BL,BR,TR,TL: [[0.63829779, -0.83094218, -0.66215302], [-0.63829779, -0.83094218, -0.66215302], [-0.63829779, -1.06235634, 0.01762163], [0.63829779, -1.06235634, 0.01762163]].
- C07: HFOV/VFOV 50.692000/29.839145 deg; near/far 1/22.0 m; promienie BL,BR,TR,TL: [[0.47368045, -0.95047071, -0.40938795], [-0.47368045, -0.95047071, -0.40938795], [-0.47368045, -1.02816055, 0.11780896], [0.47368045, -1.02816055, 0.11780896]].
- C08: HFOV/VFOV 72.000000/44.457722 deg; near/far 1/13 m; promienie BL,BR,TR,TL: [[0.94844693, -0.40800711, -0.79300828], [-0.39883007, -0.95234236, -0.79300828], [-0.26942919, -1.27262078, -0.05222824], [1.07784782, -0.72828554, -0.05222824]].

PATH1: [{"camera": "C01", "segment_local_m": [[20, 1], [20, 5.5]], "aspect": "front of northbound person", "height_range_m": [1.2, 2.0], "body_part": "upper torso, shoulders and head in absolute height band1.2..2.0m; feet/full body not required", "minimum_ppm": 250, "width_axis_site": [1, 0, 0]}, {"camera": "C02", "segment_local_m": [[20, 3.5], [20, 7]], "aspect": "rear of northbound person", "height_range_m": [1.2, 2.0], "body_part": "upper torso, shoulders and head in absolute height band1.2..2.0m; feet/full body not required", "minimum_ppm": 250, "width_axis_site": [1, 0, 0]}, {"camera": "C03", "segment_local_m": [[20, 4.2], [20, 5.8]], "aspect": "left profile / west to east", "height_range_m": [1.2, 2.0], "body_part": "upper torso, shoulders and head in absolute height band1.2..2.0m; feet/full body not required", "minimum_ppm": 250, "width_axis_site": [0, 1, 0]}, {"camera": "C04", "segment_local_m": [[20, 4.2], [20, 5.8]], "aspect": "right profile / east to west", "height_range_m": [1.2, 2.0], "body_part": "upper torso, shoulders and head in absolute height band1.2..2.0m; feet/full body not required", "minimum_ppm": 250, "width_axis_site": [0, 1, 0]}]

AI: punkt detekcji przy stopach z=0; obwiednia osoby {"half_size_xy_m": 0.3, "height_range_m": [0, 2]}.
ROI stóp SITE: [[63.3, 12.5], [66.7, 12.5], [66.7, 16.5], [63.3, 16.5]]; linia: [[63.3, 15.5], [66.7, 15.5]].
ROI w obrazie znormalizowanym (x w prawo, y w górę): [[0.454137, 0.085286], [-0.096843, 0.223355], [-0.53378, -0.341035], [0.329813, -0.73789]].

## Parking i manewr

{
  "stalls": [
    {
      "id": "P01",
      "rect_site_m": [
        50,
        20,
        3.6,
        5
      ],
      "accessible": true
    },
    {
      "id": "P02",
      "rect_site_m": [
        54,
        20,
        2.5,
        5
      ],
      "accessible": false
    },
    {
      "id": "P03",
      "rect_site_m": [
        58,
        20,
        2.5,
        5
      ],
      "accessible": false
    },
    {
      "id": "P06",
      "rect_site_m": [
        70,
        20,
        2.5,
        5
      ],
      "accessible": false
    },
    {
      "id": "P07",
      "rect_site_m": [
        50,
        38,
        2.5,
        5
      ],
      "accessible": false
    },
    {
      "id": "P08",
      "rect_site_m": [
        54,
        38,
        2.5,
        5
      ],
      "accessible": false
    },
    {
      "id": "P09",
      "rect_site_m": [
        58,
        38,
        2.5,
        5
      ],
      "accessible": false
    },
    {
      "id": "P10",
      "rect_site_m": [
        62,
        38,
        2.5,
        5
      ],
      "accessible": false
    },
    {
      "id": "P11",
      "rect_site_m": [
        66,
        38,
        2.5,
        5
      ],
      "accessible": false
    },
    {
      "id": "P12",
      "rect_site_m": [
        70,
        38,
        2.5,
        5
      ],
      "accessible": false
    }
  ],
  "aisle_polygon_site_m": [
    [
      48,
      25
    ],
    [
      74,
      25
    ],
    [
      74,
      38
    ],
    [
      48,
      38
    ]
  ],
  "pedestrian_route_site_m": [
    [
      49,
      43
    ],
    [
      49,
      30
    ],
    [
      48,
      30
    ],
    [
      46.5,
      30
    ],
    [
      46.5,
      23.5
    ],
    [
      40,
      23.5
    ],
    [
      40,
      25
    ]
  ],
  "pedestrian_clear_width_m": 1.5,
  "pedestrian_strip_rect_site_m": [
    48.25,
    20,
    1.5,
    30
  ],
  "open_pedestrian_gap": {
    "centre_site_m": [
      48,
      30
    ],
    "width_m": 1.5,
    "locked": false,
    "power_dependent": false
  },
  "existing_boundary": {
    "points_site_m": [
      [
        63,
        10
      ],
      [
        63,
        20
      ],
      [
        48,
        20
      ],
      [
        48,
        50
      ],
      [
        74,
        50
      ],
      [
        74,
        20
      ],
      [
        67,
        20
      ],
      [
        67,
        10
      ]
    ],
    "height_m": 1.8,
    "kind": "existing mesh fence, architectural boundary; G01 closes4m gap, west pedestrian gap1.5m remains open",
    "status": "assumed existing, not new installation BOM",
    "no_full_airport_perimeter_claim": true
  },
  "existing_pedestrian_bollards": {
    "points_site_m": [
      [
        49.9,
        25
      ],
      [
        49.9,
        27
      ],
      [
        49.9,
        29
      ],
      [
        49.9,
        31
      ],
      [
        49.9,
        33
      ],
      [
        49.9,
        35
      ],
      [
        49.9,
        37
      ]
    ],
    "status": "existing low-speed parking separation, no new powered mechanism"
  },
  "withdrawn_stall_ids": [
    "P04",
    "P05"
  ],
  "entry_corridor_rect_site_m": [
    63,
    0,
    4,
    28
  ],
  "design_vehicle": {
    "type": "assumed passenger car, low speed <=5km/h",
    "length_m": 4.5,
    "width_m": 1.8,
    "wheelbase_m": 2.7,
    "front_overhang_m": 0.9,
    "rear_overhang_m": 0.9,
    "minimum_rear_axle_turn_radius_m": 5.0,
    "maximum_steering_deg": 30
  },
  "sweep": {
    "rear_axle_path": [
      {
        "type": "line",
        "a": [
          65,
          5
        ],
        "b": [
          65,
          28
        ]
      },
      {
        "type": "arc",
        "centre": [
          59,
          28
        ],
        "radius_m": 6,
        "angles_deg": [
          0,
          90
        ]
      },
      {
        "type": "line",
        "a": [
          59,
          34
        ],
        "b": [
          55,
          34
        ]
      }
    ],
    "turn_radius_m": 6,
    "sample_step_m": 0.1,
    "clearance_m": 0.2,
    "inter_sample_motion_bound_m": 0.15,
    "free_rectangles_site_m": [
      [
        63,
        0,
        4,
        28
      ],
      [
        50,
        25,
        24,
        13
      ]
    ],
    "directions": [
      "ingress",
      "egress, opposite heading on reversed rear-axle path"
    ],
    "conditions": "G01 fully open and latched; all remaining stall rectangles treated as occupied solids; car keeps to specified rear axle path; 0.2m envelope margin exceeds calculated inter-sample corner motion; no claim for trucks or parking into each bay"
  },
  "chambers": [
    {
      "id": "JC01",
      "centre_site_m": [
        44.3,
        38
      ],
      "size_m": [
        0.4,
        0.4
      ],
      "traffic": "outside vehicle corridor"
    },
    {
      "id": "JC02",
      "centre_site_m": [
        44.3,
        27
      ],
      "size_m": [
        0.4,
        0.4
      ],
      "traffic": "outside vehicle corridor"
    },
    {
      "id": "JC03",
      "centre_site_m": [
        62,
        11
      ],
      "size_m": [
        0.4,
        0.4
      ],
      "traffic": "west of lane x63..67 and open gate swing, on unchanged R5, no vehicle loading"
    }
  ],
  "camera_support_rects_site_m": [
    [
      62.65,
      19.85,
      0.3,
      0.3
    ]
  ],
  "open_gate_leaf_rects_site_m": [
    [
      62.9,
      10,
      0.2,
      2
    ],
    [
      66.9,
      10,
      0.2,
      2
    ]
  ]
}

Wyniki kontroli kadru i manewru są także w obliczeniach na końcu rejestru.

## SSP: L1 w kolejności połączeń

CSP-0:L1A -> ROP-01 -> F01 -> SF-01 -> F03 -> ROP-02 -> F04 -> F02 -> SF-02 -> F05 -> SF-03 -> F06 -> ROP-03 -> F11 -> SF-08 -> F10 -> SF-07 -> F09 -> SF-06 -> F08 -> SF-05 -> F07 -> SF-04 -> CSP-0:L1B

| ID | Adres | Pomieszczenie | Współrzędne lokalne |
|---|---|---|---|
| ROP-01 | 1 | R101 | [4.8, 0.2, 1.4] |
| F01 | 2 | R101 | [4, 2.5, 3] |
| SF-01 | 3 | R101 | [4, 5, 2.7] |
| F03 | 4 | R101 | [4, 7.5, 3] |
| ROP-02 | 5 | R101 | [0.2, 6, 1.4] |
| F04 | 6 | R101 | [12, 7.5, 3] |
| F02 | 7 | R101 | [12, 2.5, 3] |
| SF-02 | 8 | R101 | [12, 5, 2.7] |
| F05 | 9 | R102 | [20, 2.5, 3] |
| SF-03 | 10 | R102 | [20, 5, 2.7] |
| F06 | 11 | R102 | [20, 7.5, 3] |
| ROP-03 | 12 | R102 | [23.8, 7, 1.4] |
| F11 | 13 | R107 | [22, 13, 3] |
| SF-08 | 14 | R107 | [22, 12, 2.7] |
| F10 | 15 | R106 | [18, 13, 3] |
| SF-07 | 16 | R106 | [18, 12, 2.7] |
| F09 | 17 | R105 | [13, 13, 3] |
| SF-06 | 18 | R105 | [13, 12, 2.7] |
| F08 | 19 | R104 | [8, 13, 3] |
| SF-05 | 20 | R104 | [8, 12, 2.7] |
| F07 | 21 | R103 | [3, 13, 3] |
| SF-04 | 22 | R103 | [3, 12, 2.7] |

## Macierz przyczyna-skutek

- **CE01** any detector F01-F11; warunek: single-stage alarm; no AI, confirmation or delay; wyjścia: L1:SF-01, L1:SF-02, L1:SF-03, L1:SF-08, L1:SF-07, L1:SF-06, L1:SF-05, L1:SF-04, CSP-0:OUT1; skutek: all eight sounders on, local CSP display, fire event to SSWiN; nadzór: loop poll, isolators per device; INFO-FIRE 2EOL; reset: CSP access level2 after inspection, cause removed, guard authorisation.
- **CE02** ROP-01..03; warunek: immediate manual alarm; wyjścia: L1:SF-01, L1:SF-02, L1:SF-03, L1:SF-08, L1:SF-07, L1:SF-06, L1:SF-05, L1:SF-04, CSP-0:OUT1; skutek: same full evacuation alarm; nadzór: loop poll and broken/short loop trouble; reset: physical ROP key, then CSP level2 after safety check.
- **CE03** loop open/short/missing point or power/battery failure; warunek: fault as detected by CSP; no fire alarm from fault alone; wyjścia: CSP-0:OUT8; skutek: local fault, supervised event to Z12; nadzór: OUT8 energised healthy and 2EOL line; reset: repair, normal supervision restored, local acknowledgement.
- **CE04** LAN/VMS/AI unavailable; warunek: any duration; wyjścia: brak sterowania elektrycznego; skutek: CSP continues locally; SOC reads actual panel; no effect on egress; nadzór: IT diagnostics independent from fire controls; reset: IT repair after proof that local SSP unaffected.
- **CE05** fire while doors in KD locked; warunek: any power/LAN state; wyjścia: brak sterowania elektrycznego; skutek: inner levers mechanically retract latch on D01-D04; E01-E03 panic hardware; no electromagnetic locks; nadzór: daily physical inspection; no electrical unlock chain claimed; reset: guard inspection of door operation before re-securing.

## Przepusty przez przegrody

| ID | Ściana | Punkt SITE | Kable |
|---|---|---|---|
| PR-01 | W1 | [24.0, 25.0, 2.7] | IP-C06 |
| PR-02 | W1 | [39.2, 25.0, 2.7] | BUS-RD-D01-IN, DC-RD-D01-IN |
| PR-03 | W10 | [40.0, 38.0, 2.0] | PE-SPD-01, PE-SPD-02, PE-G01 |
| PR-04 | W10 | [40.0, 38.0, 2.7] | IP-C07-A, BUS-RD-G01-IN, DC-RD-G01-IN, DPS-G01 |
| PR-05 | W10 | [40.0, 40.0, 2.7] | AL-I06 |
| PR-06 | W10 | [40.0, 40.0, 2.9] | FL1-15 |
| PR-07 | W2 | [44.0, 27.0, -0.7] | IP-C08-B, PE-SPD-04 |
| PR-08 | W2 | [44.0, 38.0, -0.7] | IP-C07-B, PE-SPD-02 |
| PR-09 | W2 | [44.0, 38.0, 2.0] | PE-G01 |
| PR-10 | W2 | [44.0, 38.0, 2.7] | BUS-RD-G01-IN, DC-RD-G01-IN, DPS-G01 |
| PR-11 | W5 | [21.0, 35.0, 2.9] | FL1-01 |
| PR-12 | W5 | [23.0, 35.0, 2.7] | BUS-RD-D03-IN, DC-RD-D03-IN |
| PR-13 | W5 | [28.0, 35.0, 2.7] | IP-C01, IP-C02, IP-C03, IP-C04, IP-C05, IP-C06, IP-KD-01, IP-KD-02, BUS-RD-D04-IN, IP-C08-A, DC-RD-D04-IN |
| PR-14 | W5 | [28.5, 35.0, 2.7] | AL-I01, AL-I02, AL-I03, AL-IC-E01, AL-IC-E02, AL-IC-E03, AL-IC-D01, AL-SIREN, AL-SIREN-T |
| PR-15 | W5 | [29.0, 35.0, 2.0] | PE-SPD-03, PE-SPD-04 |
| PR-16 | W5 | [43.8, 35.0, 2.9] | FL1-13 |
| PR-17 | W6 | [36.0, 27.0, 2.0] | PE-SPD-03, PE-SPD-04 |
| PR-18 | W6 | [36.0, 27.0, 2.7] | IP-C08-A |
| PR-19 | W6 | [36.0, 34.0, 2.7] | IP-C01, IP-C02, IP-C03, IP-C04, IP-KD-01, IP-KD-02, BUS-RD-D02-IN, AL-I03, AL-IC-E03, AL-IC-D01, DC-RD-D02-IN |
| PR-20 | W6 | [36.0, 34.0, 2.9] | FL1-09 |
| PR-21 | W7 | [26.0, 40.0, 2.7] | IP-KD-03, IP-SOC-0, BUS-KP, AL-PANIC, INFO-FIRE, INFO-FAULT, AC-SOC-0, AC-MON-01, AC-MON-02, AC-SSP, UPS-USB |
| PR-22 | W7 | [26.0, 40.0, 2.9] | FL1-21 |
| PR-23 | W8 | [30.0, 38.0, 2.0] | PE-SPD-01, PE-SPD-02, PE-G01 |
| PR-24 | W8 | [30.0, 38.0, 2.7] | IP-C07-A, BUS-RD-G01-IN, DC-RD-G01-IN, DPS-G01 |
| PR-25 | W8 | [30.0, 40.0, 2.7] | AL-I05, AL-I06 |
| PR-26 | W8 | [30.0, 40.0, 2.9] | FL1-19 |
| PR-27 | W9 | [36.0, 38.0, 2.0] | PE-SPD-01, PE-SPD-02, PE-G01 |
| PR-28 | W9 | [36.0, 38.0, 2.7] | IP-C07-A, BUS-RD-G01-IN, DC-RD-G01-IN, DPS-G01 |
| PR-29 | W9 | [36.0, 40.0, 2.7] | AL-I06 |
| PR-30 | W9 | [36.0, 40.0, 2.9] | FL1-17 |

## Kable - kompletny przebieg w układzie SITE

Zakup = ceil((rzut + pion + zapas montażowy) * (1 + odpad)). Fabryczne połączenia i patchcordy wskazane w osprzęcie nie zwiększają przedmiaru kabla instalacyjnego. Dane OSDP (RS485) i zasilanie czytników (DC-READER) są osobnymi przewodami i osobnymi połączeniami, bez podwójnego zaliczenia jednego kabla.

| ID | Końce | Typ; trasa | Rzut / pion / zapas / zakup [m] | Punkty (x,y,z) SITE |
|---|---|---|---|---|
| IP-C01 | SW-0:P01 -> C01:ETH | CAT-I; R1/R2 | 18.66333 / 1.3 / 2 / 25 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 34, 2.7] -> [40, 34, 2.7] -> [40, 34.5, 2.7] -> [40, 34.5, 2.4] |
| IP-C02 | SW-0:P02 -> C02:ETH | CAT-I; R1/R2 | 26.66333 / 1.3 / 2 / 33 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 34, 2.7] -> [40, 34, 2.7] -> [40, 25.5, 2.7] -> [40, 25.5, 2.4] |
| IP-C03 | SW-0:P03 -> C03:ETH | CAT-I; R1/R2 | 18.36333 / 1.3 / 2 / 24 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 34, 2.7] -> [36.2, 34, 2.7] -> [36.2, 30, 2.7] -> [36.2, 30, 2.4] |
| IP-C04 | SW-0:P04 -> C04:ETH | CAT-I; R1/R2 | 25.96333 / 1.3 / 2 / 33 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 34, 2.7] -> [43.8, 34, 2.7] -> [43.8, 30, 2.7] -> [43.8, 30, 2.4] |
| IP-C05 | SW-0:P05 -> C05:ETH | CAT-I; R1/R2 | 22.16333 / 1.1 / 2 / 28 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 34, 2.7] -> [20.5, 34, 2.7] -> [20.5, 25.5, 2.7] -> [20.5, 25.5, 2.8] |
| IP-C06 | SW-0:P06 -> C06:ETH | CAT-I; R1/R2 | 19.46333 / 1.1 / 2 / 25 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 34, 2.7] -> [24, 34, 2.7] -> [24, 24.7, 2.7] -> [24, 24.7, 2.8] |
| IP-KD-01 | SW-0:P09 -> KD-01:ETH | CAT-I; R1/R2 | 26.76333 / 1.3 / 2 / 34 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 34, 2.7] -> [40, 34, 2.7] -> [40, 25.4, 2.7] -> [40, 25.4, 2.4] |
| IP-KD-02 | SW-0:P10 -> KD-02:ETH | CAT-I; R1/R2 | 18.46333 / 1.3 / 2 / 24 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 34, 2.7] -> [36.3, 34, 2.7] -> [36.3, 30, 2.7] -> [36.3, 30, 2.4] |
| IP-KD-03 | SW-0:P11 -> KD-03:ETH | CAT-I; R1/R2 | 13.86333 / 1.3 / 2 / 19 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 40, 2.7] -> [23, 40, 2.7] -> [23, 35.3, 2.7] -> [23, 35.3, 2.4] |
| IP-KD-04 | SW-0:P12 -> KD-04:ETH | CAT-I; R1/R2 | 8.86333 / 1.3 / 2 / 14 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 40, 2.7] -> [28, 35.3, 2.7] -> [28, 35.3, 2.4] |
| IP-NAS-0 | SW-0:P14 -> NAS-0:ETH | CAT-I; R1/R2 | 4.32666 / 2.5 / 2 / 10 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 38, 1.2] -> [26.8, 39.8, 1.2] |
| IP-SOC-0 | SW-0:P15 -> SOC-0:ETH | CAT-I; R1/R2 | 11.16333 / 2.9 / 2 / 18 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 40, 2.7] -> [23, 40, 2.7] -> [23, 38, 2.7] -> [23, 38, 0.8] |
| IP-FW-0 | SW-0:P16 -> FW-0:ETH | CAT-I; R1/R2 | 4.32666 / 1.9 / 2 / 10 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 38, 1.8] -> [26.8, 39.8, 1.8] |
| IP-IP-I01 | SW-0:P17 -> IP-I01:ETH | CAT-I; R1/R2 | 6.66333 / 2.2 / 2 / 12 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 40, 2.7] -> [28.5, 40, 2.7] -> [28.5, 38, 2.7] -> [28.5, 38, 1.5] |
| BUS-RD-D01-IN | KD-01:READER -> RD-D01-IN:BUS | RS485; local door conduit | 18.6 / 1.9 / 0.5 / 24 | [40, 25.4, 2.4] -> [40, 25.4, 2.7] -> [40, 34, 2.7] -> [39.2, 34, 2.7] -> [39.2, 24.8, 2.7] -> [39.2, 24.8, 1.1] |
| PWR-D01 | KD-01:LOCK -> LK-D01:DC | DC-KD; local door conduit | 0.4 / 2.0 / 0.5 / 4 | [40, 25.4, 2.4] -> [40, 25.4, 2.7] -> [40, 25.4, 1] -> [40, 25, 1] |
| DPS-D01 | KD-01:DPS -> DC-D01:LINE | SIGNAL; local door conduit | 0.4 / 0.95 / 0.5 / 3 | [40, 25.4, 2.4] -> [40, 25.4, 2.7] -> [40, 25.4, 2.05] -> [40, 25, 2.05] |
| REX-D01 | KD-01:REX -> RX-D01:LINE | SIGNAL; local door conduit | 0.4 / 2.0 / 0.5 / 4 | [40, 25.4, 2.4] -> [40, 25.4, 2.7] -> [40, 25.4, 1] -> [40, 25, 1] |
| BUS-RD-D02-IN | KD-02:READER -> RD-D02-IN:BUS | RS485; local door conduit | 9.2 / 1.9 / 0.5 / 13 | [36.3, 30, 2.4] -> [36.3, 30, 2.7] -> [36.3, 34, 2.7] -> [35.8, 34, 2.7] -> [35.8, 29.3, 2.7] -> [35.8, 29.3, 1.1] |
| PWR-D02 | KD-02:LOCK -> LK-D02:DC | DC-KD; local door conduit | 0.3 / 2.0 / 0.5 / 4 | [36.3, 30, 2.4] -> [36.3, 30, 2.7] -> [36.3, 30, 1] -> [36, 30, 1] |
| DPS-D02 | KD-02:DPS -> DC-D02:LINE | SIGNAL; local door conduit | 0.3 / 0.95 / 0.5 / 2 | [36.3, 30, 2.4] -> [36.3, 30, 2.7] -> [36.3, 30, 2.05] -> [36, 30, 2.05] |
| REX-D02 | KD-02:REX -> RX-D02:LINE | SIGNAL; local door conduit | 0.3 / 2.0 / 0.5 / 4 | [36.3, 30, 2.4] -> [36.3, 30, 2.7] -> [36.3, 30, 1] -> [36, 30, 1] |
| BUS-RD-D03-IN | KD-03:READER -> RD-D03-IN:BUS | RS485; local door conduit | 2.8 / 1.9 / 0.5 / 6 | [23, 35.3, 2.4] -> [23, 35.3, 2.7] -> [23, 34, 2.7] -> [22.3, 34, 2.7] -> [22.3, 34.8, 2.7] -> [22.3, 34.8, 1.1] |
| PWR-D03 | KD-03:LOCK -> LK-D03:DC | DC-KD; local door conduit | 0.3 / 2.0 / 0.5 / 4 | [23, 35.3, 2.4] -> [23, 35.3, 2.7] -> [23, 35.3, 1] -> [23, 35, 1] |
| DPS-D03 | KD-03:DPS -> DC-D03:LINE | SIGNAL; local door conduit | 0.3 / 0.95 / 0.5 / 2 | [23, 35.3, 2.4] -> [23, 35.3, 2.7] -> [23, 35.3, 2.05] -> [23, 35, 2.05] |
| REX-D03 | KD-03:REX -> RX-D03:LINE | SIGNAL; local door conduit | 0.3 / 2.0 / 0.5 / 4 | [23, 35.3, 2.4] -> [23, 35.3, 2.7] -> [23, 35.3, 1] -> [23, 35, 1] |
| BUS-RD-D04-IN | KD-04:READER -> RD-D04-IN:BUS | RS485; local door conduit | 2.8 / 1.9 / 0.5 / 6 | [28, 35.3, 2.4] -> [28, 35.3, 2.7] -> [28, 34, 2.7] -> [27.3, 34, 2.7] -> [27.3, 34.8, 2.7] -> [27.3, 34.8, 1.1] |
| PWR-D04 | KD-04:LOCK -> LK-D04:DC | DC-KD; local door conduit | 0.3 / 2.0 / 0.5 / 4 | [28, 35.3, 2.4] -> [28, 35.3, 2.7] -> [28, 35.3, 1] -> [28, 35, 1] |
| DPS-D04 | KD-04:DPS -> DC-D04:LINE | SIGNAL; local door conduit | 0.3 / 0.95 / 0.5 / 2 | [28, 35.3, 2.4] -> [28, 35.3, 2.7] -> [28, 35.3, 2.05] -> [28, 35, 2.05] |
| REX-D04 | KD-04:REX -> RX-D04:LINE | SIGNAL; local door conduit | 0.3 / 2.0 / 0.5 / 4 | [28, 35.3, 2.4] -> [28, 35.3, 2.7] -> [28, 35.3, 1] -> [28, 35, 1] |
| AL-I01 | SSWiN-0:Z1 -> I01:LINE | ALARM; R1/R2 | 12.9 / 1.5 / 1 / 17 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 34, 2.7] -> [20.3, 34, 2.7] -> [20.3, 34.7, 2.7] -> [20.3, 34.7, 2.4] |
| AL-I02 | SSWiN-0:Z2 -> I02:LINE | ALARM; R1/R2 | 19.9 / 1.5 / 1 / 25 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 34, 2.7] -> [35.7, 34, 2.7] -> [35.7, 25.3, 2.7] -> [35.7, 25.3, 2.4] |
| AL-I03 | SSWiN-0:Z3 -> I03:LINE | ALARM; R1/R2 | 27.9 / 1.5 / 1 / 34 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 34, 2.7] -> [43.7, 34, 2.7] -> [43.7, 25.3, 2.7] -> [43.7, 25.3, 2.4] |
| AL-I04 | SSWiN-0:Z4 -> I04:LINE | ALARM; R1/R2 | 8.3 / 1.5 / 1 / 12 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 40, 2.7] -> [26.3, 40, 2.7] -> [26.3, 40.7, 2.7] -> [26.3, 40.7, 2.4] -> [29.7, 40.7, 2.4] |
| AL-I05 | SSWiN-0:Z5 -> I05:LINE | ALARM; R1/R2 | 4.5 / 1.5 / 1 / 8 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 40, 2.7] -> [30.3, 40, 2.7] -> [30.3, 40.7, 2.7] -> [30.3, 40.7, 2.4] |
| AL-I06 | SSWiN-0:Z6 -> I06:LINE | ALARM; R1/R2 | 14.5 / 1.5 / 1 / 19 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 40, 2.7] -> [40.3, 40, 2.7] -> [40.3, 40.7, 2.7] -> [40.3, 40.7, 2.4] |
| AL-IC-E01 | SSWiN-0:Z7 -> IC-E01:LINE | SIGNAL; R1 | 17.5 / 1.85 / 1 / 23 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 34, 2.7] -> [24, 34, 2.7] -> [24, 25, 2.7] -> [24, 25, 2.05] |
| AL-IC-E02 | SSWiN-0:Z8 -> IC-E02:LINE | SIGNAL; R1 | 14.5 / 1.85 / 1 / 20 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 34, 2.7] -> [20, 34, 2.7] -> [20, 32, 2.7] -> [20, 32, 2.05] |
| AL-IC-E03 | SSWiN-0:Z9 -> IC-E03:LINE | SIGNAL; R1 | 20.5 / 1.85 / 1 / 26 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 34, 2.7] -> [44, 34, 2.7] -> [44, 33, 2.7] -> [44, 33, 2.05] |
| AL-IC-D01 | SSWiN-0:Z10 -> IC-D01:LINE | SIGNAL; R1 | 24.5 / 1.85 / 1 / 31 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 34, 2.7] -> [40, 34, 2.7] -> [40, 25, 2.7] -> [40, 25, 2.05] |
| BUS-KP | SSWiN-0:BUS -> KP-I01:BUS | BUS-I; R2 | 12.3 / 2.5 / 1 / 18 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 40, 2.7] -> [22.2, 40, 2.7] -> [22.2, 36, 2.7] -> [22.2, 36, 1.4] |
| BUS-ETHM | SSWiN-0:BUS -> IP-I01:BUS | BUS-I; internal cabinet | 0 / 0 / 0.3 / 1 | [28.5, 38, 1.5] |
| AL-SIREN | SSWiN-0:OUT1 -> SI-I01:DC | ALARM; R1 | 5.8 / 1.2 / 1 / 9 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 34, 2.7] -> [27.5, 34, 2.7] -> [27.5, 34.8, 2.7] |
| AL-SIREN-T | SSWiN-0:Z13 -> SI-I01:TAMPER | SIGNAL; R1 | 5.8 / 1.2 / 1 / 9 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 34, 2.7] -> [27.5, 34, 2.7] -> [27.5, 34.8, 2.7] |
| AL-PANIC | SSWiN-0:Z15 -> PA-I01:LINE | SIGNAL; R2 | 9.5 / 3.2 / 1 / 16 | [28.5, 38, 1.5] -> [28.5, 38, 2.7] -> [28.5, 40, 2.7] -> [23, 40, 2.7] -> [23, 38, 2.7] -> [23, 38, 0.7] |
| INFO-FIRE | CSP-0:OUT1 -> SSWiN-0:Z11 | SIGNAL; R2 | 13.5 / 2.4 / 1 / 19 | [21, 36, 1.5] -> [21, 36, 2.7] -> [21, 40, 2.7] -> [28.5, 40, 2.7] -> [28.5, 38, 2.7] -> [28.5, 38, 1.5] |
| INFO-FAULT | CSP-0:OUT8 -> SSWiN-0:Z12 | SIGNAL; R2 | 13.5 / 2.4 / 1 / 19 | [21, 36, 1.5] -> [21, 36, 2.7] -> [21, 40, 2.7] -> [28.5, 40, 2.7] -> [28.5, 38, 2.7] -> [28.5, 38, 1.5] |
| FL1-01 | CSP-0:L1A -> ROP-01:IN | FIRE; R3 and room leads | 14.6 / 2.9 / 0.4 / 20 | [21, 36, 1.5] -> [21, 36, 2.9] -> [21, 34, 2.9] -> [24.8, 34, 2.9] -> [24.8, 25.2, 2.9] -> [24.8, 25.2, 1.4] |
| FL1-02 | ROP-01:OUT -> F01:IN | FIRE; R3 and room leads | 16.1 / 1.6 / 0.4 / 20 | [24.8, 25.2, 1.4] -> [24.8, 25.2, 2.9] -> [24.8, 34, 2.9] -> [24, 34, 2.9] -> [24, 27.5, 2.9] -> [24, 27.5, 3] |
| FL1-03 | F01:OUT -> SF-01:IN | FIRE; R3 and room leads | 10.5 / 0.3 / 0.4 / 13 | [24, 27.5, 3] -> [24, 27.5, 2.9] -> [24, 34, 2.9] -> [24, 30, 2.9] -> [24, 30, 2.7] |
| FL1-04 | SF-01:OUT -> F03:IN | FIRE; R3 and room leads | 5.5 / 0.3 / 0.4 / 7 | [24, 30, 2.7] -> [24, 30, 2.9] -> [24, 34, 2.9] -> [24, 32.5, 2.9] -> [24, 32.5, 3] |
| FL1-05 | F03:OUT -> ROP-02:IN | FIRE; R3 and room leads | 8.3 / 1.6 / 0.4 / 12 | [24, 32.5, 3] -> [24, 32.5, 2.9] -> [24, 34, 2.9] -> [20.2, 34, 2.9] -> [20.2, 31, 2.9] -> [20.2, 31, 1.4] |
| FL1-06 | ROP-02:OUT -> F04:IN | FIRE; R3 and room leads | 16.3 / 1.6 / 0.4 / 21 | [20.2, 31, 1.4] -> [20.2, 31, 2.9] -> [20.2, 34, 2.9] -> [32, 34, 2.9] -> [32, 32.5, 2.9] -> [32, 32.5, 3] |
| FL1-07 | F04:OUT -> F02:IN | FIRE; R3 and room leads | 8.0 / 0.2 / 0.4 / 10 | [32, 32.5, 3] -> [32, 32.5, 2.9] -> [32, 34, 2.9] -> [32, 27.5, 2.9] -> [32, 27.5, 3] |
| FL1-08 | F02:OUT -> SF-02:IN | FIRE; R3 and room leads | 10.5 / 0.3 / 0.4 / 13 | [32, 27.5, 3] -> [32, 27.5, 2.9] -> [32, 34, 2.9] -> [32, 30, 2.9] -> [32, 30, 2.7] |
| FL1-09 | SF-02:OUT -> F05:IN | FIRE; R3 and room leads | 18.5 / 0.3 / 0.4 / 22 | [32, 30, 2.7] -> [32, 30, 2.9] -> [32, 34, 2.9] -> [40, 34, 2.9] -> [40, 27.5, 2.9] -> [40, 27.5, 3] |
| FL1-10 | F05:OUT -> SF-03:IN | FIRE; R3 and room leads | 10.5 / 0.3 / 0.4 / 13 | [40, 27.5, 3] -> [40, 27.5, 2.9] -> [40, 34, 2.9] -> [40, 30, 2.9] -> [40, 30, 2.7] |
| FL1-11 | SF-03:OUT -> F06:IN | FIRE; R3 and room leads | 5.5 / 0.3 / 0.4 / 7 | [40, 30, 2.7] -> [40, 30, 2.9] -> [40, 34, 2.9] -> [40, 32.5, 2.9] -> [40, 32.5, 3] |
| FL1-12 | F06:OUT -> ROP-03:IN | FIRE; R3 and room leads | 7.3 / 1.6 / 0.4 / 11 | [40, 32.5, 3] -> [40, 32.5, 2.9] -> [40, 34, 2.9] -> [43.8, 34, 2.9] -> [43.8, 32, 2.9] -> [43.8, 32, 1.4] |
| FL1-13 | ROP-03:OUT -> F11:IN | FIRE; R3 and room leads | 11.8 / 1.6 / 0.4 / 16 | [43.8, 32, 1.4] -> [43.8, 32, 2.9] -> [43.8, 40, 2.9] -> [42, 40, 2.9] -> [42, 38, 2.9] -> [42, 38, 3] |
| FL1-14 | F11:OUT -> SF-08:IN | FIRE; R3 and room leads | 5.0 / 0.3 / 0.4 / 7 | [42, 38, 3] -> [42, 38, 2.9] -> [42, 40, 2.9] -> [42, 37, 2.9] -> [42, 37, 2.7] |
| FL1-15 | SF-08:OUT -> F10:IN | FIRE; R3 and room leads | 9.0 / 0.3 / 0.4 / 11 | [42, 37, 2.7] -> [42, 37, 2.9] -> [42, 40, 2.9] -> [38, 40, 2.9] -> [38, 38, 2.9] -> [38, 38, 3] |
| FL1-16 | F10:OUT -> SF-07:IN | FIRE; R3 and room leads | 5.0 / 0.3 / 0.4 / 7 | [38, 38, 3] -> [38, 38, 2.9] -> [38, 40, 2.9] -> [38, 37, 2.9] -> [38, 37, 2.7] |
| FL1-17 | SF-07:OUT -> F09:IN | FIRE; R3 and room leads | 10.0 / 0.3 / 0.4 / 12 | [38, 37, 2.7] -> [38, 37, 2.9] -> [38, 40, 2.9] -> [33, 40, 2.9] -> [33, 38, 2.9] -> [33, 38, 3] |
| FL1-18 | F09:OUT -> SF-06:IN | FIRE; R3 and room leads | 5.0 / 0.3 / 0.4 / 7 | [33, 38, 3] -> [33, 38, 2.9] -> [33, 40, 2.9] -> [33, 37, 2.9] -> [33, 37, 2.7] |
| FL1-19 | SF-06:OUT -> F08:IN | FIRE; R3 and room leads | 10.0 / 0.3 / 0.4 / 12 | [33, 37, 2.7] -> [33, 37, 2.9] -> [33, 40, 2.9] -> [28, 40, 2.9] -> [28, 38, 2.9] -> [28, 38, 3] |
| FL1-20 | F08:OUT -> SF-05:IN | FIRE; R3 and room leads | 5.0 / 0.3 / 0.4 / 7 | [28, 38, 3] -> [28, 38, 2.9] -> [28, 40, 2.9] -> [28, 37, 2.9] -> [28, 37, 2.7] |
| FL1-21 | SF-05:OUT -> F07:IN | FIRE; R3 and room leads | 10.0 / 0.3 / 0.4 / 12 | [28, 37, 2.7] -> [28, 37, 2.9] -> [28, 40, 2.9] -> [23, 40, 2.9] -> [23, 38, 2.9] -> [23, 38, 3] |
| FL1-22 | F07:OUT -> SF-04:IN | FIRE; R3 and room leads | 5.0 / 0.3 / 0.4 / 7 | [23, 38, 3] -> [23, 38, 2.9] -> [23, 40, 2.9] -> [23, 37, 2.9] -> [23, 37, 2.7] |
| FL1-23 | SF-04:OUT -> CSP-0:L1B | FIRE; R4 | 10.2 / 1.6 / 0.4 / 14 | [23, 37, 2.7] -> [23, 37, 2.9] -> [23, 40.6, 2.9] -> [21, 40.6, 2.9] -> [21, 36, 2.9] -> [21, 36, 1.5] |
| INT-BAT-F01 | CSP-0:BAT -> BAT-F01:DC | FACTORY; factory battery leads | 0.0 / 0.3 / 0 / 1 (fabryczne / osprzęt) | [21, 36, 1.5] -> [21, 36, 1.2] |
| INT-BAT-I01 | SSWiN-0:BAT -> BAT-I01:DC | FACTORY; factory battery leads | 0.0 / 0.3 / 0 / 1 (fabryczne / osprzęt) | [28.5, 38, 1.5] -> [28.5, 38, 1.2] |
| INT-EBM1 | UPS-0:EBM1 -> EBM-01:IN | FACTORY; rack | 4.32666 / 4.95 / 0 / 10 (fabryczne / osprzęt) | [26.8, 39.8, 0.3] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 38, 0.15] -> [26.8, 39.8, 0.15] |
| INT-EBM2 | EBM-01:OUT -> EBM-02:IN | FACTORY; rack | 4.32666 / 5.1 / 0 / 10 (fabryczne / osprzęt) | [26.8, 39.8, 0.15] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 38, 0.15] -> [26.8, 39.8, 0.15] |
| INT-HDD1 | NAS-0:HDD1 -> HDD-01:SATA | FACTORY; NAS backplane | 0 / 0 / 0 / 0 (fabryczne / osprzęt) | [26.8, 39.8, 1.2] |
| INT-HDD2 | NAS-0:HDD2 -> HDD-02:SATA | FACTORY; NAS backplane | 0 / 0 / 0 / 0 (fabryczne / osprzęt) | [26.8, 39.8, 1.2] |
| INT-HDD3 | NAS-0:HDD3 -> HDD-03:SATA | FACTORY; NAS backplane | 0 / 0 / 0 / 0 (fabryczne / osprzęt) | [26.8, 39.8, 1.2] |
| INT-HDD4 | NAS-0:HDD4 -> HDD-04:SATA | FACTORY; NAS backplane | 0 / 0 / 0 / 0 (fabryczne / osprzęt) | [26.8, 39.8, 1.2] |
| INT-SD-C01 | C01:SD -> SD-C01:CARD | FACTORY; camera card slot | 0 / 0 / 0 / 0 (fabryczne / osprzęt) | [40, 34.5, 2.4] |
| INT-SD-C02 | C02:SD -> SD-C02:CARD | FACTORY; camera card slot | 0 / 0 / 0 / 0 (fabryczne / osprzęt) | [40, 25.5, 2.4] |
| INT-SD-C03 | C03:SD -> SD-C03:CARD | FACTORY; camera card slot | 0 / 0 / 0 / 0 (fabryczne / osprzęt) | [36.2, 30, 2.4] |
| INT-SD-C04 | C04:SD -> SD-C04:CARD | FACTORY; camera card slot | 0 / 0 / 0 / 0 (fabryczne / osprzęt) | [43.8, 30, 2.4] |
| INT-SD-C05 | C05:SD -> SD-C05:CARD | FACTORY; camera card slot | 0 / 0 / 0 / 0 (fabryczne / osprzęt) | [20.5, 25.5, 2.8] |
| INT-SD-C06 | C06:SD -> SD-C06:CARD | FACTORY; camera card slot | 0 / 0 / 0 / 0 (fabryczne / osprzęt) | [24, 24.7, 2.8] |
| INT-SD-C07 | C07:SD -> SD-C07:CARD | FACTORY; camera card slot | 0 / 0 / 0 / 0 (fabryczne / osprzęt) | [60, 49, 4] |
| INT-SD-C08 | C08:SD -> SD-C08:CARD | FACTORY; camera card slot | 0 / 0 / 0 / 0 (fabryczne / osprzęt) | [63, 20, 3] |
| AC-SW-0 | UPS-0:OUT1 -> SW-0:AC | AC; R1/R2 power tray | 4.32666 / 3.4 / 0.5 / 10 | [26.8, 39.8, 0.3] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 38, 1.7] -> [26.8, 39.8, 1.7] |
| AC-NAS-0 | UPS-0:OUT2 -> NAS-0:AC | AC; R1/R2 power tray | 4.32666 / 3.9 / 0.5 / 10 | [26.8, 39.8, 0.3] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 38, 1.2] -> [26.8, 39.8, 1.2] |
| AC-SOC-0 | UPS-0:OUT3 -> SOC-0:AC | AC; R1/R2 power tray | 11.16333 / 4.3 / 0.5 / 18 | [26.8, 39.8, 0.3] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 40, 2.7] -> [23, 40, 2.7] -> [23, 38, 2.7] -> [23, 38, 0.8] |
| AC-MON-01 | UPS-0:OUT4 -> MON-01:AC | AC; R1/R2 power tray | 11.16333 / 4.0 / 0.5 / 18 | [26.8, 39.8, 0.3] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 40, 2.7] -> [23, 40, 2.7] -> [23, 38, 2.7] -> [23, 38, 1.1] |
| AC-MON-02 | UPS-0:OUT5 -> MON-02:AC | AC; R1/R2 power tray | 10.16333 / 4.0 / 0.5 / 17 | [26.8, 39.8, 0.3] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 40, 2.7] -> [24, 40, 2.7] -> [24, 38, 2.7] -> [24, 38, 1.1] |
| AC-FW-0 | UPS-0:OUT6 -> FW-0:AC | AC; R1/R2 power tray | 4.32666 / 3.3 / 0.5 / 9 | [26.8, 39.8, 0.3] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 38, 1.8] -> [26.8, 39.8, 1.8] |
| AC-UPS | RSEC:Q1 -> UPS-0:AC | AC-UPS; R104 power tray | 8.16333 / 3.6 / 0.5 / 14 | [29, 37, 1.5] -> [29, 37, 2.7] -> [29, 40, 2.7] -> [28, 40, 2.7] -> [28, 38, 2.7] -> [28, 38, 0.3] -> [26.8, 39.8, 0.3] |
| AC-SSWIN | RSEC:Q2 -> SSWiN-0:AC | AC; R104 power tray | 5.5 / 2.4 / 0.5 / 10 | [29, 37, 1.5] -> [29, 37, 2.7] -> [29, 40, 2.7] -> [28.5, 40, 2.7] -> [28.5, 38, 2.7] -> [28.5, 38, 1.5] |
| AC-SSP | RSEC:Q0 -> CSP-0:AC | AC-F; R2 dedicated fire supports, before PWP | 15.0 / 2.4 / 0.5 / 20 | [29, 37, 1.5] -> [29, 37, 2.7] -> [29, 40, 2.7] -> [21, 40, 2.7] -> [21, 36, 2.7] -> [21, 36, 1.5] |
| DP-1 | SOC-0:DP1 -> MON-01:VIDEO | DP; SOC desk | 0.0 / 0.3 / 1 / 2 | [23, 38, 0.8] -> [23, 38, 1.1] |
| DP-2 | SOC-0:DP2 -> MON-02:VIDEO | DP; SOC desk | 1.0 / 0.3 / 1 / 3 | [23, 38, 0.8] -> [23, 38, 1.1] -> [24, 38, 1.1] |
| UPS-USB | UPS-0:USB -> SOC-0:USB | USB; R2 | 11.16333 / 4.3 / 1 / 17 | [26.8, 39.8, 0.3] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 40, 2.7] -> [23, 40, 2.7] -> [23, 38, 2.7] -> [23, 38, 0.8] |
| PWP-RPO | RSEC:PWP-NC -> UPS-0:RPO | SIGNAL; R104 protected PWP control route | 8.16333 / 3.6 / 0.5 / 14 | [29, 37, 1.5] -> [29, 37, 2.7] -> [29, 40, 2.7] -> [28, 40, 2.7] -> [28, 38, 2.7] -> [28, 38, 0.3] -> [26.8, 39.8, 0.3] |
| IP-C07-A | SW-0:P07 -> SPD-01:IN | CAT-I; R1/R5 | 17.96333 / 1.7 / 2 / 24 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [43.8, 38, 2.7] -> [43.8, 38, 2] |
| IP-C07-B | SPD-01:OUT -> SPD-02:IN | CAT-O; R1/R5 | 27.2 / 6.9 / 2 / 40 | [43.8, 38, 2] -> [43.8, 38, -0.7] -> [44.3, 38, -0.7] -> [44.3, 49, -0.7] -> [60, 49, -0.7] -> [60, 49, 3.5] |
| IP-C07-C | SPD-02:OUT -> C07:ETH | PATCH; R1/R5 | 0.0 / 0.5 / 1 / 2 (fabryczne / osprzęt) | [60, 49, 3.5] -> [60, 49, 4] |
| PE-SPD-01 | RSEC:PE -> SPD-01:PE | PE; bonding path | 15.8 / 0.5 / 0.5 / 19 | [29, 37, 1.5] -> [29, 37, 2] -> [29, 38, 2] -> [43.8, 38, 2] |
| PE-SPD-02 | RSEC:PE -> SPD-02:PE | PE; bonding plus R6 | 43.0 / 7.4 / 0.5 / 56 | [29, 37, 1.5] -> [29, 37, 2] -> [29, 38, 2] -> [43.8, 38, 2] -> [43.8, 38, -0.7] -> [44.3, 38, -0.7] -> [44.3, 49, -0.7] -> [60, 49, -0.7] -> [60, 49, 3.5] |
| IP-C08-A | SW-0:P08 -> SPD-03:IN | CAT-I; R1/R5 | 28.96333 / 1.3 / 2 / 36 | [26.8, 39.8, 1.7] -> [26.8, 39.8, 2.7] -> [28, 38, 2.7] -> [28, 27, 2.7] -> [43.8, 27, 2.7] -> [43.8, 27, 2.4] |
| IP-C08-B | SPD-03:OUT -> SPD-04:IN | CAT-O; R7/R5/R8 | 44.2 / 6.3 / 2 / 58 | [43.8, 27, 2.4] -> [43.8, 27, -0.7] -> [44.3, 27, -0.7] -> [44.3, 11, -0.7] -> [63, 11, -0.7] -> [63, 20, -0.7] -> [63, 20, 2.5] |
| IP-C08-C | SPD-04:OUT -> C08:ETH | PATCH; R1/R5 | 0.0 / 0.5 / 1 / 2 (fabryczne / osprzęt) | [63, 20, 2.5] -> [63, 20, 3] |
| PE-SPD-03 | RSEC:PE -> SPD-03:PE | PE; bonding path | 24.8 / 0.9 / 0.5 / 29 | [29, 37, 1.5] -> [29, 37, 2] -> [29, 27, 2] -> [43.8, 27, 2] -> [43.8, 27, 2.4] |
| PE-SPD-04 | RSEC:PE -> SPD-04:PE | PE; R7/R5/R8 | 69.0 / 7.2 / 0.5 / 85 | [29, 37, 1.5] -> [29, 37, 2] -> [29, 27, 2] -> [43.8, 27, 2] -> [43.8, 27, 2.4] -> [43.8, 27, -0.7] -> [44.3, 27, -0.7] -> [44.3, 11, -0.7] -> [63, 11, -0.7] -> [63, 20, -0.7] -> [63, 20, 2.5] |
| IP-KD-05 | SW-0:P13 -> KD-05:ETH | PATCH; R1/R5 | 4.32666 / 0.2 / 1 / 7 (fabryczne / osprzęt) | [26.8, 39.8, 1.7] -> [26.8, 39.8, 1.5] -> [28, 38, 1.5] -> [26.8, 39.8, 1.5] |
| BUS-RD-G01-IN | KD-05:READER -> RD-G01-IN:BUS | RS485-O; R2/R5 | 67.50832 / 6.4 / 2 / 84 | [26.8, 39.8, 1.5] -> [26.8, 39.8, 2.7] -> [28.4, 38, 2.7] -> [43.8, 38, 2.7] -> [44.3, 38, 2.7] -> [44.3, 38, -0.7] -> [44.3, 11, -0.7] -> [64.5, 11, -0.7] -> [64.5, 9, -0.7] -> [64.5, 9, 1.1] |
| BUS-RD-G01-OUT | RD-G01-IN:BUS -> RD-G01-OUT:BUS | RS485; gate post conduit | 2.0 / 0.0 / 0.5 / 3 | [64.5, 9, 1.1] -> [64.5, 11, 1.1] |
| DC-RD-D01-IN | KD-01:READER-12V -> RD-D01-IN:DC | DC-READER; local door conduit | 18.6 / 1.9 / 0.5 / 24 | [40, 25.4, 2.4] -> [40, 25.4, 2.7] -> [40, 34, 2.7] -> [39.2, 34, 2.7] -> [39.2, 24.8, 2.7] -> [39.2, 24.8, 1.1] |
| DC-RD-D02-IN | KD-02:READER-12V -> RD-D02-IN:DC | DC-READER; local door conduit | 9.2 / 1.9 / 0.5 / 13 | [36.3, 30, 2.4] -> [36.3, 30, 2.7] -> [36.3, 34, 2.7] -> [35.8, 34, 2.7] -> [35.8, 29.3, 2.7] -> [35.8, 29.3, 1.1] |
| DC-RD-D03-IN | KD-03:READER-12V -> RD-D03-IN:DC | DC-READER; local door conduit | 2.8 / 1.9 / 0.5 / 6 | [23, 35.3, 2.4] -> [23, 35.3, 2.7] -> [23, 34, 2.7] -> [22.3, 34, 2.7] -> [22.3, 34.8, 2.7] -> [22.3, 34.8, 1.1] |
| DC-RD-D04-IN | KD-04:READER-12V -> RD-D04-IN:DC | DC-READER; local door conduit | 2.8 / 1.9 / 0.5 / 6 | [28, 35.3, 2.4] -> [28, 35.3, 2.7] -> [28, 34, 2.7] -> [27.3, 34, 2.7] -> [27.3, 34.8, 2.7] -> [27.3, 34.8, 1.1] |
| DC-RD-G01-IN | KD-05:READER-12V -> RD-G01-IN:DC | DC-READER-O; R2/R5 | 67.50832 / 6.4 / 2 / 84 | [26.8, 39.8, 1.5] -> [26.8, 39.8, 2.7] -> [28.4, 38, 2.7] -> [43.8, 38, 2.7] -> [44.3, 38, 2.7] -> [44.3, 38, -0.7] -> [44.3, 11, -0.7] -> [64.5, 11, -0.7] -> [64.5, 9, -0.7] -> [64.5, 9, 1.1] |
| DC-RD-G01-OUT | RD-G01-IN:DC -> RD-G01-OUT:DC | DC-READER; gate post conduit | 2.0 / 0.0 / 0.5 / 3 | [64.5, 9, 1.1] -> [64.5, 11, 1.1] |
| PE-G01 | RSEC:PE -> MECH-G01:PE | PE; R5 | 65.0 / 4.9 / 1 / 78 | [29, 37, 1.5] -> [29, 37, 2] -> [29, 38, 2] -> [44.3, 38, 2] -> [44.3, 38, -0.7] -> [44.3, 11, -0.7] -> [65, 11, -0.7] -> [65, 10, -0.7] -> [65, 10, 1] |
| INT-TAMPER-I | SSWiN-0:Z14 -> TS-I01:LINE | SIGNAL; inside SSWin cabinet | 0 / 0 / 0.3 / 1 | [28.5, 38, 1.5] |
| DPS-G01 | KD-05:DPS -> DC-G01:LINE | SIGNAL; R2/R5 | 68.62635 / 6.3 / 2 / 85 | [26.8, 39.8, 1.5] -> [26.8, 39.8, 2.7] -> [28.4, 38, 2.7] -> [43.8, 38, 2.7] -> [44.3, 38, 2.7] -> [44.3, 38, -0.7] -> [44.3, 11, -0.7] -> [64.5, 11, -0.7] -> [64.5, 9, -0.7] -> [64.5, 9, 1] -> [65, 10, 1] |

## Wyniki obliczeń

```json
{
  "optical": {
    "kd": [
      {
        "id": "D01",
        "camera": "C01",
        "minimum_ppm": 250,
        "visible": true,
        "max_abs_x": 0.17419939164839898,
        "max_abs_y": 0.47797073301530774,
        "min_ppm": 275.4779198689988,
        "min_radius_m": 9.5,
        "max_radius_m": 9.518928511129811,
        "samples": 6
      },
      {
        "id": "D02",
        "camera": "C04",
        "minimum_ppm": 250,
        "visible": true,
        "max_abs_x": 0.1699717174774282,
        "max_abs_y": 0.7548620215798925,
        "min_ppm": 265.25719880096625,
        "min_radius_m": 7.799999999999997,
        "max_radius_m": 7.823042886243176,
        "samples": 6
      },
      {
        "id": "D03",
        "camera": "C05",
        "minimum_ppm": 80,
        "visible": true,
        "max_abs_x": 0.7653690630534241,
        "max_abs_y": 0.20726411084641733,
        "min_ppm": 146.94273644640356,
        "min_radius_m": 9.7082439194738,
        "max_radius_m": 9.962429422585638,
        "samples": 6
      },
      {
        "id": "D04",
        "camera": "C05",
        "minimum_ppm": 80,
        "visible": true,
        "max_abs_x": 0.11146458037300215,
        "max_abs_y": 0.2640476066422455,
        "min_ppm": 80.80376191709567,
        "min_radius_m": 11.800423721205947,
        "max_radius_m": 12.419742348374221,
        "samples": 6
      },
      {
        "id": "G01",
        "camera": "C08",
        "minimum_ppm": 100,
        "visible": true,
        "max_abs_x": 0.5842011053328537,
        "max_abs_y": 0.875895688806359,
        "min_ppm": 116.59687871992243,
        "min_radius_m": 10.0,
        "max_radius_m": 10.770329614269007,
        "samples": 6
      }
    ],
    "path": [
      {
        "camera": "C01",
        "minimum_ppm": 250,
        "visible": true,
        "max_abs_x": 0.6647728420779973,
        "max_abs_y": 0.8585399211097531,
        "min_ppm": 296.97887769140607,
        "min_radius_m": 3.712142238654116,
        "max_radius_m": 8.845903006477068,
        "samples": 736
      },
      {
        "camera": "C02",
        "minimum_ppm": 250,
        "visible": true,
        "max_abs_x": 0.7341788055374832,
        "max_abs_y": 0.8370362899606093,
        "min_ppm": 309.14206097741663,
        "min_radius_m": 2.716615541441224,
        "max_radius_m": 6.859300255857005,
        "samples": 576
      },
      {
        "camera": "C03",
        "minimum_ppm": 250,
        "visible": true,
        "max_abs_x": 0.8206312881712496,
        "max_abs_y": 0.6207698154672902,
        "min_ppm": 429.7431902460261,
        "min_radius_m": 2.8999999999999915,
        "max_radius_m": 4.827007354458871,
        "samples": 272
      },
      {
        "camera": "C04",
        "minimum_ppm": 250,
        "visible": true,
        "max_abs_x": 0.82063128817125,
        "max_abs_y": 0.6207698154672902,
        "min_ppm": 429.7431902460261,
        "min_radius_m": 2.8999999999999915,
        "max_radius_m": 4.827007354458871,
        "samples": 272
      }
    ],
    "ai_roi": {
      "visible": true,
      "max_abs_x": 0.7729250212570143,
      "max_abs_y": 0.9059606578577736,
      "min_ppm": 143.93004813736314,
      "min_radius_m": 3.1999999999999993,
      "max_radius_m": 8.765842800324451,
      "samples": 2040,
      "min_person_height_px": 212.25986069853866
    },
    "ai_line": {
      "visible": true,
      "max_abs_x": 0.5553902207853889,
      "max_abs_y": 0.6766499543387285,
      "min_ppm": 198.41535191541146,
      "min_radius_m": 4.199999999999999,
      "max_radius_m": 6.248199740725324,
      "samples": 288
    }
  },
  "parking": {
    "clashes": [],
    "poses_per_direction": 368,
    "steering_deg": 24.22774531795417
  },
  "count": {
    "camera": 8,
    "sd_card": 8,
    "access_controller": 5,
    "reader": 6,
    "strike": 4,
    "contact": 10,
    "exit_contact": 4,
    "mechanical": 1,
    "switch": 1,
    "storage": 1,
    "disk": 4,
    "workstation": 1,
    "monitor": 2,
    "firewall": 1,
    "ups": 1,
    "ups_battery": 2,
    "distribution": 1,
    "fire_panel": 1,
    "battery": 2,
    "intrusion_panel": 1,
    "intrusion_ip": 1,
    "keypad": 1,
    "intrusion_siren": 1,
    "panic": 1,
    "intrusion_detector": 6,
    "fire_detector": 11,
    "fire_callpoint": 3,
    "fire_sounder": 8,
    "ethernet_spd": 4
  },
  "cables": {
    "CAT-I": {
      "plan_m": 272.63995377501107,
      "vertical_m": 25.100000000000005,
      "installed_m": 329.73995377501103,
      "purchase_m": 369,
      "connections": 16
    },
    "RS485": {
      "plan_m": 35.399999999999984,
      "vertical_m": 7.600000000000001,
      "installed_m": 45.49999999999999,
      "purchase_m": 52,
      "connections": 5
    },
    "DC-KD": {
      "plan_m": 1.29999999999999,
      "vertical_m": 8.000000000000002,
      "installed_m": 11.299999999999992,
      "purchase_m": 16,
      "connections": 4
    },
    "SIGNAL": {
      "plan_m": 198.68968366978675,
      "vertical_m": 38.30000000000001,
      "installed_m": 251.78968366978674,
      "purchase_m": 288,
      "connections": 19
    },
    "ALARM": {
      "plan_m": 93.8,
      "vertical_m": 10.200000000000003,
      "installed_m": 111.0,
      "purchase_m": 124,
      "connections": 7
    },
    "BUS-I": {
      "plan_m": 12.3,
      "vertical_m": 2.5000000000000004,
      "installed_m": 16.1,
      "purchase_m": 19,
      "connections": 2
    },
    "FIRE": {
      "plan_m": 217.59999999999997,
      "vertical_m": 17.20000000000001,
      "installed_m": 243.9999999999999,
      "purchase_m": 281,
      "connections": 23
    },
    "AC": {
      "plan_m": 50.96997688750552,
      "vertical_m": 25.300000000000004,
      "installed_m": 79.76997688750552,
      "purchase_m": 92,
      "connections": 7
    },
    "AC-UPS": {
      "plan_m": 8.16333076527839,
      "vertical_m": 3.6000000000000005,
      "installed_m": 12.26333076527839,
      "purchase_m": 14,
      "connections": 1
    },
    "AC-F": {
      "plan_m": 15.0,
      "vertical_m": 2.4000000000000004,
      "installed_m": 17.9,
      "purchase_m": 20,
      "connections": 1
    },
    "DP": {
      "plan_m": 1.0,
      "vertical_m": 0.6000000000000001,
      "installed_m": 3.5999999999999996,
      "purchase_m": 5,
      "connections": 2
    },
    "USB": {
      "plan_m": 11.16333076527839,
      "vertical_m": 4.300000000000001,
      "installed_m": 16.463330765278393,
      "purchase_m": 17,
      "connections": 1
    },
    "CAT-O": {
      "plan_m": 71.4,
      "vertical_m": 13.2,
      "installed_m": 88.6,
      "purchase_m": 98,
      "connections": 2
    },
    "PE": {
      "plan_m": 217.6,
      "vertical_m": 20.9,
      "installed_m": 241.49999999999997,
      "purchase_m": 267,
      "connections": 5
    },
    "RS485-O": {
      "plan_m": 67.50831891575845,
      "vertical_m": 6.4,
      "installed_m": 75.90831891575846,
      "purchase_m": 84,
      "connections": 1
    },
    "DC-READER": {
      "plan_m": 35.399999999999984,
      "vertical_m": 7.600000000000001,
      "installed_m": 45.49999999999999,
      "purchase_m": 52,
      "connections": 5
    },
    "DC-READER-O": {
      "plan_m": 67.50831891575845,
      "vertical_m": 6.4,
      "installed_m": 75.90831891575846,
      "purchase_m": 84,
      "connections": 1
    }
  },
  "cable_purchase_m": 1882,
  "cable_installed_m": 1666.8429136943769,
  "link_lengths": {
    "NET-C01": 21.963330765278393,
    "NET-C02": 29.963330765278393,
    "NET-C03": 21.663330765278396,
    "NET-C04": 29.26333076527839,
    "NET-C05": 25.263330765278393,
    "NET-C06": 22.563330765278394,
    "NET-KD-01": 30.063330765278394,
    "NET-KD-02": 21.76333076527839,
    "NET-KD-03": 17.163330765278396,
    "NET-KD-04": 12.163330765278394,
    "NET-NAS-0": 8.826661530556782,
    "NET-SOC-0": 16.06333076527839,
    "NET-FW-0": 8.226661530556783,
    "NET-IP-I01": 10.863330765278391,
    "NET-C07": 59.26333076527839,
    "NET-C08": 86.2633307652784,
    "NET-KD-05": 5.526661530556781
  },
  "max_copper_channel_m": 91.2633307652784,
  "voltage_checks": [
    {
      "connection": "PWR-D01",
      "resistance_ohm": 0.17399999999999993,
      "source_v": 12,
      "drop_v": 0.048719999999999986,
      "voltage_v": 11.95128,
      "required_v": 10
    },
    {
      "connection": "PWR-D02",
      "resistance_ohm": 0.16799999999999984,
      "source_v": 12,
      "drop_v": 0.047039999999999964,
      "voltage_v": 11.952960000000001,
      "required_v": 10
    },
    {
      "connection": "PWR-D03",
      "resistance_ohm": 0.16799999999999984,
      "source_v": 12,
      "drop_v": 0.047039999999999964,
      "voltage_v": 11.952960000000001,
      "required_v": 10
    },
    {
      "connection": "PWR-D04",
      "resistance_ohm": 0.16799999999999984,
      "source_v": 12,
      "drop_v": 0.047039999999999964,
      "voltage_v": 11.952960000000001,
      "required_v": 10
    },
    {
      "connection": "AL-I01",
      "resistance_ohm": 1.3860000000000001,
      "source_v": 10.5,
      "drop_v": 0.03465000000000001,
      "voltage_v": 10.46535,
      "required_v": 10.2
    },
    {
      "connection": "AL-I02",
      "resistance_ohm": 2.016,
      "source_v": 10.5,
      "drop_v": 0.0504,
      "voltage_v": 10.4496,
      "required_v": 10.2
    },
    {
      "connection": "AL-I03",
      "resistance_ohm": 2.736,
      "source_v": 10.5,
      "drop_v": 0.0684,
      "voltage_v": 10.4316,
      "required_v": 10.2
    },
    {
      "connection": "AL-I04",
      "resistance_ohm": 0.972,
      "source_v": 10.5,
      "drop_v": 0.024300000000000002,
      "voltage_v": 10.4757,
      "required_v": 10.2
    },
    {
      "connection": "AL-I05",
      "resistance_ohm": 0.6300000000000003,
      "source_v": 10.5,
      "drop_v": 0.01575000000000001,
      "voltage_v": 10.48425,
      "required_v": 10.2
    },
    {
      "connection": "AL-I06",
      "resistance_ohm": 1.53,
      "source_v": 10.5,
      "drop_v": 0.038250000000000006,
      "voltage_v": 10.46175,
      "required_v": 10.2
    },
    {
      "connection": "BUS-KP",
      "resistance_ohm": 1.422,
      "source_v": 10.5,
      "drop_v": 0.08532,
      "voltage_v": 10.41468,
      "required_v": 10.2
    },
    {
      "connection": "AL-SIREN",
      "resistance_ohm": 0.7199999999999998,
      "source_v": 10.5,
      "drop_v": 0.08639999999999996,
      "voltage_v": 10.4136,
      "required_v": 9.6
    },
    {
      "connection": "DC-RD-D01-IN",
      "resistance_ohm": 1.26,
      "source_v": 12,
      "drop_v": 0.315,
      "voltage_v": 11.685,
      "required_v": 11.4
    },
    {
      "connection": "DC-RD-D02-IN",
      "resistance_ohm": 0.6960000000000001,
      "source_v": 12,
      "drop_v": 0.17400000000000002,
      "voltage_v": 11.826,
      "required_v": 11.4
    },
    {
      "connection": "DC-RD-D03-IN",
      "resistance_ohm": 0.3119999999999996,
      "source_v": 12,
      "drop_v": 0.0779999999999999,
      "voltage_v": 11.922,
      "required_v": 11.4
    },
    {
      "connection": "DC-RD-D04-IN",
      "resistance_ohm": 0.3119999999999996,
      "source_v": 12,
      "drop_v": 0.0779999999999999,
      "voltage_v": 11.922,
      "required_v": 11.4
    },
    {
      "connection": "DC-RD-G01-IN",
      "resistance_ohm": 0.5693123918681884,
      "source_v": 12,
      "drop_v": 0.3346561959340942,
      "voltage_v": 11.665343804065905,
      "required_v": 11.4
    },
    {
      "connection": "DC-RD-G01-OUT",
      "resistance_ohm": 0.15,
      "source_v": 11.665343804065905,
      "drop_v": 0.0875,
      "voltage_v": 11.577843804065905,
      "required_v": 11.4
    }
  ],
  "poe_pd_w": 213.1,
  "poe_pse_w": 273.2,
  "poe_with_margin_w": 341.5,
  "ups_load_w": 861.1,
  "ups_design_w": 1076.375,
  "ups_curve_point": [
    1100,
    67.0
  ],
  "ups_derated_minutes": 45.56,
  "storage_raw_tb": 3.6288,
  "storage_required_tb": 4.536,
  "storage_available_tb": 14.4,
  "sd_hours": 37.92592592592593,
  "loop_standby_a": 0.00801,
  "loop_alarm_a": 0.04105,
  "loop_length_m": 244.0,
  "loop_resistance_ohm": 13.980170201192088,
  "loop_far_voltage_v": 19.826114013241064,
  "banks": [
    {
      "id": "BANK-F",
      "standby_a": 0.2428857142857143,
      "alarm_a": 0.4372857142857143,
      "required_ah": 7.559875,
      "selected_ah": 17,
      "charge_a": 0.8,
      "recharge_h": 20.4
    },
    {
      "id": "BANK-I",
      "standby_a": 0.32500000000000007,
      "alarm_a": 0.5800000000000001,
      "required_ah": 9.931250000000002,
      "selected_ah": 17,
      "charge_a": 0.35,
      "recharge_h": 46.62857142857143
    }
  ],
  "fire_supply_with_charge_a": 1.1684166666666667,
  "intrusion_supply_with_charge_a": 0.93,
  "network_mbps": 192.5,
  "fire_standby_battery_a": 0.2428857142857143,
  "fire_alarm_battery_a": 0.4372857142857143,
  "recording_mbps": 48,
  "nas_mbps": 96,
  "ac_boundary_va": 1604.9722222222222
}
```

## Źródła parametrów

- **OWN** Założenia własne, geometria i cele odbiorowe; revision A-2026-10-24-R1: assumed geometry, corrected pinhole optics and low-speed vehicle sweep; no field measurements; local:data/design.json; dostęp 2026-10-24.
- **L-FIRE** MSWiA, tekst jednolity rozporządzenia ppoż. Dz.U.2023 poz.822; §3, §28 ust1 pkt19, §29 ust1 pkt8, §31; full list of triggers reviewed for the low 384m2 model; https://eli.gov.pl/api/acts/DU/2023/822/text.html; dostęp 2026-10-22.
- **L-2024** MSWiA, zmiana Dz.U.2024 poz.1716; §1: fire separation signs, autonomous smoke/CO detection; no change of thresholds in §28/29; https://api.sejm.gov.pl/eli/acts/DU/2024/1716/text.html; dostęp 2026-10-22.
- **L-2026** MSWiA, zmiana Dz.U.2026 poz.1276; §1 and §3, effective30.09.2026: shelter marking; no change in §28/29; https://api.sejm.gov.pl/eli/acts/DU/2026/1276/text.pdf; dostęp 2026-10-22.
- **L-ACT** Ustawa o ochronie przeciwpożarowej, Dz.U.2025 poz.188 ze zm.2026 poz.815; art5: transmission for objects with mandatory SSP; change2026/815 reviewed separately; https://api.sejm.gov.pl/eli/acts/DU/2025/188/text.pdf; dostęp 2026-10-22.
- **L-KP** Kodeks pracy, tekst jednolity Dz.U.2026 poz.1245; art22(1)b and22(2); replaces 2025/277 referenced in class notes; https://api.sejm.gov.pl/eli/acts/DU/2026/1245/text.pdf; dostęp 2026-10-22.
- **L-GDPR** RODO, rozporządzenie UE2016/679; art5,6,9,13,32,35; biometric special category only for unique identification; https://eur-lex.europa.eu/eli/reg/2016/679/oj; dostęp 2026-10-22.
- **S-CAM** AXIS P3265-LVE datasheet T10170893/EN/M19.2/2404; pp2-4:1920x1080,9mm lens36-100deg,10.7Wmax,ARTPEC8; reference model supported catalogue, not claimed current sale; pp2:9mm HFOV36..100/VFOV20..53, 1920x1080, barrel distortion correction; chosen paired fields are own corrected pinhole design, not factory lens calibration; https://www.axis.com/dam/public/ac/8e/70/datasheet-axis-p3265-lve-dome-camera-en-US-437931.pdf; dostęp 2026-10-24.
- **S-KD** AXIS A1210 datasheet T10182727/EN/M17.2/202511; p2:PoEclass4, one door, two OSDP readers, reader500mA, lock900mA@12V, peripheral1400mA; local250000events; https://www.axis.com/dam/public/69/69/1e/datasheet-axis-a1210-network-door-controller-en-US-509586.pdf; dostęp 2026-10-22.
- **S-READER** HID Signo Readers Models20/40/20K/40K/40T, datasheet; p2:12VDC,peak250mA,Signo40K supportsSeos,OSDP SecureChannel; published19.10.2026; radio authentication in reader is distinct from OSDP transport; https://www.hidglobal.com/sites/default/files/documentlibrary/pacs-signo-reader-family-ds-en_4.pdf; dostęp 2026-10-22.
- **S-LOCK** ASSA ABLOY effeff118 catalogue; 118.13 A71, technical table:10-24V,280mA@12V; ordinary non-fire-rated door, separate mechanical mortise exit; https://dach.assaabloy.com/de/de/downloadportal/download/655-tueroeffner-modell-118; dostęp 2026-10-22.
- **S-FIRE** SATEL ACSP-402, karta produktu i parametry techniczne; technical data:2x128,200mA/loop,100ohm,12V17Ah battery,220/320mA,charger1.4A, Imax1.6A; installer05/23 section10; newer PL03/26 installer access restricted, not claimed fully read; https://www.satel.pl/en/products/fire-alarm-systems/acsp-system/control-panel/acsp-402/; dostęp 2026-10-22.
- **S-DMP** SATEL DMP-400 / DCP-400, karta produktu; table:500/700microA,18-26V,A1R,DB400,isolator; DCP current conservatively bounded by DMP; https://demo.satel.pl/pl/leaflet/1129%2CDMP-400; dostęp 2026-10-22.
- **S-ROP** SATEL ROP-400/PL karta; technical data:170/450microA,18-26V,isolator; https://demo.satel.pl/pl/product/10385/ROP-400/PL%2CAdresowalny-reczny-ostrzegacz-pozarowy; dostęp 2026-10-22.
- **S-SND** SATEL SPP-400 karta; technical data:250microA/4mA,18-26V,isolator; sound coverage requires actual measurement; https://demo.satel.pl/pl/product/10387/SPP-400%2CAdresowalny-sygnalizator-akustyczny-pozarowy; dostęp 2026-10-22.
- **S-SSWIN** SATEL VERSA15 / S-4 / PNK1 / B17, rodzina systemu; technical data:15inputs,2partitions,135/160mA,2A PSU,350mA charging,40VA transformer; NC dry contacts S4/PNK1; https://przemek.satel.pl/pl/product/391/versa%2015; dostęp 2026-10-22.
- **S-PIR** SATEL SLIM-PIR karta; standby10mA, maximum25mA; 2EOL2x1.1kohm,12V+-15%,2.4m mounting; conservative15m sector used; https://www.satel.pl/produkty/sswin/czujki-przewodowe/czujki-ruchu-pir/slim-pir/; dostęp 2026-10-22.
- **S-LCD** SATEL VERSA-LCDM karta; 12V+-15%,50/60mA; wired keypad, not WRL; https://profesjonalni.satel.pl/en/product/572/VERSA-LCDM-WH%2CLCD-keypad-for-VERSA-panels; dostęp 2026-10-22.
- **S-ETHM** SATEL ETHM1 Plus karta947; 70/80mA; VERSA compatible; local IP, no contracted remote monitoring; https://demo.satel.pl/pl/leaflet/947%2CETHM-1%20PLUS; dostęp 2026-10-22.
- **S-SIREN** SATEL SPW100 instrukcja04/07; p2:12V+-20%,max120mA,tamper; intrusion only, not fire sounder; https://www.satel.eu/en/download/instrukcje/spw100_pl.pdf; dostęp 2026-10-22.
- **S-SW** TP-Link SG3428MP UN6.30 datasheet20251224; p3:24PoE+,384WPD,30W/port,478.6WworstAC incl fullPD; 463.7W@220V; https://static.tp-link.com/upload/product-overview/2025/202512/20251224/SG3428MP%28UN%296.30_datasheet.pdf; dostęp 2026-10-22.
- **S-NAS** Synology DS923+ datasheet / HAT3300 compatibility; hardware:4bays,RAID6,1GbE,100Wadapter; power ceiling125W assumes >=80% adapter efficiency; 4x8TB compatible SATA drives; https://global.synologydownload.com/download/Document/Hardware/DataSheet/DiskStation/23-year/DS923%2B/enu/Synology_DS923%2B_Data_Sheet_enu.pdf; dostęp 2026-10-22.
- **S-PC** Dell OptiPlex Micro7020 Owner manual, Power adapter; table:90W19.5V adapter option; AC design112.5W assumes >=80%efficiency; https://www.dell.com/support/manuals/en-th/optiplex-7020-micro/optiplex-micro-7020-owners-manual/power-adapter?guid=guid-f26b1c4b-c8be-4a81-9936-781588327ef5&lang=en-us; dostęp 2026-10-22.
- **S-MON** Dell P2425H User guide, electrical specifications; maximum65W each including USB loads; on-mode11.7W is not used in the maximum-power envelope; https://www.dell.com/en-us/shop/dell-pro-24-plus-monitor-p2425h/apd/210-bmgh/monitors-monitor-accessories; dostęp 2026-10-22.
- **S-FW** TP-Link ER605 v2.20 datasheet20251204; max7.94W device; design15WAC envelope incl adapter; https://static.tp-link.com/upload/product-overview/2025/202512/20251204/ER605%28UN%29%20v2.20%20DataSheet.pdf; dostęp 2026-10-22.
- **S-UPS** Eaton5PX1500IRT2UG2 battery-runtime curve + advanced user guide; embedded JavaScript ebm2 load/runtime array, 2x5PXEBM48RT2UG2; manufacturer+-15%; point1100W, additional own age factor0.8; RPO safety in user guide section5; https://eg.eaton.com/ups-battery-runtime/en-gb/5PX1500IRT2UG2; dostęp 2026-10-22.
- **S-AOA** AXIS Object Analytics Technical Documentation; About/Considerations/Line crossing/Object classifications; edge person detection, no inference-Hz guarantee; September2026 Considerations: human detection point at feet, recommended human height8% of image, visible legs, object present>=2s, WDR/BDC recommended; https://help.axis.com/en-us/axis-object-analytics; dostęp 2026-10-24.
- **S-VMS** AXIS Camera Station Pro / Secure Entry; CoreDevice5y02991-001 per8camera+5controller, compatible A1210; local Windows host, SMB network storage; https://www.axis.com/en-us/products/axis-camera-station-pro; dostęp 2026-10-22.
- **S-SPD** DEHNpatch ClassE DPA M CLE RJ45B48,929121; ClassE250MHz,PoE++/4PPoE,1A,57Vpair-pair; end-to-end1Gb/s, no claim of full ClassEA channel through SPD; https://www.dehn.co.uk/en-GB/store/f/295359/dehnpatch-arrester-for-data-networks-and-ethernet-applications; dostęp 2026-10-22.
- **S-CARD** HID Seos5006, official Honeywell product integration specification; AES128/2TDEA, mutual authentication and session keys; select AES/SIO with Signo, disable CSN; no claim that ordinary DESFire support proves AES application reading; https://buildings.honeywell.com/us/en/products/by-category/access-control/credentials/cards/iclass-seos-8k-card; dostęp 2026-10-22.
- **S-FIRE-USER** SATEL ACSP402 UserManual06/23 firmware1.00; pp9-13 point/output addresses FP/OUT1..8; access-level2 alarm reset and local supervision; not installer/programming manual; https://www.satel.pl/api/download/manuals/11253; dostęp 2026-10-22.
- **L-ACT-2026** Ustawa Dz.U.2026 poz.815; art5 modifies art14fa(3) of fire act, not the art5 obligation for mandatory SSP transmission; https://api.sejm.gov.pl/eli/acts/DU/2026/815/text.pdf; dostęp 2026-10-22.
- **S-UPS-GUIDE** Eaton5PX Advanced User Guide,614-40094-00; section6.6,pp25-27:RPO open, dedicated latching SELV contact, AC must also be disconnected; input function not enabled by default; section10:1500W,48V EBM; https://www.eaton.com/content/dam/eaton/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/eaton-5px-g2-ups/eaton-5px-g2-ups-emea/eaton-5px-g2-ups-emea-resources/eaton-5pxgen2-advanceduserguide-guide-en-gb.pdf; dostęp 2026-10-22.
- **S-KD-WIRING** AXIS A1210 Technical Documentation; Supervised inputs: Serial first connection, equal1kohm/2.2kohm/4.7kohm/10kohm; chosen1kohm at5DPS contacts; https://help.axis.com/en-us/axis-a1210; dostęp 2026-10-24.
- **S-AOA2** AXIS Object Analytics, scenariusze i ustawienia; Scenarios: Time in area (time limit per object in include area), Line crossing with Change trigger direction, Tailgating detection, PPE monitoring BETA (humans without hard hats); note: time in area over 30 s not recommended as recording trigger; https://help.axis.com/en-us/axis-object-analytics; dostęp 2026-11-22.
- **S-SS2** AXIS Camera Station Pro, Smart search 2; Smart search 2: search in recordings by object class, clothing colour and visual similarity; non-biometric; no live cross-camera tracking; https://help.axis.com/en-us/axis-camera-station-pro; dostęp 2026-11-22.
- **S-PD** AXIS Perimeter Defender, dokumentacja; perimeter intrusion, zone crossing and loitering scenarios; calibration and detection distance per camera model; https://help.axis.com/en-US/axis-perimeter-defender; dostęp 2026-11-22.
- **S-PDPTZ** AXIS Perimeter Defender PTZ Autotracking; fixed camera alarm steers one paired PTZ to follow the object; pairing and placement constraints in product documentation; https://www.axis.com/products/axis-perimeter-defender-ptz-autotracking; dostęp 2026-11-22.
- **S-Q1972** AXIS Q1972-E Thermal Camera datasheet; 640x480 microbolometer, 8.3/30 fps; 10 mm HFOV 63 deg, 19 mm HFOV 31 deg; DRI human detect (1.5 px) 291 m with 10 mm, 559 m with 19 mm, recognize (6 px) 73/140 m; PoE class 3 typical 5.0 W max 12.95 W; AXIS Perimeter Defender supported; https://www.axis.com/dam/public/7c/6e/e4/datasheet-axis-q1972-e-thermal-camera-en-US-555471.pdf; dostęp 2026-11-22.
- **S-Q6355** AXIS Q6355-LE PTZ Camera datasheet; PoE IEEE 802.3bt class 6, typical 13 W without IR, max 51 W; IR illumination, AXIS Object Analytics, 300 presets; https://www.axis.com/dam/public/fd/a5/0c/datasheet-axis-q6355-le-ptz-camera-en-US-555456.pdf; dostęp 2026-11-22.
- **S-D2210** AXIS D2210-VE Radar datasheet; area monitoring: human 5 to 60 m, vehicle 5 to 90 m at 5 m height and 15 deg tilt; 95 deg coverage; PoE IEEE 802.3at class 4, typical 5.88 W, max 8 W; https://www.axis.com/dam/public/5d/97/08/datasheet-axis-d2210-ve-radar-en-US-480992.pdf; dostęp 2026-11-22.
- **S-T8504** AXIS T8504-R Industrial PoE Switch datasheet; 4 PoE++ ports up to 60 W each, 2 RJ45 and 2 SFP data ports, 240 W PoE budget, 48 to 57 V DC input (optional DIN PS56 240 W), -40 to 75 C; https://www.axis.com/dam/public/89/81/ca/datasheet-axis-t8504-r-industrial-poe-switch-en-US-308120.pdf; dostęp 2026-11-22.
- **S-RWSL** FAA, Runway Status Lights; runway entrance and takeoff hold lights switched automatically from surface surveillance; separate airport system, not CCTV analytics; https://www.faa.gov/air_traffic/technology/rwsl/pet; dostęp 2026-11-22.
- **S-PXD** Axis, Pixel density based on IEC 62676-4:2025, white paper; IEC 62676-4:2025 operational requirements: Discern 80 px/m, Perceive 125 px/m, Characterize 250 px/m (person type, gait, behaviour), Validate 500 px/m, Scrutinize 1500 px/m (identity with high certainty); September 2026; https://whitepapers.axis.com/en-us/pixel-density-based-on-iec-62676-4-2025; dostęp 2026-11-22.
- **S-GATE** FAAC 740/741 installation manual 732484 rev D; technical specifications: 741 at 230 V 50 Hz absorbed power 500 W, current 2.2 A, leaf max 900 kg, use frequency S3 40%, -20 to +55 C; manual release; https://faac.blob.core.windows.net/web/1/gate-automation/faac-sliding-gates/740-230v-sliding-gate-operator/740-741-732484-revd-en.pdf; dostęp 2026-11-22.
