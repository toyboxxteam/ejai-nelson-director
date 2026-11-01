"""Build the DKB investor PDF.  Usage: python3 build_deck.py [out.pdf] [--investor "Dr. Chad"]"""
import argparse
import os
import sys

ap = argparse.ArgumentParser(description="Build the DKB investor deck PDF")
ap.add_argument("out", nargs="?", default=None, help="output PDF path")
ap.add_argument("--investor", default="Dr. Ish", help="investor name as it should read, e.g. 'Dr. Chad'")
args = ap.parse_args()
os.environ["DKB_INVESTOR"] = args.investor   # must be set before dkb_lib is imported

from reportlab.pdfgen import canvas
from dkb_lib import W, H, Page, sub
import pages_a, pages_b, pages_c, pages_d, pages_e

OUT = args.out or "DKB_%s_Investor_Deck.pdf" % args.investor.replace(".", "").replace(" ", "_")


def build():
    c = canvas.Canvas(OUT, pagesize=(W, H))
    c.setTitle(sub("DaKickBack (DKB) - $2M Launch Opportunity - Investor Presentation - @@INV@@"))
    c.setAuthor("DAKICKBACK LLC")
    c.setSubject("Confidential investor discussion - October 2026")
    p = Page(c)
    seq = [pages_a.page01, pages_a.page02, pages_a.page03a, pages_a.page03b, pages_a.page03c,
           pages_b.page04, pages_b.page05, pages_b.page06, pages_d.page_t1, pages_d.page_t2, pages_d.page_t3, pages_e.page_b1, pages_e.page_b2, pages_c.page_ip, pages_c.page_daw, pages_c.page_akai, pages_c.page_value1, pages_c.page_value2, pages_b.page07a, pages_b.page07b,
           pages_b.appx_roster,
           lambda p: pages_b.appx_sheet(p, "A2 / FOUNDER, MUSIC TRACTION & STRATEGIC RELATIONSHIPS", "A2 / A6",
                                        "FOUNDER ONE-SHEET", "MALCOLM \u201cFRQNZY\u201d HENDERSON  /  GOOD KARMA MUSIC GROUP",
                                        "i-141.jpg", "Source artwork: DKB founder and traction one-sheet (reproduced in full)."),
           lambda p: pages_b.appx_sheet(p, "A3 / WELCOME 2 WESTVILLE WORLD & DEVELOPMENT MATERIALS", "A3 / A6",
                                        "WESTVILLE ONE-SHEET", "FLAGSHIP GAME IP  /  WORLD, DISTRICTS & CHARACTER PIPELINE",
                                        "i-142.jpg", "Source artwork: Welcome 2 Westville one-sheet (reproduced in full). Planned scope is not completed content."),
           lambda p: pages_b.appx_sheet(p, "A4 / THE LEGEND OF FRQNZY FRANCHISE SHEET", "A4 / A6",
                                        "THE LEGEND OF FRQNZY", "FANTASY ADVENTURE FRANCHISE  /  HERO, WORLD, ARTIFACTS, BOSSES",
                                        "i-143.jpg", "Source artwork: Legend of FRQNZY franchise sheet (reproduced in full). Concept art is not a completed game."),
           pages_b.appx_process, pages_b.appx_notice]
    for fn in seq:
        try:
            fn(p)
        except RuntimeError as e:
            print("OVERFLOW", fn.__name__, e)
        c.showPage()
    c.save()
    print("wrote", OUT)

if __name__ == "__main__":
    build()
