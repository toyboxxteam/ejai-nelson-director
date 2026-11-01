"""Drawing helpers for the DKB investor deck (top-down coordinates, 8 pt grid)."""
import math
import os

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph

HERE = os.path.dirname(os.path.abspath(__file__))
INVESTOR = os.environ.get("DKB_INVESTOR", "Dr. Chad")   # set via build_deck.py --investor


def sub(s):
    """Resolve investor-name tokens at render time so one source builds any investor's copy."""
    return s.replace("@@INVU@@", INVESTOR.upper()).replace("@@INV@@", INVESTOR)

ASSETS = os.path.join(HERE, "assets")

# ---- page geometry (11 x 17 in) -------------------------------------------------
W, H = 792, 1224
MX = 48                       # left / right margin (6 x 8)
CW = W - 2 * MX               # 696 content width
TOP_SAFE = 54                 # 0.75 in minimum from top trim
HDR_BASE = 72                 # running header baseline (from top)
HDR_RULE = 84
TRACK_BASE = 108              # section breadcrumb baseline
CONTENT_TOP = 128
CONTENT_BOTTOM = 1152         # footer zone starts below this
FOOT_RULE = 1176              # from top
FOOT_BASE = 1196

# ---- palette (sampled from the source artwork) --------------------------------------
NAVY = HexColor("#081D42")
BLUE = HexColor("#1472CE")
SKY = HexColor("#5BB6F0")
ICE = HexColor("#DCEBFA")
PALE = HexColor("#F2F7FC")
LINE = HexColor("#D3E1F2")
INK = HexColor("#14213D")
GREY = HexColor("#56657D")
GOLD = HexColor("#F2A81D")
GREEN = HexColor("#0FB872")
RED = HexColor("#D64545")

# ---- fonts -------------------------------------------------------------------
_FD = "/usr/share/fonts/truetype/crosextra/"
pdfmetrics.registerFont(TTFont("Body", _FD + "Carlito-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Body-B", _FD + "Carlito-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Body-I", _FD + "Carlito-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Body-BI", _FD + "Carlito-BoldItalic.ttf"))
registerFontFamily("Body", normal="Body", bold="Body-B", italic="Body-I", boldItalic="Body-BI")
_DJ = "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf"
DISPLAY = "Body-B"
if os.path.exists(_DJ):
    pdfmetrics.registerFont(TTFont("Display", _DJ))
    DISPLAY = "Display"


def S(name, size, lead, color=INK, font="Body", align=TA_LEFT, **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=lead,
                          textColor=color, alignment=align, **kw)


ST = {
    "lead": S("lead", 11.5, 16, GREY),
    "body": S("body", 9.5, 13.5, INK),
    "bodyg": S("bodyg", 9.5, 13.5, GREY),
    "card": S("card", 9, 12.5, GREY),
    "cardk": S("cardk", 9, 12.5, INK),
    "small": S("small", 8, 11, GREY),
    "src": S("src", 7.5, 10, GREY),
    "white": S("white", 9.5, 13.5, white),
    "whiteS": S("whiteS", 9, 12.5, HexColor("#C9DDF5")),
    "ctitle": S("ctitle", 9.5, 12, NAVY, "Body-B"),
    "bul": S("bul", 9.5, 13.5, INK, leftIndent=12, bulletIndent=0, spaceAfter=3),
    "bulc": S("bulc", 9, 12.5, GREY, leftIndent=10, bulletIndent=0, spaceAfter=2),
}


def s8(v):
    return int(math.ceil(v / 8.0) * 8)


def asset(name):
    return os.path.join(ASSETS, name)


class Page:
    """Canvas wrapper working in top-down coordinates (t = points from top trim)."""

    def __init__(self, c):
        self.c = c

    def Y(self, t):
        return H - t

    # --- primitives -------------------------------------------------------------
    def rect(self, x, t, w, h, fill=None, stroke=None, r=0, lw=0.75):
        c = self.c
        if fill is not None:
            c.setFillColor(fill)
        if stroke is not None:
            c.setStrokeColor(stroke)
            c.setLineWidth(lw)
        if r:
            c.roundRect(x, self.Y(t + h), w, h, r, stroke=1 if stroke is not None else 0,
                        fill=1 if fill is not None else 0)
        else:
            c.rect(x, self.Y(t + h), w, h, stroke=1 if stroke is not None else 0,
                   fill=1 if fill is not None else 0)

    def line(self, x1, t1, x2, t2, color=LINE, lw=0.75, dash=None):
        c = self.c
        c.setStrokeColor(color)
        c.setLineWidth(lw)
        if dash:
            c.setDash(*dash)
        c.line(x1, self.Y(t1), x2, self.Y(t2))
        c.setDash()

    def text(self, x, t, s, font="Body", size=9, color=INK, align="l", cs=0):
        c = self.c
        s = sub(s)
        c.saveState()
        c.setFillColor(color)
        tx = c.beginText()
        tx.setFont(font, size)
        tx.setCharSpace(cs)
        w = pdfmetrics.stringWidth(s, font, size) + cs * max(len(s) - 1, 0)
        if align == "r":
            x = x - w
        elif align == "c":
            x = x - w / 2.0
        tx.setTextOrigin(x, self.Y(t))
        tx.textOut(s)
        c.drawText(tx)
        c.restoreState()
        return w

    def para(self, x, t, w, txt, style="body"):
        st = ST[style] if isinstance(style, str) else style
        p = Paragraph(sub(txt), st)
        _, h = p.wrap(w, 10000)
        p.drawOn(self.c, x, self.Y(t + h))
        return h

    def ph(self, w, txt, style="body"):
        st = ST[style] if isinstance(style, str) else style
        return Paragraph(sub(txt), st).wrap(w, 10000)[1]

    def img(self, name, x, t, w, h, mode="cover", r=0, stroke=None, anchor=0.5):
        """mode cover = crop to fill box; contain = fit inside box (centered)."""
        path = asset(name)
        ir = ImageReader(path)
        iw, ih = ir.getSize()
        c = self.c
        c.saveState()
        if r:
            p = c.beginPath()
            p.roundRect(x, self.Y(t + h), w, h, r)
            c.clipPath(p, stroke=0, fill=0)
        else:
            p = c.beginPath()
            p.rect(x, self.Y(t + h), w, h)
            c.clipPath(p, stroke=0, fill=0)
        if mode == "cover":
            sc = max(w / float(iw), h / float(ih))
        else:
            sc = min(w / float(iw), h / float(ih))
        dw, dh = iw * sc, ih * sc
        c.drawImage(ir, x + (w - dw) / 2.0, self.Y(t + h) + (h - dh) * (1 - anchor), dw, dh, mask="auto")
        c.restoreState()
        if stroke is not None:
            self.rect(x, t, w, h, stroke=stroke, r=r)

    # --- chrome -----------------------------------------------------------------
    def frame(self, tracker, idx, cont=False):
        c = self.c
        c.setFillColor(white)
        c.rect(0, 0, W, H, stroke=0, fill=1)
        self.text(MX, HDR_BASE, "DAKICKBACK LLC", "Body-B", 10, NAVY, cs=0.6)
        self.text(W - MX, HDR_BASE, "PRIVATE DISCUSSION / @@INVU@@ / OCT 2026", "Body-B", 8, BLUE, "r", cs=0.5)
        self.line(MX, HDR_RULE, W - MX, HDR_RULE, NAVY, 1.5)
        self.text(MX, TRACK_BASE, tracker, "Body-B", 9, BLUE, cs=0.5)
        self.line(MX, FOOT_RULE, W - MX, FOOT_RULE, LINE, 0.75)
        self.text(MX, FOOT_BASE, "DKB / CONFIDENTIAL INVESTOR DISCUSSION / COMMERCIAL TERMS SUBJECT TO EXECUTION",
                  "Body-B", 6.5, GREY, cs=0.4)
        self.text(W - MX, FOOT_BASE, idx + ("  CONT." if cont else ""), "Body-B", 8, BLUE, "r", cs=0.6)

    def title(self, t, big, sub=None, lead=None, size=34):
        self.text(MX, t + size, big, DISPLAY, size, NAVY)
        cur = t + size + 16
        if sub:
            self.text(MX, cur, sub, "Body-B", 9.5, BLUE, cs=0.8)
            cur += 16
        if lead:
            cur += 4
            cur += self.para(MX, cur, CW, lead, "lead")
        return s8(cur + 8)

    def section_bar(self, t, label, tag=None, w=CW, x=MX):
        self.text(x, t + 10, label, "Body-B", 10, NAVY, cs=0.5)
        if tag:
            self.text(x + w, t + 10, tag, "Body-B", 7.5, BLUE, "r", cs=0.5)
        self.line(x, t + 18, x + w, t + 18, LINE, 0.75)
        return 32

    # --- components -------------------------------------------------------------
    def card_h(self, w, title, body, pad=12, bstyle="card", min_h=0):
        h = pad
        if title:
            h += self.ph(w - 2 * pad, title, "ctitle") + 4
        if body:
            h += self.ph(w - 2 * pad, body, bstyle)
        h += pad
        return max(s8(h), min_h)

    def card(self, x, t, w, h, title, body, accent=BLUE, fill=PALE, bar="top", pad=12,
             bstyle="card", tstyle="ctitle", stroke=LINE, r=4):
        self.rect(x, t, w, h, fill=fill, stroke=stroke, r=r)
        c = self.c
        if bar == "top":
            c.saveState()
            p = c.beginPath()
            p.roundRect(x, self.Y(t + h), w, h, r)
            c.clipPath(p, stroke=0, fill=0)
            c.setFillColor(accent)
            c.rect(x, self.Y(t + 4), w, 4, stroke=0, fill=1)
            c.restoreState()
        elif bar == "left":
            c.saveState()
            p = c.beginPath()
            p.roundRect(x, self.Y(t + h), w, h, r)
            c.clipPath(p, stroke=0, fill=0)
            c.setFillColor(accent)
            c.rect(x, self.Y(t + h), 4, h, stroke=0, fill=1)
            c.restoreState()
        cy = t + pad + (4 if bar == "top" else 0)
        if title:
            cy += self.para(x + pad + (4 if bar == "left" else 0), cy, w - 2 * pad - (4 if bar == "left" else 0), title, tstyle) + 4
        if body:
            self.para(x + pad + (4 if bar == "left" else 0), cy, w - 2 * pad - (4 if bar == "left" else 0), body, bstyle)

    def cards_row(self, x, t, w, items, gap=16, **kw):
        n = len(items)
        cw = (w - gap * (n - 1)) / float(n)
        pad = kw.get("pad", 12)
        bar = kw.get("bar", "top")
        extra = 4 if bar == "top" else 0
        h = max(self.card_h(cw - (4 if bar == "left" else 0), it[0], it[1], pad,
                            kw.get("bstyle", "card")) for it in items) + extra
        h = s8(h)
        for i, it in enumerate(items):
            acc = it[2] if len(it) > 2 else kw.get("accent", BLUE)
            self.card(x + i * (cw + gap), t, cw, h, it[0], it[1], accent=acc,
                      **{k: v for k, v in kw.items() if k != "accent"})
        return h

    def chip(self, x, t, label, fill=ICE, color=NAVY, size=8, h=20, font="Body-B", padx=10, stroke=None):
        w = pdfmetrics.stringWidth(label, font, size) + 2 * padx
        self.rect(x, t, w, h, fill=fill, stroke=stroke, r=h / 2.0)
        self.text(x + padx, t + h / 2.0 + size * 0.33, label, font, size, color)
        return w

    def chips(self, x, t, w, items, fill=ICE, color=NAVY, gap=8, h=20, size=8, stroke=None):
        cx, cy = x, t
        for it in items:
            cw = pdfmetrics.stringWidth(it, "Body-B", size) + 20
            if cx + cw > x + w:
                cx = x
                cy += h + gap
            self.chip(cx, cy, it, fill, color, size, h, stroke=stroke)
            cx += cw + gap
        return cy + h - t

    def arrow(self, x1, t1, x2, t2, color=BLUE, lw=1.6, head=6):
        self.line(x1, t1, x2, t2, color, lw)
        ang = math.atan2(-(t2 - t1), x2 - x1)
        c = self.c
        c.setFillColor(color)
        p = c.beginPath()
        p.moveTo(x2, self.Y(t2))
        p.lineTo(x2 - head * math.cos(ang - 0.45), self.Y(t2) - head * math.sin(ang - 0.45))
        p.lineTo(x2 - head * math.cos(ang + 0.45), self.Y(t2) - head * math.sin(ang + 0.45))
        p.close()
        c.drawPath(p, stroke=0, fill=1)

    def bullets(self, x, t, w, items, style="bul", gap=0):
        cy = t
        for it in items:
            p = Paragraph(it, ST[style], bulletText="•")
            _, h = p.wrap(w, 10000)
            p.drawOn(self.c, x, self.Y(cy + h))
            cy += h + gap
        return cy - t

    def bullets_h(self, w, items, style="bul", gap=0):
        tot = 0
        for it in items:
            tot += Paragraph(it, ST[style], bulletText="•").wrap(w, 10000)[1] + gap
        return tot

    def check(self, t, label=""):
        if t > CONTENT_BOTTOM:
            raise RuntimeError("content overflow on '%s': %.1f > %d" % (label, t, CONTENT_BOTTOM))


def fmt_money(v, dec=0):
    if v >= 1e6:
        return "$%.*fM" % (2 if dec else 2, v / 1e6) if dec else "$%.2fM" % (v / 1e6)
    return "${:,.0f}".format(v)
