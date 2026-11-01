---
name: dkb-investor-deck
description: Build, revise and fact-check the DaKickBack (DKB) investor PDF for the $2M launch raise, including its pitch outline. Use whenever the user mentions the DKB deck, the investor by name (currently Dr. Chad), the investor PDF, Teleric, Botim / Astra Tech, KickCoin / DKCoin, Beat Labz or the Akai / Teddy Riley DAW, Walt Reeder roster, Live Nation tour projections, Westville / ToyBoxx / Legend of FRQNZY pages, valuation or "what it's worth", use of funds, or asks for a pitch outline, even if they don't say "skill" or "deck". Also use when adding a new partner or IP tab to the deck, changing the investor name, refreshing market numbers, or pushing the deck to the repo.
---

# DKB investor deck

The deck is a Python (reportlab) build in `investor-deck/` of this repo. One command produces the PDF for any investor name. The work is half layout and half credibility: the reader is an investor who will ask "is that true?", so every number needs a source or an honest label.

## Fast path

```bash
cd investor-deck
python3 build_deck.py                          # default investor: Dr. Chad -> DKB_Dr_Chad_Investor_Deck.pdf
python3 build_deck.py --investor "Name"        # same deck, re-addressed everywhere (headers, cover note, waterfall, PDF title)
```

Investor name lives in source as tokens `@@INV@@` ("Dr. Chad") and `@@INVU@@` ("DR. CHAD"). Use the tokens in any new text instead of a literal name, so one source builds every investor's copy.

## Workflow

1. **Confirm who it is for.** The investor is Dr. Chad (replaced the earlier name on the user's instruction; no earlier-name copies are kept in the repo). The cover note thanks the investor for *their* $2M offer, so reword it if a different person didn't make that offer.
2. **Research before writing.** Use WebSearch for market figures, valuations and partner facts; prefer filings and trade press and record the date. `astratech.ae`-style fetches may be blocked by the environment's network policy: say so, name the host, and ask the user to allow it or paste the content. You cannot drive the user's screen or browser; Remote Control only exposes folders, so ask for screenshots or pasted pages instead.
3. **Classify every claim** using `references/claims-register.md`: *verified* (cite source and date), *management-reported* (say so on the page), or *unverified* (label as roadmap/target, or leave out). Do not strengthen a label because it would sound better. Where the user's drafts conflict with each other or with a source, flag it in your reply instead of silently picking one.
4. **Edit the pages** (`pages_a.py` pages 01-06, `pages_f.py` announced tour dates and the 60-day sequence, `pages_d.py` Teleric, `pages_e.py` Botim / KickCoin, `pages_c.py` IP/DAW/valuation, `pages_b.py` platform/Westville/Legend/financing/appendix). Register new pages in `build_deck.py`'s `seq` list and update the "NN / 09" index strings and section numbers consistently.
5. **Build and QA** (below). Look at the rendered pages; do not trust "no overflow" alone.
6. **Deliver.** Send the PDF with SendUserFile, commit `investor-deck/` on the designated branch, push. If push returns 403 the GitHub App lacks access: tell the user plainly, point them to the install/reconnect link, and do not retry endlessly.

## Layout rules (why they exist)

- Page is 792 x 1224 pt (11x17). Nothing is drawn in the top 54 pt (0.75 in) or within 24 pt of any other edge, so nothing clips on screens, printers or trim.
- Header, section breadcrumb and page index each sit in their own band (`HDR_BASE`, `TRACK_BASE`, footer); content starts at `CONTENT_TOP = 128` and ends at `CONTENT_BOTTOM = 1152`.
- 8 pt grid for gaps and block heights (`s8()`), 48 pt side margins, 696 pt content width.
- Every page function ends with `p.check(t, name)`; an overflow raises and prints. Fix by trimming content or splitting a page, not by shrinking type below ~7.5 pt.
- Text uses Paragraph markup: escape `&` as `&amp;` inside paragraph strings (canvas `p.text` does not need it).
- Fonts: Carlito (Lato-metric) for body, DejaVu Condensed Bold for display. The glyphs for check marks and triangles are missing; use shapes or words.

## QA commands

```bash
python3 build_deck.py out.pdf                  # watch for OVERFLOW lines
pdftoppm -r 62 -png out.pdf q                  # then view the new/changed pages
pdftotext out.pdf - | grep -c "@@"             # must be 0 (no unresolved name tokens)
```

Edge-ink audit: render at 72 dpi and confirm no non-white pixels in the top 54 px or within 24 px of the left, right and bottom edges. The last full audit passed on all 29 pages.

## Tone: confident front, disclosures in one place

The user wants the deck to sell: the $2M is launch capital, not a ceiling, and DKB should read as a category player. Do that with accurate positioning, not by dropping labels that keep claims true:
- Lead with what exists (announced dates, chart placement, partners in progress, 19 IP lines) and with market comparables; show scale as arithmetic (ARR x multiple, subscribers needed) and let the reader conclude.
- Do not assert that DKB is worth more than a named comparable (e.g. Suno) or that marketing is "proven" beyond the evidence in the files. Those are valuation / performance claims an investor can hold DKB to.
- Keep one-word labels that prevent a false impression ("proposed", "management estimates", "in progress", "announced").
- Put full risk and forward-looking language in the Important Notice appendix, not on selling pages. Internal diligence gaps (who is Evan Shive to Teleric, conflicting stats, vendor complaints) belong in `references/claims-register.md`, not in the deck.

## Honesty conventions already in the deck (keep them)

- Market figures are "latest published" with source and date; Suno / ElevenLabs valuations are post-money headlines, not liquid prices.
- Tour net figures are management estimates; the $66K downside row stays; "defined net" is set in the written agreement.
- Roster check: names on the Walt Reeder sheet are "ON ROSTER"; Krayzie Bone, Teddy Riley and AMG Twins are DKB-direct (†). "Rob Wave" is **Rod Wave**.
- Akai sponsorship, Botim integration, Live Nation routing and Teleric collaboration are *proposed or management-reported*, never "agreed".
- KickCoin / DKCoin: closed-loop platform credit, spend-only, no cash redemption, no reserve or gold-backing claims. "Digital banking" is provided by a licensed partner, never by DKB.
- Valuation: show comparables and ARR x multiple arithmetic; an independent valuation follows the proof gates. No claimed worth above a comparable.

## Pitch outline

When the user wants the talk track, read `references/pitch-outline.md` (structure, timing, objections and answers tied to deck pages).

## Open items to check at the start of any session

See the "Open items" section of `references/claims-register.md` (investor name, Botim spelling, Akai status, Evan Shive / Teleric relationship, "500+" vs "1,500+" catalog, equity vs waterfall terms).
