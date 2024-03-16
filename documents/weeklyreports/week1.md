# Viikko 1

**Käytetty aika: 8-10 tuntia**

## Mitä olen tehnyt tällä viikolla?

Olen tällä viikolla yrittänyt tutustua erilaisiin algoritmeihin ja yrittänyt löytää sopivaa harjoitustyön
aihetta. Yritin päästä ymmärrykseen Ukkosen algoritmin toiminnasta, mutta sen säännöt olivat minulle liian
monimutkaiset ymmärtää loppuun asti. Yritin tutkia systolic array -rakennetta, joka näytti kirjassa
mielenkiintoiselta. Se osoittautui laitteistopuolella tapahtuvaksi toteutukseksi, jonka käyttäminen vaatisi
myös rinnakkaisohjelmointia, mitä en osaa. Yritin tutkia Ed25519 -allekirjoitusta, mutta en pystynyt
ymmärtämään siihen liittyvää matematiikkaa äärellisestä kentästä ja elliptisestä käyrästä. Yritin tutkia
FFT:n sovellusta optioiden hinnoitteluun, mutta siihen liittyvät osittaisdifferentiaaliyhtälöt olivat liian
vaikeita ymmärtää.

Olen etsinyt tietoa äänisignaalin käsittelystä ja siitä, minkälaisia kirjastoja on signaalin kuvaamiseen
näytöllä tai signaalin kuuntelemiseen. Olen yrittänyt etsiä Internetistä äänitiedostoja, joita voisin käyttää.
En löytänyt hyviä WAV-muotoisia tiedostoja, joten tallensin MP3-muotoisia tiedostoja koneelleni. Valitsin
samankaltaisia tiedostoja - niissä on kaikissa lintujen ääntä ja lisäksi jotain tuulta tai kohinaa, jonka
yritän suodattaa pois.

## Miten ohjelma on edistynyt?

En ole aloittanut vielä ohjelman tekemistä.

## Mitä opin tällä viikolla?

Opin, että mielenkiintoiset algoritmit ovat liian vaikeita ymmärtää ilman riittäviä matemaattisia pohjatietoja.
FFT:tä voidaan käyttää differentiaaliyhtälöiden ratkaisemiseen ja sitä tunnutaan soveltavan alueilla, joissa
differentiaali- tai osittaisdifferentiaaleja esiintyy. Katsoin jopa videon, jossa yritettiin selittää miten
FFT on helppo hahmottaa kvanttifysiikan kautta, mutta kun kvanttifysiikan yhtälöt jäivät nuorena oppimatta,
niin tuokaan video ei tuonut lopullista valaistumista. Pystyn nyt käsittääkseni hahmottamaan, miten FFT:llä
saadaan käsiteltyä signaalia. Kuvan käsittely FFT:llä vaikuttaa liian vaikealta, koska siinä operaatiot pitää
tehdä kahdessa ulottuvuudessa.

## Mikä jäi epäselväksi tai on tuottanut vaikeuksia?

Sopivan aiheen löytäminen oli vaikeaa. Aiheen pitää olla riittävän kiinnostava, jotta sen parissa jaksaa
työskennellä, mutta ei kuitenkaan liian epätoivoisen vaikea. Valtaosa kurssisivulla esitetyistä aiheista
vaikutti jo ensilukemalta epätoivoisen vaikeilta tai sellaisilta, joissa käyttöliittymän kanssa tuhraamiseen
menisi (minulta) aivan liikaa aikaa.

FFT:hen tutustumiseen olen käyttänyt paljon aikaa, mutta vieläkin tuntuu, että ymmärrys on hieman hataralla
pohjalla, vaikka olen suorittanut kaksi kurssia lineaarialgebraa. FFT:tä voi lähestyä niin monesta näkökulmasta
ja varsinkin alkuvaiheessa minulla meni sekaisin tavallinen ja diskreetti Fourier-muunnos.

## Mitä teen seuraavaksi?

Yritän tutustua kirjastoihin, joiden avulla saan MP3-tiedostot WAV-muotoon ja toivottavasti tulostettua
signaalin ruudulle. Yritän selvittää, pitääkö minun pilkkoa signaali pienempiin ikkunoihin muunnosta varten
ja lisätä ikkunoiden alkuun ja loppuun tyhjää, jotta yhdistämisen jälkeen ei jäisi saumakohtiin rätinää.

Saatan aloittaa ohjelman ytimen rakentamisen omatekoisella signaalilla, jos valmiiden signaalien muokkaus
näyttää vievän kohtuuttomasti aikaa. Haluan päästä kokeilemaan algoritmiä ensin helpommilla signaaleilla,
mistä pystyn helposti itse näkemään, toimiiko algoritmi toivotulla tavalla. Näitä harjoittelusignaaleja
voin käyttää myös testeissä.
