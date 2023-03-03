# Projektmunka_1_2022-23_10d
Projektmunka leírások 2023
## Általános feladatok
- Feladatok szétosztása
- GitHub elkészítése
    - Readme.md (ide kerül a műszaki leírás angolul)
    - ReadmeHu.md (ide kerül a műszaki leírás magyarul)
    - források gyűjtése (`sources` mappa)
- Kapcsolási rajzok (fritzing)
    - Sematikus rajz (`shematic` mappa)
- Áramkör megépítése a próba panelen
- Program fejlesztés (`sourcesCode` mappa)
    - Program elkészítése kis lépések módszerével:
        - Módosítás - Tesztelés ciklus
- Prezentáció készítés a feladatról (`presentations/projeknev.ppt`)
- Videó felvétel, fotó a feladatról: `presentations/projektnev.jpg` mappába
- Prezentáció megtartása
    - Élő előadás
    - Videofelvétel
    - Előadások megbeszélése
- Értékelés
    - Felelés (teszt)
# Feladat ütemezés
## 2023.03.03-05 kapcsolási razj
- Otthoni munka: az egyik csapattag
- A csoport készítse el a repóját (a csapatkapitány githubjába)
- Mindent a github-ra kell elkészíteni
- Fritzing program telepítése az otthoni gépre
- Készüljön el a kapcsolási rajz: fritzing, képfájl
- A kapcsolási rajzok kerüljenenk a `shematic` mappába
## 2023.03.06-13 áramkör megépítése
- Csoportmunka
- A régi áramkör lebontása
- Alkatrészek összegyűjtése
- Az áramkör összerakása a próbapanelen a kapcsolási razj alapján
- Fotó készítése a kész panelről

# Fényerő szabályzás potméterrel: BrightnessControlWithPot
![Fényerő szabályzás potméterrel](./kapcsol%C3%A1sirajzok/f%C3%A9nyer%C5%91Potm%C3%A9ter/F%C3%A9nyer%C5%91%20potm%C3%A9terrel.png)
## Csoporttagok
- Bodzsár Máté János, Szűcs Péter Noel
## Feladat leírása
Pulzusszélesség alapon működő ledes fényerő szabályzó modell elkészítése.
- A ledet a GPIO PWM üzemmódban hajtsa meg közvetlenül egy megfelelő korlátozó ellenállással
- Szabálzó eszköz: potméter
- Szabályzási elv: 
    - A potméter áramát mérő A/D: [INA219 DC IUP mérő](https://malnapc.hu/a904-ina219-high-side-dc-current-sensor-aram-szenzor) átalakító által előállított áramtartomány érzékelése.
    - Az áramtartomány [0, 100] tartományra normálása
    - A kitöltési tényező folymatos állítása a normált tartomány segítségével.

# Fényerő szabályzás nyomógombbal: BrightnessControlWithButton
![Fényerő szabályzás nyomógombbal](./kapcsol%C3%A1sirajzok/F%C3%A9nyer%C5%91Nyom%C3%B3gomb/F%C3%A9nyer%C5%91%20nyom%C3%B3gombbal.png)
## Csoporttagok
- Balázs Szidónia, Jakab Adrienn
## Feladat leírása
Pulzusszélesség alapon működő ledes fényerő szabályzó modell elkészítése.
- A ledet a GPIO PWM üzemmódban hajtsa meg közvetlenül egy megfelelő korlátozó ellenállással
- Szabályzó eszköz: nyomógombok (mikrokapcsolók)
    - 1. kapcsoló: fényerő növelés (egyedi és folyamatos nyomással)
    - 2. kapcsoló: fényerő csökkentés (egyedi és folyamatos nyomással)
    - 3. kapcsoló: max fényerő ki-be kapcsolás
- Szabályzási elv: 
    - A kapcsolók egyedi vagy folamatos nyomásának impulzus számlálsa [0, 100] tartományra limitálva.
    - A kitöltési tényező folymatos állítása a tartomány segítségével.

# Távolságmérő: DistanceMeter
![Távolságmérő](./kapcsol%C3%A1sirajzok/T%C3%A1vols%C3%A1gm%C3%A9r%C5%91/T%C3%A1vols%C3%A1g%20m%C3%A9r%C5%91.png)
## Csoporttagok
- Nagy Dániel Csaba	Molnár Kristóf

## Feladat leírása
Ultrahangos távolságmérő készítése az [ULTRAHANGOS TÁVOLSÁGSZENZOR HC-SR04-4P](https://malnapc.hu/ultrahangos-tavolsagszenzor-hc-sr04-4p) szenzor segítségével.
A távolságmérő egy nyomógomb segítségével egy memóriába tárolja el a beadott távolságokat, valmint mutassa egy hétszegmenses kijelzőn: [A881 0.56 INCH CLOCK DISPLAY W/I2C BACKPACK - BLUE](https://malnapc.hu/a881-0-56-inch-clock-display-wi2c-backpack-blue)
- 1. nyomógomb: távolság rögzítése
- 2. nyomógomb: Memória törlése
- 3. nyomógomb: a memóriában tárolt távolságok váltása a hétszegmenses kijelzőn
- 4. nyomógomb: Az utolsó két mérési adat alapján számoljon területet
- 5. nyomógomb: Az utolsó három mérési adat alapján számoljon térfogatot

# Hőmérséklet szabályzó: TemperatureController
![Hőmérséklet szabályzó](./kapcsol%C3%A1sirajzok/H%C5%91m%C3%A9rs%C3%A9klet%20m%C3%A9r%C5%91/H%C5%91m%C3%A9rs%C3%A9klet%20m%C3%A9r%C5%91.png)
## Csoporttagok
- Balogh Bálint Ágoston, Botka Fanni, Barta Marcell 
## Feladat leírása
- A [DS18B20+](https://malnapc.hu/ds18b20) 1-wire (egyvezetékes) digitális hőmérséklet érzékelők egy vezetékre felfűzött (4-5 db) láncának segítségével szimulálja, hogy ezek különböző helyiségek, dolgok hőmérsékletét mérik.
- Egy kapcsoló segítségvével lehessen váltatni, hogy melyik érzékelő hőmérsékletét mutatja a 7 szegmenses kijelző: [A881 0.56 INCH CLOCK DISPLAY W/I2C BACKPACK - BLUE](https://malnapc.hu/a881-0-56-inch-clock-display-wi2c-backpack-blue)
- A hőérzékelőknél legyen egy led, ami mutatja, melyik hőmérséklete van éppen kijelezve
- A kiválasztott hőrzékelő a beprogramozott hőmérséklet határ alatt kapcsolja be a fűtést, felett pedig ki. A hiszterézis legyen 0.5 °C.
- Legyen porgramozható a hőmérséklet határ.
- Programzó gombok:
    - 

# U,I,P,R mérő: upirMeasuring
![U,I,P,R mérő](./kapcsol%C3%A1sirajzok/U%2CI%2CP%2CR%20m%C3%A9r%C5%91/%C3%81ramm%C3%A9r%C5%91%20kapcs_schem.png)
## Csoporttagok
- Sebők Bence, Szabó Zoltán
## Feladat leírása
A [INA219 DC IUP mérő](https://malnapc.hu/a904-ina219-high-side-dc-current-sensor-aram-szenzor) árammérő szenzor segítségével készítsen egy:
- Feszülség
- Áram
- Teljesítmény
- Ellenállás

mérő eszközt, ami egy 7 szegmenses kijelzőn mutatja az értékeket: [A881 0.56 INCH CLOCK DISPLAY W/I2C BACKPACK - BLUE](https://malnapc.hu/a881-0-56-inch-clock-display-wi2c-backpack-blue)
Egy nyomógomb segítségével lehessen váltani a különböző funkciók között.
A különböző funkciókhoz legyen egy dugalj elrendezés, ami meghatározza, hogy mit lehet vele mérni.

# Bicikli lámpa RGB leddel: BicycleLight
![Bicikli lámpa RGB leddel](./kapcsol%C3%A1sirajzok/Bicikli/led%20kapcsolasi%20rajz%202.png)
## Csoporttagok
- Suki Zsolt, Pap Balázs
## Feladat leírása
Az alkatrész csomagban található [RGB led(ek)](https://www.hestore.hu/prod_10037597.html) segítségével szimuláljon egy biciklilámpát
- 1. kapcsoló: Első vagy hátsó lámpa üzemmód
- 2. kapcsoló: Az üzemmódon belüli váltás

- Első lámpa üzemmód állapotok
    1. Fehér erős fény
    2. Fehér gyengébb fény
    3. Kikapcsolva
- Hátsó lámpa üzemmód állapotok
    1. Folyamatos vörös
    2. Villogó vörös
    3. Kikapcsolva 

# Közlekedési lámpa: TrafficLights
![Közlekedési lámpa](./kapcsol%C3%A1sirajzok/K%C3%B6zleked%C3%A9si%20l%C3%A1mpa/K%C3%B6zleked%C3%A9si%20l%C3%A1mpa.png)
## Csoporttagok
- Szurmai Bence Zsolt, Nagy Dominik Patrik, Seres László
## Feladat leírása
Egy kereszteződés autóforgalmi és gyalogos átkelőhely közlekedési lámpáit szimuláló rendszer elkészítése 5 megfelelő színű ledsorral.
- [A feladat részletes leírása](http://labtoll.hu/raspberry/algoritmus.html#algoritmus)

