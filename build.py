#!/usr/bin/env python3
"""Generates the Heartbeat Quilting design mockups into docs/ for GitHub Pages."""
import json
import os
from html import escape as e

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")
ITEMS = json.load(open(os.path.join(ROOT, "items.json")))

PHONE = "(509) 465-0344"
TEL = "tel:+15094650344"

# Clearer display names, built from each product's own description on the live site.
def item(slug, title, sub, cover=False, **kw):
    it = ITEMS[slug]
    d = {"slug": slug, "title": title, "sub": sub, "price": it["price"],
         "img": "assets/img/" + it["file"], "cover": cover, "old": it["name"]}
    d.update(kw)
    return d

POPULAR = [
    item("hlby-96", "Hobbs Heirloom 80/20 Batting, Natural", '96 in × 30 yd roll', cover=True),
    item("pearl-3k", "Signature Solids Thread, Pearl", "3,000 yd cone"),
    item("so-fine-402", "So Fine Thread, 402", "Cone"),
    item("parchment-6k", "Signature Cotton Thread, Parchment", "6,000 yd cone"),
]
NEW = [
    item("118-rapture-blender-navy", "Rapture Blender Fabric, Navy", "118 in wide", cover=True),
    item("118-rapture-blender-cream", "Rapture Blender Fabric, Cream", "118 in wide", cover=True),
    item("batting-soft-bright-4oz-90in-x-25yds", "Soft & Bright Polyester Batting", "4 oz, 90 in × 25 yd"),
    item("dritz-quilting-heat-erase-pens-5ct", "Dritz Heat Erase Marking Pens", "Set of 5"),
]
T = [  # slug, color, family, swatch, yards
    ("pearl-3k", "Pearl", "gray", "#b9bdc0", 3000), ("parchment-6k", "Parchment", "neutral", "#e4d9bd", 6000),
    ("black-3k", "Black", "black", "#1d1d1f", 3000), ("white-6k", "White", "white", "#ffffff", 6000),
    ("ivory-3k", "Ivory", "neutral", "#efe8d6", 3000), ("parchment-3k", "Parchment", "neutral", "#e4d9bd", 3000),
    ("iced-blue-3k", "Iced Blue", "blue", "#b5d3e4", 3000), ("mustard-3k", "Mustard", "yellow", "#d2a22c", 3000),
    ("pine-3k", "Pine", "green", "#2f5d46", 3000), ("sand-dollar-3k", "Sand Dollar", "neutral", "#dccdb3", 3000),
    ("holiday-red-3k", "Holiday Red", "red", "#b3202c", 3000), ("latte-3k", "Latte", "brown", "#b89674", 3000),
    ("seascape-3k", "Seascape", "blue", "#5f8fa3", 3000), ("oyster-shell-3k", "Oyster Shell", "neutral", "#d9d2c4", 3000),
    ("baguette-3k", "Baguette", "brown", "#c79a5e", 3000), ("camel-3k", "Camel", "brown", "#b08a5a", 3000),
    ("lavender-3k", "Lavender", "purple", "#b6a4d0", 3000),
]
THREADS = [item(s, f"Signature Thread, {c}", f"{y:,} yd cone", color=c, family=f, swatch=h, yards=y)
           for s, c, f, h, y in T]
FAMILIES = [("white", "#ffffff"), ("neutral", "#e4d9bd"), ("brown", "#b08a5a"), ("yellow", "#d2a22c"),
            ("red", "#b3202c"), ("green", "#2f5d46"), ("blue", "#5f8fa3"), ("purple", "#b6a4d0"),
            ("gray", "#b9bdc0"), ("black", "#1d1d1f")]
SHELF = ["iced-blue-3k", "mustard-3k", "holiday-red-3k", "pine-3k", "lavender-3k", "latte-3k"]
PEARL = THREADS[0]
DEPARTMENTS = ["Batting", "Threads", "Fabric", "Parts & Supplies", "Design Aids", "Notions", "Pantographs", "Gifts", "Clearance"]
LEARN = [
    ("Renter Tips & Tutorials", "Get more from your time on a rental machine."),
    ("Product Knowledge", "Compare thread, batting and more before you buy."),
    ("Free Downloadable PDFs", "Trackers for thread, batting and your skills."),
    ("Machine Troubleshooting", "Work through a machine problem step by step."),
]
SERVICES = [
    ("Classes & Events", "Rental certification, classes and area events."),
    ("Longarm Rental", "Quilt on our machines at the shop."),
    ("Quilting Services", "Drop off your top and we’ll quilt it."),
    ("Longarm Machines", "See Gammill machines in person."),
]


def img(p, cls="", path=""):
    c = " ".join(x for x in [cls, "cover" if p.get("cover") else ""] if x)
    return f'<img src="{path}{e(p["img"])}" alt="{e(p["title"])}, {e(p["sub"])}" loading="lazy" class="{c}">'


def mock_link(text, cls=""):
    return f'<a href="#" data-mock class="{cls}">{e(text)}</a>'


def page(d, name, title, body, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="../assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{d['fonts']}&display=swap">
<link rel="stylesheet" href="../assets/base.css">
<link rel="stylesheet" href="style.css">
</head>
<body class="{name}">
<div class="mockbar"><span>Design mockup: {e(d['label'])}. This is not the live store.</span> <a href="../index.html">Compare all three</a></div>
{body}
<div class="toast" role="status" aria-live="polite"></div>
<script src="../assets/mock.js"></script>
</body>
</html>
"""


def filters_html():
    fam = "".join(
        f'<label class="chip"><input type="checkbox" name="family" value="{f}"><span class="dot" style="background:{h}"></span>{f.capitalize()}</label>'
        for f, h in FAMILIES)
    return f"""<form class="filters" aria-label="Filter threads">
  <fieldset><legend>Color</legend><div class="chips">{fam}</div></fieldset>
  <fieldset><legend>Cone size</legend><div class="chips">
    <label class="chip"><input type="checkbox" name="yards" value="3000">3,000 yd</label>
    <label class="chip"><input type="checkbox" name="yards" value="6000">6,000 yd</label>
  </div></fieldset>
  <button type="reset" class="clear">Clear filters</button>
</form>"""


def data_attrs(p):
    return f'data-family="{p["family"]}" data-yards="{p["yards"]}" data-price="{p["price"].strip("$")}" data-name="{e(p["color"])}"'


def sort_html():
    return """<label class="sort">Sort by <select data-sort>
<option value="best">Best selling</option><option value="name">Color name</option>
<option value="low">Price: low to high</option><option value="high">Price: high to low</option></select></label>"""


def specs_html():
    rows = [("Brand", "Signature"), ("Line", "Signature Solids"), ("Color", "Pearl"), ("Color number", "042"),
            ("Put-up", "3,000 yd cone"), ("SKU", "042 Art. 47")]
    r = "".join(f"<tr><th scope=\"row\">{a}</th><td>{b}</td></tr>" for a, b in rows)
    return f'<table class="specs"><caption>Details</caption>{r}</table>'


TODO = '<p class="todo"><strong>Store to add:</strong> fiber, thread weight and recommended needle, so shoppers can buy without calling.</p>'


def colorway(limit=9):
    out = ""
    for p in THREADS[1:limit]:
        if p["yards"] != 3000:
            continue
        out += f'<a href="#" data-mock class="way"><span class="dot" style="background:{p["swatch"]}"></span>{e(p["color"])}</a>'
    return out


# ------------------------------------------------------------------ Direction 1
def d1_header():
    nav = "".join(f'<li><a href="threads.html">{x}</a></li>' if x == "Threads" else f"<li>{mock_link(x)}</li>" for x in DEPARTMENTS[:6])
    return f"""<header class="site">
  <div class="top wrap">
    <a href="index.html" class="logo"><img src="../assets/img/logo.webp" alt="Heartbeat Quilting home" width="170" height="68"></a>
    <form class="search" role="search" data-mockform><label class="sr" for="q">Search products</label><input id="q" type="search" placeholder="Search thread, batting, rulers…"><button>Search</button></form>
    <div class="util"><a href="{TEL}">{PHONE}</a>{mock_link("Sign in")}{mock_link("Cart")}</div>
    <button class="menu" aria-expanded="false" aria-controls="nav">Menu</button>
  </div>
  <nav id="nav" class="wrap" aria-label="Main"><ul>{nav}<li class="sep">{mock_link("Classes & Events")}</li><li>{mock_link("Services")}</li><li>{mock_link("Renters")}</li><li>{mock_link("Resources")}</li></ul></nav>
</header>"""


def d1_footer():
    return f"""<footer class="site"><div class="wrap cols">
  <div><img src="../assets/img/logo.webp" alt="Heartbeat Quilting" width="150" height="60"><p>16909 E. Sprague Ave.<br>Spokane Valley, WA 99037</p><p><a href="{TEL}">{PHONE}</a><br><a href="mailto:info@heartbeatquilting.com">info@heartbeatquilting.com</a></p></div>
  <div><h2>Shop</h2><ul><li><a href="threads.html">Threads</a></li><li>{mock_link("Batting")}</li><li>{mock_link("Fabric")}</li><li>{mock_link("Clearance")}</li></ul></div>
  <div><h2>Learn</h2><ul><li>{mock_link("Classes & Events")}</li><li>{mock_link("Tutorials & Resources")}</li><li>{mock_link("Longarm Rental")}</li><li>{mock_link("About Us")}</li></ul></div>
  <div><h2>Help</h2><ul><li>{mock_link("Shipping & Returns")}</li><li>{mock_link("Store Hours")}</li><li>{mock_link("Driving Directions")}</li><li>{mock_link("Contact Us")}</li></ul></div>
</div><div class="wrap legal"><span>© 2026 Heartbeat Quilting</span><img src="../assets/img/gammill-logo.png" alt="Gammill" width="96" height="34"></div></footer>"""


def d1_card(p, href="#"):
    extra = 'data-mock' if href == "#" else ""
    return f'<article class="card"><a href="{href}" {extra}><div class="pic">{img(p, path="../")}</div><h3>{e(p["title"])}</h3><p class="sub">{e(p["sub"])}</p><p class="price">{p["price"]}</p></a></article>'


def d1_home():
    shelf = "".join(f'<img src="../assets/img/{ITEMS[s]["file"]}" alt="" style="--i:{i}">' for i, s in enumerate(SHELF))
    depts = "".join(f'<li><a href="{"threads.html" if x == "Threads" else "#"}" {"" if x == "Threads" else "data-mock"}>{x}</a></li>' for x in DEPARTMENTS)
    learn = "".join(f'<li>{mock_link(a)}<p>{b}</p></li>' for a, b in LEARN)
    svc = "".join(f'<li>{mock_link(a)}<p>{b}</p></li>' for a, b in SERVICES)
    return d1_header() + f"""<main>
<section class="hero"><div class="wrap">
  <div class="copy"><h1>Everything your longarm needs, from people who quilt.</h1>
  <p>Thread, batting, fabric and notions, shipped from our shop in Spokane Valley.</p>
  <p class="cta"><a class="btn" href="threads.html">Shop threads</a> <a class="link" href="{TEL}">Prefer to order by phone? {PHONE}</a></p></div>
  <div class="shelf" aria-hidden="true">{shelf}</div>
</div></section>
<div class="stitch" aria-hidden="true"></div>
<section class="wrap depts"><h2>Shop by department</h2><ul>{depts}</ul></section>
<section class="wrap"><h2>Most popular</h2><div class="grid">{''.join(d1_card(p, 'product.html' if p['slug']=='pearl-3k' else '#') for p in POPULAR)}</div></section>
<section class="band"><div class="wrap two"><div><h2>Learn with us</h2><ul class="list">{learn}</ul></div><div><h2>Visit the shop</h2><ul class="list">{svc}</ul></div></div></section>
<section class="wrap"><h2>New arrivals</h2><div class="grid">{''.join(d1_card(p) for p in NEW)}</div></section>
</main>""" + d1_footer()


def d1_category():
    cards = "".join(f'<article class="card" {data_attrs(p)}><a href="{"product.html" if p["slug"]=="pearl-3k" else "#"}" {"" if p["slug"]=="pearl-3k" else "data-mock"}><div class="pic">{img(p, path="../")}</div><h3>{e(p["color"])}</h3><p class="sub">{e(p["sub"])}</p><p class="price">{p["price"]}</p></a></article>' for p in THREADS)
    return d1_header() + f"""<main class="wrap cat">
<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / <span>Threads</span></nav>
<h1>Machine quilting threads</h1>
<p class="lead">Find the right color and cone size. Want to save time winding bobbins? {mock_link("See prewound bobbins")}.</p>
<div class="catgrid"><aside>{filters_html()}</aside>
<div><div class="tools"><p class="count" data-count></p>{sort_html()}</div><div class="grid three" data-results>{cards}</div></div></div>
</main>""" + d1_footer()


def d1_product():
    return d1_header() + f"""<main class="wrap prod">
<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / <a href="threads.html">Threads</a> / <span>Pearl</span></nav>
<div class="pgrid"><div class="gallery">{img(PEARL, path="../")}</div>
<div class="buy"><h1>{e(PEARL['title'])}</h1><p class="sub">Signature Solids, color 042, 3,000 yd cone</p><p class="price big">{PEARL['price']}</p>
<form data-mockform class="add"><label>Quantity <input type="number" value="1" min="1"></label><button class="btn">Add to cart</button></form>
<p class="help">Not sure it’s the right match? Call <a href="{TEL}">{PHONE}</a>.</p>
<h2>More colors</h2><div class="ways">{colorway()}</div>
{specs_html()}{TODO}
<p class="reviews">{mock_link("Be the first to review this thread")}</p></div></div>
</main>""" + d1_footer()


# ------------------------------------------------------------------ Direction 2
def d2_header():
    dept = "".join(f'<li><a href="threads.html">{x}</a></li>' if x == "Threads" else f"<li>{mock_link(x)}</li>" for x in DEPARTMENTS)
    return f"""<header class="site">
  <div class="utility"><div class="wrap"><span>Questions or phone orders: <a href="{TEL}">{PHONE}</a></span><span class="right">{mock_link("Classes & Events")}{mock_link("Renters")}{mock_link("Resources")}{mock_link("Sign in")}</span></div></div>
  <div class="main wrap">
    <a href="index.html" class="logo"><img src="../assets/img/logo.webp" alt="Heartbeat Quilting home" width="140" height="56"></a>
    <form class="search" role="search" data-mockform><label class="sr" for="q">Search by name, brand or SKU</label><input id="q" type="search" placeholder="Search by name, brand or SKU"><button>Search</button></form>
    <a href="#" data-mock class="cart">Cart</a>
    <button class="menu" aria-expanded="false" aria-controls="nav">Departments</button>
  </div>
  <nav id="nav" aria-label="Departments"><ul class="wrap">{dept}</ul></nav>
</header>"""


def d2_footer():
    return f"""<footer class="site"><div class="wrap row"><p><strong>Heartbeat Quilting</strong><br>16909 E. Sprague Ave., Spokane Valley, WA 99037<br><a href="{TEL}">{PHONE}</a> · <a href="mailto:info@heartbeatquilting.com">info@heartbeatquilting.com</a></p>
<ul>{''.join(f'<li>{mock_link(x)}</li>' for x in ["Shipping & Returns","Store Hours","Driving Directions","Contact Us","About Us"])}</ul>
<img src="../assets/img/gammill-logo.png" alt="Gammill" width="96" height="34"></div><p class="wrap legal">© 2026 Heartbeat Quilting</p></footer>"""


def d2_row(p, href="#"):
    extra = 'data-mock' if href == "#" else ""
    name = p.get("color", p["title"])
    attrs = data_attrs(p) if "family" in p else ""
    return f'<li class="row" {attrs}><a class="thumb" href="{href}" {extra} tabindex="-1" aria-hidden="true">{img(p, path="../")}</a><div class="info"><a href="{href}" {extra}>{e(p["title"])}</a><span>{e(p["sub"])}</span></div><span class="price">{p["price"]}</span><form data-mockform class="qa"><label class="sr">Quantity for {e(name)}<input type="number" value="1" min="1"></label><button>Add</button></form></li>'


def d2_home():
    reorder = "".join(d2_row(p, "product.html" if p["slug"] == "pearl-3k" else "#") for p in POPULAR)
    newi = "".join(d2_row(p) for p in NEW)
    tiles = [("Batting", "hlby-96", True), ("Threads", "iced-blue-3k", False), ("Fabric", "118-rapture-blender-navy", True), ("Notions", "dritz-quilting-heat-erase-pens-5ct", False)]
    t = "".join(f'<a class="tile" href="{"threads.html" if a=="Threads" else "#"}" {"" if a=="Threads" else "data-mock"}><img src="../assets/img/{ITEMS[s]["file"]}" alt="" class="{"cover" if c else ""}"><span>{a}</span></a>' for a, s, c in tiles)
    links = "".join(f'<li>{mock_link(a)}<span>{b}</span></li>' for a, b in LEARN + SERVICES[:2])
    return d2_header() + f"""<main class="wrap">
<section class="intro"><div><h1>Longarm supplies, ready to reorder.</h1><p>Thread, batting and parts for working quilters. Order online or call the shop.</p></div><div class="tiles">{t}</div></section>
<div class="cols"><section><h2>Most popular</h2><ul class="rows">{reorder}</ul><h2>New arrivals</h2><ul class="rows">{newi}</ul></section>
<aside><h2>Help and how-to</h2><ul class="side">{links}</ul></aside></div>
</main>""" + d2_footer()


def d2_category():
    rows = "".join(d2_row(p, "product.html" if p["slug"] == "pearl-3k" else "#") for p in THREADS)
    return d2_header() + f"""<main class="wrap cat">
<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> › <span>Threads</span></nav>
<div class="head"><h1>Threads</h1><div class="tools"><p class="count" data-count></p>{sort_html()}</div></div>
{filters_html()}
<ul class="rows" data-results>{rows}</ul>
</main>""" + d2_footer()


def d2_product():
    return d2_header() + f"""<main class="wrap prod">
<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> › <a href="threads.html">Threads</a> › <span>Pearl</span></nav>
<div class="pgrid"><div class="gallery">{img(PEARL, path="../")}</div>
<div class="detail"><h1>{e(PEARL['title'])}</h1><p class="sub">SKU 042 Art. 47 · 3,000 yd cone</p>{specs_html()}{TODO}<h2>Other colors</h2><div class="ways">{colorway()}</div></div>
<aside class="box"><p class="price big">{PEARL['price']}</p><form data-mockform class="add"><label>Quantity <input type="number" value="1" min="1"></label><button class="btn">Add to cart</button></form><p class="help">Questions? <a href="{TEL}">{PHONE}</a></p><p>{mock_link("Add to wish list")}</p><p>{mock_link("Write the first review")}</p></aside></div>
</main>""" + d2_footer()


# ------------------------------------------------------------------ Direction 3
def d3_header():
    return f"""<header class="site"><div class="wrap bar">
  <a href="index.html" class="logo"><img src="../assets/img/logo.webp" alt="Heartbeat Quilting home" width="150" height="60"></a>
  <button class="menu" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav id="nav" aria-label="Main"><ul><li><a href="threads.html">Shop</a></li><li>{mock_link("Classes & Events")}</li><li>{mock_link("Services")}</li><li>{mock_link("Renters")}</li><li>{mock_link("Resources")}</li><li>{mock_link("About")}</li></ul></nav>
  <div class="util">{mock_link("Search")}{mock_link("Sign in")}{mock_link("Cart")}</div>
</div></header>"""


def d3_footer():
    return f"""<footer class="site"><div class="stitch" aria-hidden="true"></div><div class="wrap cols">
  <div><p class="big"><a href="{TEL}">{PHONE}</a></p><p>16909 E. Sprague Ave.<br>Spokane Valley, WA 99037</p><p><a href="mailto:info@heartbeatquilting.com">info@heartbeatquilting.com</a></p></div>
  <ul>{''.join(f'<li>{mock_link(x)}</li>' for x in ["Shop Products","Classes & Events","Quilting Services","Longarm Rental"])}</ul>
  <ul>{''.join(f'<li>{mock_link(x)}</li>' for x in ["Shipping & Returns","Store Hours","Driving Directions","About Us"])}</ul>
  <div class="mark"><img src="../assets/img/gammill-logo.png" alt="Gammill" width="110" height="39"></div>
</div><p class="wrap legal">© 2026 Heartbeat Quilting</p></footer>"""


def d3_card(p, href="#", attrs="", name=None):
    extra = 'data-mock' if href == "#" else ""
    return f'<article class="card" {attrs}><a href="{href}" {extra}><div class="pic">{img(p, path="../")}</div><div class="meta"><h3>{e(name or p["title"])}</h3><p class="sub">{e(p["sub"])}</p><p class="price">{p["price"]}</p></div></a></article>'


def d3_home():
    fan = "".join(f'<img src="../assets/img/{ITEMS[s]["file"]}" alt="" style="--i:{i}">' for i, s in enumerate(SHELF[:5]))
    worlds = [("Shop supplies", "Thread, batting, fabric, notions and pantographs.", "threads.html"),
              ("Take a class", "Rental certification, classes and area events.", "#"),
              ("Rent a longarm", "Quilt your own top on our machines.", "#"),
              ("Have it quilted", "Drop off your quilt and leave it to us.", "#")]
    w = "".join(f'<a class="world" href="{h}" {"" if h!="#" else "data-mock"}><span class="n">0{i+1}</span><h3>{a}</h3><p>{b}</p></a>' for i, (a, b, h) in enumerate(worlds))
    learn = "".join(f'<li>{mock_link(a)}<p>{b}</p></li>' for a, b in LEARN)
    return d3_header() + f"""<main>
<section class="hero"><div class="wrap"><div class="copy"><h1>Your longarm home, online and in Spokane Valley.</h1><p>Supplies, classes, rentals and quilting services, all in one shop.</p><p><a class="btn" href="threads.html">Shop supplies</a></p></div><div class="fan" aria-hidden="true">{fan}</div></div><div class="stitch" aria-hidden="true"></div></section>
<section class="wrap worlds">{w}</section>
<section class="wrap"><h2>Most popular</h2><div class="grid">{''.join(d3_card(p, 'product.html' if p['slug']=='pearl-3k' else '#') for p in POPULAR)}</div></section>
<section class="learn"><div class="wrap"><h2>Stuck? Start here.</h2><ul>{learn}</ul></div></section>
<section class="wrap"><h2>Just arrived</h2><div class="grid">{''.join(d3_card(p) for p in NEW)}</div></section>
</main>""" + d3_footer()


def d3_category():
    cards = "".join(d3_card(p, "product.html" if p["slug"] == "pearl-3k" else "#", data_attrs(p), p["color"]) for p in THREADS)
    return d3_header() + f"""<main class="wrap cat">
<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / <span>Threads</span></nav>
<h1>Threads</h1>{filters_html()}
<div class="tools"><p class="count" data-count></p>{sort_html()}</div>
<div class="grid" data-results>{cards}</div>
</main>""" + d3_footer()


def d3_product():
    return d3_header() + f"""<main class="wrap prod">
<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> / <a href="threads.html">Threads</a> / <span>Pearl</span></nav>
<div class="pgrid"><div class="gallery">{img(PEARL, path="../")}</div>
<div class="buy"><h1>{e(PEARL['title'])}</h1><p class="sub">Signature Solids, color 042, 3,000 yd cone</p><p class="price big">{PEARL['price']}</p>
<form data-mockform class="add"><label>Quantity <input type="number" value="1" min="1"></label><button class="btn">Add to cart</button></form>
<h2>More colors</h2><div class="ways">{colorway()}</div>{specs_html()}{TODO}
<p class="help">Need a color match? Call <a href="{TEL}">{PHONE}</a>.</p><p>{mock_link("Be the first to review this thread")}</p></div></div>
</main>""" + d3_footer()


DIRS = [
    {"dir": "sunroom", "label": "Sunroom", "home": d1_home, "cat": d1_category, "prod": d1_product,
     "fonts": "family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Nunito+Sans:wght@400;600;700"},
    {"dir": "supply-counter", "label": "Supply Counter", "home": d2_home, "cat": d2_category, "prod": d2_product,
     "fonts": "family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Source+Sans+3:wght@400;600;700"},
    {"dir": "night-stitch", "label": "Night Stitch", "home": d3_home, "cat": d3_category, "prod": d3_product,
     "fonts": "family=DM+Serif+Display&family=Figtree:wght@400;500;600;700"},
]

FIXES = [
    ("“Under construction” notices", "Removed. The first screen now says what you sell and how to order."),
    ("Text baked into a banner image", "Replaced with real text that reads well on any screen."),
    ("No products or purpose on the first screen", "The first screen now shows what you sell."),
    ("Two rows of mismatched red buttons", "Replaced with clear sections for shopping, learning and services."),
    ("Very large header pushing everything down", "Compact header with search always visible."),
    ("Light pink and gray text that is hard to read", "All text meets standard contrast levels."),
    ("Low-contrast footer text and a stray “WWW”", "Rebuilt, readable footer with contact details and help links."),
    ("Product photos at different sizes", "Every product photo sits in a matching frame."),
    ("No way to narrow six pages of thread", "Working color and cone size filters, plus sorting."),
    ("Codes like HLBY-96 and Pearl 3K", "Clear names, written from your own product descriptions."),
    ("Thin product pages", "Details table, color choices, and help by phone."),
    ("Outdated Twitter icon, gray empty stars, long breadcrumbs", "Removed or shortened."),
    ("Blank main heading, missing image descriptions", "Every page has a heading, and images are described."),
    ("Resources buried", "Tutorials, PDFs, troubleshooting and services are brought forward."),
]


def landing():
    cards = ""
    info = {
        "sunroom": ("Warm, light and fabric-forward. Thread colors do the work, and it feels like walking into the shop.", ["#fbf6ec", "#b92b4d", "#f3c84b", "#2c2a33"]),
        "supply-counter": ("Clean, fast and practical. Search first, with dense lists and quick add for quilters who know what they need.", ["#ffffff", "#17324d", "#c22a4c", "#eef2f6"]),
        "night-stitch": ("The boldest change: a dark, boutique feel in deep aubergine, with the logo’s yellow and products on cream tiles.", ["#231a2b", "#f6c944", "#f7f0e2", "#e2577a"]),
    }
    for d in DIRS:
        k = d["dir"]
        sw = "".join(f'<span style="background:{c}"></span>' for c in info[k][1])
        cards += f"""<article class="dir"><a class="shot" href="{k}/index.html"><img src="assets/shots/{k}.jpg" alt="{d['label']} homepage preview" loading="lazy"></a>
<h2>{d['label']}</h2><div class="sw" aria-hidden="true">{sw}</div><p>{info[k][0]}</p>
<ul><li><a href="{k}/index.html">Homepage</a></li><li><a href="{k}/threads.html">Thread category</a></li><li><a href="{k}/product.html">Product page</a></li></ul></article>"""
    fx = "".join(f"<tr><th scope=\"row\">{a}</th><td>{b}</td></tr>" for a, b in FIXES)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Heartbeat Quilting design mockups</title>
<link rel="icon" href="assets/img/favicon.png"><link rel="stylesheet" href="assets/landing.css"></head>
<body><main>
<header><img src="assets/img/logo.webp" alt="Heartbeat Quilting" width="170" height="68"><h1>Three design directions for the website</h1>
<p>Each one shows the homepage, a category page and a product page, using real products and prices. Links to other pages and the cart aren’t connected, but the thread filters and sorting work. Try them on your phone too.</p></header>
<section class="dirs">{cards}</section>
<section><h2>What all three fix</h2><table>{fx}</table></section>
<section><h2>Things to check while you look</h2><ul class="notes">
<li><strong>Headlines and clearer product names are drafts.</strong> Please correct anything that doesn’t sound like the shop.</li>
<li><strong>Thread color groups are a first pass,</strong> based on color names. The real site would need them set for each product.</li>
<li><strong>The homepage assumes everything can be ordered online.</strong> Tell us if some items are still phone-only.</li>
<li><strong>You can mix and match.</strong> For example, one direction’s colors with another’s category page.</li>
</ul></section>
</main></body></html>"""


def main():
    for d in DIRS:
        out = os.path.join(DOCS, d["dir"])
        os.makedirs(out, exist_ok=True)
        desc = "Longarm machine quilting supplies, services, rental and sales in Spokane Valley, WA."
        for fn, key, title in [("index.html", "home", "Longarm Quilting Supplies | Heartbeat Quilting"),
                               ("threads.html", "cat", "Machine Quilting Threads | Heartbeat Quilting"),
                               ("product.html", "prod", "Signature Solids Thread, Pearl | Heartbeat Quilting")]:
            open(os.path.join(out, fn), "w").write(page(d, key, title, d[key](), desc))
    open(os.path.join(DOCS, "index.html"), "w").write(landing())
    open(os.path.join(DOCS, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
    open(os.path.join(DOCS, ".nojekyll"), "w").write("")


if __name__ == "__main__":
    main()
