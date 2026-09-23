from PIL import Image
from pathlib import Path

for f in Path(".").glob("*.png"):
    im = Image.open(f)

    if im.width > 1200:
        im = im.resize(
            (1200, int(im.height * 1200 / im.width)),
            Image.Resampling.LANCZOS
        )

    im.save(f, optimize=True)
    print(f"{f.name} -> {im.size}")

print("Done!")