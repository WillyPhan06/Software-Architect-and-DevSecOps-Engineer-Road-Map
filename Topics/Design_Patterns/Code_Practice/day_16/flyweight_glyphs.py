# flyweight_glyphs.py
from dataclasses import dataclass
import weakref
from threading import RLock
from concurrent.futures import ThreadPoolExecutor

@dataclass(frozen=True)
class GlyphIntrinsic:
    char: str
    font_name: str
    font_size: int
    font_style: str


class GlyphFactory:
    _pool = weakref.WeakValueDictionary()  # key -> GlyphIntrinsic

    @classmethod
    def get_intrinsic(cls, *args):
        key = tuple(args)
        inst = cls._pool.get(key)
        if inst is None:
            inst = GlyphIntrinsic(*args)
            cls._pool[key] = inst
        return inst
    

class ThreadSafeFactory:
    _lock = RLock()
    _pool = weakref.WeakValueDictionary()

    @classmethod
    def get_intrinsic(cls, *args):
        key = tuple(args)
        with cls._lock:
            inst = cls._pool.get(key)
            if inst is None:
                inst = GlyphIntrinsic(*args)
                cls._pool[key] = inst
            return inst



# Represent each character by (intrinsic, extrinsic)
text = "a" * 200
glyph_refs = []

def put_char_to_list():
    for i, ch in enumerate(text):
        intr = GlyphFactory.get_intrinsic(ch, "Roboto", 12, "regular")
        extrinsic = {"pos": i}   # stored externally per instance
        glyph_refs.append((intr, extrinsic))



