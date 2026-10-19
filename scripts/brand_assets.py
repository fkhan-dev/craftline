"""Regenerate code-drawn social and touch assets from the central brand config.
Run with Python and Pillow: python scripts/brand_assets.py
"""
import re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT = Path(__file__).resolve().parents[1]
config = (ROOT / 'src/config.ts').read_text(encoding='utf-8')
name = re.search(r'shortName: "([^"]+)"', config).group(1)
accent = re.search(r'accent: "([^"]+)"', config).group(1)
dark = re.search(r'accentText: "([^"]+)"', config).group(1)
font_path = next((p for p in [Path('C:/Windows/Fonts/arial.ttf'), Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')] if p.exists()), None)
def font(size):
    return ImageFont.truetype(str(font_path), size) if font_path else ImageFont.load_default(size=size)
def mark(draw, x, y, size):
    draw.ellipse((x,y,x+size,y+size), fill=accent)
    draw.arc((x+size*.2,y+size*.2,x+size*.8,y+size*.8), 45, 315, fill=dark, width=max(2,int(size*.07)))
    draw.polygon([(x+size*.53,y+size*.28),(x+size*.38,y+size*.58),(x+size*.68,y+size*.58)],fill=dark)
    draw.ellipse((x+size*.38,y+size*.43,x+size*.68,y+size*.73),fill=dark)
im = Image.new('RGB',(1200,630),dark); d=ImageDraw.Draw(im)
mark(d,72,65,72)
d.text((164,76),name, font=font(42), fill='#f6f2e8')
d.text((72,220),'A little less worry.',font=font(70),fill='#f6f2e8')
d.text((72,308),'A home that works.',font=font(70),fill=accent)
d.line((72,470,1128,470),fill=accent,width=2)
d.text((72,510),'PLUMBING & HEATING  /  DEMO WEBSITE',font=font(22),fill='#f6f2e8')
im.save(ROOT/'public/og.png')
im=Image.new('RGB',(180,180),dark); mark(ImageDraw.Draw(im),14,14,152); im.save(ROOT/'public/apple-touch-icon.png')
