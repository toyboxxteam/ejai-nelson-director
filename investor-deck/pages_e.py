"""Section 07 (continued): Botim / Astra Tech as the licensed wallet layer for KickCoin."""
import math

from reportlab.lib.colors import HexColor, white

from dkb_lib import *
from pages_c import table, AMBER_BG, AMBER_FG

TRACK = "07 / INFRASTRUCTURE: TELERIC (NETWORK) + BOTIM (MONEY)"
IDX = "07 / 09"


def page_b1(p):
    p.frame(TRACK, IDX, cont=True)
    t = CONTENT_TOP
    t = p.title(t, "BOTIM: THE WALLET LAYER", "ASTRA TECH  •  ABU DHABI  •  EST. 2022  •  PARENT OF BOTIM  •  G42 ECOSYSTEM",
                "Teleric is the pipe; Botim is the money. Botim is a super-app that joins messaging, payments, credit and investing under "
                "licensed entities in the UAE. For DKB it is the regulated front door that lets fans top up, spend KickCoin and "
                "cash out, without DKB holding anyone's money.", size=34)
    stats = [("150M+", "users across 155 countries (Astra Tech-reported)"), ("$500M", "raised Dec 2022, led by G42"),
             ("1st", "UAE fintech with a full Central Bank Finance Company License (Jul 2024)"),
             ("botim 3.0", "May 2023: fintech, e-commerce and communication in one app"),
             ("AI-native", "Jul 2025: new interface bridging communication and finance")]
    cw = (CW - 4 * 12) / 5.0
    for i, (v, d) in enumerate(stats):
        x = MX + i * (cw + 12)
        hi = i in (0, 2)
        p.rect(x, t, cw, 112, fill=NAVY if hi else PALE, stroke=None if hi else LINE, r=4)
        p.text(x + 12, t + 34, v, DISPLAY, 18, SKY if hi else BLUE)
        p.para(x + 12, t + 44, cw - 24, d, S("bs", 7.5, 10, HexColor("#C9DDF5") if hi else GREY))
    t += 132

    # timeline
    t += p.section_bar(t, "ASTRA TECH TIMELINE", "FROM ASTRA TECH'S WEBSITE")
    ev = [("AUG 2022", "Acquires PayBy"), ("DEC 2022", "$500M raise led by G42"), ("JAN 2023", "Acquires botim"),
          ("MAY 2023", "Launches botim 3.0"), ("JUL 2023", "Philippines via Y-Finance"), ("JUL 2024", "botim finance licensed by CBUAE"),
          ("JUL 2025", "AI-native botim interface"), ("JUL 2025", "One brand: PayBy becomes botim money for business; CashNow becomes botim finance")]
    n = len(ev)
    lx0, lx1 = MX + 24, MX + CW - 24
    ly = t + 28
    p.line(lx0, ly, lx1, ly, BLUE, 2.4)
    step = (lx1 - lx0) / (n - 1)
    for i, (d, a) in enumerate(ev):
        x = lx0 + i * step
        p.c.setFillColor(GOLD if i == 5 else (BLUE if i % 2 == 0 else NAVY))
        p.c.circle(x, p.Y(ly), 7, stroke=0, fill=1)
        al = "c"
        p.text(x, ly - 14, d, "Body-B", 7.5, NAVY, al, cs=0.3)
        p.para(x - 38, ly + 14, 76, '<para alignment="center">%s</para>' % a, S("tl", 7.5, 9.5, GREY))
    t += 112

    t += p.section_bar(t, "THE BOTIM FAMILY, AND WHAT EACH PIECE DOES FOR DKB", "ALL CAPABILITIES AS DESCRIBED BY ASTRA TECH")
    cols = [("PRODUCT", 128, "l"), ("WHAT ASTRA TECH SAYS IT IS", 262, "l"), ("PROPOSED ROLE IN DKB", 306, "l")]
    rows = [
        ["<b>botim app</b>", "Super-app joining fintech, e-commerce, communication and on-demand services.", "Distribution: DKB entry point and, if supported, a DKB service inside the app for UAE / MENA fans."],
        ["<b>botim money</b>", "Everyday finance in one place: pay, credit, invest; local transfers, digital wallets, savings tools.", "The fan wallet that holds dirhams or dollars before they become KickCoin."],
        ["<b>botim pay</b>", "Send money locally and internationally, pay bills, recharge mobiles, manage a wallet.", "Top-ups, creator payouts and cash-out rails (the 2% instant / free standard model)."],
        ["<b>botim credit</b>", "Instant credit tools for short-term borrowing or sending money before payday.", "Optional ToyBoxx and ticket instalments, subject to Botim's own approval and licensing."],
        ["<b>botim invest</b>", "Low-barrier investing for expats and everyday earners: gold, bonds, digital assets.", "Not used for KickCoin. Kept separate so KickCoin is never pitched as an investment."],
        ["<b>botim finance</b>", "First UAE fintech with a full Finance Company License: lending, credit, microfinancing.", "Future creator-advance product on Botim's license; DKB does not lend."],
        ["<b>botim money for business</b>", "Digital payment platform from e-wallets to point-of-sale (botim.money).", "Merch, ticket and venue payments at UAE tour dates and DKB pop-ups."],
    ]
    h = table(p, MX, t, cols, rows)
    t += h + 8
    t += p.para(MX, t, CW, "Source: astratech.ae (Who We Are), supplied by the user, November 2026; user and revenue figures are Astra Tech's own. "
                "No discussions with Astra Tech or Botim are represented.", "src")
    p.check(t, "page_b1")


def flow(p, x, t, w):
    nodes = [("FAN", "Card or bank transfer", NAVY), ("BOTIM WALLET", "Licensed; holds the funds", BLUE), ("KICKCOIN", "DKB closed-loop credit", NAVY)]
    nw = 124
    gap = 28
    for i, (a, b, col) in enumerate(nodes):
        nx = x + i * (nw + gap)
        p.rect(nx, t + 64, nw, 72, fill=col, r=6)
        p.text(nx + nw / 2.0, t + 96, a, "Body-B", 9.5, white, "c", cs=0.5)
        p.para(nx + 8, t + 104, nw - 16, '<para alignment="center">%s</para>' % b, "whiteS")
        if i < 2:
            p.arrow(nx + nw + 2, t + 100, nx + nw + gap - 2, t + 100, GOLD, 2.2, 7)
    # spend boxes
    sx = x + 3 * nw + 2 * gap + 48
    sw = w - (sx - x)
    spend = ["Subscription upgrades", "Westville departments", "ToyBoxx + DKB effects", "Tickets and merch"]
    for i, s_ in enumerate(spend):
        sy = t + 8 + i * 48
        p.rect(sx, sy, sw, 40, fill=ICE, stroke=LINE, r=4)
        p.text(sx + 14, sy + 24, s_, "Body-B", 9, NAVY, cs=0.3)
        p.arrow(x + 3 * nw + 2 * gap + 2, t + 100, sx - 2, sy + 20, BLUE, 1.2, 5)
    # earn return
    p.rect(x, t + 216, w, 36, fill=PALE, stroke=LINE, r=4)
    p.text(x + 14, t + 239, "EARN AND CASH OUT", "Body-B", 8.5, NAVY, cs=0.5)
    p.text(x + 150, t + 239, "Creators earn KickCoin from tips and sales  →  cash out in dollars or dirhams through botim pay, never through DKB",
           "Body", 8.5, GREY)
    return 260


def page_b2(p):
    p.frame(TRACK, IDX, cont=True)
    t = CONTENT_TOP
    t = p.title(t, "KICKCOIN x BOTIM", "A LICENSED WALLET IN FRONT, A CLOSED-LOOP COIN INSIDE",
                "Fans fund a Botim wallet, convert to KickCoin, and spend it across DKB, Westville, Beat Labz and ToyBoxx. "
                "Botim holds the money and the licenses; DKB runs the experience.", size=34)
    t += p.section_bar(t, "THE FLOW", "ONE IDENTITY  •  ONE LEDGER")
    t += flow(p, MX, t, CW) + 24

    t += p.section_bar(t, "WHAT KICKCOIN UNLOCKS", "PROPOSED; ALL AT FIXED PRICES")
    hh = p.cards_row(MX, t, CW, [
        ("SUBSCRIPTIONS", "Upgrade a DKB tier, DKB Ticket + FRQNZY AI ($49.99 / mo) or Beat Labz plans, with optional wallet auto-renew."),
        ("WESTVILLE DEPARTMENTS", "Unlock districts, the music, WVWF, GFL, GBA and motorsport career tracks, venues and hidden bases.", NAVY),
        ("TOYBOXX PARAMETERS", "Controller RGB and haptic profiles, ToyBoxxOS themes and performance presets."),
        ("DKB EFFECTS", "Profile and visual effects, Beat Labz sound-effect packs, KickTok and FTV overlays.", NAVY)],
        bar="top", fill=PALE)
    t += hh + 8
    t += p.para(MX, t, CW, "Cosmetic and convenience unlocks only: nothing paid sets odds in a game or pays out cash. Items have fixed prices, "
                "not random drops, which keeps clear of loot-box rules.", "small")
    t = s8(t + 16)

    t += p.section_bar(t, "THE RULES THAT KEEP IT SAFE", "WHY EACH EXISTS")
    hh = p.cards_row(MX, t, CW, [
        ("SPEND-ONLY COIN", "KickCoin is not traded or redeemed for cash on DKB. That keeps it platform credit, not a security or a money service."),
        ("BOTIM HOLDS THE MONEY", "DKB never takes deposits or calls itself a bank. Funds, KYC and payouts sit with Botim's licensed entities.", NAVY),
        ("AGES AND CONSENT", "Age checks and parental controls for teen players; data shared between DKB and Botim only with consent.")],
        bar="top", fill=PALE)
    t += hh + 16

    t += p.section_bar(t, "WHERE IT WORKS FIRST, AND THE ASKS", "NOT AGREED TERMS")
    hb = 128
    p.rect(MX, t, 328, hb, fill=ICE, r=6)
    p.rect(MX, t, 4, hb, fill=GOLD)
    p.text(MX + 20, t + 26, "GEOGRAPHY", "Body-B", 9, NAVY, cs=0.7)
    p.para(MX + 20, t + 36, 292, "UAE first: Botim's financial features are licensed there, and Astra Tech targets MENA. That fits the Dubai campaign and "
           "the optional UAE tour leg. U.S. and German fans need a separate licensed partner until Botim's licenses extend.", "card")
    p.rect(MX + 344, t, 352, hb, fill=PALE, stroke=LINE, r=6)
    p.text(MX + 364, t + 26, "ASKS OF BOTIM", "Body-B", 9, NAVY, cs=0.7)
    p.bullets(MX + 364, t + 36, 316, ["Wallet and payout API with a sandbox", "Written statement of which licenses cover which activity",
                                      "Revenue split on top-ups and cash-outs", "Co-branding and a DKB entry inside the botim app",
                                      "Exclusivity limits so DKB can add rails"], "bulc")
    t += hb + 16

    items = ["<b>Capabilities are Astra Tech's own description</b> and need a written scope. Botim's investing page lists digital assets; KickCoin stays outside it.",
             "<b>Virtual-asset rules.</b> Any token feature needs UAE counsel (virtual-asset regulation) before launch, even if closed-loop.",
             "<b>Customer experience.</b> Diligence should check user complaints about transfer times and fees before DKB's brand rides on the rail."]
    hbx = p.bullets_h(CW - 40, items, "bulc", 2) + 52
    p.rect(MX, t, CW, s8(hbx), fill=AMBER_BG, r=6)
    p.rect(MX, t, 4, s8(hbx), fill=GOLD)
    p.text(MX + 20, t + 26, "THE HONEST FINE PRINT", "Body-B", 9, AMBER_FG, cs=0.7)
    p.bullets(MX + 20, t + 38, CW - 40, items, "bulc", 2)
    t += s8(hbx)
    p.check(t, "page_b2")
