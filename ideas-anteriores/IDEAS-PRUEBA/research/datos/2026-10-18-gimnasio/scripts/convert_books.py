import sys, os, re, zipfile, pathlib
import pymupdf
from bs4 import BeautifulSoup
out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
books = {
 "ries-lean-startup": r"C:\Users\Facuc\Downloads\El método Lean Startup Cómo crear empresas de éxito utilizando la innovación continua (Spanish Edition) (Eric Ries) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
 "croll-lean-analytics": r"C:\Users\Facuc\Downloads\Lean Analytics Use Data to Build a Better Startup Faster (Alistair Croll, Benjamin Yoskovitz) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
 "altman-startup-playbook": r"C:\Users\Facuc\Downloads\Startup Playbook (Sam Altman) (z-library.sk, 1lib.sk, z-lib.sk).pdf",
 "fitzpatrick-mom-test": r"C:\FACU\PSICOLOGIA\FUENTES\The Mom Test - Rob Fitzpatrick.pdf",
 "christensen-competir-contra-la-suerte": r"C:\FACU\PSICOLOGIA\FUENTES\Competir contra la suerte - Clayton M. Christensen, Taddy Hall, Karen Dillon y David S. Duncan.pdf",
 "goldratt-la-meta": r"C:\FACU\FACU\FACULTAD\INFORMACION EXTRA\La_Meta.pdf",
 "hvidkjaer-how-to-fck-up-your-startup": r"C:\Users\Facuc\Downloads\How to Fck Up Your Startup - The Science Behind Why 90 of Companies Fail and How You Can Avoid It (Kim Hvidkjaer) (z-library.sk, 1lib.sk, z-lib.sk).epub",
 "blank-startup-owners-manual": r"C:\Users\Facuc\Downloads\The Startup Owners Manual The Step-By-Step Guide for Building a Great Company (Steve Blank, Bob Dorf) (z-library.sk, 1lib.sk, z-lib.sk).epub",
 "bhargava-herman-startup-playbook": r"C:\Users\Facuc\Downloads\The Startup Playbook Founder-to-Founder Advice from Two Startup Veterans (Rajat Bhargava  Will Herman) (z-library.sk, 1lib.sk, z-lib.sk).epub",
 "ali-kubba-unfair-advantage": r"C:\Users\Facuc\Downloads\The Unfair Advantage How You Already Have What It Takes to Succeed (Ash Ali, Hasan Kubba) (z-library.sk, 1lib.sk, z-lib.sk).epub",
}
for slug, path in books.items():
    try:
        p = pathlib.Path(path)
        if p.suffix.lower() == ".pdf":
            doc = pymupdf.open(path)
            parts = []
            for i, page in enumerate(doc):
                t = page.get_text("text")
                parts.append(f"\n[p.{i+1}]\n{t}")
            txt = "".join(parts)
        else:
            z = zipfile.ZipFile(path)
            names = [n for n in z.namelist() if n.lower().endswith((".xhtml",".html",".htm"))]
            # keep spine order if OPF available
            opf = [n for n in z.namelist() if n.lower().endswith(".opf")]
            order = names
            if opf:
                soup = BeautifulSoup(z.read(opf[0]), "xml")
                ids = {it.get("id"): it.get("href") for it in soup.find_all("item")}
                base = os.path.dirname(opf[0])
                spine = [ids.get(ir.get("idref")) for ir in soup.find_all("itemref")]
                spine = [os.path.normpath(os.path.join(base, h)).replace("\\","/") for h in spine if h]
                order = [h for h in spine if h in names] + [n for n in names if n not in spine]
            parts = []
            for k, n in enumerate(order):
                s = BeautifulSoup(z.read(n), "html.parser")
                for tag in s(["script","style"]): tag.decompose()
                t = s.get_text("\n")
                t = re.sub(r"\n{3,}", "\n\n", t)
                if len(t.strip()) > 200:
                    parts.append(f"\n[sección {k+1}: {os.path.basename(n)}]\n{t}")
            txt = "".join(parts)
        (out / f"{slug}.txt").write_text(txt, encoding="utf-8")
        print(f"{slug}: {len(txt):,} chars, ~{len(txt)//4:,} tokens")
    except Exception as e:
        print(f"{slug}: ERROR {e}")
