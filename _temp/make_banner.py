from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 628
bg_color = (0, 95, 115)
text_color = (255, 255, 255)
subtitle_color = (200, 225, 230)

banner = Image.new("RGB", (W, H), bg_color)
draw = ImageDraw.Draw(banner)

logo = Image.open("/Users/kc/websites/fplaunchpad.org/assets/images/logo-400.png").convert("RGBA")
logo_h = 100
ratio = logo_h / logo.size[1]
logo_w = int(logo.size[0] * ratio)
logo = logo.resize((logo_w, logo_h), Image.LANCZOS)

logo_x = (W - logo_w) // 2
logo_y = 120
banner.paste(logo, (logo_x, logo_y), logo)

title = "Applications Open"
subtitle = "Post-Baccalaureate Fellowship"
tagline = "FP Launchpad \u00b7 IIT Madras"

font_paths = [
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/SFNSDisplay.ttf",
    "/Library/Fonts/Arial.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
]

font_large = font_medium = font_small = None
for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_large = ImageFont.truetype(fp, 54)
            font_medium = ImageFont.truetype(fp, 36)
            font_small = ImageFont.truetype(fp, 24)
            break
        except Exception:
            continue

if font_large is None:
    font_large = ImageFont.load_default()
    font_medium = font_large
    font_small = font_large

title_bbox = draw.textbbox((0, 0), title, font=font_large)
title_w = title_bbox[2] - title_bbox[0]
draw.text(((W - title_w) // 2, 270), title, fill=text_color, font=font_large)

sub_bbox = draw.textbbox((0, 0), subtitle, font=font_medium)
sub_w = sub_bbox[2] - sub_bbox[0]
draw.text(((W - sub_w) // 2, 345), subtitle, fill=text_color, font=font_medium)

tag_bbox = draw.textbbox((0, 0), tagline, font=font_small)
tag_w = tag_bbox[2] - tag_bbox[0]
draw.text(((W - tag_w) // 2, 460), tagline, fill=subtitle_color, font=font_small)

out_path = "/Users/kc/websites/fplaunchpad.org/assets/images/fellowship-banner.png"
banner.save(out_path, "PNG")
print(f"Saved to {out_path}, size: {banner.size}")
