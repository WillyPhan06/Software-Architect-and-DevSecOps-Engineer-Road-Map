from dataclasses import dataclass
import weakref
import tracemalloc

# -------------------------
# Naive class (no slots)
@dataclass
class GlyphNaive:
    char: str
    font_name: str
    font_size: int
    font_style: str

# -------------------------
# Flyweight class with slots
@dataclass(frozen=True, slots=True, weakref_slot=True)
class GlyphIntrinsic:
    char: str
    font_name: str
    font_size: int
    font_style: str



class GlyphFactory:
    _pool = weakref.WeakValueDictionary()

    @classmethod
    def get_intrinsic(cls, *args):
        key = tuple(args)
        inst = cls._pool.get(key)
        if inst is None:
            inst = GlyphIntrinsic(*args)
            cls._pool[key] = inst
        return inst

# -------------------------
# Test data
num_objects = 1000
text = ["a"] * num_objects

# -------------------------
# Measure naive objects
tracemalloc.start()
naive_objs = [GlyphNaive(ch, "Roboto", 12, "regular") for ch in text]
snap1 = tracemalloc.take_snapshot()

# -------------------------
# Measure flyweight objects
glyph_refs = []
for i, ch in enumerate(text):
    intr = GlyphFactory.get_intrinsic(ch, "Roboto", 12, "regular")
    extrinsic = {"pos": i}   # stored externally
    glyph_refs.append((intr, extrinsic))
snap2 = tracemalloc.take_snapshot()

# -------------------------
# Compare memory
print("Top memory differences:")
for stat in snap2.compare_to(snap1, 'lineno')[:10]:
    print(stat)
