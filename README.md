# slooves.si

Spletna stran za ovseni napitek **slooves**. Trenutno je objavljena samo stran
"v izgradnji".

## Tehnicno

Staticna stran brez orodij za gradnjo - navaden HTML in CSS. Gostuje na GitHub
Pages, domena `slooves.si`.

```
index.html                 naslovnica ("v izgradnji")
qr/index.html              cilj QR kode z embalaze -> preusmeri na naslovnico
images/                    vektorska grafika blagovne znamke (glej spodaj)
favicon.svg                ikona
CNAME                      domena za GitHub Pages
.nojekyll                  izklopi Jekyll obdelavo
```

## Grafika blagovne znamke

Vsa grafika v `images/` je izrezana neposredno iz vektorskih datotek studia
Forming Brands (mapa `2026-7_GLOBOCNIK_embalaza` na Drive). Nic ni prerisano.

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

Ena ponovitev vzorca sta dva gorenjska nageljna in dva lipova lista. Rez je v
sredini krem prostora med njima, zato se ponovitve stikajo brez vidnega sticisca.

**Visina traku mora biti veckratnik 8 px.** Trak se riše kot `background-image`,
zato ga brskalnik prevzorci. Ce visina ni cela stevilka zaslonskih pik, se
zgornji in spodnji trak zgladita razlicno in zeleni odtenek izgleda razlicno -
pri 34 px je bilo to 42,5 zaslonske pike in spodnji trak je bil vidno svetlejsi.
Veckratnik 8 je cel pri vseh obicajnih `devicePixelRatio` (1, 1,25, 1,5, 2).

Zato tudi `background-size` ni `auto 100%`, ampak izrecna cela vrednost
(`128px 32px`, oz. `96px 24px` na mobilnem). Razmerje ploscice je skoraj
natanko 4:1 (638,37 x 159,70 pt), zato je popacenje zanemarljivo.

Ko bo stran daljsa od zaslona, bo polozaj spodnjega traku odvisen od visine
vsebine - takrat je treba znova preveriti, da oba trakova padeta na celo
zaslonsko piko.

## Lokalni predogled

```powershell
cd C:\Users\Ales\repos\slooves
python -m http.server 8080
```

Nato odpri <http://localhost:8080/>.

## QR koda na embalazi

Na embalazo je natisnjena QR koda, ki kaze na `https://slooves.si/qr/`.
Ta naslov je namenoma vmesni korak: ce se ciljna stran kdaj spremeni, se
popravi samo `qr/index.html` in vse ze natisnjene embalaze delujejo naprej.

## Objava

Vsak `git push` na `main` sprozi objavo prek GitHub Pages.
