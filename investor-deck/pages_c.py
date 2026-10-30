"""Section 07: IP portfolio, Beat Labz DAW (Akai x Teddy Riley) and valuation framework."""
import math

from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph

from dkb_lib import *

TRACK = "07 / IP PORTFOLIO, DAW & VALUATION"
DARK = HexColor("#0D1B3A")
GREEN_BG, GREEN_FG = HexColor("#D9F5E8"), HexColor("#0A7A4B")
AMBER_BG, AMBER_FG = HexColor("#FFF0CF"), HexColor("#8A5A00")


def snap4(v):
    return int(math.ceil(v / 4.0) * 4)


def table(p, x, t, cols, rows, head_h=28, pad=7, zebra=True, first_bold=True):
    """cols = [(header, width, align)], rows = [[markup,...]]. Returns height."""
    tw = sum(c[1] for c in cols)
    p.rect(x, t, tw, head_h, fill=NAVY, r=4)
    cx = x
    for lab, w, al in cols:
        tx = cx + 8 if al == "l" else cx + w - 8
        p.text(tx, t + head_h / 2.0 + 3, lab, "Body-B", 7, white, "l" if al == "l" else "r", cs=0.4)
        cx += w
    cur = t + head_h
    for i, row in enumerate(rows):
        hs = []
        for (lab, w, al), cell in zip(cols, row):
            hs.append(p.ph(w - 16, cell, "tcell"))
        rh = snap4(max(hs) + 2 * pad)
        p.rect(x, cur, tw, rh, fill=PALE if (zebra and i % 2 == 0) else white, stroke=LINE)
        cx = x
        for (lab, w, al), cell in zip(cols, row):
            p.para(cx + 8, cur + pad, w - 16, cell, "tcellr" if al == "r" else "tcell")
            cx += w
        cur += rh
    return cur - t


ST["tcell"] = S("tcell", 8, 10.5, GREY)
ST["tcellr"] = S("tcellr", 8, 10.5, INK, align=2)


# =============================================================================
# 07A  IP PORTFOLIO
# =============================================================================
IP = [
    ("DKB Hot 100", "Discovery", "Independent streaming chart with proprietary stream verification.", "Billboard / Spotify charts",
     "Brand • Data • Method", "Chart live; verification method published"),
    ("DaKickTapes", "Discovery", "Curated mixtape and release drops from DKB artists.", "DatPiff / Audiomack",
     "Brand • Content licenses", "First licensed tape series"),
    ("KickTok", "Social", "Vertical short-form video feed tied to charts and tickets.", "TikTok / Reels",
     "Software • Brand", "Creator beta; 30-day retention"),
    ("Timeline + Respect", "Social", "Social feed with fan-to-creator tipping (“Respect”).", "Instagram + Patreon tips",
     "Software • Brand", "Tipping live on licensed rails"),
    ("Creator Profiles", "Social", "Verified artist pages that anchor every release and ticket.", "Spotify for Artists / Linktree",
     "Software • Data", "Verified profiles for tour artists"),
    ("FTV", "Video", "Live shows and pay-per-view from tour stops.", "Twitch / YouTube Live / PPV",
     "Software • Content rights", "First paid live stream"),
    ("KickFlix", "Video", "Documentary, BTS and original series library.", "Netflix / Tubi",
     "Content • Brand", "First original title"),
    ("FRQNZY Beat Labz", "Studio", "AI-native, pad-first DAW with direct publish to DKB (see next page).", "FL Studio / Ableton / BandLab / Suno",
     "Software • AI models • Brand", "Alpha + closed producer beta"),
    ("Creator Locker", "Studio", "Secure vault for stems, masters, splits and contracts.", "Splice / Dropbox",
     "Software • Data", "Vault used by tour artists"),
    ("DKB Ticket + FRQNZY AI", "Commerce", "Primary ticketing plus artist-booking, rider and routing workspace ($49.99 / mo).",
     "Ticketmaster; booking SaaS", "Software • Data • Brand", "Portal live on tour dates"),
    ("Merch + Creator Sales", "Commerce", "Physical and digital goods, collectibles and creator storefronts.", "Shopify / Bandcamp",
     "Brand • Software", "First merch drop"),
    ("Ourcade", "Game", "Arcade and mini-game hub inside the DKB account.", "Roblox experiences / arcade portals",
     "Software • Content", "Three launch titles"),
    ("Welcome 2 Westville", "Game", "Seven-city open-world flagship with music, sports and crime careers.", "GTA-style open worlds",
     "Game IP • Characters • World", "Playable UE slice"),
    ("Legend of FRQNZY", "Game", "Independent fantasy franchise: games, animation, collectibles, soundtrack.", "Action-RPG franchises",
     "Franchise IP • Characters", "Vertical-slice trailer"),
    ("DaLimes", "Community", "Audio lounges and live rooms around artists and charts.", "X Spaces / Discord",
     "Software • Brand", "Rooms hosted at tour stops"),
    ("Kupid + Mail + Search", "Community", "Matchmaking, messaging and discovery utilities.", "Hinge / Gmail / search",
     "Software", "Held until core engagement proven"),
    ("ToyBoxx + ToyBoxxOS", "Hardware", "Couch-first console, controller and operating layer ($274.99).", "Console / handheld hardware",
     "Design • Patents (TBD) • OS", "Functional prototype; BOM audit"),
    ("Teleric", "Infrastructure", "High-density venue Wi-Fi, edge delivery and live streaming.", "Venue connectivity / CDN",
     "Know-how • Contracts", "Live at first tour date"),
    ("Payments Rail", "Advanced", "Licensed P2P payouts and creator royalties.", "Cash App / Venmo",
     "Licenses • Software", "Licensed partner signed"),
]


def page_ip(p):
    p.frame(TRACK, "07 / 08")
    t = CONTENT_TOP
    t = p.title(t, "EVERY TAB IS AN ASSET", "THE DKB IP PORTFOLIO",
                "DKB is not one app. Each module below is a separately ownable product with its own brand, code, data and "
                "revenue line: built once, monetized many times, and licensable or saleable on its own. All items are roadmap "
                "or concept unless stated; registration status is documented in diligence.")
    cols = [("IP / MODULE", 132, "l"), ("WHAT IT IS", 196, "l"), ("PUBLIC COMPARABLE", 112, "l"),
            ("IP TYPE", 120, "l"), ("PROPOSED PROOF GATE", 136, "l")]
    rows = []
    for n, m, w, c, ty, g in IP:
        rows.append(["<font name='Body-B' color='#081D42' size='8.5'>%s</font><br/><font color='#1472CE' size='7'>%s</font>" % (n, m.upper()),
                     w, c, ty, g])
    h = table(p, MX, t, cols, rows)
    t += h + 12
    t += p.para(MX, t, CW, "Comparables are public analogues for orientation only; they do not imply partnership, equivalence or "
                "valuation. “Proof gate” is the first measurable evidence that turns a concept into an investable asset. "
                "Patent, trademark and copyright registrations will be itemized in a diligence schedule.", "src")
    p.check(t, "page_ip")


# =============================================================================
# 07B  BEAT LABZ DAW
# =============================================================================
def daw_mock(p, x, t, w, h):
    p.rect(x, t, w, h, fill=DARK, r=8)
    p.rect(x, t, w, 32, fill=HexColor("#13264F"), r=8)
    for i, col in enumerate((RED, GOLD, GREEN)):
        p.c.setFillColor(col)
        p.c.circle(x + 18 + i * 14, p.Y(t + 16), 4, stroke=0, fill=1)
    p.text(x + 70, t + 20, "FRQNZY BEAT LABZ", "Body-B", 9, white, cs=0.8)
    p.chip(x + w - 250, t + 6, "BPM 92", fill=HexColor("#1F3A70"), color=white, size=7.5, h=20)
    p.chip(x + w - 188, t + 6, "KEY F MIN", fill=HexColor("#1F3A70"), color=white, size=7.5, h=20)
    p.chip(x + w - 112, t + 6, "AI: LICENSED DATA", fill=BLUE, color=white, size=7.5, h=20)
    # pads
    px, py = x + 24, t + 56
    lit = {0, 3, 5, 6, 9, 10, 12, 15}
    for r in range(4):
        for c in range(4):
            i = r * 4 + c
            col = (BLUE if i % 3 else SKY) if i in lit else HexColor("#1B2F5C")
            p.rect(px + c * 50, py + r * 50, 44, 44, fill=col, r=6)
            p.text(px + c * 50 + 22, py + r * 50 + 27, str(i + 1), "Body-B", 8, white if i in lit else HexColor("#5C74A6"), "c")
    p.text(px, py + 212, "PADS  •  MPC-STYLE FINGER DRUMMING", "Body-B", 7, SKY, cs=0.5)
    # sequencer
    sx, sy = x + 252, t + 56
    names = ["KICK", "SNARE", "HAT", "808"]
    pat = [[0, 4, 8, 11], [4, 12], [0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 8, 10, 14]]
    for r in range(4):
        p.text(sx, sy + r * 36 + 20, names[r], "Body-B", 7.5, SKY, cs=0.4)
        for c in range(16):
            on = c in pat[r]
            p.rect(sx + 44 + c * 14, sy + r * 36, 11, 28, fill=GOLD if on and r == 3 else (BLUE if on else HexColor("#1B2F5C")), r=2)
    p.text(sx, sy + 156, "STEP SEQUENCER  •  16 STEPS  •  SWING 58%", "Body-B", 7, SKY, cs=0.5)
    # waveform strip
    wy = sy + 172
    p.rect(sx, wy, 268, 44, fill=HexColor("#13264F"), r=4)
    for i in range(53):
        hh = 6 + 14 * abs(math.sin(i * 0.55)) * (0.5 + 0.5 * math.sin(i * 0.17 + 1))
        p.rect(sx + 8 + i * 4.8, wy + 22 - hh / 2.0, 2.6, hh, fill=SKY if i < 38 else HexColor("#3A5A9A"))
    # AI panel
    ax = x + w - 168
    p.rect(ax, t + 48, 148, 224, fill=HexColor("#13264F"), r=6)
    p.text(ax + 12, t + 68, "AI ASSIST", "Body-B", 8, SKY, cs=0.8)
    btns = ["Generate drum pattern", "Split stems", "Key-aware chords", "Match vibe: new jack swing", "Humanize groove"]
    for i, b in enumerate(btns):
        p.rect(ax + 10, t + 80 + i * 32, 128, 26, fill=BLUE if i == 3 else HexColor("#1F3A70"), r=13)
        p.text(ax + 74, t + 97 + i * 32, b, "Body-B", 7.5, white, "c")
    # publish bar
    p.rect(x + 20, t + h - 52, w - 40, 36, fill=GOLD, r=6)
    p.text(x + 36, t + h - 30, "PUBLISH  →", "Body-B", 9.5, NAVY, cs=0.8)
    p.text(x + 130, t + h - 30, "DKB HOT 100   •   KICKTOK   •   FTV   •   TICKET LINK", "Body-B", 8.5, NAVY, cs=0.5)


def page_daw(p):
    p.frame(TRACK, "07 / 08", cont=True)
    t = CONTENT_TOP
    t = p.title(t, "BEAT LABZ: THE DKB DAW", "FLAGSHIP CREATOR-TOOL IP  •  AI-NATIVE  •  PAD-FIRST",
                "FL Studio taught a generation to make beats on a laptop; Suno proved AI music is a venture-scale category. "
                "Beat Labz sits between them: a producer-grade workstation with licensed-data AI built in, wired straight into "
                "DKB's charts, ticketing and fan base.")
    daw_mock(p, MX, t, CW, 340)
    t += 348
    p.text(MX, t + 8, "Concept mock-up for illustration; not a shipped product.", "Body-I", 7, GREY)
    t += 28

    # market strip
    stats = [("$3.1–3.5B", "DAW software market, 2025; published estimates span $2.2–4.4B, ~8–10% CAGR"),
             ("~$300M", "Suno annual recurring revenue (reported); 2M+ paid subscribers as of Feb 2026"),
             ("$5.4B", "Suno post-money valuation, Series D, June 2026 (about 18x ARR)"),
             ("$11B", "ElevenLabs valuation, Feb 2026; expanding from voice into AI music")]
    cw = (CW - 3 * 12) / 4.0
    for i, (v, d) in enumerate(stats):
        x = MX + i * (cw + 12)
        p.rect(x, t, cw, 96, fill=NAVY if i == 2 else PALE, stroke=None if i == 2 else LINE, r=4)
        p.text(x + 14, t + 32, v, DISPLAY, 20, SKY if i == 2 else BLUE)
        p.para(x + 14, t + 42, cw - 28, d, S("ds", 7.5, 10, HexColor("#C9DDF5") if i == 2 else GREY))
    t += 112

    t += p.section_bar(t, "WHY IT IS DEFENSIBLE IP", "MODELS • DATA • DISTRIBUTION • CREDIBILITY")
    hh = p.cards_row(MX, t, CW, [
        ("LICENSED-DATA AI", "Models trained on cleared stems and partner catalogs. The industry is moving toward licensed AI "
         "(Suno says its next model is built with the music industry) while litigation continues, so clean data is a feature, "
         "not a cost."),
        ("A BUILT-IN FAN LOOP", "Every beat can be published inside DKB: Hot 100, KickTok, FTV and a ticket link. A standalone DAW "
         "sells software; Beat Labz also feeds an owned audience.", NAVY),
        ("PRODUCER CREDIBILITY", "Teddy Riley, creator of new jack swing, has been featured by Akai Professional on the MPC XL that "
         "shaped his sound. That is authentic pad-first lineage that generic AI tools cannot buy.")],
        bar="top", fill=PALE)
    t += hh + 16

    # roadmap gates
    t += p.section_bar(t, "BEAT LABZ GATES", "FUNDED WITHIN THE $450K PLATFORM LINE UNTIL PROOF")
    gates = [("PROTOTYPE", "Pad sequencer, sampler and stem tools"), ("CLOSED BETA", "Working producers; retention measured"),
             ("EDITION BUNDLE", "Teddy Riley Edition with Akai"), ("LICENSED AI v1", "Cleared-data generation and assist"),
             ("PUBLIC LAUNCH", "Subscriptions live on DKB")]
    gw = (CW - 4 * 20) / 5.0
    for i, (a_, b_) in enumerate(gates):
        x = MX + i * (gw + 20)
        col = GOLD if i == 2 else (NAVY if i % 2 == 0 else BLUE)
        p.rect(x, t, gw, 80, fill=col, r=6)
        p.text(x + 12, t + 26, "GATE %d" % (i + 1), "Body-B", 7, NAVY if col == GOLD else SKY, cs=0.6)
        p.text(x + 12, t + 42, a_, "Body-B", 9, NAVY if col == GOLD else white, cs=0.3)
        p.para(x + 12, t + 48, gw - 24, b_, S("gt2", 8, 10, NAVY if col == GOLD else HexColor("#E6F0FC")))
        if i < 4:
            p.arrow(x + gw + 2, t + 40, x + gw + 18, t + 40, GOLD, 1.8, 6)
    t += 96
    p.check(t, "page_daw")


def page_akai(p):
    p.frame(TRACK, "07 / 08", cont=True)
    t = CONTENT_TOP
    t = p.title(t, "THE AKAI ASK", "WHAT TO NEGOTIATE FOR: TEDDY RILEY x AKAI PROFESSIONAL x BEAT LABZ",
                "A signature-edition deal is only as good as its terms. This is the framework for what DKB should request, in "
                "priority order, and what each side gets.", size=34)
    # status + ask
    t += p.section_bar(t, "NEGOTIATING FRAMEWORK", "NOT AGREED TERMS")
    hb = p.card_h(CW - 4, "STATUS", "Management reports an Akai Professional sponsorship through Teddy Riley is pending. As of October "
                  "2026 no public announcement was found. Everything below is what DKB should ask for, not what has been agreed.", 12)
    p.card(MX, t, CW, hb, "STATUS", "Management reports an Akai Professional sponsorship through Teddy Riley is pending. As of October "
           "2026 no public announcement was found. Everything below is what DKB should ask for, not what has been agreed.",
           accent=GOLD, fill=ICE, bar="left")
    t += hb + 12
    cols = [("THE ASK", 160, "l"), ("WHY IT MATTERS", 376, "l"), ("PRIORITY", 160, "l")]
    rows = [
        ["<b>Signature “Teddy Riley Edition” bundle</b>", "Co-branded hardware or software edition. Precedent: Akai's Timbaland-branded MPC Live 2 BeatClub Edition (Apr 2023).", "Must-have"],
        ["<b>Beat Labz in the box</b>", "Activation code bundled with Akai units makes every sale a DKB account: hardware-scale distribution at no ad cost.", "Must-have"],
        ["<b>Minimum guarantee + per-unit royalty</b>", "Signature units pay Teddy Riley and DKB a guaranteed floor plus a royalty; amounts set by counsel.", "Must-have"],
        ["<b>IP split in writing</b>", "DKB owns Beat Labz code, AI models and user data; Akai licenses its brand for bundles; Teddy's name and likeness licensed with approvals and a defined term.", "Must-have"],
        ["<b>Co-marketing commitment</b>", "Dealer-network placement, trade-show presence and an Akai-presented stage at DKB tour dates.", "High"],
        ["<b>Native controller mapping</b>", "Pads, knobs and screens mapped natively so MPC owners get Beat Labz on day one.", "High"],
        ["<b>Co-branded sound library</b>", "Teddy Riley / FRQNZY sample packs sold in Beat Labz and Akai channels with revenue share.", "High"],
        ["<b>Category exclusivity window</b>", "A limited period in which Akai does not sign a competing AI-DAW celebrity edition.", "Nice-to-have"],
    ]
    h = table(p, MX, t, cols, rows)
    t += h + 12
    t = s8(t + 16)
    t += p.section_bar(t, "WHAT AKAI GETS", "WHY A YES MAKES SENSE FOR THEM")
    hh = p.cards_row(MX, t, CW, [
        ("A SOFTWARE + AI STORY", "Pad hardware paired with a modern, licensed-data AI workstation, without Akai building it alone."),
        ("A NEW-USER FUNNEL", "Beat Labz and DKB bring producers and fans who may buy their first pad controller.", NAVY),
        ("TEDDY-FRONTED MARKETING", "A credible signature edition plus DKB tour activation and content. Akai Professional is a brand of inMusic.")],
        bar="top", fill=PALE)
    t += hh
    t = s8(t + 16)
    t += p.section_bar(t, "GUARDRAILS BUILT INTO THE DEAL", "PROTECTING DKB, TEDDY AND DR. ISH")
    hh = p.cards_row(MX, t, CW, [
        ("LICENSED DATA ONLY", "AI features trained and served only on cleared stems and partner catalogs, with written provenance, so "
         "the product can be sold to labels, brands and retailers."),
        ("OPT-IN DATA", "User data is collected only with consent and stays DKB's, consistent with privacy law and Akai's own "
         "customer terms.", NAVY),
        ("LIKENESS APPROVALS", "Teddy Riley's name, voice and likeness are licensed per use with approval rights; no synthetic voice "
         "clone without explicit written consent.")], bar="top", fill=PALE)
    t += hh
    p.check(t, "page_akai")




# =============================================================================
# 07C  VALUATION I: comps, what must be true, scenarios
# =============================================================================
def page_value1(p):
    p.frame(TRACK, "07 / 08", cont=True)
    t = CONTENT_TOP
    t = p.title(t, "WHAT $2M LAUNCHES, AND WHAT IT CAN BE WORTH", "AN HONEST VALUATION FRAMEWORK",
                "The $2M launches the company; it does not claim to value it. DKB is pre-revenue today. Below is how Silicon Valley "
                "will price it: by comparable, by IP asset and by the traction each gate proves.", size=30)
    t += p.section_bar(t, "WHERE MARKET VALUE IS BEING SET RIGHT NOW", "LATEST PUBLISHED, OCT 2026")
    cols = [("COMPARABLE", 120, "l"), ("VALUE SIGNAL", 190, "l"), ("REVENUE SIGNAL", 190, "l"), ("RELEVANCE TO DKB", 196, "l")]
    rows = [
        ["<b>Suno</b>", "$5.4B post-money, Series D (+$400M), Jun 2026; up from $2.45B in Nov 2025", "~$300M ARR (reported); 2M+ paid subs (Feb 2026); ~18x ARR", "AI music creation: Beat Labz and FRQNZY AI category"],
        ["<b>ElevenLabs</b>", "$11B, $500M Series D, Feb 2026", "Reported above $500M annual revenue; ~22x", "AI audio moving into music; platform partner potential"],
        ["<b>Splice</b>", "~$450–500M, last priced 2021", "Not disclosed", "Closest producer-marketplace precedent for Creator Locker and sound packs"],
        ["<b>Roblox</b>", "Public company", "FY2025 revenue $4.9B; bookings $6.8B; creators earned $1.5B+", "Creator-economy platform: Westville, Ourcade, virtual shows"],
        ["<b>Live Nation</b>", "Public company", "FY2025 revenue $25.2B; concerts $20.9B; Ticketmaster $3.1B", "Touring and ticketing channel; DKB Ticket comparable"],
        ["<b>DAW market</b>", "~$3.1–3.5B in 2025 (estimates $2.2–4.4B)", "~8–10% CAGR across published reports", "Sizing for Beat Labz; definitions vary by report"],
    ]
    h = table(p, MX, t, cols, rows)
    t += h + 8
    t += p.para(MX, t, CW, "Private valuations are post-money headlines from trade press and filings, not liquid prices, and are not a DKB "
                "valuation. Context: US video games $60.8B (ESA, restated Mar 2026), global recorded music $31.7B (IFPI, Mar 2026).", "src")
    t = s8(t + 16)

    # what must be true
    t += p.section_bar(t, "WHAT MUST BE TRUE: ARR NEEDED FOR A TARGET VALUE", "6x CONSERVATIVE  •  12x MID  •  18x SUNO PARITY")
    sub = 29.99 * 12
    cols = [("TARGET VALUE", 112, "l"), ("ARR @ 6x", 120, "r"), ("ARR @ 12x", 120, "r"), ("ARR @ 18x", 120, "r"),
            ("CREATOR SUBS NEEDED @ 12x ($29.99 / MO)", 224, "r")]
    rows = []
    for v in (25e6, 50e6, 100e6, 250e6):
        rows.append(["<b>$%dM</b>" % (v / 1e6)] + ["$%.1fM" % (v / m / 1e6) for m in (6, 12, 18)] +
                    ["{:,.0f}".format(v / 12 / sub)])
    h = table(p, MX, t, cols, rows)
    t += h + 8
    t += p.para(MX, t, CW, "For scale, Suno reports 2M+ paid subscribers. Multiples are illustrative: 18x is Suno's reported ratio; 6x and 12x "
                "are haircuts for an unproven early-stage company. Subscribers = target ÷ 12 ÷ ($29.99 × 12).", "src")
    t = s8(t + 16)

    # scenario capitalization
    t += p.section_bar(t, "THE DECK'S OWN SCENARIOS, CAPITALIZED CONSERVATIVELY", "ONLY RECURRING CREATOR SUBSCRIPTIONS COUNTED")
    sc = [("STANDARD", 500), ("GOOD", 1500), ("GREAT", 3500)]
    ax0 = MX + 232
    aw = 360
    mx_v = 25e6
    p.line(ax0, t, ax0, t + 3 * 56, LINE)
    for k in range(0, 6):
        gx = ax0 + aw * k * 5e6 / mx_v
        p.line(gx, t + 3 * 56 - 4, gx, t + 3 * 56, LINE)
        p.text(gx, t + 3 * 56 + 12, "$%dM" % (k * 5), "Body", 7, GREY, "c")
    for i, (n, subs) in enumerate(sc):
        arr = subs * 12 * 29.99
        lo, mid, hi = arr * 6, arr * 12, arr * 18
        y = t + i * 56
        p.text(MX, y + 22, n, "Body-B", 9.5, NAVY, cs=0.4)
        p.text(MX, y + 36, "{:,} subs / mo  =  ${:,.0f} ARR".format(subs, arr), "Body", 8, GREY)
        p.rect(ax0, y + 12, aw, 22, fill=PALE, r=3)
        p.rect(ax0 + aw * lo / mx_v, y + 12, aw * (hi - lo) / mx_v, 22, fill=BLUE, r=3)
        mxp = ax0 + aw * mid / mx_v
        p.line(mxp, y + 8, mxp, y + 38, NAVY, 2)
        p.text(ax0 + aw + 12, y + 22, "$%.1fM–$%.1fM" % (lo / 1e6, hi / 1e6), "Body-B", 9, NAVY)
        p.text(ax0 + aw + 12, y + 34, "mid $%.1fM" % (mid / 1e6), "Body", 8, GREY)
    gx = ax0 + aw * 2e6 / mx_v
    p.line(gx, t - 4, gx, t + 3 * 56, RED, 1.2, (3, 3))
    p.text(gx, t - 8, "$2M LAUNCH CAPITAL", "Body-B", 7, RED, "l", cs=0.4)
    t += 3 * 56 + 28
    hb = p.card_h(CW - 4, "THE CANDID READ", "At Standard adoption the subscription line alone is worth about the same as the "
                  "$2M (mid case $2.2M); at Great it reaches the mid-teens of millions. Touring, hardware, games and publishing are counted at zero here: "
                  "they are upside. A venture-scale outcome needs distribution deals like the Akai bundle and several IP lines monetizing "
                  "one fan base. That is the thesis the $2M is built to test.", 12)
    p.card(MX, t, CW, hb, "THE CANDID READ", "At Standard adoption the subscription line alone is worth about the same as the "
           "$2M (mid case $2.2M); at Great it reaches the mid-teens of millions. Touring, hardware, games and publishing are counted at zero here: "
           "they are upside. A venture-scale outcome needs distribution deals like the Akai bundle and several IP lines monetizing "
           "one fan base. That is the thesis the $2M is built to test.", accent=BLUE, fill=ICE, bar="left")
    t += hb
    p.check(t, "page_value1")


# =============================================================================
# 07D  VALUATION II: equity reference, what $2M buys, ladder
# =============================================================================
def page_value2(p):
    p.frame(TRACK, "07 / 08", cont=True)
    t = CONTENT_TOP
    t = p.title(t, "WHAT THE $2M BUYS: AND WHAT IT DOESN'T", "BE UPFRONT. EARN THE NEXT STEP.",
                "The $2M launches proof across the portfolio. It does not finish a console, a flagship open-world game and a "
                "full platform; it funds the gates that earn the right to raise or fund those.", size=30)
    cw2 = (CW - 16) / 2.0
    left = ["Ticket portal live and a 4–8 date tour with Walt Reeder talent",
            "365-song radio-first rollout in tour markets, with FM and creator pushes",
            "Playable Westville slice and DKB web / ticketing core",
            "Beat Labz alpha and the Akai framework negotiated and papered",
            "ToyBoxx controller verification and functional prototype gates",
            "Legal, KYC / compliance, rider contracts and live-event escrow"]
    right = ["A finished AAA open-world game: such titles are typically budgeted in the hundreds of millions",
             "Console mass production: needs certified prototypes, audited BOM and tooling capital",
             "All 13 tabs at consumer scale: each is sequenced behind its proof gate",
             "Guaranteed investor returns: figures are management estimates, not promises",
             "Any valuation claim today: DKB is pre-revenue and has no independent appraisal"]
    hl = p.bullets_h(cw2 - 32, left, "bulc") + 56
    hr = p.bullets_h(cw2 - 32, right, "bulc") + 56
    h = s8(max(hl, hr))
    for i, (ttl, items, col) in enumerate((("WHAT $2M LAUNCHES", left, GREEN), ("WHAT $2M DOES NOT BUY", right, RED))):
        x = MX + i * (cw2 + 16)
        p.rect(x, t, cw2, h, fill=PALE, stroke=LINE, r=4)
        p.rect(x, t, cw2, 5, fill=col)
        p.text(x + 16, t + 30, ttl, "Body-B", 9.5, NAVY, cs=0.5)
        p.bullets(x + 16, t + 42, cw2 - 32, items, "bulc")
    t += h + 24

    # ladder
    t += p.section_bar(t, "THE VALUE LADDER: WHAT EACH GATE PROVES", "VALUE FOLLOWS EVIDENCE")
    steps = [("01  LAUNCH", "$2M deployed", "Pre-revenue. Value is option value: IP, relationships and a plan with controls.", NAVY),
             ("02  PROVE", "Tour + ticket accounts", "First settlements, DKB registrations, Beat Labz beta cohort, Akai terms signed.", BLUE),
             ("03  PLATFORM", "Recurring revenue", "Creator subscriptions and bundle-driven signups; ARR becomes measurable.", BLUE),
             ("04  SCALE", "Multiple IP lines", "Games, hardware and licensing layered on one fan base; strategic buyers appear.", NAVY)]
    sw = (CW - 3 * 16) / 4.0
    for i, (a, b, c_, col) in enumerate(steps):
        x = MX + i * (sw + 16)
        top = t + (3 - i) * 24
        hh = 144 - (3 - i) * 24 + 24
        p.rect(x, top, sw, hh, fill=col, r=6)
        p.text(x + 14, top + 26, a, "Body-B", 9, white, cs=0.5)
        p.text(x + 14, top + 44, b, DISPLAY, 10, SKY)
        p.para(x + 14, top + 52, sw - 28, c_, S("lad", 8, 10.5, HexColor("#E6F0FC")))
    t += 168 + 16
    t = s8(t)

    # equity reference
    t += p.section_bar(t, "$2M IN EQUITY TERMS (FOR REFERENCE ONLY)", "ILLUSTRATIVE POST-MONEY OPTIONS")
    cols = [("IF PRICED AT A POST-MONEY OF", 224, "l"), ("$2M WOULD BUY", 150, "r"), ("COMPARED WITH THE PROPOSED STRUCTURE", 322, "l")]
    rows = []
    for pm in (8e6, 12e6, 20e6):
        rows.append(["<b>$%dM</b>" % (pm / 1e6), "%.1f%%" % (2e6 / pm * 100), "Reference only; no equity is offered in the current terms."])
    h = table(p, MX, t, cols, rows)
    t += h + 8
    t += p.para(MX, t, CW, "<b>Proposed structure instead:</b> 100% of defined net tour and merchandise receipts to principal first; then a "
                "permanent 50 / 50 split of net live and merchandise profit; 1% publishing participation on each of the 365 campaign songs; "
                "a $75,000 bonus on a defined label milestone. Equity or IP-licence participation in the portfolio can be raised in "
                "negotiation and is not part of these terms. Pricing is for discussion with counsel, not a valuation opinion.", "small")
    t = s8(t + 16)

    t += p.section_bar(t, "NATURAL COUNTERPARTIES BY IP", "WHO COULD LICENSE, PARTNER OR ACQUIRE LATER")
    cp = [("BEAT LABZ", "Music-tech and hardware strategics"), ("TOUR + DKB TICKET", "Promoters, ticketers, venue groups"),
          ("WESTVILLE / LEGEND", "Game publishers, streaming and animation studios"), ("HOT 100 + TAPES", "Labels, distributors, streaming services"),
          ("TOYBOXX", "Hardware OEMs and retail partners")]
    kw = (CW - 4 * 12) / 5.0
    for i, (a_, b_) in enumerate(cp):
        x = MX + i * (kw + 12)
        p.rect(x, t, kw, 80, fill=PALE, stroke=LINE, r=4)
        p.rect(x, t, kw, 4, fill=BLUE if i % 2 else NAVY)
        p.text(x + 12, t + 28, a_, "Body-B", 8.5, NAVY, cs=0.3)
        p.para(x + 12, t + 36, kw - 24, b_, "card")
    t += 96
    p.para(MX, t, CW, "Illustrative categories of interested parties; no discussions are represented.", "src")
    t = s8(t + 28)

    # one-line close
    p.rect(MX, t, CW, 72, fill=NAVY, r=6)
    p.text(MX + 24, t + 30, "THE HONEST ONE-LINER", "Body-B", 8.5, SKY, cs=0.8)
    p.para(MX + 24, t + 38, CW - 48, "$2M launches DKB and buys evidence across 19 IP lines. What it is worth is decided by the "
           "gates it clears, measured monthly and reported to Dr. Ish.", S("ol", 11.5, 15, white, "Body-B"))
    t += 72
    p.check(t, "page_value2")
