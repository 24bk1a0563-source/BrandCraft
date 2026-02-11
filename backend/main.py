from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests
import uuid
import random

# ------------------ API KEYS ------------------
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

# ------------------ APP ------------------
app = FastAPI(title="BrandCraft API")
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# ------------------ MODELS ------------------
class BrandInput(BaseModel):
    business_type: str
    product_category: str
    target_audience: str

class LogoInput(BaseModel):
    brand_name: str
    category: str

# ------------------ ROOT ------------------
@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return f.read()


# ------------------ BRAND NAME GENERATOR ------------------
@app.post("/generate-brand-names-local")
def generate_brand_names_local(data: BrandInput):
    category_data = {
        "food": {
            "prefixes": ["Eco", "Fresh", "Pure", "Tasty", "Green"],
            "suffixes": ["Bite", "Kitchen", "Foods", "Eats", "Plates"]
        },
        "fashion": {
            "prefixes": ["Urban", "Vogue", "Nova", "Luxe", "Style"],
            "suffixes": ["Wear", "Studio", "Mode", "Attire", "Label"]
        },
        "footwear": {
            "prefixes": ["Stride", "Flex", "Run", "Step", "Sole"],
            "suffixes": ["Shoes", "Foot", "Walk", "Gear", "Steps"]
        },
        "default": {
            "prefixes": ["Nova", "Prime", "Core", "Zen", "Peak"],
            "suffixes": ["Co", "Hub", "Lab", "Works"]
        }
    }

    category = (data.product_category or "default").lower()
    group = category_data.get(category, category_data["default"])

    names = set()
    while len(names) < 12:
        names.add(
            random.choice(group["prefixes"]) +
            random.choice(group["suffixes"])
        )

    return {"brand_names": list(names)}

# ------------------ HELPER: contrast text color ------------------
def hex_to_rgb(hex_color: str):
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = ''.join([c*2 for c in h])
    r = int(h[0:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)
    return r, g, b

def pick_contrast_color(hex_color: str):
    try:
        r, g, b = hex_to_rgb(hex_color)
    except Exception:
        return "#000000"
    # perceptive luminance
    luminance = (0.299*r + 0.587*g + 0.114*b) / 255
    return "#ffffff" if luminance < 0.5 else "#000000"

# ------------------ LOGO SVG GENERATOR ------------------

@app.post("/generate-logo-svg")
def generate_logo_svg(
    brand_name: str,
    primary_color: str,
    category: str = "default",
    style: str = "circle"
):
    # -------- NORMALIZE INPUTS --------
    style = style or "circle"
    category = (category or "default").lower()
    primary_color = primary_color or "#2E7D32"

    # -------- TYPOGRAPHY (CONSISTENT ACROSS DEVICES) --------
    typography = {
        "food": {
            "family": "sans-serif",
            "weight": "600",
            "spacing": "1px",
            "transform": "none"
        },
        "fashion": {
            "family": "serif",
            "weight": "500",
            "spacing": "2px",
            "transform": "uppercase"
        },
        "footwear": {
            "family": "sans-serif",
            "weight": "800",
            "spacing": "0.5px",
            "transform": "uppercase"
        },
        "default": {
            "family": "sans-serif",
            "weight": "500",
            "spacing": "1px",
            "transform": "none"
        }
    }

    typo = typography.get(category, typography["default"])

    # -------- SHAPE BASED ON STYLE (RELATIVE COORDS) --------
    if style == "circle":
        shape = f'<circle cx="40" cy="40" r="30" fill="{primary_color}" />'

    elif style == "square":
        shape = f'<rect x="10" y="10" width="60" height="60" fill="{primary_color}" />'

    elif style == "badge":
        shape = f'<rect x="5" y="20" width="70" height="40" rx="12" fill="{primary_color}" />'

    elif style == "diamond":
        shape = (
            f'<rect x="20" y="20" width="40" height="40" '
            f'transform="rotate(45 40 40)" fill="{primary_color}" />'
        )

    elif style == "line":
        shape = f'<line x1="0" y1="40" x2="80" y2="40" stroke="{primary_color}" stroke-width="6" />'

    else:
        shape = f'<circle cx="40" cy="40" r="30" fill="{primary_color}" />'

    # -------- SAFE BRAND NAME --------
    safe_name = (
        brand_name.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )

    # -------- TEXT COLOR (AUTO CONTRAST) --------
    def pick_text_color(hex_color: str):
        try:
            hex_color = hex_color.lstrip("#")
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            luminance = (0.299*r + 0.587*g + 0.114*b) / 255
            return "#ffffff" if luminance < 0.5 else "#000000"
        except Exception:
            return "#000000"

    text_color = pick_text_color(primary_color)

    # -------- SVG OUTPUT --------
    svg_logo = f"""
    <svg width="420" height="140" viewBox="0 0 420 140"
         xmlns="http://www.w3.org/2000/svg">
        <rect width="420" height="140" fill="white"/>

        <g transform="translate(30,30)">
            {shape}
        </g>

        <text x="160" y="85"
              font-size="34"
              font-family="{typo['family']}"
              font-weight="{typo['weight']}"
              letter-spacing="{typo['spacing']}"
              text-transform="{typo['transform']}"
              fill="{text_color}">
            {safe_name}
        </text>
    </svg>
    """

    return {
        "svg_logo": svg_logo.strip(),
        "style": style,
        "category": category
    }


# ------------------ COLOR PALETTE ------------------
@app.post("/generate-color-palette")
def generate_color_palette():
    palettes = [
        ["#2E7D32", "#A5D6A7", "#1B5E20"],  # Green / organic
        ["#6A1B9A", "#CE93D8", "#4A148C"],  # Premium purple
        ["#0277BD", "#81D4FA", "#01579B"],  # Trust blue
        ["#EF6C00", "#FFCC80", "#E65100"],  # Food orange
        ["#263238", "#B0BEC5", "#000000"]   # Minimal dark
    ]
    return {"colors": random.choice(palettes)}
