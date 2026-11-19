"""
HappyMax main hub site — page generator.

All text, phone numbers, emails and links live in this file. Run

    py build.py

and it rewrites index.html plus one folder per service
(auto-detailing/, yachts/, home-cleaning/, business-cleaning/, tv-mounting/).
Do not edit the generated .html files by hand — the next build overwrites them.

Legal (Hawaii HRS §444-9.2): never write "Licensed" / "Licensed & Insured"
anywhere. No fake reviews, ratings or customer counts. TV mounting stays
inside the handyman exemption — no electrical or plumbing work.
"""

from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSET_VERSION = "20261119"   # bump when assets/css/style.css changes
YEAR = date.today().year

# ───────────────────────── contacts ─────────────────────────
CONTACTS = {
    "main": {
        "tel": "+18082011311",
        "display": "(808) 201-1311",
        "email": "happymaxhandyman@gmail.com",
        "label": "TV mounting, home &amp; business cleaning",
    },
    "detailing": {
        "tel": "+18084520002",
        "display": "(808) 452-0002",
        "email": "happymaxautodetailing@gmail.com",
        "label": "Auto &amp; yacht detailing",
    },
}

# ───────────────────────── icons (24×24 line) ─────────────────────────
ICONS = {
    "car": '<path d="M3 13l1.8-4.6A2 2 0 0 1 6.7 7h10.6a2 2 0 0 1 1.9 1.4L21 13v4a1 1 0 0 1-1 1h-1.5M3 13v4a1 1 0 0 0 1 1h1.5M3 13h18M9.5 18h5"/><circle cx="7.5" cy="18" r="2"/><circle cx="16.5" cy="18" r="2"/>',
    "boat": '<path d="M12 3v12"/><path d="M12 4.5l6 9.5h-6"/><path d="M12 7l-4.5 7H12"/><path d="M3 16.5h18l-2.4 3.5H5.4z"/>',
    "home": '<path d="M3 11l9-7 9 7"/><path d="M5 9.5V20h14V9.5"/><path d="M12 11.5l1 2.1 2.1 1-2.1 1-1 2.1-1-2.1-2.1-1 2.1-1z"/>',
    "building": '<rect x="4" y="3" width="11" height="18" rx="1"/><path d="M15 9h4a1 1 0 0 1 1 1v11h-5M7.5 7h1M11 7h1M7.5 11h1M11 11h1M7.5 15h1M11 15h1M8.5 21v-3h2v3"/>',
    "tv": '<rect x="2.5" y="4" width="19" height="12.5" rx="1.5"/><path d="M8 20.5h8M12 16.5v4"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9.5h8M8 12.5h5"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 7l8.5 6 8.5-6"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "external": '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "pin": '<path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    "tag": '<path d="M3 12V4a1 1 0 0 1 1-1h8l9 9-9 9z"/><circle cx="8" cy="8" r="1.6"/>',
    "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/>',
}


def icon(name, cls="i"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


# ───────────────────────── services (tab order) ─────────────────────────
# site: the service's own full website (None = not built yet; the page then
# leads with call / text instead of a "visit site" button).
SERVICES = [
    {
        "slug": "auto-detailing",
        "card_link": "Explore auto detailing",
        "tab": "Auto Detailing",
        "icon": "car",
        "contact": "detailing",
        "site": "https://happymaxautodetailing.com/",
        "site_label": "happymaxautodetailing.com",
        "site_cta": "See packages &amp; book",
        "site_blurb": "Packages, prices and online booking live on our dedicated detailing site.",
        "title": "Mobile Auto Detailing on Oʻahu — HappyMax",
        "description": "Mobile auto detailing anywhere on Oʻahu: hand wash, interior deep clean, paint correction, ceramic coating and headlight restoration at your home or office.",
        "tile_sub": "Cars, trucks &amp; SUVs",
        "card_h3": "Mobile detailing for cars, trucks &amp; SUVs",
        "card_desc": "Showroom shine without leaving your driveway — we bring the detail to your home or office.",
        "points": ["Hand wash &amp; interior deep clean", "Paint correction &amp; ceramic coating", "Built for salt air, sun &amp; red dirt"],
        "eyebrow": "Auto Detailing",
        "h1": "Mobile auto detailing, right in your driveway.",
        "lede": "Hand wash, interior deep clean, paint correction and ceramic coating — done at your home or office anywhere on Oʻahu. Built for island salt, sun and red dirt.",
        "what_h2": "Everything your car needs, nothing it doesn’t.",
        "items": [
            ("Hand Wash &amp; Seal", "A careful hand wash of paint, glass, wheels and tires, finished with a protective sealant."),
            ("Interior Deep Clean", "Seats, carpets and mats vacuumed and shampooed; dash, console, vents and glass wiped down."),
            ("Paint Correction", "Machine polishing that takes out swirls, light scratches and oxidation to bring back depth and gloss."),
            ("Ceramic Coating", "Long-lasting protection against UV, salt air and water spots — easier washes and a deeper shine."),
            ("Headlight Restoration", "Cloudy, yellowed lenses polished clear and sealed, so you see — and are seen — at night."),
            ("Salt &amp; Sand Detox", "The beach-day aftermath gone: sand out of the carpets, salt film off the paint and wheels."),
        ],
        "steps": [
            ("Pick a package", "Choose one online or call us — tell us about your car and where it’s parked."),
            ("We confirm by text", "We’ll confirm the day and time that work for you."),
            ("We come to you", "We pull up at your home or office and get to work while you get on with your day."),
        ],
        "faqs": [
            ("Do you come to me?", "Yes. Our detailing is fully mobile — we come to your home or office anywhere on Oʻahu."),
            ("Where can I see packages and prices?", 'On our dedicated detailing site, <a href="https://happymaxautodetailing.com/" target="_blank" rel="noopener">happymaxautodetailing.com</a> — pick a package and request a time in about a minute. Prefer to talk? Call or text (808) 452-0002.'),
            ("How long does a detail take?", "It depends on the package and the car — from about an hour and a half for a quick shine to a day or two for ceramic coating."),
        ],
        "note": None,
    },
    {
        "slug": "yachts",
        "card_link": "Explore yacht detailing",
        "tab": "Yachts",
        "icon": "boat",
        "contact": "detailing",
        "site": None,
        "title": "Yacht &amp; Boat Detailing on Oʻahu — HappyMax",
        "description": "Yacht and boat detailing on Oʻahu: wash-downs, gelcoat oxidation removal, polish and wax, teak care and interior cleaning — at the harbor or on the trailer.",
        "tile_sub": "Sail &amp; power boats",
        "card_h3": "Detailing for sailboats, powerboats &amp; yachts",
        "card_desc": "Salt never sleeps. We keep your boat clean, protected and ready for the water.",
        "points": ["Wash-downs &amp; interior cleaning", "Gelcoat polish, wax &amp; teak care", "At the harbor or on the trailer"],
        "eyebrow": "Yacht &amp; Boat Detailing",
        "h1": "Yacht and boat detailing that keeps up with the Pacific.",
        "lede": "Wash-downs, gelcoat polishing, wax, teak and interior cleaning for sailboats, powerboats and yachts — at the harbor or on the trailer, anywhere on Oʻahu.",
        "what_h2": "Clean, protected and ready to cast off.",
        "items": [
            ("Wash-Down", "A fresh-water wash of topsides, deck, hardware and glass to clear salt before it builds up."),
            ("Gelcoat Polish &amp; Oxidation Removal", "Chalky, faded gelcoat compounded and polished back to color and gloss."),
            ("Wax &amp; Sealant", "A protective layer against UV and salt that holds the shine longer and makes washing easier."),
            ("Teak Care", "Gentle cleaning and brightening of teak decks and trim, with sealing on request."),
            ("Interior &amp; Cabin Cleaning", "Cabins, galley, heads, upholstery and windows cleaned top to bottom."),
            ("Stainless, Vinyl &amp; Canvas", "Rails, cleats and fittings polished; vinyl, canvas and clear panels cleaned."),
        ],
        "steps": [
            ("Tell us about your boat", "Length, type, where she’s kept and what needs attention. Photos help a lot."),
            ("Get a quote", "We’ll give you a price and suggest a plan — a one-time detail or regular wash-downs."),
            ("We come to the boat", "We work at the harbor or on the trailer, so you don’t lose a day on the water."),
        ],
        "faqs": [
            ("What kinds of boats do you detail?", "Sailboats, center consoles, powerboats and yachts. If it floats and needs cleaning, ask us."),
            ("Can you work at my harbor?", "In most cases, yes. Some harbors have their own rules for outside vendors — tell us where the boat is kept and we’ll confirm before booking."),
            ("Do you offer regular wash-downs?", "Yes. Besides one-time details, we can set up a recurring schedule so salt never gets the chance to build up."),
            ("How do I get a quote?", "Call or text (808) 452-0002 with your boat’s length, type and location. A few photos help us price it accurately."),
        ],
        "note": None,
    },
    {
        "slug": "home-cleaning",
        "card_link": "Explore home cleaning",
        "tab": "For Home",
        "icon": "home",
        "contact": "main",
        "site": None,
        "title": "Home Deep Cleaning on Oʻahu — HappyMax",
        "description": "Deep cleaning for houses, condos and apartments on Oʻahu: top-to-bottom deep cleans, kitchens and bathrooms, move-in / move-out and post-renovation cleanup.",
        "tile_sub": "Deep cleaning",
        "card_h3": "Deep cleaning for houses, condos &amp; apartments",
        "card_desc": "For when your home needs more than a quick tidy — top to bottom, corner to corner.",
        "points": ["Whole-home, kitchen &amp; bathroom deep cleans", "Move-in / move-out cleaning", "Post-renovation dust cleanup"],
        "eyebrow": "For Home · Deep Cleaning",
        "h1": "Deep cleaning for homes that need more than a quick tidy.",
        "lede": "Top-to-bottom deep cleans, move-in and move-out cleaning and post-renovation dust cleanup for houses, condos and apartments across Oʻahu.",
        "what_h2": "The build-up a regular clean leaves behind.",
        "items": [
            ("Whole-Home Deep Clean", "Every room, top to bottom: dusting high and low, baseboards, doors, switches and floors."),
            ("Kitchen Deep Clean", "Counters, backsplash, cabinet fronts and appliances degreased — inside the oven and fridge on request."),
            ("Bathroom Deep Clean", "Soap scum, hard-water spots and grout grime scrubbed away; glass, fixtures and tile left shining."),
            ("Move-In / Move-Out", "An empty home cleaned inside cabinets, closets and drawers — ready for the keys or the walk-through."),
            ("Post-Renovation Cleanup", "Fine dust and debris cleared from surfaces, sills, vent covers and floors after a remodel."),
            ("Add-Ons", "Inside the oven or fridge, interior windows, blinds and cabinet interiors."),
        ],
        "steps": [
            ("Tell us about your home", "Size, bedrooms and bathrooms, and what needs the most attention."),
            ("Get a clear quote", "We’ll give you a price and find a day and time that work for you."),
            ("Come home to clean", "We clean top to bottom while you get on with your day."),
        ],
        "faqs": [
            ("What’s the difference between a deep clean and a regular clean?", "A regular clean keeps a home tidy. A deep clean goes after the build-up: baseboards, grout, inside and behind appliances, cabinet fronts, switches and the corners a regular clean skips. It’s the right start for a new home, a move-out or a reset after a busy season."),
            ("Do I need to be home?", "Not necessarily. If you won’t be there, we’ll arrange access with you ahead of time."),
            ("How is the price set?", "It depends on the size of the home, its condition and any add-ons. Tell us the details and you’ll get a quote before any work begins."),
        ],
        "note": None,
    },
    {
        "slug": "business-cleaning",
        "card_link": "Explore business cleaning",
        "tab": "For Business",
        "icon": "building",
        "contact": "main",
        "site": None,
        "title": "Commercial Cleaning for Businesses on Oʻahu — HappyMax",
        "description": "Commercial cleaning on Oʻahu for offices, retail spaces, vacation rentals and property managers — one-time or recurring, scheduled around your hours.",
        "tile_sub": "Commercial cleaning",
        "card_h3": "Cleaning for offices, shops &amp; vacation rentals",
        "card_desc": "A spotless space for your team, customers and guests — scheduled around your hours.",
        "points": ["Offices, retail &amp; showrooms", "Vacation rental turnovers", "One-time or recurring"],
        "eyebrow": "For Business · Commercial Cleaning",
        "h1": "Commercial cleaning that keeps your business guest-ready.",
        "lede": "Office, retail and vacation-rental cleaning on a schedule that suits you — before opening, after closing or between guests — across Oʻahu.",
        "what_h2": "First impressions, handled.",
        "items": [
            ("Office Cleaning", "Desks, kitchens, restrooms, floors and trash — a clean, healthy workspace for your team."),
            ("Retail &amp; Showrooms", "Floors, glass, fitting rooms and displays kept spotless for your customers."),
            ("Vacation Rental Turnovers", "Thorough cleaning between guests, so every check-in feels like the first."),
            ("Move-Out &amp; End-of-Lease", "Empty units and suites cleaned and ready for the next tenant."),
            ("Post-Construction Cleanup", "Dust and debris cleared after a build-out or renovation, ready for opening day."),
            ("Common Areas", "Lobbies, hallways, stairwells and shared restrooms for property managers and associations."),
        ],
        "steps": [
            ("Tell us about the space", "Type and size of the space, your hours and what matters most."),
            ("Get a plan &amp; quote", "One-time or recurring — daily, weekly or monthly, scheduled around your hours."),
            ("Same standard every visit", "A clear checklist for your space, so you always know what you’re getting."),
        ],
        "faqs": [
            ("Can you clean outside business hours?", "Usually, yes — tell us your hours and we’ll find a time that stays out of your customers’ way."),
            ("Do you offer recurring service?", "Yes: one-time, weekly, bi-weekly or monthly. We’ll set up a schedule that fits your space."),
            ("Do you clean vacation rentals?", "Yes. Share your booking calendar and we’ll plan cleanings around check-outs and check-ins."),
        ],
        "note": ("tv", 'Need TVs or displays mounted in your office, lobby or restaurant? <a href="../tv-mounting/">See TV mounting</a>.'),
    },
    {
        "slug": "tv-mounting",
        "card_link": "Explore TV mounting",
        "tab": "TV Mounting",
        "icon": "tv",
        "contact": "main",
        "site": "https://happymaxhandymanservice.com/",
        "site_label": "happymaxhandymanservice.com",
        "site_cta": "Get a quote in 60 seconds",
        "site_blurb": "Answer a few quick questions about your TV and wall, pick a preferred time, and we’ll confirm by phone.",
        "title": "TV Mounting on Oʻahu — HappyMax Handyman Service",
        "description": "TV mounting on Oʻahu: any size TV on drywall, concrete or brick, cables hidden in-wall or in a clean raceway, sound bars mounted. Call (808) 201-1311.",
        "tile_sub": "Any size, any wall",
        "card_h3": "TV mounting done level, solid &amp; clean",
        "card_desc": "Any size TV on drywall, concrete or brick — with the cables out of sight.",
        "points": ["Drywall, concrete &amp; brick", "Cables hidden in-wall or in a raceway", "Sound bars mounted"],
        "eyebrow": "TV Mounting",
        "h1": "TV mounting done level, solid and clean.",
        "lede": "Any size TV on drywall, concrete or brick, with cables hidden in-wall or in a clean raceway and your sound bar mounted. Most installs take about an hour.",
        "what_h2": "What every install includes.",
        "items": [
            ("Any Size TV", "From a 32&quot; bedroom TV to an 85&quot;+ living-room centerpiece, mounted dead-level."),
            ("Concrete &amp; Brick", "Most Oʻahu condos are poured concrete, and it’s most of what we drill. Brick too."),
            ("Cables Out of Sight", "Hidden in-wall where possible, or in a slim paintable raceway where it isn’t."),
            ("Sound Bars", "Your sound bar mounted and lined up neatly under the TV."),
            ("Mount Selection &amp; Pick-Up", "Not sure which mount? We’ll help you choose and bring it — you pay only for the mount itself."),
            ("Clean Finish", "Packaging gone, dust cleaned up, and your home left the way we found it."),
        ],
        "steps": [
            ("Get a quote", "Answer a few questions about your TV and wall on our TV mounting site — or just call or text."),
            ("Pick a time", "Choose a preferred day and time window. We’ll confirm by phone."),
            ("Mounted &amp; clean", "Level, anchored, cables hidden, packaging gone."),
        ],
        "faqs": [
            ("Can you mount a TV on concrete walls?", "Yes — concrete is our home turf. Most Oʻahu condos and townhomes are poured concrete, so we carry masonry bits and anchors rated well beyond your TV’s weight."),
            ("Can you hide the cables inside the wall?", "Usually, yes. We check for studs, fire blocks and outlets first. Where in-wall isn’t possible (like solid concrete), we use a slim paintable raceway so nothing dangles."),
            ("Are you a licensed contractor?", "No, and we won’t pretend otherwise. Happy Max Handyman Service LLC works within Hawaii’s handyman exemption (HRS §444-2): jobs where labor and materials together come to $1,500 or less, that don’t need a building permit, and that aren’t electrical or plumbing work. TV mounting sits comfortably inside that. If a job needs new wiring, a new outlet behind the TV or any other licensed trade, we’ll say so up front and point you to someone who holds the right license."),
        ],
        "note": ("info", "Handyman scope only: we don’t add or move outlets or do any electrical work. If your install needs that, we’ll tell you before we start."),
        "photo": ("assets/img/tv-install.jpg", 720, 960, "TV mounted on a wall with a sound bar below and cables run in a white raceway", "A recent HappyMax install: TV, sound bar and cables in a neat raceway."),
    },
]

BY_SLUG = {s["slug"]: s for s in SERVICES}

# ───────────────────────── hub copy ─────────────────────────
HUB = {
    "title": "HappyMax Handyman Service — Detailing, Deep Cleaning &amp; TV Mounting on Oʻahu",
    "description": "HappyMax Handyman Service: mobile auto detailing, yacht and boat detailing, deep cleaning for homes and businesses, and TV mounting across Oʻahu. Call (808) 201-1311.",
    "eyebrow": "Honolulu · Serving all of Oʻahu",
    "h1": 'Cars, boats, homes and businesses — <span class="hl">HappyMax</span> takes care of it.',
    "lede": "One local team for mobile auto detailing, yacht care, deep cleaning and TV mounting. Pick a service to see what we do and how to book.",
    "steps": [
        ("Pick a service", "Use the tabs at the top or the cards above to find what you need."),
        ("Tell us the details", "Call, text or email — or book online for auto detailing and TV mounting. Photos always help."),
        ("We come to you", "Your driveway, harbor, home or business — we show up and get it done."),
    ],
    "why": [
        ("pin", "We come to you", "Driveway, harbor, home or office — anywhere on Oʻahu."),
        ("chat", "Easy to reach", "Call, text or email, whichever suits you. Clear answers, no runaround."),
        ("tag", "Know the price first", "Tell us what you need and get a straightforward quote before any work begins."),
        ("layers", "One name, many jobs", "Your car, your boat, your home and your TV — handled by a local company you already know."),
    ],
}

LEGAL = (
    "Happy Max Handyman Service LLC is <strong>not a licensed contractor</strong>. TV mounting is handyman-scope work "
    "performed under Hawaii’s handyman exemption (HRS&nbsp;§444-2): jobs of <strong>$1,500</strong> or less in combined "
    "labor and materials, requiring no building permit, and excluding all electrical and plumbing work. "
    "Larger jobs and licensed trades are referred out."
)


# ───────────────────────── page parts ─────────────────────────
def head(title, description, root, body_class=""):
    cls = f' class="{body_class}"' if body_class else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#0b1f42">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <link rel="icon" href="{root}assets/img/favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="{root}assets/img/icon-192.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Plus+Jakarta+Sans:wght@600;700;800&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{root}assets/css/style.css?v={ASSET_VERSION}">
</head>
<body{cls}>
  <a class="skip" href="#main">Skip to content</a>
"""


def brand(root):
    inner = (
        f'<img src="{root}assets/img/logo-mark.png" width="42" height="42" alt="">'
        '<span class="brand-text"><span class="brand-name">HAPPY <b>MAX</b></span>'
        '<span class="brand-sub">Handyman Service</span></span>'
    )
    return f'<a class="brand" href="{root or "./"}" aria-label="HappyMax Handyman Service — home">{inner}</a>'


def header(root, current=None, contact="main"):
    c = CONTACTS[contact]
    tabs = []
    for s in SERVICES:
        cur = ' aria-current="page"' if s["slug"] == current else ""
        tabs.append(
            f'<a class="tab t-{s["slug"]}" href="{root}{s["slug"]}/"{cur}>{icon(s["icon"])}<span>{s["tab"]}</span></a>'
        )
    return f"""
  <header class="site-header">
    <div class="container header-row">
      {brand(root)}
      <nav class="tabs" aria-label="Services">
        {''.join(tabs)}
      </nav>
      <a class="btn btn-sm btn-accent header-call" href="tel:{c['tel']}" aria-label="Call {c['display']}">{icon('phone')}<span class="num">{c['display']}</span><span class="lbl">Call</span></a>
    </div>
  </header>
"""


def footer(root):
    links = "".join(f'<li><a href="{root}{s["slug"]}/">{s["tab"]}</a></li>' for s in SERVICES)
    m, d = CONTACTS["main"], CONTACTS["detailing"]
    return f"""
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <span class="brand-text"><span class="brand-name">HAPPY <b>MAX</b></span><span class="brand-sub">Handyman Service</span></span>
          <p>One local team for auto &amp; yacht detailing, deep cleaning and TV mounting across Oʻahu. Based in Honolulu, Hawaiʻi.</p>
        </div>
        <div>
          <h4>Services</h4>
          <ul>{links}</ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="tel:{m['tel']}">{m['display']}</a> — {m['label']}</li>
            <li><a href="mailto:{m['email']}">{m['email']}</a></li>
            <li><a href="tel:{d['tel']}">{d['display']}</a> — {d['label']}</li>
            <li><a href="mailto:{d['email']}">{d['email']}</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-legal">
        <p>{LEGAL}</p>
        <p>© {YEAR} Happy Max Handyman Service LLC · Honolulu, HI</p>
      </div>
    </div>
  </footer>
</body>
</html>
"""


def steps_html(steps):
    return "".join(f'<li class="step"><h3>{t}</h3><p>{p}</p></li>' for t, p in steps)


def contact_card(key):
    c = CONTACTS[key]
    return f"""
        <div class="contact-card">
          <p class="eyebrow">{c['label']}</p>
          <h3><a href="tel:{c['tel']}">{c['display']}</a></h3>
          <div class="contact-actions">
            <a class="btn btn-navy" href="tel:{c['tel']}">{icon('phone')}Call</a>
            <a class="btn btn-outline" href="sms:{c['tel']}">{icon('chat')}Text</a>
          </div>
          <a class="contact-mail" href="mailto:{c['email']}">{icon('mail')}{c['email']}</a>
        </div>"""


# ───────────────────────── hub page ─────────────────────────
def build_hub():
    root = ""
    tiles = "".join(
        f'<a class="tile t-{s["slug"]}" href="{s["slug"]}/"><span class="tile-icon">{icon(s["icon"])}</span>'
        f'<span class="tile-name">{s["tab"]}</span><span class="tile-sub">{s["tile_sub"]}</span></a>'
        for s in SERVICES
    )
    cards = []
    for s in SERVICES:
        pts = "".join(f"<li>{icon('check')}<span>{p}</span></li>" for p in s["points"])
        cards.append(f"""
        <a class="svc-card t-{s['slug']}" href="{s['slug']}/">
          <div class="svc-art">{icon(s['icon'])}</div>
          <div class="svc-body">
            <p class="svc-kicker">{s['tab']}</p>
            <h3>{s['card_h3']}</h3>
            <p>{s['card_desc']}</p>
            <ul class="svc-points">{pts}</ul>
            <span class="svc-link">{s['card_link']}{icon('arrow')}</span>
          </div>
        </a>""")
    why = "".join(
        f'<div class="why-item"><div class="why-icon">{icon(ic)}</div><h3>{t}</h3><p>{p}</p></div>'
        for ic, t, p in HUB["why"]
    )
    m = CONTACTS["main"]
    html = head(HUB["title"], HUB["description"], root) + header(root) + f"""
  <main id="main">
    <section class="hub-hero">
      <div class="container hero-grid">
        <div class="hero-copy">
          <p class="eyebrow">{icon('pin')}{HUB['eyebrow']}</p>
          <h1>{HUB['h1']}</h1>
          <p class="lede">{HUB['lede']}</p>
          <div class="cta-row">
            <a class="btn btn-gold btn-lg" href="#services">Explore services{icon('arrow')}</a>
            <a class="btn btn-outline-light btn-lg" href="tel:{m['tel']}">{icon('phone')}{m['display']}</a>
          </div>
        </div>
        <nav class="hero-tiles" aria-label="Services">{tiles}</nav>
      </div>
    </section>

    <section class="section" id="services">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Our services</p>
          <h2>What can we take care of for you?</h2>
          <p>Five services, one local team. Pick one to see what’s included and how to book.</p>
        </div>
        <div class="svc-grid">{''.join(cards)}
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">How it works</p>
          <h2>Three steps, whatever the job.</h2>
        </div>
        <ol class="steps">{steps_html(HUB['steps'])}</ol>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Why HappyMax</p>
          <h2>Local, straightforward, on your schedule.</h2>
        </div>
        <div class="why-grid">{why}</div>
      </div>
    </section>

    <section class="section section-alt" id="contact">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Get in touch</p>
          <h2>Call, text or email — we’ll take it from there.</h2>
        </div>
        <div class="contact-grid">{contact_card('main')}{contact_card('detailing')}
        </div>
      </div>
    </section>
  </main>
""" + footer(root)
    (ROOT / "index.html").write_text(html, encoding="utf-8")


# ───────────────────────── service pages ─────────────────────────
def build_service(s):
    root = "../"
    c = CONTACTS[s["contact"]]
    # hero call-to-action buttons
    if s["site"]:
        ctas = (
            f'<a class="btn btn-accent btn-lg" href="{s["site"]}" target="_blank" rel="noopener">{s["site_cta"]}{icon("external")}</a>'
            f'<a class="btn btn-outline btn-lg" href="tel:{c["tel"]}">{icon("phone")}{c["display"]}</a>'
        )
    else:
        ctas = (
            f'<a class="btn btn-accent btn-lg" href="tel:{c["tel"]}">{icon("phone")}Call {c["display"]}</a>'
            f'<a class="btn btn-outline btn-lg" href="sms:{c["tel"]}">{icon("chat")}Text us</a>'
        )
    # hero visual: real photo when we have one, otherwise an illustrated card
    if s.get("photo"):
        src, w, h, alt, cap = s["photo"]
        art = (
            f'<figure class="hero-photo"><img src="{root}{src}" width="{w}" height="{h}" alt="{alt}" loading="eager">'
            f"<figcaption>{cap}</figcaption></figure>"
        )
    else:
        lis = "".join(f"<li>{icon('check')}<span>{t}</span></li>" for t, _ in s["items"][:3])
        art = (
            f'<div class="hero-art" aria-hidden="true"><div class="hero-art-icon">{icon(s["icon"])}</div>'
            f'<p class="hero-art-title">Most requested</p><ul class="hero-art-list">{lis}</ul></div>'
        )
    items = "".join(
        f'<div class="item"><div class="item-mark">{icon("check")}</div><h3>{t}</h3><p>{p}</p></div>'
        for t, p in s["items"]
    )
    note = ""
    if s.get("note"):
        ic, txt = s["note"]
        note = f'<div class="note">{icon(ic)}<p>{txt}</p></div>'
    band = ""
    if s["site"]:
        band = f"""
        <div class="site-band">
          <div><h3>{s['site_label']}</h3><p>{s['site_blurb']}</p></div>
          <a class="btn btn-gold" href="{s['site']}" target="_blank" rel="noopener">{s['site_cta']}{icon('external')}</a>
        </div>"""
    faqs = "".join(
        f"<details><summary>{q}{icon('plus')}</summary><p>{a}</p></details>" for q, a in s["faqs"]
    )
    if s["site"]:
        cta_buttons = (
            f'<a class="btn btn-white btn-lg" href="{s["site"]}" target="_blank" rel="noopener">{s["site_cta"]}{icon("external")}</a>'
            f'<a class="btn btn-outline-light btn-lg" href="tel:{c["tel"]}">{icon("phone")}{c["display"]}</a>'
        )
    else:
        cta_buttons = (
            f'<a class="btn btn-white btn-lg" href="tel:{c["tel"]}">{icon("phone")}Call {c["display"]}</a>'
            f'<a class="btn btn-outline-light btn-lg" href="sms:{c["tel"]}">{icon("chat")}Text us</a>'
        )
    more = "".join(
        f'<a class="more-card t-{o["slug"]}" href="{root}{o["slug"]}/"><span class="tile-icon">{icon(o["icon"])}</span>'
        f'<span><strong>{o["tab"]}</strong><span>{o["tile_sub"]}</span></span></a>'
        for o in SERVICES if o["slug"] != s["slug"]
    )
    html = head(s["title"], s["description"], root, f"t-{s['slug']}") + header(root, s["slug"], s["contact"]) + f"""
  <main id="main">
    <section class="page-hero">
      <div class="container page-hero-grid">
        <div>
          <nav class="crumbs" aria-label="Breadcrumb"><a href="{root}">HappyMax</a><span aria-hidden="true">/</span><span>{s['tab']}</span></nav>
          <p class="eyebrow">{icon(s['icon'])}{s['eyebrow']}</p>
          <h1>{s['h1']}</h1>
          <p class="lede">{s['lede']}</p>
          <div class="cta-row">{ctas}</div>
          <a class="hero-mail" href="mailto:{c['email']}">{icon('mail')}{c['email']}</a>
        </div>
        {art}
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">What we do</p>
          <h2>{s['what_h2']}</h2>
        </div>
        <div class="items-grid">{items}</div>
        {note}{band}
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">How it works</p>
          <h2>Simple from first message to finished job.</h2>
        </div>
        <ol class="steps">{steps_html(s['steps'])}</ol>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Questions</p>
          <h2>Good to know.</h2>
        </div>
        <div class="faq">{faqs}</div>
      </div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="container">
        <div class="cta-band">
          <h2>Ready when you are.</h2>
          <p>Call, text or email — tell us what you need and we’ll take it from there.</p>
          <div class="cta-row">{cta_buttons}</div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">More from HappyMax</p>
          <h2>Other ways we can help.</h2>
        </div>
        <div class="more-grid">{more}</div>
      </div>
    </section>
  </main>
""" + footer(root)
    out = ROOT / s["slug"]
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    build_hub()
    for s in SERVICES:
        build_service(s)
    print("built: index.html +", ", ".join(s["slug"] + "/" for s in SERVICES))
