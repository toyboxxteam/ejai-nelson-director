"""Section 03 (continued): announced tour dates and the 60-day radio / viral / PR sequence."""
import math

from reportlab.lib.colors import HexColor, white

from dkb_lib import *
from pages_c import table, AMBER_BG, AMBER_FG, GREEN_BG, GREEN_FG

TRACK = "03 / LIVE ENTERTAINMENT & GLOBAL TOURING FLYWHEEL"
IDX = "03 / 09"


def page_dates(p):
    p.frame(TRACK, IDX, cont=True)
    t = CONTENT_TOP
    t = p.title(t, "TOUR DATES: BOOKED OR BEING BOOKED", "DAKICKBACK TOUR  •  WALT REEDER PRESENTS  •  ANNOUNCED DATES",
                "Two dates are announced with public flyers. Each is built as a radio-first campaign: a record, a video, an A-list "
                "voice and a 60-day run into the room.", size=32)
    fw = (CW - 16) / 2.0
    fh = 440
    p.img("flyer-portsmouth.jpg", MX, t, fw, fh, "cover", r=6)
    p.img("flyer-hampton.jpg", MX + fw + 16, t, fw, fh, "cover", r=6)
    t += fh + 8
    p.text(MX, t + 8, "Tour flyers as supplied by management. The flyers read “Walt Reed”; the agency is Walt Reeder Entertainment.",
           "Body-I", 7, GREY)
    t += 24

    facts = [("THU NOV 12, 2026  •  PORTSMOUTH, VA",
              "<b>Grown &amp; Sexy Thursdays: DaKickBack Tour</b> at Serenity 5 Lounge, 3938 George Washington Hwy. FRQNZY and Slim from 112 "
              "(host, performing his hits); vibes by DJ Kidd. Tour and single release: “Tha Vibe”. Tickets on Eventbrite per the flyer."),
             ("THU DEC 31, 2026  •  HAMPTON, VA",
              "<b>FRQNZY x GloRilla, live in concert.</b> New radio single “Unmatched”. Doors 9 PM; VIP and bottle service; "
              "tickets on sale per the flyer. Venue is not named on the flyer.")]
    hh = max(p.card_h(fw - 4, a, b, 12) for a, b in facts)
    for i, (a, b) in enumerate(facts):
        p.card(MX + i * (fw + 16), t, fw, hh, a, b, accent=BLUE if i == 0 else GOLD, fill=ICE, bar="left")
    t += hh + 16

    t += p.section_bar(t, "TOUR PIPELINE", "ANNOUNCED = PUBLIC FLYER; CONTRACT STATUS PER MANAGEMENT")
    cols = [("DATE / LEG", 132, "l"), ("WHERE", 150, "l"), ("BILLING / RECORD", 254, "l"), ("STATUS", 160, "l")]
    rows = [["<b>Thu Nov 12, 2026</b>", "Portsmouth, VA", "FRQNZY + Slim from 112; DJ Kidd; “Tha Vibe”", "Announced; tickets live"],
            ["<b>Thu Dec 31, 2026</b>", "Hampton, VA", "FRQNZY x GloRilla; “Unmatched”", "Announced; tickets on sale"],
            ["<b>East Coast route</b>", "Major metros", "Culminating with Babyface Ray", "Being booked"],
            ["<b>West Coast route</b>", "TBA", "FRQNZY + Krayzie Bone", "Being booked"],
            ["<b>Germany / UAE</b>", "Optional", "Packages under discussion", "Exploring"]]
    h = table(p, MX, t, cols, rows)
    t += h + 8
    t += p.para(MX, t, CW, "Executed artist agreements, venue contracts and capacities are confirmed per date before any figure in this deck is "
                "relied on; the flyers show public promotion, not settlement terms.", "src")
    p.check(t, "page_dates")


def page_seq(p):
    p.frame(TRACK, IDX, cont=True)
    t = CONTENT_TOP
    t = p.title(t, "THE 60-DAY SEQUENCE", "RADIO  •  VIRAL  •  PR  •  A COORDINATED BUILD TO SHOW NIGHT",
                "Every record comes with an A-list voice, a video and an artist commitment to promote it until the show. The campaign is "
                "staged so pressure builds each week, then lands on one night.", size=34)
    # staircase
    steps = [("D-60", "SUN NOV 1", "Record + video drop; radio add day"),
             ("D-45", "MON NOV 16", "A-list profile live on DKB; artist promo begins"),
             ("D-30", "TUE DEC 1", "PR wave: late-night, morning shows, podcasts"),
             ("D-14", "THU DEC 17", "Creator and fan challenge on KickTok"),
             ("D-7", "THU DEC 24", "Ticket push, countdown, Hot 100 chart run"),
             ("D-0", "THU DEC 31", "Hampton: the show; replay and label meetings")]
    sw = (CW - 5 * 10) / 6.0
    base = t + 232
    for i, (d, dt, txt) in enumerate(steps):
        h = 96 + i * 26
        x = MX + i * (sw + 10)
        col = GOLD if i == 5 else (NAVY if i % 2 == 0 else BLUE)
        p.rect(x, base - h, sw, h, fill=col, r=6)
        fg = NAVY if col == GOLD else white
        p.text(x + 12, base - h + 26, d, DISPLAY, 15, fg)
        p.text(x + 12, base - h + 42, dt, "Body-B", 7.5, NAVY if col in (GOLD,) else (SKY if col == NAVY else HexColor("#DCEBFA")), cs=0.4)
        p.para(x + 12, base - h + 50, sw - 24, txt, S("st", 8, 10.5, NAVY if col == GOLD else HexColor("#E6F0FC")))
    t = base + 8
    t += p.para(MX, t, CW, "Dates count back from the Hampton show on Dec 31, which is exactly 60 days after Nov 1. Portsmouth (Nov 12) is the "
                "compressed pilot run for the same sequence. The 60-day window sits inside the 14–121-day campaign range.", "small")
    t = s8(t + 16)

    t += p.section_bar(t, "WHAT RUNS IN EACH CHANNEL", "TARGETS, NOT GUARANTEES")
    hh = p.cards_row(MX, t, CW, [
        ("RADIO ROTATION", "Targeted adds and rotation in the tour markets across the 60 days, tracked with radio monitoring and streaming velocity. "
         "Paid promotion is disclosed under sponsorship-identification rules; no undisclosed pay-for-play."),
        ("VIRAL", "Vertical clips from both artists, a KickTok challenge and creator seeding, released in a planned order so each wave "
         "builds on the last.", NAVY),
        ("PR", "Late-night and morning-show pitches, plus the radio and podcast circuit named earlier, timed to the weeks above."),
        ("DKB + PARTNERS", "Artist profiles and ticket funnel on DKB; UAE / MENA seeding through Botim; venue connectivity from Evan Shive's "
         "network. All proposed.", NAVY)], bar="top", fill=PALE)
    t += hh + 16

    t += p.section_bar(t, "FROM A RECORD TO A LABEL CONVERSATION", "WHY EACH RECORD RAISES CATALOGUE VALUE")
    lad = [("1", "A-LIST RECORD", "A celebrity feature makes the single worth a major's attention."),
           ("2", "PROOF", "Radio adds and spins, streams, Shazams, ticket sell-through and DKB sign-ups."),
           ("3", "LABEL TALKS", "Distribution or licence, marketing budget, advance; keep as much ownership as the terms allow."),
           ("4", "CATALOGUE EQUITY", "Each proven record lifts the value of the masters and of Dr. Ish's 1% publishing participation.")]
    lw = (CW - 3 * 20) / 4.0
    for i, (n, a, b) in enumerate(lad):
        x = MX + i * (lw + 20)
        col = GOLD if i == 3 else (NAVY if i % 2 == 0 else BLUE)
        p.rect(x, t, lw, 112, fill=col, r=6)
        fg = NAVY if col == GOLD else white
        p.text(x + 14, t + 28, n, DISPLAY, 18, fg)
        p.text(x + 40, t + 26, a, "Body-B", 8.5, fg, cs=0.3)
        p.para(x + 14, t + 40, lw - 28, b, S("lb", 8.5, 11, NAVY if col == GOLD else HexColor("#E6F0FC")))
        if i < 3:
            p.arrow(x + lw + 2, t + 56, x + lw + 18, t + 56, GOLD, 1.8, 6)
    t += 128

    t += p.section_bar(t, "FOUR BRANDS GROWN BY EVERY RECORD", "GOAL: HOUSEHOLD NAMES")
    br = [("DAKICKBACK", "The platform and tour brand on every flyer, profile and ticket."), ("FRQNZY", "The artist at the center of each record and video."),
          ("BOTIM", "The money layer: wallet, top-ups and fan payments in UAE / MENA."), ("EVAN SHIVE'S NETWORK", "The connectivity behind live nights and streaming.")]
    bw = (CW - 3 * 12) / 4.0
    for i, (a, b) in enumerate(br):
        x = MX + i * (bw + 12)
        p.rect(x, t, bw, 80, fill=PALE, stroke=LINE, r=4)
        p.rect(x, t, bw, 4, fill=BLUE if i % 2 else NAVY)
        p.text(x + 12, t + 28, a, "Body-B", 8.5, NAVY, cs=0.3)
        p.para(x + 12, t + 36, bw - 24, b, "card")
    t += 96

    items = ["<b>Commitments are a proposed rider term.</b> Each artist agrees to create a DKB profile and promote the record, video and ticket link "
             "through show night; flyers show participation, signed riders are confirmed per artist.",
             "<b>Virality cannot be guaranteed.</b> The sequence raises the odds; it does not promise a result. No label deal exists today.",
             "<b>Clearances.</b> Features, samples and likeness approvals are cleared before release."]
    hb = p.bullets_h(CW - 40, items, "bulc", 2) + 52
    p.rect(MX, t, CW, s8(hb), fill=AMBER_BG, r=6)
    p.rect(MX, t, 4, s8(hb), fill=GOLD)
    p.text(MX + 20, t + 26, "THE HONEST FINE PRINT", "Body-B", 9, AMBER_FG, cs=0.7)
    p.bullets(MX + 20, t + 38, CW - 40, items, "bulc", 2)
    t += s8(hb)
    p.check(t, "page_seq")
