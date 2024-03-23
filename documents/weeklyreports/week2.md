# Viikko 2

**Käytetty aika: 6-8 tuntia**

## Mitä olen tehnyt tällä viikolla?

Olen yrittänyt tutustua kirjastoihin, joita tarvitaan äänisignaalien tulostamisessa ja soittamisessa. Olen yrittänyt selvittää, saako MP3-tiedostosta raakadataa suoraan, vai pitääkö se ensin muuttaa WAV-muotoon. Olen tehnyt kokeiluja signaalin tulostamisesta ja soittamisesta ja yrittänyt hahmottaa miten signaalin saisi jaettua pienempiin palasiin fft-muunnosta varten.

Minulla oli ajatus aloittaa tämän sovelluksen tekeminen ensin omatekoisella signaalilla, joka olisi generoitu matemaattisista funktioista, jolloin olisin päässyt nopeammin tekemään kokeiluja oman FFT:n parissa. Kuitenkin kaikki tietotyyppeihin ja tulostamiseen liittyvät kysymykset vaivasivat siinä määrin, että päädyin setvimään niitä, enkä päässyt oman koodin kanssa edes alkuun.

## Miten ohjelma on edistynyt?

En ole päässyt alkuun varsinaisen ohjelman tekemisen kanssa.

## Mikä jäi epäselväksi tai on tuottanut vaikeuksia?

Melkein kaikki asiat, jotka olivat viime viikolla epäselviä, ovat edelleen epäselviä. En pysty oikein hahmottamaan, mitä kaikkea tässä pitäisi käytännössä tehdä. Tai tiedän, mitä pitäisi tehdä, mutta en tiedä, miten saan tehtyä tarvittavat toiminnot. En ehkä ole vielä kunnolla ymmärtänyt aiheen matemaattista taustaa ja siksi käytännön toteutukseen liittyy vielä paljon kysymysmerkkejä.

Tällaisten omien projektien aloittaminen on minulle aina vaikeaa, kun kokonaisuutta on vaikea hahmottaa ja jään liian pitkäksi aikaa murehtimaan ratkaisemattomia ongelmia sen sijaan, että tekisin edes jotain, mitä arvelen osaavani tehdä.

## Mitä teen seuraavaksi?

Koska en saanut tällä viikolla tehtyä sitä, mitä olin kuvitellut tekeväni, kirjaan uudelleen tämän aiemman suunnitelman: 

Saatan aloittaa ohjelman ytimen rakentamisen omatekoisella signaalilla, jos valmiiden signaalien muokkaus
näyttää vievän kohtuuttomasti aikaa. Haluan päästä kokeilemaan algoritmiä ensin helpommilla signaaleilla,
mistä pystyn helposti itse näkemään, toimiiko algoritmi toivotulla tavalla. Näitä harjoittelusignaaleja
voin käyttää myös testeissä.

Yritän siis saada ohjelman ydintä alulle (oma FFT) ja tehdä siihen sopivia testejä, joihin lasken vertailuarvot valmiilla kirjastolla.
