# naive_glyphs.py
from dataclasses import dataclass

@dataclass
class Glyph:
    char: str
    font_name: str
    font_size: int
    font_style: str
    color: tuple  # extrinsic could be here but naive keeps it

# create many glyphs: "aaaa...." etc
text = "a" * 200_000
glyphs = [Glyph(ch, "Roboto", 12, "regular", (0,0,0)) for ch in text]
