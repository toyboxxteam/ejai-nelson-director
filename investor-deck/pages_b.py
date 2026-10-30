"""Pages 04-07 and appendices of the DKB investor deck."""
import math

from reportlab.lib.colors import HexColor, white

from dkb_lib import *
from pages_a import SCEN, money

DONUT = [BLUE, NAVY, HexColor("#3A9BE0"), HexColor("#8CC8F2"), HexColor("#C8E2F8")]


def num_bar(p, t, n, label):
    p.rect(MX, t, 28, 28, fill=BLUE, r=14)
    p.text(MX + 14, t + 19, n, DISPLAY, 13, white, "c")
    p.text(MX + 40, t + 19, label, "Body-B", 11, NAVY, cs=0.4)


# =============================================================================
# 04  DKB WEB / TICKETING / CREATOR ECONOMY
# =============================================================================
def page04(p):
    p.frame("04 / DKB WEB, TICKETING & CREATOR ECONOMY", "04 / 07")
    t = CONTENT_TOP
    t = p.title(t, "ONE FAN. MANY PATHWAYS.", None,
                "The planned web / mobile core integrates music, social feeds, tickets, games, video, creator tools and "
                "commerce into a single opt-in relationship.")

    t += p.section_bar(t, "THE DKB ACQUISITION-TO-MONETIZATION LOOP", "PLANNED CUSTOMER JOURNEY")
    steps = ["TOUR / RADIO", "JOIN DKB", "FOLLOW ARTIST", "BUY / STREAM", "PLAY WESTVILLE", "SUPPORT / RETURN"]
    sw = (CW - 5 * 12) / 6.0
    for i, a in enumerate(steps):
        x = MX + i * (sw + 12)
        col = NAVY if i == 0 else (BLUE if i in (1, 3, 4) else PALE)
        p.rect(x, t, sw, 48, fill=col, stroke=LINE if col == PALE else None, r=4)
        p.text(x + sw / 2.0, t + 20, "0%d" % (i + 1), DISPLAY, 9, white if col != PALE else BLUE, "c")
        p.text(x + sw / 2.0, t + 36, a, "Body-B", 7.5, white if col != PALE else NAVY, "c", cs=0.3)
        if i < 5:
            p.arrow(x + sw + 1, t + 24, x + sw + 11, t + 24, GOLD, 1.6, 5)
    t += 72

    t += p.section_bar(t, "PLATFORM MODULES / 13-TAB ARCHITECTURE", "FEATURES ARE ROADMAP ITEMS")
    mods = [("SOCIAL", "Timeline / Respect, profiles, KickTok"), ("VIDEO", "FTV live + video, KickFlix"),
            ("DISCOVERY", "DKB Hot 100, music charts, DaKickTapes"), ("STUDIO", "FRQNZY Beat Labz, creator locker"),
            ("GAME", "Ourcade, Westville, live events"), ("COMMERCE", "DKB Ticket, merchandise, creator sales"),
            ("COMMUNITY", "Mail, DaLimes, Kupid, search"), ("ADVANCED", "Licensed payments, regulated functions")]
    cw = (CW - 16) / 2.0
    for i, (a, b) in enumerate(mods):
        x = MX + (i % 2) * (cw + 16)
        y = t + (i // 2) * 64
        p.rect(x, y, cw, 56, fill=PALE, stroke=LINE, r=4)
        p.rect(x, y, 4, 56, fill=BLUE if i % 3 else NAVY)
        p.text(x + 20, y + 24, a, "Body-B", 9.5, NAVY, cs=0.5)
        p.text(x + 20, y + 40, b, "Body", 9, GREY)
    t += 4 * 64 + 8

    t += p.section_bar(t, "NEW COMMERCE PRODUCTS / TRANSPARENT PROPOSED ECONOMICS", "SUBSCRIPTIONS + P2P")
    hh = p.cards_row(MX, t, CW, [
        ("DKB TICKET + FRQNZY AI  •  $49.99 / MO", "Proposed premium workspace for artist-booking intake, rider management, "
         "deal templates, tour routing, contract tracking, and premium chart access. A professional must approve legal "
         "terms; “unlimited” usage and subscriptions require realistic hosting and data licensing."),
        ("FAN-TO-CREATOR PAYOUTS", "Proposed cash-out: <b>2% service fee</b> for eligible instant transfers; no DKB fee for "
         "eligible standard transfers taking roughly 3–5 banking days. External processing charges, eligibility, "
         "chargebacks, fraud controls, KYC / AML and applicable licenses must be established.")],
        bar="left", fill=ICE)
    t += hh + 16

    t += p.section_bar(t, "LIVE DIGITAL PERFORMANCES / TALENT DISCOVERY / EXPERIENCE COMMERCE", "")
    hh = p.cards_row(MX, t, CW, [
        ("VIRTUAL + PHYSICAL SHOWS", "Motion capture / Live Link may synchronize a performer with an in-world avatar. Remote "
         "ticketed PPV, sponsored sets, paid designs and merch are possible once the tech stack is tested."),
        ("RAP BATTLE CIRCUITS", "8 Mile-style leagues, fan voting, qualified label judges, moderated prize contests and producer "
         "showcases. Any money wagers stay disabled absent gaming approvals."),
        ("CREATOR PROGRESSION", "In-game music career: make recordings, sell digital or physical music, book local venues, earn "
         "audience reputation and build toward major tours with measurable engagement.")], bar="top", fill=PALE)
    t += hh + 16

    # precedent strip
    p.rect(MX, t, CW, 72, fill=NAVY, r=6)
    p.text(MX + 20, t + 24, "PUBLIC PRECEDENTS FOR IN-WORLD CONCERTS", "Body-B", 8.5, SKY, cs=0.7)
    prec = [("12M+", "concurrent players at Travis Scott's Fortnite “Astronomical” event, Apr 2020 (Epic Games)"),
            ("33M+", "visits to Lil Nas X's Roblox concert weekend, Nov 2020 (Roblox)")]
    for i, (v, d) in enumerate(prec):
        x = MX + 20 + i * 344
        p.text(x, t + 54, v, DISPLAY, 22, white)
        p.para(x + 76, t + 36, 252, d, "whiteS")
    t += 88

    p.card(MX, t, CW, 56, "EDUCATION IS A PARTNERSHIP OPPORTUNITY, NOT AN ISSUED CREDENTIAL",
           "Proposed virtual campuses and immersive instruction for GED / high-school-equivalency preparation, industry "
           "training and certain licenses. Only authorized schools, testing organizations and regulators can issue valid "
           "credentials.", accent=GOLD, fill=PALE, bar="left")
    t += 72
    t += p.para(MX, t, CW, "DKCoin / Ghana concept: proposed platform currency and potential gold-linked partner discussions "
                "are not evidence of reserves, redemption rights or stable value. Creator royalties require licensed "
                "payment partners, audit trails and legal review. Model: DKB product roadmap; licensing, educational "
                "accreditation and payment functionality not yet verified. Precedent figures are as publicly reported by "
                "the platforms at the time.", "src")
    p.check(t, "page04")


# =============================================================================
# 05  WELCOME 2 WESTVILLE
# =============================================================================
def page05(p):
    p.frame("05 / FLAGSHIP INTERACTIVE WORLD", "05 / 07")
    t = CONTENT_TOP
    t = p.title(t, "WELCOME 2 WESTVILLE", None,
                "Hero: Malcolm Samir. Aspirational cinematic quality, a living seven-city framework and interlocking career "
                "systems; the finished GTA VI-level production standard remains a target.")
    ih = 235
    p.img("i-084.png", MX, t, 432, ih, "cover", r=6)
    p.img("i-085.png", MX + 448, t, 248, 96, "cover", r=6, anchor=0.35)
    p.img("i-086.png", MX + 448, t + 102, 248, 133, "cover", r=6)
    t += ih + 16

    t += p.section_bar(t, "A SEVEN-CITY FRAMEWORK, NOT A SINGLE GTA-STYLE HUB", "30KM × 30KM / PROPOSED WORLD SCALE")
    t += p.para(MX, t, CW, "The world plan draws on the DMV, San Francisco and Long Beach, Chicago, Los Angeles, New York, "
                "Tokyo / Hong Kong, Las Vegas / Nubai and the pristine ancient architecture of Azure Egypt. City identities and "
                "geography will be reconciled to the approved Westville map bible; the “seven cities” aspiration "
                "includes multiple distinct subdistricts and surrounding biomes.", "body")
    t += 8
    h = p.chips(MX, t, CW, ["DMV", "San Francisco + Long Beach", "Chicago", "Los Angeles", "New York", "Tokyo / Hong Kong",
                            "Las Vegas / Nubai", "Azure Egypt"], fill=NAVY, color=white, h=22, size=8.5)
    t += h + 8
    h = p.chips(MX, t, CW, ["Lush forests", "Waterfalls", "Tombs", "Caverns", "Secret mansions", "Underwater tunnels",
                            "Elevated roads", "Hidden bases"], fill=ICE, color=NAVY, h=22, size=8.5)
    t = s8(t + h + 16)

    t += p.section_bar(t, "WHERE WESTVILLE DIFFERENTIATES ITSELF", "SYSTEMS THAT CREATE REPLAY VALUE")
    cards = [("LIVING NPC NETWORK", "Characters with daily schedules, rivalries, careers, choices and mission chains "
              "triggered by whom a player actually meets."),
             ("STORY + ACTION", "101-mission base target; heists, dilemmas, cinematic driving, on-foot action, reactive "
              "police, complex character outcomes."),
             ("SPORTS AS CAREERS", "WVWF wrestling, boxer / fight-night championship paths, GFL football and GBA "
              "basketball: street play through scouting and pro stages."),
             ("MOTORSPORT", "Street and sanctioned races, high-stakes risk / reward, cinematic vehicle missions and "
              "car-to-car action sequences."),
             ("MUSIC STAR ARC", "Create a performer, sell records, promote locally, book and headline venues, perform live, "
              "build label / fan relationships."),
             ("WORLD ECONOMY", "Real money only through permitted payment rails; virtual goods, real merchandise, commerce, "
              "venue rentals and earned creator shares.")]
    for r in range(2):
        hh = p.cards_row(MX, t, CW, [cards[r * 3 + i] + ((NAVY,) if (r + i) % 2 else ()) for i in range(3)],
                         bar="top", fill=PALE)
        t += hh + 16

    # tech stack + slice
    t += p.section_bar(t, "THE PRODUCTION STACK & THE FIRST PLAYABLE SLICE", "PLANNED SCOPE / NOT COMPLETED CONTENT")
    h = p.chips(MX, t, CW, ["Unreal Engine 5", "MetaHuman characters", "Strand-based hair", "Nanite geometry", "Lumen lighting",
                            "World Partition streaming", "Mass crowd AI", "Chaos vehicles", "Niagara FX", "Live Link mocap"],
                fill=PALE, color=NAVY, h=22, size=8.5, stroke=LINE)
    t += h + 12
    ph = [("PHASE 1", "Map-bible reconciliation + in-engine block-outs"),
          ("PHASE 2", "Hero character, driving loop, first district"),
          ("PHASE 3", "DKB ticketing + stage-event integration"),
          ("PHASE 4", "Playable Unreal Engine 5.8 slice for investors")]
    pw = (CW - 3 * 20) / 4.0
    for i, (a, b) in enumerate(ph):
        x = MX + i * (pw + 20)
        p.rect(x, t, pw, 52, fill=BLUE if i == 3 else PALE, stroke=None if i == 3 else LINE, r=4)
        p.text(x + 12, t + 22, a, "Body-B", 8.5, white if i == 3 else BLUE, cs=0.6)
        p.para(x + 12, t + 28, pw - 24, b, S("ph", 8.5, 11.5, white if i == 3 else INK))
        if i < 3:
            p.arrow(x + pw + 2, t + 26, x + pw + 18, t + 26, GOLD, 1.6, 5)
    t += 68

    # bridge
    t += p.section_bar(t, "THE BRIDGE BETWEEN THE GAME AND THE REAL WORLD", "A PRODUCT PATHWAY, NOT A SHIPPED FEATURE")
    bh = p.card_h(CW - 4, "TOYBOXX DIGITAL TWIN / REAL-WORLD PURCHASE",
                  "A player buying a ToyBoxx console in Westville could connect that order to a real USD checkout and a "
                  "synchronized in-game virtual console, timed to real fulfillment. The promise is more than an unboxing "
                  "moment: a branded physical / digital experience. Availability, legal currency conversion, order "
                  "integration, refunds and shipping remain development tasks.", 12)
    p.card(MX, t, CW, bh, "TOYBOXX DIGITAL TWIN / REAL-WORLD PURCHASE",
           "A player buying a ToyBoxx console in Westville could connect that order to a real USD checkout and a "
           "synchronized in-game virtual console, timed to real fulfillment. The promise is more than an unboxing "
           "moment: a branded physical / digital experience. Availability, legal currency conversion, order "
           "integration, refunds and shipping remain development tasks.", accent=BLUE, fill=ICE, bar="left")
    t += bh + 8
    p.text(MX, t + 8, "Source: Westville creative materials and new concept screenshots. Planned scope is not completed content.",
           "Body-I", 7, GREY)
    p.check(t + 8, "page05")


# =============================================================================
# 06  LEGEND OF FRQNZY + TOYBOXX
# =============================================================================
def page06(p):
    p.frame("06 / ORIGINAL GAME IP + HARDWARE + DISTRIBUTION", "06 / 07")
    t = CONTENT_TOP
    t = p.title(t, "LEGEND OF FRQNZY + TOYBOXX", None,
                "Two complementary opportunities: an independent fantasy world and a connected physical console. Fantasy "
                "assets remain entirely separate from Westville.")
    t += p.section_bar(t, "THE LEGEND OF FRQNZY: DARK AGE AWAKENING", "INDEPENDENT FANTASY IP")
    gh = 256
    p.img("i-093.jpg", MX, t, 172, gh, "cover", r=6)
    gx = MX + 188
    gw = CW - 188
    p.img("i-094.jpg", gx, t, 272, 128, "cover", r=6)
    p.img("i-095.jpg", gx + 280, t, gw - 280, 128, "cover", r=6)
    sw = (gw - 16) / 3.0
    p.img("i-096.jpg", gx, t + 136, sw, 120, "cover", r=6)
    p.img("i-097.jpg", gx + sw + 8, t + 136, sw, 120, "cover", r=6)
    p.img("i-098.jpg", gx + 2 * (sw + 8), t + 136, sw, 120, "cover", r=6)
    t += gh + 16
    t += p.para(MX, t, CW, "An ancient-world fantasy adventure spanning desert kingdoms, forests, sky structures, lost "
                "civilizations, mystic artifacts, temple bosses and signature eye-of-Horus-inspired relics. Planned media "
                "extensions include soundtracks, collectibles, animation and narrative expansion. Concept art is evidence of "
                "creative development, not a completed consumer game.", "body")
    t = s8(t + 16)

    t += p.section_bar(t, "TOYBOXX CONSOLE / A CONNECTED HOUSEHOLD PRODUCT", "PHYSICAL + DIGITAL MODEL")
    ih = 128
    p.img("i-099.jpg", MX, t, 296, ih, "cover", r=6)
    p.img("i-100.jpg", MX + 304, t, 152, ih, "cover", r=6)
    p.img("i-101.jpg", MX + 464, t, 232, ih, "cover", r=6)
    t += ih + 16
    t += p.para(MX, t, CW, "ToyBoxx is conceived as a couch-first console integrating gaming, music, community tools, media "
                "playback and selected legacy media functionality, subject to technical validation and intellectual-property "
                "rights. No PS / Xbox disc compatibility or cross-play is asserted as functional without licenses and testing.",
                "body")
    t = s8(t + 12)
    st = [("$274.99", "PROPOSED RETAIL PRICE", BLUE), ("$125", "MANAGEMENT BOM TARGET (UNVERIFIED)", NAVY),
          ("$149.99", "IMPLIED SPREAD BEFORE FULFILLMENT, WARRANTY, TAX, CAC", GREY)]
    cw = (CW - 32) / 3.0
    for i, (v, l, col) in enumerate(st):
        x = MX + i * (cw + 16)
        p.rect(x, t, cw, 72, fill=PALE, stroke=LINE, r=4)
        p.text(x + 16, t + 34, v, DISPLAY, 24, col)
        p.para(x + 16, t + 42, cw - 32, l, S("stl", 7.5, 9.5, GREY, "Body-B"))
    t += 88
    p.para(MX, t, CW, "The claimed $149.99 net margin has not been supported by manufacturer bills of materials, fulfillment, "
           "warranty, tax or customer acquisition costs; treat it as a target to be proven at the hardware gates below.", "small")
    t += 32

    # hardware gates
    gates = ["Functional PCB prototype", "Controller verification", "FCC / CE safety certification", "Audited manufacturer BOM",
             "Pilot production run"]
    gw5 = (CW - 4 * 12) / 5.0
    for i, g in enumerate(gates):
        x = MX + i * (gw5 + 12)
        p.rect(x, t, gw5, 48, fill=NAVY if i % 2 == 0 else BLUE, r=4)
        p.text(x + 10, t + 18, "GATE %d" % (i + 1), "Body-B", 7, SKY if i % 2 == 0 else HexColor("#DCEBFA"), cs=0.6)
        p.para(x + 10, t + 22, gw5 - 20, g, S("gt", 8.5, 10.5, white, "Body-B"))
        if i < 4:
            p.arrow(x + gw5 + 1, t + 24, x + gw5 + 11, t + 24, GOLD, 1.4, 4)
    t += 72

    t += p.section_bar(t, "SURREAL ENGINE / FRQNZY AI / TELERIC EXPANSION", "CREDIBLE PHASED DELIVERY")
    hh = p.cards_row(MX, t, CW, [
        ("CREATION LAYER", "UE / Blender-centered prompt and pipeline automation for environments, assets, build management "
         "and technical QA. Claimed 1,200+ skills and 3–6 month AAA completion are not independently validated."),
        ("INFRASTRUCTURE", "Evan Shive contributes to the proposed Teleric access and connectivity strategy. Festival-scale "
         "Wi-Fi, edge delivery and commercial media streaming must be engineered, budgeted and contracted.", NAVY),
        ("LIVE STREAMING", "A strong production opportunity: virtual events, live fan participation, venue internet services "
         "and paid platform access for third-party broadcasters, with rights and capacity tested first.")],
        bar="top", fill=PALE)
    t += hh + 8
    p.text(MX, t + 8, "Source: user game / hardware designs and management technical concept; features pending certification "
           "or proof.", "Body-I", 7, GREY)
    p.check(t + 8, "page06")


# =============================================================================
# 07  FINANCING  (A: use of funds + waterfall,  B: scenarios + controls)
# =============================================================================
USE = [("Touring & Live Production", 600000, "Leveraged with Walt Reeder's below-market wholesale artist fees to fund initial "
        "deposits, Live Nation co-pro guarantees, and stage design."),
       ("Welcome 2 Westville & DKB Web Platform", 450000, "Core buildout for 13-tab architecture, ticketing portal, and "
        "playable Unreal Engine 5.8 slice."),
       ("ToyBoxx Console & Hardware Engineering", 350000, "Tooling, ToyBoxxOS architecture, and controller verification "
        "prototypes."),
       ("Media, Radio & Global PR", 300000, "Regional FM pushes in tour markets, late-night media relations, and 365-song "
        "rollout support."),
       ("Legal, Compliance & Working Capital Reserve", 300000, "SEC / KYC compliance, talent rider contracts, and live event "
        "escrow.")]


def donut(p, cx, cy, ro, ri, vals, cols):
    c = p.c
    tot = float(sum(vals))
    ang = 90.0
    for v, col in zip(vals, cols):
        ext = -360.0 * v / tot
        c.setFillColor(col)
        c.setStrokeColor(white)
        c.setLineWidth(2)
        c.wedge(cx - ro, p.Y(cy) - ro, cx + ro, p.Y(cy) + ro, ang, ext, stroke=1, fill=1)
        ang += ext
    c.setFillColor(white)
    c.circle(cx, p.Y(cy), ri, stroke=0, fill=1)


def page07a(p):
    p.frame("07 / FINANCING, SCENARIOS & INVESTOR PROTECTION", "07 / 07")
    t = CONTENT_TOP
    t = p.title(t, "THE $2M LAUNCH ECONOMICS", None,
                "Four adoption cases illustrate potential gross activity, not investor cash returns. Execution and reporting "
                "are milestone-based and no additional investment is requested.")
    t += p.section_bar(t, "USE OF FUNDS / $2,000,000 TOTAL ALLOCATION", "SOURCE ALLOCATION / 100%")
    cx, cy = MX + 120, t + 124
    donut(p, cx, cy, 112, 66, [u[1] for u in USE], DONUT)
    p.text(cx, cy + 4, "$2M", DISPLAY, 30, NAVY, "c")
    p.text(cx, cy + 22, "CAPPED", "Body-B", 8, BLUE, "c", cs=0.8)
    lx = MX + 272
    lw = CW - 272
    y = t + 4
    for i, (n, v, d) in enumerate(USE):
        rh = 50
        p.rect(lx, y + 3, 10, 10, fill=DONUT[i], r=2)
        p.text(lx + 20, y + 12, n, "Body-B", 9.5, NAVY)
        p.text(lx + lw, y + 12, "${:,.0f}".format(v), DISPLAY, 11, BLUE, "r")
        p.text(lx + lw, y + 26, "%.1f%%" % (v / 20000.0), "Body-B", 7.5, GREY, "r")
        p.para(lx + 20, y + 16, lw - 96, d, "small")
        y += rh
    t += 256
    t = s8(t)

    # waterfall
    t += p.section_bar(t, "RECOUPMENT WATERFALL / TERMS FOR NEGOTIATION", "PROPOSED / SUBJECT TO WRITTEN AGREEMENT")
    p.rect(MX, t, 440, 88, fill=NAVY, r=6)
    p.text(MX + 20, t + 26, "TIER 1  •  PRIORITY RECOUPMENT", "Body-B", 9, SKY, cs=0.7)
    p.text(MX + 20, t + 56, "100%", DISPLAY, 28, white)
    p.para(MX + 112, t + 34, 308, "of defined net tour and merchandise receipts flow directly to Dr. Ish until the "
           "<b>$2,000,000 principal</b> is fully returned.", "white")
    p.arrow(MX + 220, t + 92, MX + 220, t + 112, GOLD, 2.4, 8)
    p.rect(MX, t + 116, 440, 88, fill=BLUE, r=6)
    p.text(MX + 20, t + 142, "TIER 2  •  PERMANENT PARTICIPATION", "Body-B", 9, white, cs=0.7)
    p.text(MX + 20, t + 172, "50 / 50", DISPLAY, 28, white)
    p.para(MX + 152, t + 150, 268, "permanent net profit split on ongoing live / merch ventures after principal is returned.",
           "white")
    sx = MX + 456
    sw = CW - 456
    p.rect(sx, t, sw, 204, fill=ICE, r=6)
    p.rect(sx, t, 4, 204, fill=GOLD)
    p.text(sx + 20, t + 26, "ALONGSIDE", "Body-B", 9, NAVY, cs=0.7)
    p.text(sx + 20, t + 62, "1%", DISPLAY, 28, BLUE)
    p.para(sx + 72, t + 40, sw - 88, "publishing participation on each of the 365 FRQNZY campaign songs. Not 365% catalog "
           "ownership; rights, calculation base and duration to be defined in writing.", "card")
    p.line(sx + 20, t + 118, sx + sw - 16, t + 118, LINE)
    p.text(sx + 20, t + 154, "$75K", DISPLAY, 28, BLUE)
    p.para(sx + 104, t + 130, sw - 120, "bonus payable on a defined label milestone.", "card")
    t += 220
    t = s8(t)

    # recovery reality
    t += p.section_bar(t, "RECOVERY REALITY: WHAT THE TOUR SCENARIOS IMPLY", "DERIVED FROM MANAGEMENT NET ESTIMATES")
    cols = [("SCENARIO", MX + 12, "l"), ("TOUR NET (EST.)", MX + 280, "r"), ("NET PER DATE", MX + 410, "r"),
            ("% OF $2M PRINCIPAL", MX + 560, "r"), ("DATES TO $2M AT THAT RATE", MX + CW - 12, "r")]
    p.rect(MX, t, CW, 28, fill=NAVY, r=4)
    for lab, x, al in cols:
        p.text(x, t + 18, lab, "Body-B", 7.5, white, al, cs=0.4)
    t += 28
    for i, (n, d, cap, avg, g, net, note) in enumerate(SCEN):
        p.rect(MX, t, CW, 28, fill=PALE if i % 2 == 0 else white, stroke=LINE)
        per = net / float(d)
        p.text(MX + 12, t + 18, n.title().replace("Amplified", "Amplified"), "Body-B", 9, NAVY)
        p.text(MX + 280, t + 18, money(net) + "+", "Body-B", 9.5, INK, "r")
        p.text(MX + 410, t + 18, "${:,.0f}".format(per), "Body-B", 9.5, INK, "r")
        p.text(MX + 560, t + 18, "%d%%" % round(net / 2e6 * 100), "Body-B", 9.5, GREEN if net >= 2e6 else BLUE, "r")
        p.text(MX + CW - 12, t + 18, "%d dates" % math.ceil(2e6 / per), "Body-B", 9.5, INK, "r")
        t += 28
    t += 12
    t += p.para(MX, t, CW, "<b>Recovery reality:</b> management's earlier illustrative $61K / event net would require about 33 "
                "comparable events to accumulate $2M if every dollar were available; the updated wholesale-basis estimates imply "
                "$35K–$175K per date. The 41–70-day goal refers only to first receipts, not full repayment, and the "
                "12–24-month horizon is unverified. Defined net, settlement timing and merchandise receipts will be fixed "
                "in the agreement.", "small")
    t = s8(t + 16)
    t += p.section_bar(t, "PROPOSED NEXT STEPS", "")
    ns = [("01", "TERM SHEET", "Confirm waterfall, defined net, publishing terms and draw schedule in writing."),
          ("02", "ESCROW & CONTROLS", "Open dual-authorization account; appoint auditor; agree monthly reporting."),
          ("03", "TRANCHE 1 TRIGGERS", "Executed Walt Reeder talent agreements, Live Nation routing LOIs, clearance."),
          ("04", "FIRST MILESTONE REPORT", "Ticket portal live, first registrations, first settlement receipts.")]
    nw = (CW - 3 * 16) / 4.0
    for i, (n, a, b_) in enumerate(ns):
        x = MX + i * (nw + 16)
        p.rect(x, t, nw, 96, fill=NAVY if i == 0 else PALE, stroke=None if i == 0 else LINE, r=4)
        p.text(x + 14, t + 28, n, DISPLAY, 20, SKY if i == 0 else BLUE)
        p.text(x + 14, t + 46, a, "Body-B", 8.5, white if i == 0 else NAVY, cs=0.3)
        p.para(x + 14, t + 54, nw - 28, b_, "whiteS" if i == 0 else "card")
    t += 96
    p.check(t, "page07a")


def page07b(p):
    p.frame("07 / FINANCING, SCENARIOS & INVESTOR PROTECTION", "07 / 07", cont=True)
    t = CONTENT_TOP
    t += p.section_bar(t, "GREAT • GOOD • STANDARD • BAD", "GROSS CUSTOMER SPENDING, NOT PROFIT")
    cases = [("BAD", 100, 5000, 250, 2, 600, 55), ("STANDARD", 500, 15000, 1000, 4, 1200, 65),
             ("GOOD", 1500, 40000, 2500, 6, 1800, 75), ("GREAT", 3500, 80000, 6000, 8, 2400, 85)]
    comps = [("Creator subs", BLUE), ("Game upgrades", SKY), ("Consoles", NAVY), ("Concert tickets", GOLD)]
    ax0 = MX + 96
    aw = CW - 96 - 72
    mx_v = 6.5e6
    for i, (n, subs, up, con, dt, g, tp) in enumerate(cases):
        vals = [subs * 12 * 29.99, up * 19.99, con * 274.99, dt * g * tp]
        tot = sum(vals)
        y = t + i * 72
        p.text(MX, y + 18, n, "Body-B", 10, NAVY, cs=0.5)
        p.rect(ax0, y + 4, aw, 24, fill=PALE, r=3)
        x = ax0
        for v, (lab, col) in zip(vals, comps):
            w = aw * v / mx_v
            p.rect(x, y + 4, w, 24, fill=col)
            x += w
        p.text(ax0 + aw + 12, y + 22, "$%.2fM" % (tot / 1e6), DISPLAY, 13, NAVY)
        p.text(ax0, y + 46, "{:,} creator subs / mo • {:,} game upgrades • {:,} consoles • {} dates".format(
            subs, up, con, dt), "Body", 8, GREY)
    t += 4 * 72 + 4
    lx = ax0
    for lab, col in comps:
        p.rect(lx, t, 10, 10, fill=col, r=2)
        p.text(lx + 16, t + 9, lab, "Body", 8, GREY)
        lx += 16 + 96
    t += 28
    hh = p.card_h(CW - 4, "", "<b>Exact sensitivity formula:</b> 12 months × subscribed creators × $29.99 + game upgrades "
                  "× $19.99 + console units × $274.99, plus concerts × paid tickets / show × average ticket price. "
                  "Show tickets are modeled from 600 × $55 to 2,400 × $85. Gross customer spending is not profit and is "
                  "not distributable cash.", 12)
    p.card(MX, t, CW, hh, "", "<b>Exact sensitivity formula:</b> 12 months × subscribed creators × $29.99 + game upgrades "
           "× $19.99 + console units × $274.99, plus concerts × paid tickets / show × average ticket price. "
           "Show tickets are modeled from 600 × $55 to 2,400 × $85. Gross customer spending is not profit and is "
           "not distributable cash.", accent=BLUE, fill=ICE, bar="left")
    t += hh + 24

    # controls
    t += p.section_bar(t, "INVESTOR PROTECTION & PRUDENT CONTROLS", "MILESTONE-GATED DRAWS")
    ctrl = [("MILESTONE-BASED DRAWS", "Capital is disbursed in tranches tied to verified milestones: executed talent agreements, "
             "certified BOMs, working ticketing software."),
            ("DUAL-AUTHORIZATION ESCROW", "Treasury / account oversight with dual authorization and live-event escrow on "
             "deposits and settlements."),
            ("MONTHLY REPORTING", "Monthly verified profit-and-loss statements and settlements, plus a maintained cap table."),
            ("THIRD-PARTY AUDIT", "Independent auditing, manufacturer quotes, and education / payment compliance review."),
            ("LEGAL CLEARANCE", "Artist / venue contracts, licensable rights and full legal clearance before any "
             "international tour routing."),
            ("HARDWARE GATES", "Mass production only after functional PCB prototypes and FCC / CE certification.")]
    for r in range(2):
        hh = p.cards_row(MX, t, CW, [ctrl[r * 3 + i] + ((NAVY,) if (r + i) % 2 else ()) for i in range(3)], bar="top", fill=PALE)
        t += hh + 16

    # market context
    t += p.section_bar(t, "PUBLIC MARKET CONTEXT / NO INFERRED DKB VALUATION", "INDEPENDENT REPORTING")
    p.img("i-130c.png", MX, t, CW, 112, "contain")
    t += 128
    t += p.para(MX, t, CW, "Suno is a market signal, not a DKB valuation. Its financing illustrates music-technology demand; DKB "
                "links recorded music, ticketing, games and hardware, with additional execution complexity. The national PR plan "
                "calls for a Dubai team photo and Forbes pitch, followed by TV / press outreach including Kimmel and Fallon, with "
                "Malcolm, Teddy Riley, Evan Shive, Dr. Ish and the DKB team. Media placements depend on editorial acceptance and "
                "scheduling. Research: theesa.com (2025 restated); ifpi.org (Mar 2026); news.livenationentertainment.com (FY25); "
                "suno.com (Jun 2026).", "src")
    t = s8(t + 16)

    t = s8(t + 16)
    t += p.section_bar(t, "MONTHLY INVESTOR SCORECARD", "REPORTED TO DR. ISH EVERY MONTH")
    kp = [("DKB ACCOUNTS", "Registrations created per tour date and per market"),
          ("TICKET SELL-THROUGH", "Paid tickets vs. capacity and average ticket price"),
          ("NET vs. ESTIMATE", "Defined net per date against the management estimate"),
          ("CAMPAIGN STREAMS", "Radio-first single and video performance by market"),
          ("CONVERSION", "Fans moving to subscriptions, merch and Westville")]
    kw = (CW - 4 * 12) / 5.0
    for i, (a_, b_) in enumerate(kp):
        x = MX + i * (kw + 12)
        p.rect(x, t, kw, 88, fill=NAVY if i % 2 == 0 else BLUE, r=4)
        p.text(x + 12, t + 24, a_, "Body-B", 8, white, cs=0.4)
        p.para(x + 12, t + 32, kw - 24, b_, S("kp", 8.5, 11.5, HexColor("#E6F0FC")))
    t += 88
    p.check(t, "page07b")


# =============================================================================
# APPENDIX
# =============================================================================
ROSTER_ROWS = [
    ("GloRilla", "Current & Elite", "Hip Hop & Rap", "p.12", 1), ("Future", "Current & Elite", "Hip Hop & Rap", "p.12", 1),
    ("Bossman Dlow", "Current & Elite", "Hip Hop & Rap", "p.11", 1), ("G-Herbo", "Current & Elite", "Hip Hop & Rap", "p.12", 1),
    ("Luh Tyler", "Current & Elite", "Hip Hop & Rap", "p.13", 1), ("Key Glock", "Current & Elite", "Hip Hop & Rap", "p.13", 1),
    ("Sexyy Red", "Current & Elite", "Hip Hop & Rap", "p.14", 1), ("Babyface Ray", "Current & Elite", "Hip Hop & Rap", "p.11", 1),
    ("21 Savage", "Current & Elite", "Hip Hop & Rap", "p.11", 1),
    ("Rod Wave*", "Current & Elite", "Hip Hop & Rap", "p.14", 1), ("Gunna", "Current & Elite", "Hip Hop & Rap", "p.12", 1),
    ("Doechii", "Current & Elite", "Hip Hop & Rap", "p.12", 1),
    ("Bone Thugs-N-Harmony", "Legacy Icon", "Hip Hop & Rap", "p.11", 1), ("Krayzie Bone", "Legacy Icon", "—", "—", 0),
    ("Teddy Riley", "Legacy Icon", "—", "—", 0), ("Slim (112)", "Legacy Icon", "R&B (as “112”)", "p.3", 1),
    ("AMG Twins", "Legacy Icon", "—", "—", 0), ("Charlie Wilson", "Legacy Icon", "R&B", "p.3", 1),
    ("Guy", "Legacy Icon", "R&B", "p.4", 1), ("Keith Sweat", "Legacy Icon", "R&B", "p.4", 1),
    ("Dru Hill", "Legacy Icon", "R&B", "p.3", 1), ("Jagged Edge", "Legacy Icon", "R&B", "p.4", 1),
    ("DJ Quik", "Roster Depth", "$10K–$15K or less list", "p.29–30", 1),
    ("Slick Rick", "Roster Depth", "$10K–$15K or less list", "p.29–30", 1),
    ("Big Daddy Kane", "Roster Depth", "$10K–$15K or less list", "p.29", 1),
    ("Case", "Roster Depth", "$10K–$15K or less list", "p.29", 1),
    ("J Holiday", "Roster Depth", "$10K–$15K or less list", "p.29", 1),
    ("Adina Howard", "Roster Depth", "$10K–$15K or less list", "p.29", 1),
]


def appx_roster(p):
    p.frame("A1 / WALT REEDER ROSTER CROSS-CHECK", "A1 / A6")
    t = CONTENT_TOP
    t = p.title(t, "ROSTER CROSS-CHECK", None,
                "Every artist named in this deck was checked against the Walt Reeder Entertainment 2026 roster sheet "
                "(30 pages: R&amp;B, Gospel, Hip Hop & Rap, Southern Soul, Jazz, Reggae, Latin, DJ, Comedy and a “$10K–$15K "
                "Artist or LESS” list).")
    cols = [("ARTIST", MX + 12), ("DECK TIER", MX + 216), ("ROSTER CATEGORY", MX + 352), ("SHEET PAGE", MX + 548), ("STATUS", MX + CW - 12)]
    p.rect(MX, t, CW, 28, fill=NAVY, r=4)
    for i, (lab, x) in enumerate(cols):
        p.text(x, t + 18, lab, "Body-B", 7.5, white, "r" if i == 4 else "l", cs=0.5)
    t += 28
    for i, (a, tier, cat, pg, ok) in enumerate(ROSTER_ROWS):
        rh = 28
        p.rect(MX, t, CW, rh, fill=PALE if i % 2 == 0 else white, stroke=LINE)
        p.text(MX + 12, t + 18, a, "Body-B", 9.5, NAVY)
        p.text(MX + 216, t + 18, tier, "Body", 9, GREY)
        p.text(MX + 352, t + 18, cat, "Body", 9, INK)
        p.text(MX + 548, t + 18, pg, "Body", 9, GREY)
        if ok:
            p.chip(MX + CW - 12 - 78, t + 5, "ON ROSTER", fill=HexColor("#D9F5E8"), color=HexColor("#0A7A4B"), size=7, h=18, padx=8)
        else:
            p.chip(MX + CW - 12 - 78, t + 5, "DKB-DIRECT †", fill=HexColor("#FFF0CF"), color=HexColor("#8A5A00"), size=7, h=18, padx=8)
        t += rh
    t += 12
    t += p.para(MX, t, CW, "† DKB-direct: Krayzie Bone, Teddy Riley and AMG Twins are DKB collaborations / bookings and do not appear on the "
                "roster sheet; Slim (112) is listed on the sheet as “112”. * The draft text read “Rob Wave”; the roster "
                "lists <b>Rod Wave</b>. The $10K–$15K list is the roster's published support-act tier; actual fees, "
                "availability and routing are confirmed per date in executed agreements. Roster source: Walt Reeder "
                "Entertainment / Vertical International Corporation, Jenkintown, PA (waltreeder.net).", "small")
    p.check(t, "appx_roster")


def appx_sheet(p, tracker, idx, big, sub, img, note):
    p.frame(tracker, idx)
    t = CONTENT_TOP
    p.text(MX, t + 24, big, DISPLAY, 24, NAVY)
    p.text(MX, t + 42, sub, "Body-B", 9, BLUE, cs=0.7)
    t += 64
    ir = __import__("reportlab.lib.utils", fromlist=["ImageReader"]).ImageReader(asset(img))
    iw, ih = ir.getSize()
    h = CW * ih / float(iw)
    avail = CONTENT_BOTTOM - t - 24
    w = CW
    if h > avail:
        w = CW * avail / h
        h = avail
    x = MX + (CW - w) / 2.0
    p.rect(x - 1, t - 1, w + 2, h + 2, stroke=LINE, r=4)
    p.img(img, x, t, w, h, "contain", r=4)
    p.text(MX, t + h + 16, note, "Body-I", 7.5, GREY)


def appx_process(p):
    p.frame("A5 / THE PROCESS: WORLD-BUILDING BLOCK-OUTS", "A5 / A6")
    t = CONTENT_TOP
    t = p.title(t, "THE PROCESS", "FROM CONCEPT TO IN-ENGINE WORLD",
                "Early block-outs and environment tests show how the maps, castles and terrain are drafted before final "
                "art. This is the pipeline the Westville / Legend slice funds: reconcile the map bible, block out in-engine, "
                "then replace with production assets.")
    p.img("i-144.png", MX, t, 340, 336, "cover", r=6)
    p.img("i-145.png", MX + 356, t, 340, 144, "cover", r=6)
    p.img("i-146.png", MX + 356, t + 152, 340, 184, "cover", r=6)
    t += 352
    p.img("i-147.png", MX, t, CW, 304, "cover", r=6)
    t += 320
    hh = p.cards_row(MX, t, CW, [
        ("1 • BLOCK-OUT", "Scale, sight-lines and traversal are proven with simple geometry first."),
        ("2 • REPLACE", "Production meshes, MetaHuman characters and materials replace the placeholders.", NAVY),
        ("3 • PLAYABLE SLICE", "A vertical slice demonstrates driving, a district, a stage event and DKB ticketing.")],
        bar="top", fill=PALE)
    t += hh + 8
    p.text(MX, t + 8, "Source: user-supplied process captures. Block-outs are development evidence, not final game visuals.",
           "Body-I", 7, GREY)
    p.check(t + 8, "appx_process")


def appx_notice(p):
    p.frame("A6 / IMPORTANT NOTICE, SOURCES & DEFINITIONS", "A6 / A6")
    t = CONTENT_TOP
    t = p.title(t, "IMPORTANT NOTICE", None,
                "This document is a confidential discussion draft prepared by DaKickBack LLC for Dr. Ish. It is not an offer "
                "to sell, or a solicitation of an offer to buy, any security.")
    blocks = [
        ("FORWARD-LOOKING INFORMATION", "Projections, scenarios, tour estimates, net-to-DKB figures, margins and timelines are "
         "management estimates, illustrate potential outcomes only, and are not guarantees. Actual results depend on executed "
         "talent and venue agreements, rights clearance, ticket demand, costs, delivery and regulatory approvals."),
        ("BOOKING & ROSTER STATEMENTS", "Walt Reeder Entertainment pricing, availability and routing are subject to executed "
         "agreements for each date. Live Nation venue routing is a target channel; no Live Nation agreement is represented "
         "unless and until one is executed. Booking status (e.g. Slim (112), AMG Twins) is management-reported."),
        ("PRODUCT & PLATFORM STATUS", "Welcome 2 Westville, Legend of FRQNZY, ToyBoxx hardware, DKB web features, Teleric "
         "infrastructure, subscriptions, payouts, DKCoin and education concepts are roadmap items. Concept art, block-outs and "
         "mock-ups are development evidence, not completed products."),
        ("DEFINED TERMS", "“Defined net” tour and merchandise receipts, publishing participation, the $75,000 label milestone "
         "bonus, draw schedule and reporting will be fixed in a written agreement reviewed by counsel. The 1% publishing "
         "participation is not catalog ownership."),
        ("SOURCES", "ESA (revised 2025 figures); IFPI Global Music Report 2026; Live Nation FY2025; Suno (Jun 2026); Walt Reeder "
         "Entertainment 2026 roster (R&amp;B, Hip Hop &amp; Rap, $10K–$15K lists); DKB management October 2026 tour update; "
         "user-supplied founder photographs, chart captures, tour artwork and game / hardware designs. Fortnite and Roblox "
         "attendance figures are as publicly reported by Epic Games and Roblox in 2020.")]
    for a, b in blocks:
        h = p.card_h(CW - 4, a, b, 14, "cardk")
        p.card(MX, t, CW, h, a, b, accent=BLUE, fill=PALE, bar="left", pad=14, bstyle="cardk")
        t += h + 16
    t += 16
    p.rect(MX, t, CW, 112, fill=NAVY, r=6)
    p.rect(MX + 20, t + 12, 136, 88, fill=white, r=6)
    p.img("i-003.jpg", MX + 28, t + 16, 120, 80, "contain")
    p.text(MX + 176, t + 44, "DAKICKBACK LLC", DISPLAY, 20, white)
    p.text(MX + 176, t + 66, "GOOD KARMA MUSIC GROUP  /  REAL MUSIC MATTERS", "Body-B", 8.5, SKY, cs=0.8)
    p.text(MX + 176, t + 86, "Prepared for Dr. Ish  •  October 2026  •  Confidential", "Body", 9, HexColor("#C9DDF5"))
    t += 112
    p.check(t, "appx_notice")
