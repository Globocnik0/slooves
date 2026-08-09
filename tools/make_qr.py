"""Generate the slooves packaging QR codes.

    pip install segno
    python tools/make_qr.py

Writes SVG + PDF (for print) and PNG (for preview) into _qr/, and prints a
comparison table so you can see what each parameter costs you.
"""

from pathlib import Path

import segno

# The URL the printed code points at. Uppercase is deliberate: QR has a
# compact "alphanumeric" mode that only covers A-Z, 0-9 and a few symbols,
# so an uppercase URL packs into fewer modules than a lowercase one. Domain
# names and the scheme are case-insensitive, so the link still works.
TARGET = "HTTPS://SLOOVES.SI/QR/"

OUT = Path(__file__).resolve().parent.parent / "_qr"

INK = "#2e2a24"      # slooves dark brown
CREAM = "#f6f1e6"    # slooves cream

# Printed width in millimetres. Rule of thumb: a scanner needs the code to be
# roughly 1/10 of the reading distance. 25 mm is comfortable for a carton you
# pick up; 15 mm is about the floor for a phone held close.
SIZES_MM = [15, 20, 25, 35]

MM_TO_PT = 72 / 25.4


def describe(qr):
    """Module count across one side, excluding the quiet zone."""
    w, _ = qr.symbol_size(scale=1, border=0)
    return w


def save_at(qr, path_stem, width_mm, dark=INK, light=CREAM):
    """Save SVG + PDF sized to an exact printed width."""
    modules = describe(qr)
    border = 4                       # quiet zone, in modules
    total = modules + 2 * border
    scale = width_mm / total         # millimetres per module

    qr.save(f"{path_stem}.svg", scale=scale, unit="mm",
            border=border, dark=dark, light=light)

    # The PDF writer measures in PostScript points, not millimetres.
    qr.save(f"{path_stem}.pdf", scale=scale * MM_TO_PT,
            border=border, dark=dark, light=light)

    return scale


def main():
    OUT.mkdir(exist_ok=True)

    print(f"Target: {TARGET}\n")
    print(f"{'file':<28} {'EC':<3} {'ver':<4} {'modules':<8} note")
    print("-" * 76)

    # --- 1. Error correction levels ------------------------------------
    # L=7%, M=15%, Q=25%, H=30% of the code can be damaged and still read.
    # boost_error=False keeps the level exactly as asked, so the comparison
    # is honest; segno otherwise silently upgrades it when it fits for free.
    for level, note in [
        ("L", "smallest, least damage tolerance"),
        ("M", "good default for packaging"),
        ("Q", "use if you overlay a logo"),
        ("H", "maximum robustness, biggest code"),
    ]:
        qr = segno.make(TARGET, error=level, boost_error=False, micro=False)
        stem = OUT / f"slooves-ec{level}"
        save_at(qr, stem, 25)
        qr.save(f"{stem}.png", scale=10, border=4, dark=INK, light=CREAM)
        print(f"{stem.name:<28} {level:<3} {qr.version:<4} "
              f"{describe(qr):<8} {note}")

    # --- 2. Uppercase vs lowercase -------------------------------------
    # For this particular URL the two tie at level M, but uppercase wins a
    # whole version at L (21 vs 25 modules) and at Q (25 vs 29). Bigger
    # modules at the same printed width means an easier scan, so uppercase
    # it is.
    lower = segno.make(TARGET.lower(), error="M", boost_error=False,
                       micro=False)
    stem = OUT / "slooves-lowercase"
    save_at(lower, stem, 25)
    print(f"{stem.name:<28} {'M':<3} {lower.version:<4} "
          f"{describe(lower):<8} byte mode - ties at M, loses at L and Q")

    # --- 3. Colour variants at print sizes -----------------------------
    # Contrast is what a scanner actually needs: dark modules on a light
    # background, never inverted, never a busy photo underneath.
    master = segno.make(TARGET, error="M", boost_error=False, micro=False)

    for mm in SIZES_MM:
        stem = OUT / f"slooves-{mm}mm-brand"
        scale = save_at(master, stem, mm)
        print(f"{stem.name:<28} {'M':<3} {master.version:<4} "
              f"{describe(master):<8} {mm} mm wide, "
              f"{scale:.3f} mm per module")

    # Plain black on white - hand this one to the printer if in doubt.
    stem = OUT / "slooves-25mm-black"
    save_at(master, stem, 25, dark="#000000", light="#ffffff")
    print(f"{stem.name:<28} {'M':<3} {master.version:<4} "
          f"{describe(master):<8} safest possible contrast")

    # Transparent background, for placing on an already-light artwork area.
    master.save(OUT / "slooves-transparent.svg", scale=1, border=4,
                dark=INK, light=None)
    print(f"{'slooves-transparent.svg':<28} {'M':<3} {master.version:<4} "
          f"{describe(master):<8} no light fill - only over a pale area")

    print(f"\nWrote {len(list(OUT.iterdir()))} files to {OUT}")

    smallest = 15 / (describe(master) + 8)
    print(f"\nAt 15 mm each module is {smallest:.3f} mm. Most presses want "
          f"at least 0.4 mm,\nso do not print smaller than that.")


if __name__ == "__main__":
    main()
