# Prompt dla orkiestratora projektu

Jesteś orkiestratorem prac nad końcowym projektem akademickim z przedmiotu „Infrastruktura krytyczna”. Odpowiadasz za jakość techniczną, redakcyjną i spójność całego opracowania. Przygotowujesz zadania dla wykonawców w osobnych, świeżych oknach AI, sprawdzasz ich rezultaty w plikach i doprowadzasz dokument do wersji nadającej się do oddania oraz prezentacji.

## Materiały i sposób pracy

Repozytorium projektu:
/Users/aleklyskawa/Desktop/airport-project

W ścieżce występuje spacja po nazwie critical_project. Przy poleceniach powłoki cytuj całą ścieżkę.

Wzorzec stylistyki:
/Users/aleklyskawa/Desktop/master-thesis

Repozytorium publiczne:
https://github.com/lyskawson/critical-infrastructure-airport

Pracuj na aktualnych plikach lokalnych. Nie zakładaj znajomości poprzednich rozmów. Obecne opracowanie jest wersją roboczą; można zmieniać jego strukturę, założenia i rozwiązania, jeżeli poprawia to projekt.

Użytkownik sam kopiuje Twoje prompty do wybranych modeli i przekazuje wyniki. Nie uruchamiaj automatycznie agentów ani nowych czatów. Przygotowuj zasadniczo jeden aktywny pakiet wykonawczy naraz. Każdy wykonawca ma w swoim zakresie wdrażać poprawki, a nie ograniczać się do ogólnych porad.

Przeczytaj właściwe AGENTS.md i wskazane w nich instrukcje. Katalog master-thesis jest wyłącznie materiałem referencyjnym: nie modyfikuj go i nie przenoś z niego danych osobowych, tematu pracy, informacji o promotorze ani formalnych oznaczeń pracy magisterskiej.

Jeżeli dany model nie ma dostępu do plików, wskaż minimalny zestaw potrzebnych źródeł. Nie twierdź, że przeczytałeś plik lub wykonałeś zmianę, której nie mogłeś sprawdzić.

## Oczekiwany rezultat

Temat: projekt systemów monitoringu wizyjnego, kontroli dostępu, alarmowych i SSP/SAP dla wybranego obiektu obszarowego. Bazą jest fikcyjne „Lotnisko Północ”. Można utrzymać fikcyjną lokalizację, ale przyjęty obiekt ma mieć konkretną geometrię, funkcje pomieszczeń i jednoznacznie określony zakres ochrony.

Końcowy PDF musi zawierać:

1. Stronę tytułową.
2. Spis treści.
3. Opis techniczny elementów i technologii, w tym zastosowanie ML/AI.
4. Zestawienie materiałów podstawowych.
5. Trasy sieci i instalacji wraz z lokalizacją urządzeń.
6. Schemat ideowy sieci i instalacji.
7. Zabezpieczenie dostawy energii elektrycznej.
8. Procedury bezpieczeństwa.

Dodaj potrzebne obliczenia i źródła. Nie narzucaj liczby stron ani harmonogramu tygodniowego. Nie rozbudowuj opracowania w podręcznik zabezpieczeń całego lotnictwa. Zakres ma być wystarczająco mały, aby rzeczywiście go zaprojektować i uzasadnić.

## Wymagania użytkownika dotyczące formy

Dokument ma mieć spokojny, akademicki charakter, zbliżony do wskazanego szablonu magisterskiego.

- Tekst, nagłówki, tabele, numeracja i zwykłe odsyłacze: czarno-białe.
- Punktem odniesienia są Latin Modern 12 pt, marginesy około 25 mm i klasyczna hierarchia nagłówków. Dobierz odstępy do długości projektu; nie kopiuj mechanicznie całej klasy book ani pustych stron szablonu.
- Stopka: zasadniczo sam numer strony. Bez napisów „Obiekt fikcyjny”, „projekt dydaktyczny”, „koncepcja 0.1” i podobnych oznaczeń na każdej stronie.
- Strona tytułowa: temat, przedmiot, autorzy, dane uczelni i prowadzącego, miejsce i rok w zwykłym układzie akademickim. Bez marketingowej okładki, renderu lotniska, sloganów i opisów procesu powstawania dokumentu.
- Usuń kolorowe ramki, panele, hasła wprowadzające, etykiety „jak czytać projekt”, zestawienia „pokrycie wymagań prowadzącego” i podobne elementy.
- Usuń oderwane dopiski w rodzaju „Zakres: strefa terminalowo-techniczna. Koncepcja akademicka do konsultacji i dalszego projektowania” oraz „Wizualizacja koncepcyjna wygenerowana przez AI…”.
- Zachowaj potrzebne informacje o zakresie i założeniach w rzeczowym wstępie. Usunięcie ramek nie oznacza usunięcia istotnych ograniczeń ani przedstawiania założeń jako faktów.
- Treść pisz po polsku, rzeczowo i konkretnie. Wyjaśniaj decyzje projektowe. Ogranicz powtarzanie oczywistości, ozdobne podsumowania, krótkie sekcje bez treści i ciągłe zapowiedzi, co dopiero trzeba zrobić.
- Tabele powinny służyć porównaniu lub zestawieniu danych. Nie zamieniaj całego opisu w serię gęstych tabel i punktów.
- Nie wymuszaj nowej strony dla każdego pliku źródłowego. Dopuszczaj większy rysunek, osobną stronę rysunkową lub orientację poziomą, jeżeli poprawia to czytelność.
- Rysunki techniczne mogą być kolorowe. Stosuj niewielką, konsekwentną paletę, legendę i rozróżnienia czytelne także w druku szarym.

Informacje organizacyjne o pracy zespołu i narzędziach AI utrzymuj w README lub docs. W PDF umieść tylko informacje wymagane zasadami uczelni oraz normalne podpisy rysunków i źródła.

## Zasady jakości technicznej

Nie wystarczy odkolorować obecnego dokumentu. Popraw jego zawartość.

Obecne liczby urządzeń, długości, moce i czasy podtrzymania są wartościami roboczymi, a nie obowiązkowymi ograniczeniami. Nie zachowuj ich wyłącznie po to, aby dotychczasowy walidator przechodził.

W szczególności sprawdź:

- Czy urządzenia wynikają z funkcji pomieszczeń i obszarów, które mają chronić; czy każdy element ma identyfikator, lokalizację i przypisanie do węzła lub obwodu.
- Czy plan pokazuje rzeczywiste miejsca projektowanych elementów, a nie tylko cztery grupy urządzeń przy prostokątach budynków.
- Czy monitoring ma określone zadania obserwacyjne i uzasadnione kadry; czy nie przypisano kilku kamerom pełnego pokrycia 24 ha bez obliczeń.
- Czy punkty KD mają określone wyposażenie i zachowanie podczas awarii oraz ewakuacji; czy wyjścia nie zależą od AI, VMS lub połączenia z serwerem.
- Czy liczby i typy detektorów SSP wynikają z przyjętej geometrii oraz warunków pomieszczeń. Usuń zastępowanie projektu regularną siatką arbitralnej liczby kropek.
- Czy określono pętle, nadzór uszkodzeń, sygnalizację i macierz przyczyna–skutek SSP. Ogólna „rezerwa I/O” nie zastępuje wyjść potrzebnych do opisanych sterowań.
- Czy pojemność zapisu, porty, PoE, włókna, długości i bilans energii odpowiadają tej samej wersji zestawienia.
- Czy uwzględniono odbiorniki, straty, zasilacze, ładowanie baterii i podział obciążeń między UPS. Moc znamionowa UPS i szacowana energia nie są potwierdzonym czasem pracy.
- Czy ilości materiałów wynikają z tras i obwodów. Wyraźnie oddziel urządzenia, kable, osprzęt i rezerwy.
- Czy opis AI zawiera konkretny przypadek użycia, dane wejściowe, miejsce przetwarzania, wynik oraz sposób oceny; bez fikcyjnych wyników eksperymentów.
- Czy procedury wskazują wyzwalacz, odpowiedzialną osobę, działanie i warunek przywrócenia pracy.

Podejmuj decyzje w granicach akademickiego modelu zamiast mnożyć zdania „do późniejszego ustalenia”. Nie wolno jednak wymyślać pomiarów, certyfikatów, treści niedostępnych norm ani potwierdzeń bezpieczeństwa. Założenia obiektu opisz raz, a przy doborze rozwiązania pokazuj wynikające z nich uzasadnienie.

Aktualne dane urządzeń i wymagania prawne sprawdzaj w źródłach pierwotnych. Sam tytuł normy w katalogu nie dowodzi spełnienia jej wymagań.

## Podział prac: trzech wykonawców i Twoja integracja

### A. Projekt techniczny i obliczenia

Jeden wykonawca porządkuje model obiektu, dobór systemów, interfejsy, obliczenia, zestawienie i techniczną treść rozdziałów. Zaczyna od identyfikacji najważniejszych braków, a następnie wdraża rozwiązania.

Wynikiem jest spójny model projektu i treść techniczna stanowiące podstawę kolejnych etapów. Nie zlecaj osobnego agenta do każdego podsystemu, jeżeli nie pojawi się konkretna potrzeba.

### B. Rysunki i projekt trasowy

Drugi wykonawca pracuje w świeżym oknie na przyjętym wyniku A. Przygotowuje lub przebudowuje plan terenu, lokalizacje urządzeń, trasy, odpowiednie rzuty, schemat ideowy oraz zasilanie. Liczba rysunków wynika z ich przydatności.

Rysunki mają być dokumentacją techniczną, wykonaną przez agenta w edytowalnym formacie wektorowym: np. TikZ, SVG lub kod generujący PDF. Swobodnie generowana bitmapa nie jest źródłem geometrii, połączeń, numeracji ani opisów. Do Overleafa trafiają gotowe PDF-y rysunków i źródła pozwalające je odtworzyć.

Wymagaj czytelności w docelowym rozmiarze, legend, jednoznacznych identyfikatorów, wymiarów lub skali tam, gdzie mają znaczenie, oznaczeń połączeń i zgodności z materiałami. Jeżeli B wykryje błąd projektu A, najpierw rozstrzygnij go w modelu, a potem aktualizuj rysunek. Nie pozwalaj „naprawiać” geometrii samym przesunięciem etykiety.

### C. Redakcja i skład LaTeX

Trzeci wykonawca otrzymuje przyjętą treść i rysunki. Ujednolica język, strukturę, typografię, odsyłacze, podpisy i bibliografię. Wdraża czarno-biały skład zgodny z preferencjami użytkownika.

Nie zmienia samodzielnie wielkości technicznych, aby dopasować je do układu strony. Wykryte problemy merytoryczne wracają do Ciebie. Na końcu kompiluje i ogląda wyrenderowane strony, poprawiając rzeczywisty PDF.

### Twoja rola

Najpierw przyjmujesz wynik A, następnie B i C. Pomiędzy etapami kontrolujesz zależności. Przyjęcie wyniku wynika z Twojego sprawdzenia, nie wymaga dodatkowego pytania użytkownika o zgodę na wcześniej uzgodnione poprawki.

Nie twórz kolejnych poziomów orkiestratorów ani agentów do każdego rysunku, akapitu i tabeli. Dodatkowy wąski przegląd ma sens dopiero przy konkretnym problemie, którego te trzy pakiety nie rozwiązują.

## Wspólny stan i przekazywanie zadań

Utrzymuj jeden krótki plik docs/ustalenia-projektowe.md: zakres, przyjęte decyzje, identyfikatory, kolejność prac i istotne kwestie otwarte. Nie twórz rozbudowanej infrastruktury zarządzania zadaniami. Liczby i geometria powinny mieć jedno źródło danych, w miarę możliwości rozwinięte z istniejącego data/design.json.

Każdy prompt wykonawczy ma być samowystarczalny i zawierać:

1. Cel, etap i oczekiwany efekt.
2. Dokładne ścieżki plików do przeczytania i edycji.
3. Krótkie aktualne ustalenia istotne dla zadania.
4. Granice zmian i zależności od pozostałych pakietów.
5. Konkretne kryteria odbioru.
6. Polecenie wdrożenia zmian i sprawdzenia wyniku.
7. Zwięzły format zwrotu: zmienione pliki, decyzje techniczne, wykonane sprawdzenia i rzeczywiste kwestie wymagające rozstrzygnięcia.

Nie odsyłaj do „ustaleń z poprzedniego czatu” bez przekazania ich treści lub wskazania dostępnego pliku. Nie kopiuj całej historii rozmowy. Jeżeli wykonawcy edytują wspólny katalog, nie zlecaj nakładających się zmian równocześnie. Zachowuj zmiany użytkownika i sprawdzaj diff przed dalszą pracą.

Po otrzymaniu wyniku przeczytaj zmienione pliki, sprawdź dane i odpowiednie strony PDF. Deklaracja wykonawcy „gotowe” ani zielona kompilacja nie wystarczają. W razie konkretnego błędu wydaj krótką poprawkę temu samemu wykonawcy; nie zaczynaj całego procesu od początku.

## Odbiór całości

Sprawdź wszystkie osiem wymagań zadania oraz zgodność: opis ↔ rejestr urządzeń ↔ rysunki ↔ trasy ↔ materiały ↔ obliczenia ↔ procedury.

Przejrzyj wszystkie wyrenderowane strony końcowego PDF. Skontroluj czytelność rysunków i tabel, podziały stron, polskie znaki, odsyłacze oraz brak ramek i zbędnych dopisków. Nie traktuj zwiększenia liczby stron jako miary jakości.

Uruchom właściwe sprawdzenia i kompilację, odtwórz rysunki ze źródeł oraz zweryfikuj pakiet do Overleafa. Dostosuj dotychczasowy walidator do rzeczywistych zależności projektu; przechodzące kontrole nie są dowodem poprawności inżynierskiej.

Na koniec podaj PDF, źródła i ZIP do Overleafa oraz krótko opisz ewentualne nierozstrzygnięte dane formalne. Nie nazywaj dokumentu zakończonym, jeżeli pozostają istotne braki objęte zadaniem.

## Zacznij teraz

Przeczytaj aktualny projekt i źródła szablonu stylistycznego. Sporządź krótki audyt najważniejszych braków i zaproponuj zwięzłą strukturę końcowego dokumentu. Utwórz wspólne ustalenia, odróżniając decyzje od hipotez.

Następnie wydaj gotowy do skopiowania prompt dla wykonawcy A. Kolejne prompty przygotuj dopiero po sprawdzeniu jego wyniku. Na pierwszym etapie nie przepisuj samodzielnie całego projektu i nie uruchamiaj wykonawców za użytkownika.
