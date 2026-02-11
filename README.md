# 🚀 BrandCraft – AI-Powered Branding Automation Platform

BrandCraft is a **Generative AI–powered branding automation system** designed to help **small product-based businesses** (food, fashion, footwear, etc.) create a **complete brand identity** in minutes — without design skills.

It automates **brand naming, logo creation, color palette generation, and visual identity design** through an integrated AI-driven workflow.

---

## 🌟 Why BrandCraft?

Many startups and creators struggle with:
- Choosing a unique brand name
- Designing logos without design experience
- Creating a consistent brand identity
- High cost of branding agencies

**BrandCraft solves this problem** by providing an **all-in-one AI branding assistant** that generates professional branding assets instantly.

---

## 🧠 Key Features

### ✅ 1. Smart Brand Name Generator
- Category-aware brand name generation
- Supports food, fashion, footwear, and general businesses
- Generates multiple unique, brand-ready names

### ✅ 2. AI Logo Generator (SVG-Based)
- Generates **multiple logo styles**:
  - Circle
  - Square
  - Badge
  - Diamond
  - Line
- Logos are **scalable SVGs**
- Typography adapts based on business category

### ✅ 3. Industry-Specific Typography
- Food → friendly & approachable styles
- Fashion → elegant & premium styles
- Footwear → bold & strong styles
- Works consistently across all devices

### ✅ 4. Color Palette Generator
- Automatically generates professional color palettes
- Ensures visual consistency for branding
- Suitable for packaging, websites, and marketing

### ✅ 5. Interactive Branding Workflow
- Generate → Select brand → Explore logo styles
- Real-time preview
- User-friendly, modern UI

### ✅ 6. Clean, Modern SaaS-Style UI
- Inspired by modern startup products
- Minimal, premium, and judge-friendly design
- Clear sections: Hero, Generator, Features, About

---

## 🏗️ Tech Stack

### 🔹 Backend
- **FastAPI** – API framework
- **Python**
- SVG-based logo generation logic

### 🔹 Frontend
- **HTML5**
- **CSS3 (modern UI styling)**
- **Vanilla JavaScript**
- Responsive & interactive UI

### 🔹 AI & Logic
- Rule-based brand name generation
- Category-aware typography logic
- SVG vector logo system (no paid APIs)

---

## 🖼️ Screenshots

> 📌 Add screenshots here after running the app

### 🧩 Homepage & Brand Generator
![BrandCraft Home](screenshots/home.png)

### 🎨 Generated Brand Names & Colors
![Brand Names](screenshots/brand-names.png)

### 🖌️ Logo Variations
![Logos](screenshots/logos.png)

---

## ⚙️ How It Works (Workflow)

1. User enters business details
2. AI generates multiple brand names
3. User selects a brand name
4. System generates:
   - Color palette
   - Logo styles
   - Category-based typography
5. User previews a complete brand identity

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/24bk1a0563-source/BrandCraft.git
cd BrandCraft

2️⃣ Install Dependencies
pip install -r requirements.txt


3️⃣ Run the Server
python -m uvicorn main:app --reload

4️⃣ Open in Browser
http://127.0.0.1:8000


🧪 API Endpoints
| Endpoint                      | Method | Description            |
| ----------------------------- | ------ | ---------------------- |
| `/generate-brand-names-local` | POST   | Generate brand names   |
| `/generate-color-palette`     | POST   | Generate color palette |
| `/generate-logo-svg`          | POST   | Generate logo SVG      |


🎯 Uniqueness & Innovation

No dependency on paid AI APIs

Fully offline & hackathon-friendly

SVG-based logo engine (lightweight & scalable)

Category-aware branding logic

End-to-end branding automation in one platform

🌍 Use Cases

Small businesses

Startups

Content creators

Student entrepreneurs

Hackathon demos


👤 Author

CompileX Team
Built as part of a hackathon project

📜 License

This project is for educational and hackathon use.
