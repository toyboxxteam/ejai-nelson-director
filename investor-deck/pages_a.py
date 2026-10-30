"""Pages 01-03 of the DKB investor deck."""
import math

from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics

from dkb_lib import *


# =============================================================================
# 01  EXECUTIVE SUMMARY
# =============================================================================
def page01(p):
    p.frame("01 / EXECUTIVE SUMMARY & LAUNCH ARCHITECTURE", "01 / 07")
    # logo row (isolated zone below the running header)
    p.img("i-001.jpg", MX, 128, 48, 48, "contain")
    p.img("i-002.jpg", MX + 64, 136, 72, 40, "contain")
    p.line(MX + 152, 128, MX + 152, 176, LINE, 1)
    p.text(MX + 168, 148, "CONFIDENTIAL / OCTOBER 2026", "Body-B", 8.5, BLUE, cs=0.6)
    p.text(MX + 168, 164, "PREPARED FOR DR. ISH", "Body-B", 8.5, NAVY, cs=0.6)

    # navy banner
    p.rect(MX, 200, CW, 96, fill=NAVY, r=6)
    p.rect(MX, 200, 6, 96, fill=BLUE)
    p.text(MX + 28, 242, "AN INTEGRATED ENTERTAINMENT", DISPLAY, 32, white)
    p.text(MX + 28, 278, "& CREATOR ECONOMY", DISPLAY, 32, SKY)
    p.text(W - MX - 24, 280, "DKB / MUSIC / GAMES / HARDWARE / LIVE EVENTS", "Body-B", 7.5, SKY, "r", cs=0.6)

    # hero
    p.rect(MX, 320, 272, 232, fill=PALE, stroke=LINE, r=6)
    p.img("i-003.jpg", MX + 16, 340, 240, 192, "contain")
    rx = MX + 304
    rw = CW - 304
    p.text(rx, 338, "THE $2,000,000 LAUNCH OPPORTUNITY", "Body-B", 9, BLUE, cs=0.7)
    p.text(rx - 2, 394, "$2M", DISPLAY, 58, NAVY)
    h = p.para(rx, 410, rw, "<b>DaKickBack (DKB)</b> is a proposed connected entertainment system: touring builds "
               "audiences; music and creators sustain daily engagement; <b>Welcome 2 Westville</b> turns the culture "
               "into an interactive world; <b>ToyBoxx</b> makes it tangible; and the DKB network organizes commerce, "
               "media and fan support.", "body")
    ny = s8(410 + h + 8)
    nh = 552 - ny
    p.rect(rx, ny, rw, nh, fill=ICE, r=4)
    p.rect(rx, ny, 4, nh, fill=BLUE)
    p.text(rx + 16, ny + 18, "A PERSONAL NOTE TO DR. ISH", "Body-B", 8, NAVY, cs=0.5)
    p.para(rx + 16, ny + 26, rw - 32, "Dr. Ish, we sincerely appreciate your generous $2 million offer to help bring DKB "
           "to market. We intend to earn that trust through controlled draws, measurable launch milestones, "
           "artist-led audience growth and transparent investor reporting. This proposal does not seek more than "
           "$2 million.", "card")

    # deal at a glance
    t = 576
    cells = [("$2,000,000", "TOTAL RAISE / HARD CAP"), ("100%", "NET TOUR + MERCH TO PRINCIPAL FIRST"),
             ("50 / 50", "PERMANENT NET SPLIT AFTER RECOUPMENT"), ("1%", "PUBLISHING ON ALL 365 FRQNZY SONGS"),
             ("$75K", "BONUS ON DEFINED LABEL MILESTONE")]
    cw = (CW - 4 * 8) / 5.0
    for i, (v, l) in enumerate(cells):
        x = MX + i * (cw + 8)
        p.rect(x, t, cw, 64, fill=NAVY if i == 0 else PALE, stroke=None if i == 0 else LINE, r=4)
        p.text(x + 12, t + 30, v, DISPLAY, 19, white if i == 0 else BLUE)
        p.para(x + 12, t + 38, cw - 20, l, S("dl", 7, 9, SKY if i == 0 else GREY, "Body-B"))

    # pillars
    t = 656
    t += p.section_bar(t, "SIX CONNECTED COMMERCIAL PILLARS", "ONE AUDIENCE / MULTIPLE OFFERINGS")
    pillars = [("LIVE EVENTS", "Touring, sponsor packages, tickets", BLUE),
               ("MUSIC", "Recordings, radio, video, licensing", NAVY),
               ("DKB WEB", "Creator tools, profiles, ticketing", BLUE),
               ("GAMES", "Westville + Legend of Frqnzy", NAVY),
               ("TOYBOXX", "Console, accessories, real goods", BLUE),
               ("INFRASTRUCTURE", "Event connectivity, distribution", NAVY)]
    cw = (CW - 32) / 3.0
    for i, (a, b, col) in enumerate(pillars):
        x = MX + (i % 3) * (cw + 16)
        y = t + (i // 3) * 72
        p.card(x, y, cw, 64, a, b, accent=col, fill=PALE)
    t += 144

    # markets
    t += p.section_bar(t, "WHY THESE MARKETS MATTER", "PUBLIC INDUSTRY DATA / NOT DKB REVENUE")
    mk = [("$60.8B", "U.S. video game spending, 2025"), ("$31.7B", "Global recorded music, 2025"),
          ("$25.2B", "Live Nation revenue, 2025")]
    for i, (v, l) in enumerate(mk):
        x = MX + i * (cw + 16)
        p.rect(x, t, cw, 64, fill=PALE, stroke=LINE, r=4)
        p.text(x + 16, t + 36, v, DISPLAY, 26, NAVY)
        p.text(x + 16, t + 54, l, "Body-B", 8.5, GREY)
    t += 76
    t += p.para(MX, t, CW, "<b>Investment framing:</b> DKB's launch involves both active music collaborations and an "
                "ambitious platform roadmap. Commercial performance depends on execution, rights, delivery and costs. "
                "Public market sizes are context, not DKB sales or valuation. Sources: ESA (revised 2025 figures); "
                "IFPI Global Music Report 2026; Live Nation FY2025.", "small")
    t = s8(t + 16)

    # milestone gate
    t += p.section_bar(t, "THE LAUNCH WILL BE MILESTONE-GATED", "A PRACTICAL $2M START")
    steps = [("01", "CONTRACT & LAUNCH", "Confirm bookings, clearance, financial controls and opt-in artist campaigns."),
             ("02", "PROVE PRODUCT", "Release core DKB ticketing / creator tools and a measured Westville experience."),
             ("03", "REINVEST ON SIGNAL", "Expand only against verified demand, margins, prototypes and settlements.")]
    for i, (n, a, b) in enumerate(steps):
        x = MX + i * (cw + 16)
        p.rect(x, t, cw, 72, fill=PALE, stroke=LINE, r=4)
        p.text(x + 12, t + 30, n, DISPLAY, 22, BLUE)
        p.text(x + 52, t + 24, a, "Body-B", 9, NAVY, cs=0.4)
        p.para(x + 52, t + 32, cw - 64, b, "card")
        if i < 2:
            p.arrow(x + cw + 1, t + 36, x + cw + 15, t + 36, BLUE, 1.4, 5)
    t += 88
    p.rect(MX, t, CW, 40, fill=NAVY, r=4)
    p.text(W / 2.0, t + 25, "ONE $2M COMMITMENT.  ONE ACCOUNTABLE BUILD-AND-LAUNCH PLAN.", "Body-B", 11, white, "c", cs=0.8)
    p.check(t + 40, "page01")


# =============================================================================
# 02  FOUNDER & TRACTION
# =============================================================================
def page02(p):
    p.frame("02 / FOUNDER, CREDIBILITY & LAUNCH", "02 / 07")
    t = CONTENT_TOP
    t = p.title(t, "MUSIC, MUSIC, MORE MUSIC", None,
                "The founder's music, existing chart history and booked collaborations are the marketing engine "
                "behind the platform launch.")
    # hero strip
    h = 224
    p.img("i-008.jpg", MX, t, 272, h, "cover", r=6)
    p.img("i-009.jpg", MX + 288, t, 200, h, "cover", r=6, stroke=LINE)
    p.img("i-010.jpg", MX + 504, t, 192, h, "cover", r=6, stroke=LINE)
    t += h + 8
    p.text(MX + 288, t + 8, "Billboard-related chart history reported; exact week pending", "Body-I", 7.5, GREY)
    t += 32

    # founder
    p.text(MX, t + 10, "MALCOLM “FRQNZY” HENDERSON", DISPLAY, 15, NAVY)
    p.text(W - MX, t + 10, "FOUNDER / MUSIC ARTIST / CREATIVE DIRECTOR", "Body-B", 7.5, BLUE, "r", cs=0.5)
    t += 24
    t += p.para(MX, t, CW, "Founder of DaKickBack and Good Karma Music Group, FRQNZY is the recording and creative face "
                "of the DKB artist-to-fan launch. His submitted chart evidence includes <b>“Unify” at #64 on an "
                "R&amp;B/Hip-Hop sales chart</b>, a displayed <b>#1 Amazon R&amp;B bestseller placement for “Thing On "
                "Me”</b>, and international song rankings. Management also reports Billboard chart appearances; "
                "exact Billboard chart names, dates and positions will be provided with archival records. The 365-song "
                "campaign is built around radio-quality releases across genres, not placeholder tracks.", "body")
    t = s8(t + 16)

    t += p.section_bar(t, "RADIO-QUALITY SONG-A-DAY + ALBUM PROGRAM", "BUILD AUDIENCE FIRST")
    stats = [("365", "SONG-A-DAY CAMPAIGN", "An original-song-each-day campaign intended for Guinness consideration."),
             ("1,500+", "CATALOG MASTER VAULT", "Management-stated archive; rights schedules support diligence."),
             ("14–121", "DAY PROMOTION WINDOW", "Artist profile, collaboration, video and targeted radio campaign.")]
    cw = (CW - 32) / 3.0
    for i, (v, a, b) in enumerate(stats):
        x = MX + i * (cw + 16)
        p.rect(x, t, cw, 96, fill=PALE, stroke=LINE, r=4)
        p.text(x + 16, t + 36, v, DISPLAY, 28, BLUE)
        p.text(x + 16, t + 54, a, "Body-B", 8, NAVY, cs=0.5)
        p.para(x + 16, t + 62, cw - 32, b, "card")
    t += 112

    # relationships + artwork
    t += p.section_bar(t, "CREATIVE RELATIONSHIPS AND TOUR ACTIVATION", "EVIDENCE VS PROPOSED ACCESS")
    ih = 232
    x = MX
    for nm, w in (("i-011.jpg", 190), ("i-012.jpg", 107), ("i-013.jpg", 107), ("i-014.jpg", 107)):
        p.img(nm, x, t, w, ih, "cover", r=6, stroke=LINE)
        x += w + 12
    p.card(x + 4, t, MX + CW - x - 4, ih, "BUSINESS USE", "Pair music-video releases with city-specific radio campaigns, "
           "profile signups, ticket registration and recorded music monetization.", accent=BLUE, fill=ICE, bar="left")
    t += ih + 8
    p.text(MX, t + 10, "Creative campaign: Teddy Riley is producing \u201cAll Good\u201d", "Body-I", 7.5, GREY)
    t += 32

    cw2 = (CW - 16) / 2.0
    hh = p.cards_row(MX, t, CW, [
        ("365-SONG CAMPAIGN / ALBUM", "A 365-day sequence of original multi-genre songs is designed for Guinness World "
         "Records consideration. A 17-song Teddy Riley / FRQNZY album is in development; management reports Teddy is "
         "currently producing “All Good” featuring Teddy Riley and Ty Dolla $ign."),
        ("FEATURED RELEASE PIPELINE", "“The Vibe” with Slim (112); “Love Don't Live Here” with AMG Twins; "
         "“DaKickBack” featuring Future; “Unmatched” featuring GloRilla; “Victim” featuring "
         "Krayzie Bone. Status varies by recording and agreement.")], bar="left", fill=ICE)
    t += hh + 8
    p.text(MX, t + 8, "Source: user-supplied founder photographs, chart captures, tour artwork and management draft.",
           "Body-I", 7, GREY)
    p.check(t + 8, "page02")


# =============================================================================
# 03  LIVE ENTERTAINMENT (revised) -- part A
# =============================================================================
HEAD = [("GloRilla", 1), ("Future", 1), ("Bossman Dlow", 1), ("G-Herbo", 1), ("Luh Tyler", 1), ("Key Glock", 1),
        ("Sexyy Red", 1), ("Babyface Ray", 1), ("21 Savage", 1), ("Rod Wave", 1), ("Gunna", 1), ("Doechii", 1)]
LEGACY = [("Bone Thugs-N-Harmony", 1), ("Krayzie Bone", 0), ("Teddy Riley", 0), ("Slim (112)", 1), ("AMG Twins", 0),
          ("Charlie Wilson", 1), ("Guy", 1), ("Keith Sweat", 1), ("Dru Hill", 1), ("Jagged Edge", 1)]
DEPTH = [("DJ Quik", 1), ("Slick Rick", 1), ("Big Daddy Kane", 1), ("Case", 1), ("J Holiday", 1), ("Adina Howard", 1)]


def _roster_block(p, x, t, w, label, sub, items, fill, color):
    p.text(x, t + 9, label, "Body-B", 8.5, NAVY, cs=0.5)
    p.text(x + w, t + 9, sub, "Body-B", 7, BLUE, "r", cs=0.4)
    names = [n + ("" if v else " †") for n, v in items]
    h = p.chips(x, t + 20, w, names, fill=fill, color=color, h=22, size=8.5)
    return 20 + h


def page03a(p):
    p.frame("03 / LIVE ENTERTAINMENT & GLOBAL TOURING FLYWHEEL", "03 / 07")
    t = CONTENT_TOP
    t = p.title(t, "THE DAKICKBACK TOUR", "TURNKEY TALENT ENGINE & LIVE NATION DISTRIBUTION",
                "The DKB Tour pairs legendary and elite contemporary talent directly with FRQNZY collaborations, turning "
                "every live arena and theater date into an onboarding engine for the DKB Platform, where fans register, "
                "stream, and buy tickets exclusively.")

    # route banner
    p.rect(MX, t, CW, 96, fill=NAVY, r=6)
    p.rect(MX, t, 6, 96, fill=BLUE)
    p.text(MX + 28, t + 38, "EAST COAST  →  WEST COAST  →  GERMANY / UAE (OPTIONAL)", DISPLAY, 17, white)
    p.para(MX + 28, t + 52, CW - 56, "East Coast route culminating with Babyface Ray; FRQNZY and Krayzie Bone on the West "
           "Coast. Management is actively exploring Germany and UAE routing as incremental international markets.",
           "whiteS")
    t += 120

    # [1] Walt Reeder
    p.rect(MX, t, 28, 28, fill=BLUE, r=14)
    p.text(MX + 14, t + 19, "1", DISPLAY, 13, white, "c")
    p.text(MX + 40, t + 19, "THE WALT REEDER TURNKEY ADVANTAGE: IN-HOUSE BOOKING EFFICIENCY", "Body-B", 11, NAVY, cs=0.4)
    t += 44
    t += p.para(MX, t, CW, "<b>Walt Reeder Entertainment</b> (management-described as the nation's premier Black-owned "
                "talent agency; Senior Talent Buyer &amp; Partner with the Black Promoters Collective) serves as DKB's "
                "direct routing and booking engine.", "body")
    t = s8(t + 12)

    cw2 = (CW - 16) / 2.0
    hh = p.cards_row(MX, t, CW, [
        ("WHOLESALE BELOW-MARKET PRICING", "Because roster talent is signed and aligned directly through Walt Reeder's "
         "institutional pipeline, DKB targets booking fees at internal wholesale rates—drastically lowering upfront "
         "guarantees compared to open-market talent buys. Final rates are set in each executed talent agreement."),
        ("LIVE NATION WHOLESALE-TO-PROMOTER ARBITRAGE", "Walt Reeder packages and sells the DKB Tour directly into Live "
         "Nation venue networks and global routing circuits. DKB controls artist curation, co-branded stage production "
         "and exclusive ticketing integration while offloading venue risk and maximizing tour settlement profits.",
         NAVY)], bar="top", fill=PALE)
    t += hh + 16

    # roster
    p.text(MX, t + 10, "CURATED ROSTER ALIGNMENT — FRQNZY COLLABORATIONS & CO-BILLS", "Body-B", 10, NAVY, cs=0.5)
    p.line(MX, t + 18, W - MX, t + 18, LINE)
    t += 32
    t += _roster_block(p, MX, t, CW, "CURRENT & ELITE HEADLINERS", "12 ARTISTS", HEAD, NAVY, white) + 12
    t += _roster_block(p, MX, t, CW, "LEGACY ICONS & HITMAKERS", "10 ARTISTS", LEGACY, BLUE, white) + 12
    t += _roster_block(p, MX, t, CW, "STRATEGIC ROSTER DEPTH — $10K–$15K ROSTER TIER",
                       "HIGH-MARGIN SUPPORT ACTS", DEPTH, ICE, NAVY) + 8
    t += p.para(MX, t, CW, "High-margin support acts and regional heavyweights deployed for maximum ROI. "
                "<b>†</b> DKB-direct collaboration or booking—not listed on the Walt Reeder Entertainment 2026 roster "
                "sheet. All other names appear on that roster; availability and pricing are confirmed per date.", "small")
    t = s8(t + 16)

    # Live Nation chain
    p.text(MX, t + 10, "THE DISTRIBUTION CHAIN: FROM ROSTER TO ROOM TO PLATFORM", "Body-B", 10, NAVY, cs=0.5)
    p.line(MX, t + 18, W - MX, t + 18, LINE)
    t += 32
    nodes = [("WALT REEDER", "Roster access at wholesale rates", NAVY),
             ("DKB TOUR", "Curation, co-branded production, ticketing", BLUE),
             ("LIVE NATION NETWORK", "Venue routing, venue risk offloaded", NAVY),
             ("FAN → DKB ACCOUNT", "Register, stream, buy, subscribe", BLUE)]
    nw = (CW - 3 * 24) / 4.0
    for i, (a, b, col) in enumerate(nodes):
        x = MX + i * (nw + 24)
        p.rect(x, t, nw, 80, fill=col, r=6)
        p.text(x + nw / 2.0, t + 30, a, "Body-B", 9, white, "c", cs=0.4)
        p.para(x + 10, t + 40, nw - 20, '<para alignment="center">%s</para>' % b, "whiteS")
        if i < 3:
            p.arrow(x + nw + 3, t + 40, x + nw + 21, t + 40, GOLD, 2.2, 7)
    t += 96
    p.check(t, "page03a-chain")

    # [2] funnel
    p.rect(MX, t, 28, 28, fill=BLUE, r=14)
    p.text(MX + 14, t + 19, "2", DISPLAY, 13, white, "c")
    p.text(MX + 40, t + 19, "THE MANDATORY DKB TICKETING & FAN CONVERSION FUNNEL", "Body-B", 11, NAVY, cs=0.4)
    t += 40
    t += p.para(MX, t, CW, "Every show is engineered as a viral customer-acquisition vehicle for DKB:", "body")
    t = s8(t + 8)
    steps = [("01  EXCLUSIVE / PRIMARY DKB TICKET PORTAL", "Tickets, VIP upgrades and meet-and-greets are funneled through the "
              "DKB platform. To purchase tickets, attend, or claim exclusive merch, fans register a DKB account."),
             ("02  IN-VENUE MOBILE ENGAGEMENT", "Evan Shive's high-density infrastructure powers live interactive event "
              "Wi-Fi, driving in-arena streaming of FRQNZY's catalogue, instant profile creation, and real-time voting "
              "on Westville leaderboards."),
             ("03  POST-SHOW FAN LIFETIME VALUE", "Attendees transition from one-night concertgoers into active monthly "
              "subscribers, streamers on DKB Hot 100, and players inside Welcome 2 Westville.")]
    hh = p.cards_row(MX, t, CW, steps, gap=16, bar="top", fill=PALE)
    t += hh
    p.check(t, "page03a")


# =============================================================================
# 03  LIVE ENTERTAINMENT (revised) -- part B
# =============================================================================
SCEN = [  # name, dates, cap, avg, gross, net, note
    ("REGIONAL LAUNCH", 4, 1200, 65, 312000, 140000, "Theaters / mid-size"),
    ("NATIONAL CIRCUIT", 8, 2400, 85, 1632000, 750000, "Major metros"),
    ("ARENA / LIVE NATION AMPLIFIED", 16, 4000, 75, 4800000, 2150000, "Live Nation amphitheaters"),
    ("GLOBAL PHENOMENON", 24, 5000, 80, 9600000, 4200000, "US arenas + Germany / UAE"),
]


def money(v):
    if v >= 1e6:
        return "$%.2fM" % (v / 1e6)
    return "${:,.0f}".format(v)


def flywheel(p, cx, cy, r):
    c = p.c
    nodes = [("RADIO-FIRST SINGLE", "joint record + video drops\n14–121 days out"),
             ("LIVE DATE", "co-headline moment,\nWalt Reeder / Live Nation"),
             ("DKB TICKET + ACCOUNT", "mandatory registration"),
             ("STREAM + PLAY", "Hot 100, FTV, Westville"),
             ("MERCH + TOYBOXX", "collectibles, console,\nsubscriptions"),
             ("NEXT MARKET", "fans carry the record\ninto the next date")]
    n = len(nodes)
    # ring
    c.setStrokeColor(ICE)
    c.setLineWidth(14)
    c.circle(cx, p.Y(cy), r, stroke=1, fill=0)
    c.setStrokeColor(BLUE)
    c.setLineWidth(1.4)
    c.setDash(3, 4)
    c.circle(cx, p.Y(cy), r, stroke=1, fill=0)
    c.setDash()
    # centre
    c.setFillColor(NAVY)
    c.circle(cx, p.Y(cy), r * 0.5, stroke=0, fill=1)
    p.text(cx, cy - 6, "DKB", DISPLAY, 26, white, "c")
    p.text(cx, cy + 12, "FAN FLYWHEEL", "Body-B", 8, SKY, "c", cs=0.8)
    for i, (a, b) in enumerate(nodes):
        ang = -math.pi / 2 + i * 2 * math.pi / n
        nx, ny = cx + r * math.cos(ang), cy + r * math.sin(ang)
        c.setFillColor(BLUE if i % 2 == 0 else NAVY)
        c.circle(nx, p.Y(ny), 13, stroke=0, fill=1)
        p.text(nx, ny + 4.5, str(i + 1), DISPLAY, 11, white, "c")
        # label placement
        lx = cx + (r + 30) * math.cos(ang)
        ly = cy + (r + 30) * math.sin(ang)
        al = "c" if abs(math.cos(ang)) < 0.2 else ("l" if math.cos(ang) > 0 else "r")
        if al == "c":
            ly += -6 if math.sin(ang) < 0 else 16
        p.text(lx, ly, a, "Body-B", 8, NAVY, al, cs=0.3)
        for k, ln in enumerate(b.split("\n")):
            p.text(lx, ly + 10 + 10 * k, ln, "Body", 7.5, GREY, al)
        # arrow along ring to next
        a2 = ang + (2 * math.pi / n) * 0.5
        ax, ay = cx + r * math.cos(a2), cy + r * math.sin(a2)
        tang = a2 + math.pi / 2
        p.arrow(ax - 5 * math.cos(tang), ay - 5 * math.sin(tang), ax + 5 * math.cos(tang), ay + 5 * math.sin(tang),
                BLUE, 1.5, 7)


def page03b(p):
    p.frame("03 / LIVE ENTERTAINMENT & GLOBAL TOURING FLYWHEEL", "03 / 07", cont=True)
    t = CONTENT_TOP
    p.rect(MX, t, 28, 28, fill=BLUE, r=14)
    p.text(MX + 14, t + 19, "3", DISPLAY, 13, white, "c")
    p.text(MX + 40, t + 19, "SCALED TOUR PROJECTIONS: EXPANDED ROUTING CAPACITY (WHOLESALE TALENT BASIS)", "Body-B", 11, NAVY, cs=0.4)
    t += 48

    # table
    cols = [("SCENARIO", MX + 12, "l"), ("ROUTING & SCALE", MX + 214, "l"), ("AVG TICKET GROSS", MX + 470, "r"),
            ("EST. NET TO DKB FLYWHEEL", MX + CW - 12, "r")]
    p.rect(MX, t, CW, 32, fill=NAVY, r=4)
    for lab, x, al in cols:
        p.text(x, t + 20, lab, "Body-B", 7.5, white, al, cs=0.5)
    t += 32
    rh = 48
    for i, (n, d, cap, avg, g, net, note) in enumerate(SCEN):
        p.rect(MX, t, CW, rh, fill=PALE if i % 2 == 0 else white, stroke=LINE)
        p.text(MX + 12, t + 21, n, "Body-B", 9.5, NAVY)
        p.text(MX + 12, t + 35, note, "Body", 8, GREY)
        p.text(MX + 214, t + 21, "%d Dates" % d + ("+" if i == 3 else ""), "Body-B", 9.5, INK)
        p.text(MX + 214, t + 35, "%s cap @ $%d avg" % ("{:,}".format(cap) + ("+" if i == 3 else ""), avg), "Body", 8, GREY)
        p.text(MX + 470, t + 29, money(g) + ("+" if i == 3 else ""), DISPLAY, 13, NAVY, "r")
        p.text(MX + CW - 12, t + 29, money(net) + "+", DISPLAY, 13, BLUE, "r")
        t += rh
    # downside row (carried from prior draft)
    p.rect(MX, t, CW, 48, fill=white, stroke=LINE)
    p.text(MX + 12, t + 22, "DOWNSIDE FLOOR (PRIOR DRAFT)", "Body-B", 8.5, GREY)
    p.text(MX + 12, t + 36, "Carried forward for investor transparency", "Body", 8, GREY)
    p.text(MX + 214, t + 22, "2 Dates", "Body-B", 9.5, INK)
    p.text(MX + 214, t + 36, "600 cap @ $55 avg", "Body", 8, GREY)
    p.text(MX + 470, t + 29, "$66,000", DISPLAY, 12, GREY, "r")
    p.text(MX + CW - 12, t + 29, "Not projected", "Body-I", 9, GREY, "r")
    t += 48
    t += 8
    t += p.para(MX, t, CW, "Gross = dates × capacity × average ticket. Net figures are management estimates after talent, "
                "production, venue, marketing and settlement costs; “defined net” will be fixed in the written agreement "
                "and is not a guarantee of investor cash.", "src")
    t = s8(t + 16)

    # chart: net vs $2M principal
    p.text(MX, t + 10, "NET TO DKB FLYWHEEL vs. THE $2,000,000 PRINCIPAL", "Body-B", 10, NAVY, cs=0.5)
    p.text(W - MX, t + 10, "FIRST-DOLLAR WATERFALL COVERAGE", "Body-B", 7.5, BLUE, "r", cs=0.5)
    p.line(MX, t + 18, W - MX, t + 18, LINE)
    t += 36
    ax0 = MX + 176
    aw = CW - 176 - 168
    mx_v = 4.5e6
    for i, (n, d, cap, avg, g, net, note) in enumerate(SCEN):
        y = t + i * 36
        p.text(MX, y + 16, n.replace(" AMPLIFIED", ""), "Body-B", 8, NAVY, cs=0.3)
        p.text(MX, y + 27, "%d dates" % d + ("+" if i == 3 else ""), "Body", 7.5, GREY)
        p.rect(ax0, y + 6, aw, 22, fill=PALE, r=3)
        bw = aw * net / mx_v
        p.rect(ax0, y + 6, bw, 22, fill=BLUE if net < 2e6 else GREEN, r=3)
        cov = net / 2e6 * 100
        p.text(ax0 + aw + 12, y + 22, "%s" % money(net) + "+", "Body-B", 9.5, NAVY)
        p.text(ax0 + aw + 12 + 54, y + 22, "= %d%% of principal" % round(cov), "Body", 8, GREY)
    mx = ax0 + aw * 2e6 / mx_v
    p.line(mx, t, mx, t + 4 * 36 - 4, RED, 1.2, (3, 3))
    p.text(mx, t - 4, "$2.0M PRINCIPAL", "Body-B", 7, RED, "c", cs=0.4)
    t += 4 * 36 + 8
    p.para(MX, t, CW, "Illustrative: on management's net estimates, tour net alone first covers the full $2M at the "
           "<b>Arena / Live Nation Amplified</b> scale (16 dates). Smaller scenarios return a portion of principal and rely "
           "on merchandise receipts and later reinvestment. Implied net per date: $35K / $94K / $134K / $175K.", "small")
    t += 40
    t = s8(t)

    # [4] PR
    page03b_pr(p, t)


def page03c(p):
    p.frame("03 / LIVE ENTERTAINMENT & GLOBAL TOURING FLYWHEEL", "03 / 07", cont=True)
    t = CONTENT_TOP
    # flywheel + rider
    t += p.section_bar(t, "THE FLYWHEEL & THE ARTIST RIDER", "14–121 DAY CAMPAIGN WINDOW")
    fy = t + 176
    flywheel(p, MX + 176, fy, 112)
    rx = MX + 392
    rw = CW - 392
    rider = [("01", "Feature + clear", "Music collaboration with master / publishing splits agreed."),
             ("02", "Video + clips", "Joint visuals, BTS, vertical short-form creative."),
             ("03", "Artist profile", "Verified DKB presence and promotional content."),
             ("04", "Local FM push", "Paid / earned radio in markets tied to tour dates."),
             ("05", "Ticket to DKB", "Opt-in account and conversion; privacy compliant."),
             ("06", "Post-show tail", "Replay, merchandise and ongoing creator participation.")]
    for i, (n, a, b) in enumerate(rider):
        y = t + 8 + i * 56
        p.rect(rx, y, rw, 48, fill=PALE, stroke=LINE, r=4)
        p.text(rx + 12, y + 30, n, DISPLAY, 15, BLUE)
        p.text(rx + 48, y + 20, a, "Body-B", 9, NAVY)
        p.para(rx + 48, y + 24, rw - 60, b, "small")
    t += 8 + 6 * 56 + 8
    t = max(t, fy + 112 + 56)
    t = s8(t + 16)

    # hot-trigger playbook
    p.rect(MX, t, CW, 88, fill=NAVY, r=6)
    p.text(MX + 20, t + 26, "THE HOT-TRIGGER PLAYBOOK", "Body-B", 9, SKY, cs=0.8)
    trig = [("JOINT SINGLE + VIDEO", "drops in each tour market"),
            ("~69 DAYS OUT", "planning benchmark inside the 14\u2013121-day window"),
            ("LOCAL FM + CREATORS", "radio-first demand before the tour arrives"),
            ("CO-HEADLINE MOMENT", "FRQNZY + headliner perform the record together")]
    tw = (CW - 40) / 4.0
    for i, (a, b) in enumerate(trig):
        x = MX + 20 + i * tw
        p.text(x, t + 50, a, "Body-B", 8.5, white, cs=0.3)
        p.para(x, t + 56, tw - 16, b, "whiteS")
        if i:
            p.line(x - 10, t + 38, x - 10, t + 76, HexColor("#2D4A7A"), 0.75)
    t += 104

    # international + festival upside
    t += p.section_bar(t, "GERMANY, UAE AND FESTIVAL UPSIDE", "OPTIONAL / TESTED SEPARATELY")
    hh = p.cards_row(MX, t, CW, [
        ("GERMANY EXPANSION", "Management plans potential packages involving GloRilla, G-Herbo, Key Glock and "
         "Bone-related acts, with the UAE as an added route. Germany / UAE dates are included only in the "
         "<b>Global Phenomenon</b> scenario."),
        ("UPSIDE TO PRICE AND TEST", "International fees, additional pop-up dates, live broadcasting (FTV pay-per-view) and "
         "festival partnerships create upside that is priced and tested separately from the base scenarios."),
        ("LEGAL CLEARANCE FIRST", "Full legal clearance, talent riders and live-event escrow are required before any "
         "international routing is committed.", GOLD)], bar="top", fill=PALE)
    t += hh + 24

    t += p.section_bar(t, "MANDATORY FANBASE CROSS-PROMOTION", "PROPOSED RIDER TERM / TO BE CONTRACTED")
    hh = p.cards_row(MX, t, CW, [
        ("CONTRACTED PROMOTION", "Every booked headliner is required to promote the collaborative song, the video and the "
         "DKB ticket link to their own audiences."),
        ("COMBINED REACH", "The roster's combined social audiences become the top of the DKB funnel, supplementing paid FM and "
         "creator campaigns in each market.", NAVY),
        ("MEASURED, NOT ASSUMED", "Sign-up surges per metro date are a target to be measured and reported monthly; they are "
         "not yet a historical result.")], bar="top", fill=PALE)
    t += hh + 24

    t += p.section_bar(t, "A DKB NIGHT: RUN OF SHOW", "EVERY MOMENT FEEDS THE PLATFORM")
    ros = [("DOORS", "DKB Wi-Fi onboarding; profiles created on arrival"),
           ("SUPPORT ACTS", "$10K\u2013$15K roster-tier talent opens the night"),
           ("HEADLINER SET", "Booked headliner performs the catalogue"),
           ("CO-HEADLINE MOMENT", "FRQNZY + headliner perform the joint record"),
           ("AFTER-SHOW", "Replay, merch drop and Westville invite on DKB")]
    rw = (CW - 4 * 20) / 5.0
    for i, (a_, b_) in enumerate(ros):
        x = MX + i * (rw + 20)
        col = GOLD if i == 3 else (NAVY if i % 2 == 0 else BLUE)
        p.rect(x, t, rw, 96, fill=col, r=6)
        p.text(x + 12, t + 26, "0%d" % (i + 1), DISPLAY, 13, white if col != GOLD else NAVY)
        p.para(x + 12, t + 34, rw - 24, "<b>%s</b>" % a_, S("ro", 8.5, 11, white if col != GOLD else NAVY, "Body-B"))
        p.para(x + 12, t + 58, rw - 24, b_, S("ro2", 8, 10.5, HexColor("#E6F0FC") if col != GOLD else NAVY))
        if i < 4:
            p.arrow(x + rw + 2, t + 48, x + rw + 18, t + 48, GOLD, 1.8, 6)
    t += 112
    p.check(t, "page03c")
    return t


def page03b_pr(p, t):
    p.rect(MX, t, 28, 28, fill=BLUE, r=14)
    p.text(MX + 14, t + 19, "4", DISPLAY, 13, white, "c")
    p.text(MX + 40, t + 19, "GLOBAL PR & MEDIA LEVERAGE", "Body-B", 11, NAVY, cs=0.4)
    t += 44
    ih = 128
    p.img("i-011.jpg", MX, t, 104, ih, "cover", r=6)
    x0 = MX + 120
    w0 = CW - 120
    p.text(x0, t + 10, "TOP-TIER BROADCAST BLITZ — TIMED AROUND MAJOR METRO TOUR STOPS", "Body-B", 8.5, NAVY, cs=0.4)
    h = p.chips(x0, t + 20, w0, ["Fallon", "Kimmel", "The Breakfast Club", "Sway in the Morning",
                                 "Big Boy's Neighborhood", "COLORS", "Tiny Desk", "On the Radar"], h=22, size=8.5)
    ty = t + 20 + h + 14
    hh = p.card_h(w0, "GLOBAL LANDMARK CAMPAIGN",
                  "Dubai team visual campaign and Forbes feature spotlighting Malcolm “FRQNZY” Henderson, Teddy Riley, "
                  "Dr. Ish, and Evan Shive launching a sovereign entertainment ecosystem. Editorial placements follow each "
                  "outlet's process and are not guaranteed.", 12)
    p.card(x0, ty, w0, hh, "GLOBAL LANDMARK CAMPAIGN",
           "Dubai team visual campaign and Forbes feature spotlighting Malcolm “FRQNZY” Henderson, Teddy Riley, "
           "Dr. Ish, and Evan Shive launching a sovereign entertainment ecosystem. Editorial placements follow each "
           "outlet's process and are not guaranteed.", accent=GOLD, fill=ICE, bar="left")
    t = max(t + ih, ty + hh)
    t = s8(t + 16)

    # booking status
    t += p.section_bar(t, "BOOKING STATUS & CONTRACT DELIVERABLES", "SLIM (112) + AMG TWINS BOOKED (MANAGEMENT-REPORTED)")
    cw2 = (CW - 16) / 2.0
    for i, (a_, b_) in enumerate((("SLIM (112)", "Booked for \u201cThe Vibe\u201d"), ("AMG TWINS", "Booked for \u201cLove Don't Live Here\u201d"))):
        x = MX + i * (cw2 + 16)
        p.rect(x, t, cw2, 56, fill=PALE, stroke=LINE, r=4)
        p.text(x + 16, t + 24, a_, DISPLAY, 12, NAVY)
        p.text(x + 16, t + 42, b_, "Body", 9, GREY)
        p.chip(x + cw2 - 16 - 62, t + 18, "BOOKED", fill=HexColor("#D9F5E8"), color=HexColor("#0A7A4B"), size=8, h=20)
    t += 72
    p.text(MX, t + 8, "IN ACTIVE PROGRAMMING DISCUSSIONS", "Body-B", 8.5, NAVY, cs=0.4)
    h = p.chips(MX, t + 20, CW, ["GloRilla", "G-Herbo", "Sexyy Red", "Bossman Dlow", "Future", "Teddy Riley", "Bone Thugs-N-Harmony",
                                  "Luh Tyler", "Key Glock", "Babyface Ray"], fill=ICE, color=NAVY, h=22, size=8.5)
    t = s8(t + 20 + h + 12)
    t += p.para(MX, t, CW, "DKB's artist agreements are structured to include a FRQNZY feature, visual content, an artist "
                "profile and promotion for a negotiated 14\u2013121-day campaign. Specific deal deliverables are governed by each "
                "artist's contract.", "small")
    t = s8(t + 8)
    p.text(MX, t + 8, "Source: DKB management's October 2026 tour update and Walt Reeder Entertainment 2026 roster; "
           "booking status supplied by management.", "Body-I", 7, GREY)
    p.check(t + 8, "page03b")
