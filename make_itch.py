#!/usr/bin/env python3
"""Build itch.io variants of Affix Merchant: itch/free and itch/premium (+ zips with index.html at root)."""
import os, zipfile
D = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(D, "index.html")
src = open(SRC, encoding="utf-8").read()
def rep(s, a, b):
    assert s.count(a) == 1, "pattern not found/unique: " + a[:70]; return s.replace(a, b, 1)
def base(s):  # itch builds: English default (already), html lang en
    return s.replace('<html lang="sk">', '<html lang="en">')
def free(s):
    return rep(s, "const PREMIUM=false;", "const PREMIUM=false;")
def premium(s):
    s = rep(s, "const PREMIUM=false;", "const PREMIUM=true;")
    return s.replace("<title>Affix Merchant</title>", "<title>Affix Merchant – Premium</title>", 1)
def write(path, txt):
    os.makedirs(os.path.dirname(path), exist_ok=True); open(path, "w", encoding="utf-8").write(txt)
for name, fn in (("free", free), ("premium", premium)):
    out = fn(base(src)); p = os.path.join(D, "itch", name, "index.html"); write(p, out)
    with zipfile.ZipFile(os.path.join(D, f"affix-merchant-{name}.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("index.html", out)
print("built itch/free, itch/premium, affix-merchant-free.zip, affix-merchant-premium.zip")
