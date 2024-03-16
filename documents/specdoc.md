## Signaalinkäsittely

Käytän ohjelman toteutuksessa Pythonia, en osaa toistaiseksi muita ohjelmointikieliä.

Pyrin tekemään sovelluksen, joka poistaa äänisignaalista kohinaa. Toteutan FFT:n, jonka avulla saan
eroteltua signaalissa esiintyvät taajuudet. Tästä datasta on tarkoitus tunnistaa tärkeimmät taajuudet,
jotka halutaan säilyttää, ja tärkeimmät taajuudet, jotka halutaan suodattaa pois. Toteutan IFFT:n, jolla
suodatettu data palautetaan takaisin äänisignaaliksi.

Sovelluksen avulla poimitaan äänisignaalista haluttu tieto (esimerkiksi linnunlaulu) ja siivotaan pois
epätoivottu kohina (esimerkiksi tuuli).

Sovellus saa syötteeksi tallennetun WAV-muotoisen tiedoston ja palauttaa tallennetun WAV-muotoisen tiedoston.

Tavoitteena on kirjallisuudessa esiintyvä FFT:n aikavaativuus O(n log<sub>2</sub> n).

Tietolähteinä toistaiseksi käytössä kurssimateriaali, Wikipedia (Fast Fourier Transform ja Cooley-Tukey
FFT algorithm).

Harjoitustyön ydin on signaalinkäsittely FFT:n avulla. Diskreetti data, joka sisältää kaikki päällekkäiset
taajuudet, käsitellään FFT:n avulla muotoon, josta voidaan erotella signaalissa esiintyvät taajuudet ja
niiden osuus kokonaissignaalista. Datasta suodatetaan pois epätoivotut taajuudet ja jäljellä oleva data
palautetaan yhdeksi signaalisti käänteisen FFT:n (IFFT) avulla.

Opiskelen tietojenkäsittelytieteen kandidaattiohjelmassa (TKT) Helsingin yliopistossa. Laadin dokumentaation
suomen kielellä. Ohjelmoinnissa käytän englanninkielistä muuttujien nimentää ja kommentoin ohjelmakoodin
englanniksi alalla vallitsevan käytännön mukaisesti.
 
