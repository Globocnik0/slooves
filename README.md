# slooves.si

Spletna stran za ovseni napitek **slooves**. Trenutno je objavljena samo stran
"v izgradnji".

## Tehnicno

Staticna stran brez orodij za gradnjo - navaden HTML in CSS. Gostuje na GitHub
Pages, domena `slooves.si`.

```
index.html      naslovnica ("v izgradnji")
qr/index.html   cilj QR kode z embalaze -> preusmeri na naslovnico
favicon.svg     ikona
CNAME           domena za GitHub Pages
.nojekyll       izklopi Jekyll obdelavo
```

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
