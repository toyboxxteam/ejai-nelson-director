"""Section 07: Teleric, DKB's own network (three pages)."""
import math

from reportlab.lib.colors import HexColor, white

from dkb_lib import *
from pages_c import table, DARK, AMBER_BG, AMBER_FG

TRACK = "07 / INFRASTRUCTURE: TELERIC (NETWORK) + BOTIM (MONEY)"
IDX = "07 / 09"


def pon_diagram(p, x, t, w, h):
    half = (w - 24) / 2.0
    for k, (ttl, sub, col, shared) in enumerate((
            ("INDUSTRY: SHARED PON FIBER", "32+ homes share each fiber and its 1 Gbps; powered splitters in the field", GREY, True),
            ("TELERIC: DEDICATED POINT-TO-POINT", "One fiber per home; no powered splitters; upgrade only the end electronics", BLUE, False))):
        bx = x + k * (half + 24)
        p.rect(bx, t, half, h, fill=PALE, stroke=LINE, r=6)
        p.text(bx + 16, t + 24, ttl, "Body-B", 8.5, NAVY, cs=0.5)
        p.para(bx + 16, t + 30, half - 32, sub, "small")
        hy = t + 88 + 60
        hx = bx + 36
        # hub
        p.rect(hx - 20, hy - 18, 40, 36, fill=NAVY, r=4)
        p.text(hx, hy + 3, "HUB", "Body-B", 7.5, white, "c")
        homes = 8
        ys = [t + 88 + i * 17 for i in range(homes)]
        if shared:
            sx = bx + half * 0.45
            p.line(hx + 20, hy, sx - 8, hy, GREY, 2.4)
            p.c.setFillColor(GOLD)
            p.c.circle(sx, p.Y(hy), 8, stroke=0, fill=1)
            p.text(sx, hy + 22, "SPLITTER", "Body-B", 6.5, GREY, "c")
            for yy in ys:
                p.line(sx + 8, hy, bx + half - 44, yy, GREY, 0.9)
        else:
            for yy in ys:
                p.line(hx + 20, hy, bx + half - 44, yy, BLUE, 1.2)
        for yy in ys:
            p.rect(bx + half - 40, yy - 7, 14, 14, fill=SKY if not shared else HexColor("#B7C3D6"), r=2)
        p.text(bx + 16, t + h - 34, "32x" if not shared else "1x", DISPLAY, 20, GOLD if not shared else GREY)
        p.text(bx + 16, t + h - 14, "RELATIVE CAPACITY PER HOME (TELERIC-REPORTED)", "Body-B", 6.5, GREY, cs=0.3)


def stack(p, x, t, w):
    layers = [("LIVE", "Tour dates, FTV, virtual shows", "PARTNER: WALT REEDER / LIVE NATION", NAVY),
              ("CONTENT", "FRQNZY music, Westville, Legend", "OWNED IP", BLUE),
              ("PLATFORM", "DKB web, Beat Labz, Ticket, 13 modules", "OWNED IP", NAVY),
              ("DEVICE", "ToyBoxx console and controller", "OWNED DESIGN", BLUE),
              ("NETWORK", "Teleric dedicated fiber", "PROPOSED PARTNER", GOLD)]
    for i, (a, b, c_, col) in enumerate(layers):
        y = t + i * 56
        inset = (4 - i) * 0
        p.rect(x, y, w, 48, fill=col, r=6)
        fg = NAVY if col == GOLD else white
        p.text(x + 18, y + 22, a, DISPLAY, 11, fg)
        p.text(x + 18, y + 38, b, "Body", 8.5, fg)
        p.chip(x + w - 18 - (pdfmetrics_w(c_) + 20), y + 14, c_, fill=white, color=NAVY, size=6.5, h=20)
    return 5 * 56


def pdfmetrics_w(s):
    from reportlab.pdfbase import pdfmetrics
    return pdfmetrics.stringWidth(s, "Body-B", 6.5)


# =============================================================================
def page_t1(p):
    p.frame(TRACK, IDX)
    t = CONTENT_TOP
    t = p.title(t, "TELERIC: OWN THE PIPE", "FIBER ISP  •  NAPERVILLE, IL  •  FOUNDED 2015  •  FOUNDER KHALIQ REHMAN",
                "Every rival in DKB's lane rents its network from the carriers it competes with. Teleric is a fiber internet provider built "
                "to deliver dedicated gigabit service at a fraction of the usual build cost. Wired into DKB, it turns a platform into a "
                "full stack from the pipe to the pad.", size=34)
    ih = 168
    p.img("tel-006.jpg", MX, t, 168, ih, "cover", r=6)
    p.img("tel-026.jpg", MX + 184, t, 168, ih, "cover", r=6)
    p.img("tel-027.jpg", MX + 368, t, 168, ih, "cover", r=6)
    p.img("tel-032.jpg", MX + 552, t, 144, ih, "cover", r=6)
    t += ih + 8
    p.text(MX, t + 8, "Left to right: fiber bundle; traditional trenching vs. Teleric nano-trench; optical fiber. "
           "Source: Teleric pitch deck 2025.", "Body-I", 7, GREY)
    t += 28

    t += p.section_bar(t, "WHAT TELERIC SAYS IT DELIVERS", "TELERIC-REPORTED; TO BE INDEPENDENTLY VERIFIED")
    stats = [("1 Gbps", "dedicated, symmetric (equal up and down); upgradable to 400 Gbps"), ("~5 ms", "ping vs. ~70 ms industry average at peak"),
             ("~$500", "deployment cost per home vs. ~$2,000 estimated industry average"),
             ("500–600 m", "of fiber laid per day vs. 7–20 m by traditional trenching"),
             ("50+ yrs", "design life; end electronics upgraded, not the fiber")]
    cw = (CW - 4 * 12) / 5.0
    for i, (v, d) in enumerate(stats):
        x = MX + i * (cw + 12)
        p.rect(x, t, cw, 104, fill=NAVY if i in (0, 2) else PALE, stroke=None if i in (0, 2) else LINE, r=4)
        p.text(x + 12, t + 34, v, DISPLAY, 17, SKY if i in (0, 2) else BLUE)
        p.para(x + 12, t + 44, cw - 24, d, S("ts", 7.5, 10, HexColor("#C9DDF5") if i in (0, 2) else GREY))
    t += 124

    t += p.section_bar(t, "WHY IT IS A DIFFERENT KIND OF NETWORK", "ARCHITECTURE ADVANTAGE")
    pon_diagram(p, MX, t, CW, 232)
    t += 248
    p.text(MX, t + 8, "Diagram simplified from Teleric's architecture slides. Capacity figure is Teleric's own claim.", "Body-I", 7, GREY)
    t += 28

    t += p.section_bar(t, "THE MARKET GAP IT ATTACKS", "FCC FORM 477, JUNE 2024, AS CITED BY TELERIC")
    gap = [("128.9M", "U.S. households"), ("47%", "had no 1 Gbps provider"), ("42%", "had only one 1 Gbps option"),
           ("~43M", "households whose current speed is below 1 Gbps (Teleric estimate)")]
    gw = (CW - 3 * 12) / 4.0
    for i, (v, d) in enumerate(gap):
        x = MX + i * (gw + 12)
        p.rect(x, t, gw, 80, fill=PALE, stroke=LINE, r=4)
        p.text(x + 14, t + 36, v, DISPLAY, 22, NAVY)
        p.para(x + 14, t + 44, gw - 28, d, "small")
    t += 96
    p.check(t, "page_t1")


# =============================================================================
def page_t2(p):
    p.frame(TRACK, IDX, cont=True)
    t = CONTENT_TOP
    t = p.title(t, "HOW TELERIC MAKES DKB DEADLY", "SEVEN FORCE MULTIPLIERS: WHAT EACH DOES, AND WHAT IT STILL NEEDS",
                "Most entertainment platforms are tenants on someone else's network. DKB with Teleric is aligned from content to "
                "connection: cheaper bandwidth, a billing relationship with the household, and infrastructure no rival "
                "can copy quickly.", size=32)
    h = stack(p, MX, t, 336)
    # callout beside stack
    cx = MX + 352
    cw = CW - 352
    p.rect(cx, t, cw, h - 8, fill=ICE, r=6)
    p.rect(cx, t, 4, h - 8, fill=GOLD)
    p.text(cx + 20, t + 26, "THE VERTICAL STACK", "Body-B", 9, NAVY, cs=0.7)
    p.para(cx + 20, t + 36, cw - 36, "A fan hears a record, buys a ticket, joins DKB, makes a beat in Beat Labz, plays Westville on a "
           "ToyBoxx, and does it over one fiber line. Each layer feeds the next, and each layer is another reason not to leave.",
           "card")
    p.text(cx + 20, t + 118, "WHAT RIVALS RENT", "Body-B", 8, BLUE, cs=0.6)
    p.bullets(cx + 20, t + 128, cw - 36, ["Streaming apps rent bandwidth from ISPs and CDNs.", "Ticketers rent venue networks.",
                                         "Console makers depend on third-party ISPs for downloads and multiplayer."], "bulc")
    p.para(cx + 20, t + 192, cw - 36, "<b>Not ownership.</b> Teleric is a separate company. The stack is aligned through contracts and "
           "co-branding, not a claim that DKB owns the network.", "small")
    t += h + 24

    mult = [
        ("01", "SYMMETRIC UPLOAD FOR CREATORS", "Cable upload is a fraction of download. Producers uploading stems, streamers going live and "
         "KickTok creators posting video all live on upload. Equal up and down speed is a creator feature.", "Fits: Beat Labz, FTV, KickTok"),
        ("02", "LOW LATENCY FOR REAL-TIME", "Teleric reports ~5 ms ping. That is the budget remote co-production, rap battles and cloud-streamed "
         "Westville need. End-to-end latency still depends on DKB's servers and routing.", "Fits: battles, jam sessions, cloud play"),
        ("03", "VENUE BACKHAUL AT DKB NIGHTS", "Fiber to the venue gives the Wi-Fi that handles ticket scans, account sign-ups and live voting a "
         "reliable uplink. Wi-Fi radios and cabling are separate costs; Chicago-area dates come first.", "Fits: tour funnel, Evan Shive's Wi-Fi"),
        ("04", "BUNDLE ON THE INTERNET BILL", "An ISP has a monthly bill and a household. Carriers routinely bundle streaming subscriptions; "
         "a DKB tier, ToyBoxx financing and Beat Labz can ride the same invoice and cut churn.", "Fits: subscriptions, ToyBoxx"),
        ("05", "CHEAP BUILD, SMART TARGETS", "At ~$500 per home Teleric can economically wire studios, creator hubs, venues and partner schools "
         "for DKB's education pathway, including areas that qualify for broadband grants (verify current rules).", "Fits: education, creator hubs"),
        ("06", "EDGE DELIVERY", "Where Teleric is lit, DKB can cache Westville builds, FTV streams and tape drops close to the fan, lowering "
         "delivery cost per gigabyte. Planned, not built.", "Fits: Westville, FTV, DaKickTapes"),
        ("07", "BRAND + ACTIVATION INVENTORY", "Teleric already runs branded trailers and billboards (“Master of Faster”). At tour dates that "
         "becomes a sponsor-style activation: signups, speed demos, free-trial offers beside the DKB ticket booth.", "Fits: tour, sponsorship"),
    ]
    cw3 = (CW - 16) / 2.0
    for i, (n, a, b, tag) in enumerate(mult):
        col, row = i % 2, i // 2
        x = MX + col * (cw3 + 16)
        y = t + row * 120
        if i == 6:
            x, cw_ = MX, CW
        else:
            cw_ = cw3
        p.rect(x, y, cw_, 104, fill=PALE, stroke=LINE, r=4)
        p.rect(x, y, 4, 104, fill=BLUE if i % 2 == 0 else NAVY)
        p.text(x + 18, y + 30, n, DISPLAY, 18, BLUE)
        p.text(x + 58, y + 24, a, "Body-B", 9, NAVY, cs=0.3)
        p.para(x + 58, y + 30, (cw_ - 76) - (216 if i == 6 else 0), b, "card")
        if i == 6:
            p.img("tel-067.jpg", x + cw_ - 220, y + 8, 208, 88, "cover", r=6)
        p.chip(x + 58, y + 104 - 28, tag, fill=ICE, color=NAVY, size=7, h=18, padx=8)
    t += 4 * 120
    p.check(t, "page_t2")


# =============================================================================
def page_t3(p):
    p.frame(TRACK, IDX, cont=True)
    t = CONTENT_TOP
    t = p.title(t, "FROM PILOT TO PARTNER", "WHERE TELERIC IS TODAY, THE DEAL FRAMEWORK, AND THE FINE PRINT",
                "Teleric is early. The upside is real because the technology gap is real, and the honest picture below is what lets "
                "@@INV@@ value it correctly.", size=34)
    # deployment photos
    ih = 144
    ws = [200, 96, 96, 96, 152]
    imgs = ["tel-054.jpg", "tel-060.jpg", "tel-062.jpg", "tel-063.jpg", "tel-068.jpg"]
    x = MX
    gap = (CW - sum(ws)) / 4.0
    for nm, w in zip(imgs, ws):
        p.img(nm, x, t, w, ih, "cover", r=6)
        x += w + gap
    t += ih + 8
    p.text(MX, t + 8, "Elk Grove Village drilling; Lisle trench, fiber laid, restored; neighborhood billboard. Source: Teleric pitch deck 2025.",
           "Body-I", 7, GREY)
    t += 28

    t += p.section_bar(t, "FOOTPRINT AND ROADMAP (TELERIC-REPORTED)", "ILLINOIS PILOT FIRST")
    cols = [("PHASE", 130, "l"), ("WHAT", 400, "l"), ("STATUS", 166, "l")]
    rows = [["<b>2021 Test bed</b>", "50 office units inside Teleric's Naperville headquarters park; platform for new services.", "Built"],
            ["<b>2022–25 First markets</b>", "Permitting for 5,000 homes and businesses across 3 towns; Elk Grove Village business district; Lisle 280-unit apartment complex plus ~3,000 adjacent homes.", "In progress"],
            ["<b>2026 Expansion</b>", "Contiguous neighborhoods and arterial roads; priority on areas without high-speed options; state grants where eligible.", "Planned"],
            ["<b>2026+ Major markets</b>", "Ten second-tier U.S. markets (towns of 50,000+ homes) via franchise / licensing model.", "Planned"]]
    h = table(p, MX, t, cols, rows)
    t += h + 16

    t += p.section_bar(t, "TELERIC'S OWN UNIT ECONOMICS", "$70 / MONTH PER SUBSCRIBER, AS REPORTED; NO DKB ATTACH ASSUMED")
    cols = [("SUBSCRIBERS", 140, "l"), ("MONTHLY REVENUE", 180, "r"), ("ANNUAL REVENUE", 180, "r"), ("DKB ANGLE", 196, "l")]
    rows = []
    notes = {100: "Pilot; bundle test", 500: "First creator hubs", 1000: "Funding target; first venues", 2000: "Regional footprint", 5000: "Revenue-share pool cap"}
    for n in (100, 500, 1000, 2000, 5000):
        rows.append(["<b>{:,}</b>".format(n), "${:,.0f}".format(n * 70), "${:,.0f}".format(n * 70 * 12), notes[n]])
    h = table(p, MX, t, cols, rows)
    t += h + 8
    t += p.para(MX, t, CW, "Teleric is seeking $150K to reach 1,000 homes and businesses, with a 33% perpetual revenue-share pool "
                "(pool $300K as of 12/31/24; $450K target). That capital is Teleric's own raise; it is <b>not</b> part of the $2M DKB use of funds.", "small")
    t = s8(t + 16)

    t += p.section_bar(t, "DKB x TELERIC: PARTNERSHIP FRAMEWORK", "NOT AGREED TERMS")
    fw = [("PREFERRED INFRASTRUCTURE", "Preferred-rate service for DKB studios, hubs and Chicago-area venues."),
          ("“DKB FIBER” TIER", "Co-branded plan and bundle with revenue share on attached DKB subscriptions."),
          ("TOUR ACTIVATION", "Teleric trailer and sign-up booth at tour dates, as sponsor-style inventory."),
          ("EDGE HOSTING FIRST-LOOK", "First option to host Westville, FTV and tape-drop edge caches."),
          ("ROLES IN WRITING", "Evan Shive's role and any DKB-Teleric equity or fee terms papered by counsel.")]
    kw = (CW - 4 * 12) / 5.0
    hh = max(p.card_h(kw, a, b, 12) for a, b in fw) + 4
    for i, (a, b) in enumerate(fw):
        p.card(MX + i * (kw + 12), t, kw, s8(hh), a, b, accent=GOLD if i == 4 else BLUE, fill=PALE)
    t += s8(hh) + 16

    # fine print
    items = ["<b>Claims are Teleric's own.</b> Speed, latency, cost and the “patented” status need independent tests and patent filings in diligence. "
             "Shallow micro-trenching failed for Google Fiber in Louisville (per Teleric's deck), so nano-trench durability data matters.",
             "<b>Footprint is local.</b> Today's lit areas are in Illinois. Tour dates elsewhere use carrier backhaul until a Teleric market exists.",
             "<b>Market size.</b> Teleric's “$20B for 10% of households” does not reconcile with its own $70 / month price (10% of 128.9M homes "
             "× $840 ≈ $10.8B per year). We use per-subscriber economics only.",
             "<b>Relationships.</b> Teleric's deck does not mention DKB or Evan Shive; the connection to DKB must be documented before it is relied on."]
    hb = p.bullets_h(CW - 40, items, "bulc", 2) + 52
    p.rect(MX, t, CW, s8(hb), fill=AMBER_BG, r=6)
    p.rect(MX, t, 4, s8(hb), fill=GOLD)
    p.text(MX + 20, t + 26, "THE HONEST FINE PRINT", "Body-B", 9, AMBER_FG, cs=0.7)
    p.bullets(MX + 20, t + 38, CW - 40, items, "bulc", 2)
    t += s8(hb)
    p.check(t, "page_t3")
