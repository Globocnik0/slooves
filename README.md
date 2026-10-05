# slooves.si

Spletna stran za ovseni napitek **slooves**. Enostranska stran brez menija.

## Tehnicno

Staticna stran brez orodij za gradnjo - navaden HTML in CSS. Gostuje na GitHub
Pages, domena `slooves.si`.

```
index.html                 naslovnica (enostranska stran)
qr/index.html              cilj QR kode z embalaze -> preusmeri na naslovnico
images/                    vektorska grafika blagovne znamke (glej spodaj)
favicon.svg                ikona
robots.txt, sitemap.xml    za Google (Search Console)
CLAUDE.md                  navodila za delo v repozitoriju
_config.yml                datoteke, ki se ne objavijo na strani (README, CLAUDE.md)
CNAME                      domena za GitHub Pages
```

## Grafika blagovne znamke

Vsa grafika v `images/` je izrezana neposredno iz vektorskih datotek celostne
graficne podobe (CGP). Nic ni prerisano.

| datoteka | kaj je |
|---|---|
| `logo.svg` | primarni logotip (brez slogana) |
| `logo-slogan.svg` | primarni logotip s sloganom "ovseni napitek" - osnovna oblika |
| `logo-slogan-alt.svg` | razlicica s sloganom "iz slovenskih polj" |
| `logo-white.svg`, `logo-slogan-white.svg` | beli razlicici za temno podlago |
| `logo-stacked.svg`, `logo-stacked-slogan.svg` | sekundarni (zlozeni) logotip |
| `mark.svg`, `mark-cream.svg` | znak (samo "O" z listom), uporabljen tudi kot favicon |
| `border.svg` | okrasni trak, natanko ena ponovitev |
| `flowers.svg`, `leaves.svg` | posamezna elementa traku |
| `badge-*.svg` | oznake izdelka (vegansko, brez laktoze, sladkorjev, dodatkov) |

### Barve

Iz CGP prirocnika, stran "barve & barvni zapisi". Za splet se uporablja HEX.

| | HEX | Pantone |
|---|---|---|
| gozdno zelena | `#165600` | 2427 C |
| kadmijevo rumena | `#F09E03` | 2012 C |
| mering bela | `#FFF2E2` | P 7-1 C |
| olivno rjava | `#898067` | 6207 C |

Izvirne datoteke so pripravljene v CMYK za tisk, zato se pri pretvorbi v RGB
vsaka datoteka razlikuje za odtenek. Barve v `images/*.svg` so zato poenotene
na zgornje vrednosti iz CGP. Rdeca iz nageljnov (`#BB2832`) v CGP paleti ni
navedena.

### Tipografija

Iz CGP, stran "tipografije in fonti". Oboje je na Google Fonts.

- **Raleway Extra Bold** - naslovi, vedno velike tiskane crke
- **Raleway Semi Bold** - podnaslovi
- **Archivo Condensed Light/Regular** - navadno besedilo

### Trak (`border.svg`)

Ena ponovitev vzorca sta dva gorenjska nageljna in dva lipova lista. Kot na
embalazi je en trak obrobljen z listi, naslednji z nageljni (`data-ends`).

Visino in zamik traku nastavi skripta na dnu `index.html` glede na sirino
zaslona: trak pokaze cele ponovitve plus en dodaten motiv, zato se na obeh
straneh konca z istim motivom in enakim praznim prostorom. Ciljna visina je
72 px na telefonu in 100 px na racunalniku; dejanska se malo prilagodi, da se
motivi izidejo. Prazen prostor na koncih prekrijeta `::before`/`::after`, da
ne pokuka kos sosednjega motiva. Zelene crte so narisane se enkrat cez celo
sirino (`linear-gradient`), ker so se na sticiscih ploscic videli tanki presledki.

**Visina je vedno cela stevilka zaslonskih pik.** Ce ni, se trakovi zgladijo
razlicno in zeleni odtenek izgleda razlicno - pri 34 px in `devicePixelRatio`
1,25 je bil spodnji trak vidno svetlejsi. Skripta zato tudi vsak trak zamakne
na celo zaslonsko piko.

Barva podlage je bez s koncne embalaze (`#EED9B2`), ne svetla krem barva iz CGP.

## Lokalni predogled

V mapi repozitorija:

```
python -m http.server 8080
```

Nato odpri <http://localhost:8080/>.

## QR koda na embalazi

Na embalazo je natisnjena QR koda, ki kaze na `https://slooves.si/qr/`.
Ta naslov je namenoma vmesni korak: ce se ciljna stran kdaj spremeni, se
popravi samo `qr/index.html` in vse ze natisnjene embalaze delujejo naprej.

## Objava

Vsak `git push` na `main` sprozi objavo prek GitHub Pages.
