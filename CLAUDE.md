# HappyMax main hub site — CLAUDE.md

Static hub for HappyMax Handyman Service with five service tabs. Read README.md first.

- Content lives in `build.py`; run `py build.py` to regenerate every page. Never hand-edit the generated HTML.
- No forms, no JS, no backend. Do not wire this site to the shared Supabase project
  (`fujjzktpumaxnyofsszy`) or the Telegram bot without checking `../Handyman world/CLAUDE.md` first —
  that backend is shared with the live TV-mounting funnel and the CRM.
- The live sites it links to are separate repos — do not edit them from here:
  TV mounting → `AzizullaSas/websitehandyman` (happymaxhandymanservice.com),
  auto detailing → `AzizullaSas/happymax-auto-detailing` (happymaxautodetailing.com).
- Legal (Hawaii HRS §444-9.2): never write "Licensed" / "Licensed & Insured"; no fake reviews,
  ratings or customer counts; TV mounting stays inside the §444-2 handyman exemption
  (≤ $1,500, no permit, no electrical or plumbing). Prices, guarantees and response times only
  when the owner has confirmed them.
- Changing `assets/css/style.css` → bump `ASSET_VERSION` in `build.py` and rebuild.
