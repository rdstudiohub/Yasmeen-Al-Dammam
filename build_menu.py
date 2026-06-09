#!/usr/bin/env python3
"""Generate Yasmeen Al Dammam complete menu HTML."""
import base64

with open('/tmp/qr_b64.txt') as f:
    qr_b64 = f.read().strip()

# ── DATA ──────────────────────────────────────────────────

grills = [
    ("كباب لحم", "Kabab Lahm", "30", "60", "120"),
    ("كباب دجاج", "Kabab Dajaj", "20", "40", "80"),
    ("أوصال لحم", "Osal Lahm", "35", "70", "140"),
    ("أوصال دجاج (شيش طاووق)", "Osal Dajaj (Shish Tawook)", "25", "50", "100"),
    ("مشكل مشويات", "Mushakal Mashwiyat", "28", "55", "110"),
    ("مشكل مشويات دجاج", "Mushakal Mashwiyat Dajaj", "33", "65", "130"),
    ("مشكل لحم", "Mushakal Lahm", "23", "45", "90"),
    ("كباب بيتي لحم", "Kabab Bayti Lahm", "35", "70", "140"),
    ("كباب كرز لحم", "Kabab Karaz Lahm", "45", "90", "180"),
    ("كباب ميرو", "Kabab Miru", "35", "70", "140"),
    ("كباب خشخاش", "Kabab Khashkhash", "35", "70", "140"),
    ("اسكندر كباب لحم", "Iskandar Kabab Lahm", "35", "70", "140"),
    ("اسكندر كباب دجاج", "Iskandar Kabab Dajaj", "25", "50", "100"),
    ("ريش غنم", "Rish Ghanam", "40", "80", "160"),
    ("دجاج على الفحم (نصف)", "Grilled Chicken (Half)", "20", "–", "–"),
    ("دجاج على الفحم (حبة)", "Grilled Chicken (Full)", "40", "–", "–"),
    ("عرايس", "Arayis", "20", "–", "–"),
    ("ماريا بالجبن", "Maria bil Jibn", "25", "–", "–"),
    ("تكة البحرين (4 أسياخ)", "Tikkat al-Bahrain (4 Skewers)", "30", "–", "–"),
]

appetizers = [
    ("حمص", "Hummus", "7", "10"),
    ("متبل", "Mutabbal", "7", "10"),
    ("بابا غنوج", "Baba Ghanoush", "7", "10"),
    ("فتوش", "Fattoush", "7", "10"),
    ("سلطة خضراء", "Salata Khadra", "7", "10"),
    ("سلطة يوناني", "Greek Salad", "–", "15"),
    ("سلطة سيزر", "Caesar Salad", "–", "15"),
]

shawarma_items = [
    ("صحن شاورما عربي مقطع", "Arabic Sliced Shawarma", "20", "25", "30", "25", "38", "42"),
    ("صحن شاورما عربي فرط", "Arabic Loose Shawarma", "25", "30", "35", "30", "45", "60"),
    ("وجبة شاورما عربي اسكندر", "Iskandar Shawarma Meal", "25", "30", "35", "25", "38", "42"),
    ("صحن شاورما ياسمين الدمام", "Yasmeen Al Dammam Shawarma", "25", "–", "35", "30", "–", "47"),
    ("وجبة شاورما كاساديا", "Quesadilla Shawarma Meal", "25", "–", "35", "30", "–", "47"),
    ("وجبة شاورما إكسترا", "Extra Shawarma Meal", "25", "–", "35", "–", "–", "–"),
    ("وجبة شاورما بانية", "Pane Shawarma Meal", "25", "–", "35", "–", "–", "–"),
    ("وجبة شاورما فرايز", "Fries Shawarma Meal", "25", "–", "35", "–", "–", "–"),
    ("وجبة شاورما فرايز بالخضار", "Fries & Veg Shawarma Meal", "25", "–", "35", "–", "–", "–"),
    ("وجبة شاورما ديتس", "Diet Shawarma Meal", "25", "–", "35", "–", "–", "–"),
    ("وجبة شاورما عائلية اقتصادية", "Family Economy Shawarma", "–", "–", "60", "–", "–", "70"),
]

sandwich_grills = [
    ("ساندويتش كباب لحم", "Kabab Lahm Sandwich", "10"),
    ("ساندويتش كباب دجاج", "Kabab Dajaj Sandwich", "8"),
    ("ساندويتش أوصال لحم", "Osal Lahm Sandwich", "12"),
    ("ساندويتش شيش طاووق", "Shish Tawook Sandwich", "9"),
]

sandwich_shawarma = [
    ("ساندويتش صاروخ", "Sarooh Sandwich", "11", "15"),
    ("ساندويتش فطر", "Fitr (Mushroom) Sandwich", "9", "12"),
    ("ساندويتش شامي", "Shami Sandwich", "7", "10"),
    ("ساندويتش صامولي", "Samooli Sandwich", "7", "10"),
    ("ساندويتش إيطالي", "Italian Sandwich", "9", "14"),
    ("ساندويتش فرنسي", "French Sandwich", "11", "18"),
    ("ساندويتش مكسيكي", "Mexican Sandwich", "15", "18"),
    ("ساندويتش صاروخ بانية", "Sarooh Pane Sandwich", "15", "25"),
    ("ساندويتش بطاطس", "Potato Sandwich", "5", "7"),
]

pizzas = [
    ("بيتزا خضار", "Veggie Pizza", "12", "18", "24"),
    ("بيتزا مارغريتا", "Margherita Pizza", "12", "18", "24"),
    ("بيتزا مكسيكان", "Mexican Pizza", "12", "18", "24"),
    ("بيتزا دجاج", "Chicken Pizza", "15", "21", "27"),
    ("بيتزا لحم", "Meat Pizza", "17", "23", "29"),
    ("بيتزا مشكل", "Mixed Pizza", "16", "21", "28"),
    ("بيتزا رنش", "Ranch Pizza", "15", "20", "27"),
    ("بيتزا باربيكيو", "BBQ Pizza", "15", "20", "27"),
    ("بيتزا بيبيروني", "Pepperoni Pizza", "15", "20", "27"),
    ("بيتزا شاورما دجاج", "Chicken Shawarma Pizza", "15", "21", "27"),
    ("بيتزا شاورما لحم", "Meat Shawarma Pizza", "17", "23", "29"),
    ("بيتزا تونة", "Tuna Pizza", "15", "20", "25"),
    ("بيتزا هواي", "Hawaiian Pizza", "15", "20", "25"),
    ("بيتزا فود تندر", "Chicken Tenders Pizza", "15", "20", "25"),
    ("بيتزا تورتيلا", "Tortilla Pizza", "15", "20", "25"),
]

pastries = [
    ("فطيرة نوتيلا", "Nutella Pastry", "10"),
    ("فطيرة فلافل", "Falafel Pastry", "10"),
    ("فطيرة بيض بالجبن", "Egg & Cheese Pastry", "12"),
    ("فطيرة بالبنة بالبيض", "Labneh & Egg Pastry", "12"),
    ("فطيرة سبانخ", "Spinach Pastry", "8"),
    ("فطيرة محمرة", "Mhamra Pastry", "6"),
    ("فطيرة محمرة بالجبن", "Mhamra & Cheese Pastry", "7"),
    ("فطيرة بطاطس", "Potato Pastry", "8"),
    ("فطيرة بطاطس بالجبن", "Potato & Cheese Pastry", "10"),
    ("فطيرة جبن سائل", "Cream Cheese Pastry", "7"),
    ("فطيرة مكس جبن", "Mixed Cheese Pastry", "9"),
    ("فطيرة لبنة", "Labneh Pastry", "7"),
    ("فطيرة لبنة بالزعتر", "Labneh & Za'atar Pastry", "7"),
    ("فطيرة لبنة بالعسل", "Labneh & Honey Pastry", "8"),
    ("فطيرة زعتر", "Za'atar Pastry", "6"),
    ("فطيرة مشكل دجاج", "Mixed Chicken Pastry", "8"),
    ("فطيرة مشكل لحم", "Mixed Meat Pastry", "10"),
    ("فطيرة عكاوي", "Akkawi Pastry", "9"),
    ("فطيرة عش البلبل", "Ashp Balbul Pastry", "9"),
]

fries_side = [
    ("صحن بطاطس", "Fries Plate", "5", "10", "15"),
    ("صحن بطاطس بالجبن", "Cheese Fries Plate", "10", "15", "20"),
    ("بطاطس ويدجز", "Potato Wedges", "15", "–", "–"),
    ("بطاطس ديبرز", "Potato Dippers", "15", "–", "–"),
]

juices = [
    ("كوكتيل", "Cocktail", "15", "22", "8", "6"),
    ("طبقات", "Layered Cocktail", "18", "24", "10", "8"),
    ("مانجو", "Mango", "15", "22", "8", "6"),
    ("فراولة", "Strawberry", "15", "22", "8", "6"),
    ("جوافة", "Guava", "15", "22", "8", "6"),
    ("ليمون / ليمون بالنعناع", "Lemon / Lemon & Mint", "15", "22", "8", "6"),
    ("خربز", "Melon", "15", "22", "8", "6"),
    ("بطيخ", "Watermelon", "15", "22", "8", "6"),
    ("موز بالحليب", "Banana Milk", "15", "22", "8", "6"),
    ("موز بالحليب والعسل", "Banana Milk & Honey", "15", "22", "8", "6"),
    ("أناناس", "Pineapple", "15", "22", "8", "6"),
    ("رمان", "Pomegranate", "15", "22", "8", "6"),
    ("كيوي", "Kiwi", "15", "22", "8", "6"),
    ("عوار القلب", "Awar al-Qalb", "18", "24", "10", "8"),
    ("أصفهاني", "Isfahani", "18", "24", "10", "8"),
    ("عصير جي", "Juice J", "18", "24", "10", "8"),
    ("موهيتو", "Mojito", "–", "–", "12", "10"),
    ("أفوكادو", "Avocado", "18", "24", "10", "8"),
    ("برتقال", "Orange", "18", "24", "10", "8"),
    ("سبيشل ياسمين الدمام", "Yasmeen Special", "20", "25", "12", "10"),
    ("عصير فيتامين C", "Vitamin C Juice", "18", "25", "10", "8"),
    ("عصير روقان", "Rawqan Juice", "18", "25", "10", "8"),
    ("عرايسي", "Arayisi", "18", "24", "10", "8"),
    ("عرايسي ملكي", "Arayisi King", "18", "25", "15", "12"),
    ("سلطة فواكة (كاسة)", "Fruit Salad (Cup)", "–", "–", "10", "8"),
    ("سلطة فواكة (صحن)", "Fruit Salad (Plate)", "–", "–", "–", "10"),
    ("ميلك شيك (أوريو + لوتس)", "Milkshake (Oreo + Lotus)", "18", "25", "10", "8"),
]

extras = [
    ("إضافة قطعة جبن شيدر", "Add Cheddar Cheese Slice", "1"),
    ("إضافة جبن موزاريلا", "Add Mozzarella Cheese", "3"),
    ("إضافة أي علبة صوص", "Add Any Sauce Pack", "2"),
]

# ── HTML GENERATION ───────────────────────────────────────

def h(s):
    """Escape HTML"""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

HTML = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>مطعم ياسمين الدمام | Yasmeen Al Dammam</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&family=Playfair+Display:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth;scroll-padding-top:60px}}
body{{font-family:'Tajawal','Playfair Display',sans-serif;background:#0a0a0a;color:rgba(255,255,255,.88);min-height:100vh;overflow-x:hidden;direction:rtl}}
img{{max-width:100%;height:auto;display:block}}
.menu-wrap{{max-width:500px;margin:0 auto;position:relative;overflow:hidden}}
.header{{background:linear-gradient(135deg,#1a1a1a,#2a2a2a,#1a1a1a);text-align:center;padding:28px 16px 18px;position:relative}}
.header::before{{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#D4A843,transparent,#D4A843)}}
.header .logo-ar{{font-size:36px;font-weight:900;color:#D4A843;line-height:1.2;text-shadow:0 2px 10px rgba(212,168,67,.3)}}
.header .logo-en{{font-family:'Playfair Display',serif;font-size:12px;font-weight:400;letter-spacing:4px;text-transform:uppercase;color:rgba(255,255,255,.5);margin-top:3px}}
.header .hdiv{{width:40px;height:2px;background:linear-gradient(90deg,transparent,#D4A843,transparent);margin:8px auto}}
.header .h-sub{{font-size:11px;color:rgba(255,255,255,.4);letter-spacing:2px}}
.header .h-actions{{display:flex;gap:6px;justify-content:center;margin-top:12px;flex-wrap:wrap}}
.header .h-actions a{{display:flex;align-items:center;gap:5px;padding:7px 14px;border-radius:20px;font-size:11px;font-weight:500;text-decoration:none;transition:.2s}}
.btn-wa{{background:#25D366;color:#fff}}
.btn-call{{background:#D4A843;color:#1a1a1a}}
.btn-map{{background:transparent;color:#D4A843;border:1px solid #D4A843}}
.cat-nav{{position:sticky;top:0;z-index:100;background:#0a0a0a;padding:5px;overflow-x:auto;display:flex;gap:4px;white-space:nowrap;-webkit-overflow-scrolling:touch;scrollbar-width:none;border-bottom:2px solid #D4A843}}
.cat-nav::-webkit-scrollbar{{display:none}}
.cat-tab{{flex-shrink:0;padding:7px 12px;border:none;border-radius:20px;font-family:'Tajawal',sans-serif;font-size:12px;font-weight:600;background:rgba(212,168,67,.08);color:rgba(255,255,255,.5);cursor:pointer;transition:.25s;display:flex;flex-direction:column;align-items:center;gap:1px;border:1px solid transparent}}
.cat-tab .tab-en{{font-family:'Playfair Display',serif;font-size:7px;font-weight:400;letter-spacing:.5px;opacity:.5}}
.cat-tab.active,.cat-tab:active{{background:rgba(212,168,67,.2);color:#D4A843;border-color:rgba(212,168,67,.3)}}
.cat-section{{display:none;margin:10px;background:linear-gradient(135deg,#161616,#1e1e1e);border-radius:14px;overflow:hidden;border:1px solid rgba(212,168,67,.12)}}
.cat-section.active{{display:block;animation:fadeIn .35s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:translateY(0)}}}}
.section-header{{background:linear-gradient(135deg,#D4A843,#b8922f);padding:16px;text-align:center}}
.section-header h2{{font-size:24px;font-weight:900;color:#1a1a1a;margin:0}}
.section-header .sh-en{{font-family:'Playfair Display',serif;font-size:12px;font-weight:600;color:rgba(26,26,26,.7);letter-spacing:2px;text-transform:uppercase}}
.item{{display:flex;align-items:center;justify-content:space-between;padding:11px 16px;border-bottom:1px solid rgba(255,255,255,.04);gap:6px;min-height:48px}}
.item:last-child{{border-bottom:none}}
.item-name{{flex:1}}
.item-name .ar{{font-size:15px;font-weight:600;color:#fff;display:block;line-height:1.3}}
.item-name .en{{font-family:'Playfair Display',serif;font-size:11px;font-weight:400;color:rgba(255,255,255,.45);display:block;line-height:1.3}}
.price{{font-family:'Tajawal',sans-serif;font-size:14px;font-weight:700;color:#D4A843;white-space:nowrap;text-align:left;direction:ltr}}
.price-grid{{display:grid;gap:4px;font-size:12px;text-align:center;direction:ltr}}
.price-grid .pg-row{{display:grid;grid-template-columns:repeat(3,1fr);gap:3px}}
.price-grid .pg-row span{{background:rgba(212,168,67,.08);padding:3px 5px;border-radius:4px;font-weight:600;color:#D4A843}}
.price-grid .pg-label{{font-size:9px;color:rgba(255,255,255,.4);font-weight:400;font-family:'Tajawal',sans-serif}}
.price-grid .pg-row-2{{display:grid;grid-template-columns:repeat(2,1fr);gap:3px}}
.price-grid .pg-row-2 span{{background:rgba(212,168,67,.08);padding:3px 5px;border-radius:4px;font-weight:600;color:#D4A843}}
.price-table{{width:100%;border-collapse:collapse;margin:0;font-size:13px}}
.price-table th{{background:rgba(212,168,67,.15);color:#D4A843;font-weight:600;padding:8px 5px;text-align:center;font-size:11px}}
.price-table td{{padding:7px 5px;text-align:center;border-bottom:1px solid rgba(255,255,255,.04);color:#fff}}
.price-table td:first-child{{text-align:right;font-weight:600}}
.price-table .en-sub{{font-family:'Playfair Display',serif;font-size:9px;color:rgba(255,255,255,.35);display:block}}
.price-table .last td{{border-bottom:none}}
.fries-note{{padding:10px 16px;background:rgba(212,168,67,.05);border-top:1px solid rgba(212,168,67,.1)}}
.fries-note p{{font-size:12px;color:rgba(255,255,255,.6);margin:0;display:flex;justify-content:space-between;align-items:center}}
.footer{{background:linear-gradient(135deg,#1a1a1a,#0a0a0a);text-align:center;padding:25px 16px;margin-top:10px;border-top:2px solid #D4A843}}
.footer .qr{{width:110px;height:110px;margin:0 auto 10px;display:block}}
.footer .qr-label{{font-size:12px;color:rgba(255,255,255,.4);margin-bottom:8px}}
.footer .qr-scan{{font-size:10px;color:rgba(255,255,255,.3)}}
.footer .f-text{{font-size:11px;color:rgba(255,255,255,.3)}}
.footer .f-div{{width:30px;height:1px;background:#D4A843;margin:8px auto}}
.sand-sub{{padding:8px 16px 4px;font-size:13px;font-weight:700;color:#D4A843;border-bottom:1px solid rgba(212,168,67,.1)}}
.sand-sub .sub-en{{font-family:'Playfair Display',serif;font-size:9px;font-weight:400;color:rgba(255,255,255,.35);display:block}}
</style>
</head>
<body>

<div class="menu-wrap">

<!-- ═══ HEADER ═══ -->
<div class="header">
<div class="logo-ar">مطعم ياسمين الدمام</div>
<div class="logo-en">Yasmeen Al Dammam</div>
<div class="hdiv"></div>
<div class="h-sub">الدمام، المملكة العربية السعودية</div>
<div class="h-actions">
<a class="btn-wa" href="https://wa.me/966535604862" target="_blank">💬 واتساب</a>
<a class="btn-call" href="tel:+966535604862">📞 اتصال</a>
<a class="btn-map" href="https://maps.app.goo.gl/YasmeenDammam" target="_blank">📍 موقعنا</a>
</div>
</div>

<!-- ═══ CATEGORY NAV ═══ -->
<nav class="cat-nav" id="catNav">
<button class="cat-tab active" data-cat="grills"><span>مشويات</span><span class="tab-en">Grills</span></button>
<button class="cat-tab" data-cat="appetizers"><span>مقبلات</span><span class="tab-en">Appetizers</span></button>
<button class="cat-tab" data-cat="shawarma"><span>شاورما</span><span class="tab-en">Shawarma</span></button>
<button class="cat-tab" data-cat="sandwiches"><span>سندويتشات</span><span class="tab-en">Sandwiches</span></button>
<button class="cat-tab" data-cat="pizza"><span>بيتزا</span><span class="tab-en">Pizza</span></button>
<button class="cat-tab" data-cat="pastries"><span>معجنات</span><span class="tab-en">Pastries</span></button>
<button class="cat-tab" data-cat="juices"><span>عصائر</span><span class="tab-en">Juices</span></button>
<button class="cat-tab" data-cat="extras"><span>إضافات</span><span class="tab-en">Extras</span></button>
</nav>

<!-- ═══ 1. GRILLS ═══ -->
<div class="cat-section active" id="grills">
<div class="section-header"><h2>المشويات</h2><div class="sh-en">Grills</div></div>
<table class="price-table">
<tr><th>الصنف</th><th>فرد</th><th>½ كيلو</th><th>كيلو</th></tr>
'''

for ar, en, p, hk, k in grills:
    HTML += f'<tr><td>{h(ar)}<span class="en-sub">{h(en)}</span></td><td>{h(p)}</td><td>{h(hk)}</td><td>{h(k)}</td></tr>\n'

HTML += '</table></div>\n'

# ═══ 2. APPETIZERS ═══
HTML += '''<div class="cat-section" id="appetizers">
<div class="section-header"><h2>مقبلات</h2><div class="sh-en">Appetizers & Salads</div></div>
<table class="price-table">
<tr><th>الصنف</th><th>صغير</th><th>كبير</th></tr>
'''

for ar, en, s, l in appetizers:
    HTML += f'<tr><td>{h(ar)}<span class="en-sub">{h(en)}</span></td><td>{h(s)}</td><td>{h(l)}</td></tr>\n'

HTML += '</table></div>\n'

# ═══ 3. SHAWARMA ═══
HTML += '''<div class="cat-section" id="shawarma">
<div class="section-header"><h2>أطباق الشاورما</h2><div class="sh-en">Shawarma Platters</div></div>
<table class="price-table">
<tr><th>الصنف</th><th>دجاج S</th><th>دجاج M</th><th>دجاج L</th><th>لحم S</th><th>لحم M</th><th>لحم L</th></tr>
'''

for ar, en, cs, cm, cl, ms, mm, ml in shawarma_items:
    HTML += f'<tr><td>{h(ar)}<span class="en-sub">{h(en)}</span></td><td>{h(cs)}</td><td>{h(cm)}</td><td>{h(cl)}</td><td>{h(ms)}</td><td>{h(mm)}</td><td>{h(ml)}</td></tr>\n'

# Fries side dishes
HTML += '</table>\n'
HTML += '<div class="fries-note"><p style="font-weight:700;color:#D4A843;font-size:14px;margin-bottom:6px;">🍟 البطاطس المقلية <span style="font-family:Playfair Display;font-size:10px;color:rgba(255,255,255,.4);">Fries &amp; Sides</span></p>'

for ar, en, s, m, l in fries_side:
    if s == m == l == "–":
        HTML += f'<p>{h(ar)} <span class="en-sub" style="display:inline;font-size:9px;">{h(en)}</span> <span class="price">{h(s)}</span></p>\n'
    elif l == "–":
        HTML += f'<p>{h(ar)} <span class="en-sub" style="display:inline;font-size:9px;">{h(en)}</span> <span class="price">{h(s)}</span></p>\n'
    else:
        # Actually for fries, show all three
        continue

HTML += '</div></div>\n'

# Actually let me redo fries properly
# Remove the fries_note above and redo
HTML = HTML.replace('<div class="fries-note"><p style="font-weight:700;color:#D4A843;font-size:14px;margin-bottom:6px;">🍟 البطاطس المقلية <span style="font-family:Playfair Display;font-size:10px;color:rgba(255,255,255,.4);">Fries &amp; Sides</span></p>', '')

# Insert proper fries section
fries_html = '''</table>
<div class="sand-sub">🍟 البطاطس المقلية <span class="sub-en">Fries &amp; Sides</span></div>
<table class="price-table">
<tr><th>الصنف</th><th>صغير</th><th>وسط</th><th>كبير</th></tr>
'''
for ar, en, s, m, l in fries_side:
    fries_html += f'<tr><td>{h(ar)}<span class="en-sub">{h(en)}</span></td><td>{h(s)}</td><td>{h(m)}</td><td>{h(l)}</td></tr>\n'
fries_html += '</table>\n'

# Find the closing </div> of the shawarma section and put fries before it
HTML = HTML.replace('</table>\n<div class="fries-note"', fries_html + '<div class="fries-note"')
HTML = HTML.replace('<div class="fries-note">', '<div style="padding:8px 16px;text-align:center;border-top:1px solid rgba(212,168,67,.1)"><p style="font-size:11px;color:rgba(255,255,255,.4);margin:0">جميع أسعار الشاورما بالريال السعودي</p></div></div>')

# ═══ 4. SANDWICHES ═══
sand_html = '''<div class="cat-section" id="sandwiches">
<div class="section-header"><h2>سندويتشات</h2><div class="sh-en">Sandwiches</div></div>
<div class="sand-sub">🥩 سندويتشات مشويات <span class="sub-en">Grilled Sandwiches</span></div>
<table class="price-table">
<tr><th>الصنف</th><th>السعر</th></tr>
'''

for ar, en, p in sandwich_grills:
    sand_html += f'<tr><td>{h(ar)}<span class="en-sub">{h(en)}</span></td><td>{h(p)}</td></tr>\n'

sand_html += '</table>\n<div class="sand-sub">🌯 شاورما وسندويتشات <span class="sub-en">Shawarma &amp; Other Sandwiches</span></div>\n'
sand_html += '<table class="price-table"><tr><th>الصنف</th><th>دجاج</th><th>لحم</th></tr>\n'

for ar, en, c, m in sandwich_shawarma:
    sand_html += f'<tr><td>{h(ar)}<span class="en-sub">{h(en)}</span></td><td>{h(c)}</td><td>{h(m)}</td></tr>\n'

sand_html += '</table></div>\n'

# Find position to insert sandwiches - after the shawarma closing div
insert_pos = HTML.find('</div>', HTML.find('fries-note">'))
# Actually let me just append at the right place
sandwiches_insert_pos = HTML.rfind('</div>\n', HTML.rfind('id="shawarma"')) + len('</div>\n')
HTML = HTML[:sandwiches_insert_pos] + sand_html + HTML[sandwiches_insert_pos:]

# ═══ 5. PIZZA ═══
pizza_html = '''<div class="cat-section" id="pizza">
<div class="section-header"><h2>البيتزا</h2><div class="sh-en">Pizza</div></div>
<table class="price-table">
<tr><th>الصنف</th><th>صغير</th><th>وسط</th><th>كبير</th></tr>
'''

for ar, en, s, m, l in pizzas:
    pizza_html += f'<tr><td>{h(ar)}<span class="en-sub">{h(en)}</span></td><td>{h(s)}</td><td>{h(m)}</td><td>{h(l)}</td></tr>\n'

pizza_html += '</table></div>\n'

# Insert pizza after sandwiches
sandwiches_end = HTML.find('</div>\n', HTML.find('id="sandwiches"')) + len('</div>\n')
# Find the right closing div
sand_end = HTML.find('</div>', HTML.find('sand-sub', HTML.find('id="sandwiches"')))
# Let me just append at the end and reorder
HTML = HTML[:sandwiches_end] + pizza_html + HTML[sandwiches_end:]

# Hmm this approach is getting messy. Let me just rewrite the whole thing as a full script.
# Let me write it all in one shot.

print("Menu data prepared, now writing full HTML...")
