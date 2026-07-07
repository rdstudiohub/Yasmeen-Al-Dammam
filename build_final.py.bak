#!/usr/bin/env python3
"""Build Yasmeen Al Dammam menu with banners and working tabs."""
import os, base64

QR = '/tmp/qr_b64.txt'

with open(QR) as f:
    qr = f.read().strip()

# ── DATA ──────────────────────────────────────────────────

grills = [
    ('كباب لحم','Kabab Lahm','30','60','120'),
    ('كباب دجاج','Kabab Dajaj','20','40','80'),
    ('أوصال لحم','Osal Lahm','35','70','140'),
    ('أوصال دجاج شيش طاووق','Shish Tawook','25','50','100'),
    ('مشكل مشويات','Mixed Grills','28','55','110'),
    ('مشكل مشويات دجاج','Mixed Grills Chicken','33','65','130'),
    ('مشكل لحم','Mixed Meat','23','45','90'),
    ('كباب بيتي لحم','Kabab Bayti','35','70','140'),
    ('كباب كرز لحم','Kabab Karaz','45','90','180'),
    ('كباب ميرو','Kabab Miru','35','70','140'),
    ('كباب خشخاش','Kabab Khashkhash','35','70','140'),
    ('اسكندر كباب لحم','Iskandar Lahm','35','70','140'),
    ('اسكندر كباب دجاج','Iskandar Dajaj','25','50','100'),
    ('ريش غنم','Lamb Chops','40','80','160'),
    ('دجاج على الفحم نصف','Grilled Chicken Half','20','-','-'),
    ('دجاج على الفحم حبة','Grilled Chicken Full','40','-','-'),
    ('عرايس','Arayis','20','-','-'),
    ('ماريا بالجبن','Maria bil Jibn','25','-','-'),
    ('تكة البحرين 4 أسياخ','Tikkat Bahrain','30','-','-'),
]

apps = [
    ('حمص','Hummus','7','10'),
    ('متبل','Mutabbal','7','10'),
    ('بابا غنوج','Baba Ghanoush','7','10'),
    ('فتوش','Fattoush','7','10'),
    ('سلطة خضراء','Green Salad','7','10'),
    ('سلطة يوناني','Greek Salad','-','15'),
    ('سلطة سيزر','Caesar Salad','-','15'),
]

shawarma = [
    ('صحن شاورما عربي مقطع','Arabic Sliced','20','25','30','25','38','42'),
    ('صحن شاورما عربي فرط','Arabic Loose','25','30','35','30','45','60'),
    ('وجبة شاورما اسكندر','Iskandar Meal','25','30','35','25','38','42'),
    ('شاورما ياسمين الدمام','Yasmeen Special','25','-','35','30','-','47'),
    ('وجبة كاساديا','Quesadilla Meal','25','-','35','30','-','47'),
    ('وجبة إكسترا','Extra Meal','25','-','35','-','-','-'),
    ('وجبة بانية','Pane Meal','25','-','35','-','-','-'),
    ('وجبة فرايز','Fries Meal','25','-','35','-','-','-'),
    ('وجبة فرايز بالخضار','Fries & Veg','25','-','35','-','-','-'),
    ('وجبة ديتس','Diet Meal','25','-','35','-','-','-'),
    ('وجبة عائلية اقتصادية','Family Economy','-','-','60','-','-','70'),
]

fries = [
    ('صحن بطاطس','Fries Plate','5','10','15'),
    ('صحن بطاطس بالجبن','Cheese Fries','10','15','20'),
    ('بطاطس ويدجز','Wedges','15','-','-'),
    ('بطاطس ديبرز','Dippers','15','-','-'),
]

sand_grill = [
    ('ساندويتش كباب لحم','Kabab Lahm','10'),
    ('ساندويتش كباب دجاج','Kabab Dajaj','8'),
    ('ساندويتش أوصال لحم','Osal Lahm','12'),
    ('ساندويتش شيش طاووق','Shish Tawook','9'),
]

sand_other = [
    ('صاروخ','Sarooh','11','15'),
    ('فطر','Mushroom','9','12'),
    ('شامي','Shami','7','10'),
    ('صامولي','Samooli','7','10'),
    ('إيطالي','Italian','9','14'),
    ('فرنسي','French','11','18'),
    ('مكسيكي','Mexican','15','18'),
    ('صاروخ بانية','Pane Sarooh','15','25'),
    ('بطاطس','Potato','5','7'),
]

pizzas = [
    ('خضار','Veggie','12','18','24'),
    ('مارغريتا','Margherita','12','18','24'),
    ('مكسيكان','Mexican','12','18','24'),
    ('دجاج','Chicken','15','21','27'),
    ('لحم','Meat','17','23','29'),
    ('مشكل','Mixed','16','21','28'),
    ('رنش','Ranch','15','20','27'),
    ('باربيكيو','BBQ','15','20','27'),
    ('بيبيروني','Pepperoni','15','20','27'),
    ('شاورما دجاج','Chicken Shawarma','15','21','27'),
    ('شاورما لحم','Meat Shawarma','17','23','29'),
    ('تونة','Tuna','15','20','25'),
    ('هواي','Hawaiian','15','20','25'),
    ('فود تندر','Chicken Tenders','15','20','25'),
    ('تورتيلا','Tortilla','15','20','25'),
]

pastries = [
    ('نوتيلا','Nutella','10'),
    ('فلافل','Falafel','10'),
    ('بيض بالجبن','Egg & Cheese','12'),
    ('بالبنة والبيض','Labneh & Egg','12'),
    ('سبانخ','Spinach','8'),
    ('محمرة','Mhamra','6'),
    ('محمرة بالجبن','Mhamra & Cheese','7'),
    ('بطاطس','Potato','8'),
    ('بطاطس بالجبن','Potato & Cheese','10'),
    ('جبن سائل','Cream Cheese','7'),
    ('مكس جبن','Mixed Cheese','9'),
    ('لبنة','Labneh','7'),
    ('لبنة بالزعتر','Labneh Zaatar','7'),
    ('لبنة بالعسل','Labneh Honey','8'),
    ('زعتر','Zaatar','6'),
    ('مشكل دجاج','Mixed Chicken','8'),
    ('مشكل لحم','Mixed Meat','10'),
    ('عكاوي','Akkawi','9'),
    ('عش البلبل','Ashp Balbul','9'),
]

juices = [
    ('كوكتيل','Cocktail','15','22','8','6'),
    ('طبقات','Layered','18','24','10','8'),
    ('مانجو','Mango','15','22','8','6'),
    ('فراولة','Strawberry','15','22','8','6'),
    ('جوافة','Guava','15','22','8','6'),
    ('ليمون نعناع','Lemon Mint','15','22','8','6'),
    ('خربز','Melon','15','22','8','6'),
    ('بطيخ','Watermelon','15','22','8','6'),
    ('موز بالحليب','Banana Milk','15','22','8','6'),
    ('موز حليب عسل','Banana Honey','15','22','8','6'),
    ('أناناس','Pineapple','15','22','8','6'),
    ('رمان','Pomegranate','15','22','8','6'),
    ('كيوي','Kiwi','15','22','8','6'),
    ('عوار القلب','Awar al-Qalb','18','24','10','8'),
    ('أصفهاني','Isfahani','18','24','10','8'),
    ('عصير جي','Juice J','18','24','10','8'),
    ('موهيتو','Mojito','-','-','12','10'),
    ('أفوكادو','Avocado','18','24','10','8'),
    ('برتقال','Orange','18','24','10','8'),
    ('سبيشل ياسمين','Yasmeen Special','20','25','12','10'),
    ('فيتامين C','Vitamin C','18','25','10','8'),
    ('عصير روقان','Rawqan','18','25','10','8'),
    ('عرايسي','Arayisi','18','24','10','8'),
    ('عرايسي ملكي','Arayisi King','18','25','15','12'),
    ('سلطة فواكة كاسة','Fruit Salad Cup','-','-','10','8'),
    ('سلطة فواكة صحن','Fruit Salad Plate','-','-','-','10'),
    ('ميلك شيك أوريو لوتس','Oreo Lotus Shake','18','25','10','8'),
]

extras = [
    ('قطعة جبن شيدر','Cheddar Cheese','1'),
    ('جبن موزاريلا','Mozzarella','3'),
    ('أي علبة صوص','Sauce Pack','2'),
]

# ── HELPERS ───────────────────────────────────────────────

def h(s):
    return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def section(id_, title, en_title, banner, headers, rows):
    """Generate section with banner + table. rows = [(ar, en, *prices), ...]"""
    out = '<div class="sec'
    if id_ == 'g':
        out += ' a'
    out += f'" id="{id_}" data-title="{h(en_title)}">\n'
    out += f'<div class="sh"><h2>{h(title)}</h2><div class="she">{h(en_title)}</div></div>\n'
    if banner:
        out += f'<img class="bimg" src="{banner}" alt="{h(title)}" loading="lazy">\n'
    out += '<table class="tbl"><tr>'
    for hh in headers:
        out += f'<th>{h(hh)}</th>'
    out += '</tr>\n'
    for row in rows:
        ar = row[0]
        en = row[1]
        prices = row[2:]
        out += '<tr>'
        out += f'<td>{h(ar)}<span class="es">{h(en)}</span></td>'
        for p in prices:
            out += f'<td>{h(p)}</td>'
        out += '</tr>\n'
    out += '</table>\n</div>\n'
    return out

# ── BUILD HTML ───────────────────────────────────────────

html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>\u0645\u0637\u0639\u0645 \u064a\u0627\u0633\u0645\u064a\u0646 \u0627\u0644\u062f\u0645\u0627\u0645 | Yasmeen Al Dammam</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&family=Playfair+Display:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:60px}
body{font-family:Tajawal,Playfair Display,sans-serif;background:#0a0a0a;color:rgba(255,255,255,.88);min-height:100vh;overflow-x:hidden;direction:rtl}
img{max-width:100%;height:auto;display:block}
.m-wrap{max-width:500px;margin:0 auto;overflow:hidden}
.hdr{background:linear-gradient(135deg,#1a1a1a,#2a2a2a,#1a1a1a);text-align:center;padding:28px 16px 18px;position:relative}
.hdr::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#D4A843,transparent,#D4A843)}
.hdr .l-ar{font-size:34px;font-weight:900;color:#D4A843;text-shadow:0 2px 10px rgba(212,168,67,.3)}
.hdr .l-en{font-family:Playfair Display,serif;font-size:11px;letter-spacing:3px;text-transform:uppercase;color:rgba(255,255,255,.5);margin-top:3px}
.hdr .hdv{width:40px;height:2px;background:linear-gradient(90deg,transparent,#D4A843,transparent);margin:8px auto}
.hdr .hs{font-size:10px;color:rgba(255,255,255,.4);letter-spacing:1px}
.hdr .ha{display:flex;gap:6px;justify-content:center;margin-top:12px;flex-wrap:wrap}
.hdr .ha a{display:flex;align-items:center;gap:5px;padding:7px 14px;border-radius:20px;font-size:11px;font-weight:500;text-decoration:none;transition:.2s}
.bw{background:#25D366;color:#fff}
.bc{background:#D4A843;color:#1a1a1a}
.bm{background:transparent;color:#D4A843;border:1px solid #D4A843}
.cn{display:block;width:100%}
.cn img{width:100%;height:260px;object-fit:cover;display:block}
.cnav{position:sticky;top:0;z-index:100;background:#0a0a0a;padding:6px 4px;overflow-x:auto;display:flex;gap:3px;white-space:nowrap;-webkit-overflow-scrolling:touch;scrollbar-width:none;border-bottom:2px solid #D4A843}
.cnav::-webkit-scrollbar{display:none}
.ctab{flex-shrink:0;padding:6px 10px;border:none;border-radius:20px;font-family:Tajawal,sans-serif;font-size:12px;font-weight:600;background:rgba(212,168,67,.08);color:rgba(255,255,255,.5);cursor:pointer;transition:.25s;border:1px solid transparent;line-height:1.2}
.ctab .te{font-family:Playfair Display,serif;font-size:7px;opacity:.5;display:block}
.ctab.a,.ctab:active{background:rgba(212,168,67,.2);color:#D4A843;border-color:rgba(212,168,67,.3)}
.sec{display:none;margin:8px;background:linear-gradient(135deg,#161616,#1e1e1e);border-radius:14px;overflow:hidden;border:1px solid rgba(212,168,67,.12)}
.sec.a{display:block;animation:fadeIn .3s}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.sh{background:linear-gradient(135deg,#D4A843,#b8922f);padding:14px;text-align:center}
.sh h2{font-size:22px;font-weight:900;color:#1a1a1a;margin:0}
.sh .she{font-family:Playfair Display,serif;font-size:11px;font-weight:600;color:rgba(26,26,26,.7);letter-spacing:2px;text-transform:uppercase}
.bimg{width:100%;height:200px;object-fit:cover;display:block}
.tbl{width:100%;border-collapse:collapse;font-size:12px}
.tbl th{background:rgba(212,168,67,.15);color:#D4A843;font-weight:600;padding:7px 4px;text-align:center;font-size:10px}
.tbl td{padding:6px 4px;text-align:center;border-bottom:1px solid rgba(255,255,255,.04);color:#fff}
.tbl td:first-child{text-align:right;font-weight:600;font-size:13px}
.tbl .es{font-family:Playfair Display,serif;font-size:8px;color:rgba(255,255,255,.35);display:block;font-weight:400}
.sb{padding:7px 14px 3px;font-size:12px;font-weight:700;color:#D4A843;border-bottom:1px solid rgba(212,168,67,.1);background:rgba(212,168,67,.03)}
.sb .sbe{font-family:Playfair Display,serif;font-size:8px;font-weight:400;color:rgba(255,255,255,.35);display:block}
.ft{background:linear-gradient(135deg,#1a1a1a,#0a0a0a);text-align:center;padding:25px 16px;margin-top:10px;border-top:2px solid #D4A843}
.ft .qr{width:110px;height:110px;margin:0 auto 10px;display:block}
.ft .ql{font-size:11px;color:rgba(255,255,255,.4);margin-bottom:6px}
.ft .qs{font-size:9px;color:rgba(255,255,255,.25)}
.ft .fdv{width:30px;height:1px;background:#D4A843;margin:8px auto}
</style>
</head>
<body>
<div class="m-wrap">
<div class="hdr">
<div class="l-ar">\u0645\u0637\u0639\u0645 \u064a\u0627\u0633\u0645\u064a\u0646 \u0627\u0644\u062f\u0645\u0627\u0645</div>
<div class="l-en">Yasmeen Al Dammam</div>
<div class="hdv"></div>
<div class="hs">\u0627\u0644\u062f\u0645\u0627\u0645\u060c \u0627\u0644\u0645\u0645\u0644\u0643\u0629 \u0627\u0644\u0639\u0631\u0628\u064a\u0629 \u0627\u0644\u0633\u0639\u0648\u062f\u064a\u0629</div>
<div class="ha">
<a class="bw" href="https://wa.me/966554159831" target="_blank">\U0001f4ac \u0648\u0627\u062a\u0633\u0627\u0628</a>
<a class="bc" href="tel:+966****9831">\U0001f4de \u0627\u062a\u0635\u0627\u0644</a>
<a class="bm" href="#">\U0001f4cd \u0627\u0644\u0645\u0648\u0642\u0639</a>
</div>
</div>

<div class="cn"><img src="hero_banner.jpg" alt="Yasmeen Al Dammam" loading="lazy"></div>

<nav class="cnav" id="cnav">
<button class="ctab a" data-c="g"><span>\u0645\u0634\u0648\u064a\u0627\u062a</span><span class="te">Grills</span></button>
<button class="ctab" data-c="ap"><span>\u0645\u0642\u0628\u0644\u0627\u062a</span><span class="te">Appetizers</span></button>
<button class="ctab" data-c="sw"><span>\u0634\u0627\u0648\u0631\u0645\u0627</span><span class="te">Shawarma</span></button>
<button class="ctab" data-c="sd"><span>\u0633\u0646\u062f\u0648\u064a\u062a\u0634\u0627\u062a</span><span class="te">Sandwiches</span></button>
<button class="ctab" data-c="pz"><span>\u0628\u064a\u062a\u0632\u0627</span><span class="te">Pizza</span></button>
<button class="ctab" data-c="pt"><span>\u0641\u0637\u0627\u0626\u0631</span><span class="te">Pastries</span></button>
<button class="ctab" data-c="jc"><span>\u0639\u0635\u0627\u0626\u0631</span><span class="te">Juices</span></button>
<button class="ctab" data-c="ex"><span>\u0625\u0636\u0627\u0641\u0627\u062a</span><span class="te">Extras</span></button>
</nav>
'''

# 1. Grills
html += section('g', '\u0627\u0644\u0645\u0634\u0648\u064a\u0627\u062a', 'Grills', 'grills_banner.jpg',
    ['\u0627\u0644\u0635\u0646\u0641', '\u0641\u0631\u062f', '\u0646\u0635\u0641 \u0643\u064a\u0644\u0648', '\u0643\u064a\u0644\u0648'], grills)

# 2. Appetizers
html += section('ap', '\u0645\u0642\u0628\u0644\u0627\u062a \u0648\u0633\u0644\u0637\u0627\u062a', 'Appetizers & Salads', 'appetizers_banner.jpg',
    ['\u0627\u0644\u0635\u0646\u0641', '\u0635\u063a\u064a\u0631', '\u0643\u0628\u064a\u0631'], apps)

# 3. Shawarma
html += '<div class="sec" id="sw">\n'
html += '<div class="sh"><h2>\u0623\u0637\u0628\u0627\u0642 \u0627\u0644\u0634\u0627\u0648\u0631\u0645\u0627</h2><div class="she">Shawarma Platters</div></div>\n'
html += '<img class="bimg" src="shawarma_banner.jpg" alt="Shawarma" loading="lazy">\n'
html += '<table class="tbl"><tr><th>\u0627\u0644\u0635\u0646\u0641</th><th>\u062f S</th><th>\u062f M</th><th>\u062f L</th><th>\u0644 S</th><th>\u0644 M</th><th>\u0644 L</th></tr>\n'
for row in shawarma:
    html += '<tr>'
    html += f'<td>{h(row[0])}<span class="es">{h(row[1])}</span></td>'
    for p in row[2:]:
        html += f'<td>{h(p)}</td>'
    html += '</tr>\n'
html += '</table>\n'
html += '<div class="sb">\U0001f35f \u0627\u0644\u0628\u0637\u0627\u0637\u0633 \u0627\u0644\u0645\u0642\u0644\u064a\u0629 <span class="sbe">Fries &amp; Sides</span></div>\n'
html += '<table class="tbl"><tr><th>\u0627\u0644\u0635\u0646\u0641</th><th>\u0635\u063a\u064a\u0631</th><th>\u0648\u0633\u0637</th><th>\u0643\u0628\u064a\u0631</th></tr>\n'
for row in fries:
    html += '<tr>'
    html += f'<td>{h(row[0])}<span class="es">{h(row[1])}</span></td>'
    for p in row[2:]:
        html += f'<td>{h(p)}</td>'
    html += '</tr>\n'
html += '</table>\n</div>\n'

# 4. Sandwiches
html += '<div class="sec" id="sd">\n'
html += '<div class="sh"><h2>\u0633\u0646\u062f\u0648\u064a\u062a\u0634\u0627\u062a</h2><div class="she">Sandwiches</div></div>\n'
html += '<img class="bimg" src="sandwiches_banner.jpg" alt="Sandwiches" loading="lazy">\n'
html += '<div class="sb">\U0001f969 \u0633\u0646\u062f\u0648\u064a\u062a\u0634\u0627\u062a \u0645\u0634\u0648\u064a\u0627\u062a <span class="sbe">Grilled Sandwiches</span></div>\n'
html += '<table class="tbl"><tr><th>\u0627\u0644\u0635\u0646\u0641</th><th>\u0627\u0644\u0633\u0639\u0631</th></tr>\n'
for row in sand_grill:
    html += '<tr>'
    html += f'<td>{h(row[0])}<span class="es">{h(row[1])}</span></td>'
    html += f'<td>{h(row[2])}</td>'
    html += '</tr>\n'
html += '</table>\n'
html += '<div class="sb">\U0001f32f \u0634\u0627\u0648\u0631\u0645\u0627 \u0648\u0633\u0646\u062f\u0648\u064a\u062a\u0634\u0627\u062a <span class="sbe">Shawarma &amp; Other</span></div>\n'
html += '<table class="tbl"><tr><th>\u0627\u0644\u0635\u0646\u0641</th><th>\u062f\u062c\u0627\u062c</th><th>\u0644\u062d\u0645</th></tr>\n'
for row in sand_other:
    html += '<tr>'
    html += f'<td>{h(row[0])}<span class="es">{h(row[1])}</span></td>'
    html += f'<td>{h(row[2])}</td>'
    html += f'<td>{h(row[3])}</td>'
    html += '</tr>\n'
html += '</table>\n</div>\n'

# 5. Pizza
html += section('pz', '\u0627\u0644\u0628\u064a\u062a\u0632\u0627', 'Pizza', 'pizza_banner.jpg',
    ['\u0627\u0644\u0635\u0646\u0641', '\u0635\u063a\u064a\u0631', '\u0648\u0633\u0637', '\u0643\u0628\u064a\u0631'], pizzas)

# 6. Pastries
html += section('pt', '\u0641\u0637\u0627\u0626\u0631 \u064a\u0627\u0633\u0645\u064a\u0646', 'Yasmeen Pastries', 'pastries_banner.jpg',
    ['\u0627\u0644\u0635\u0646\u0641', '\u0627\u0644\u0633\u0639\u0631'], pastries)

# 7. Juices
html += '<div class="sec" id="jc">\n'
html += '<div class="sh"><h2>\u0639\u0635\u0627\u0626\u0631 \u0648\u0645\u0634\u0631\u0648\u0628\u0627\u062a</h2><div class="she">Fresh Juices &amp; Smoothies</div></div>\n'
html += '<img class="bimg" src="juices_banner.jpg" alt="Juices" loading="lazy">\n'
html += '<table class="tbl"><tr><th>\u0627\u0644\u0635\u0646\u0641</th><th>1 \u0644\u062a\u0631</th><th>1.5 \u0644\u062a\u0631</th><th>\u0643\u0628\u064a\u0631</th><th>\u0648\u0633\u0637</th></tr>\n'
for row in juices:
    html += '<tr>'
    html += f'<td>{h(row[0])}<span class="es">{h(row[1])}</span></td>'
    for p in row[2:]:
        html += f'<td>{h(p)}</td>'
    html += '</tr>\n'
html += '</table>\n</div>\n'

# 8. Extras
html += section('ex', '\u0625\u0636\u0627\u0641\u0627\u062a', 'Extras', '',
    ['\u0627\u0644\u0635\u0646\u0641', '\u0627\u0644\u0633\u0639\u0631'], extras)

# Footer
html += '<div class="ft">\n'
html += '<div class="ql">\U0001f4f1 \u0642\u0645 \u0628\u0645\u0633\u062d \u0627\u0644\u0643\u0648\u062f \u0644\u0639\u0631\u0636 \u0627\u0644\u0642\u0627\u0626\u0645\u0629</div>\n'
html += f'<img class="qr" src="data:image/png;base64,{qr}" alt="QR Code">\n'
html += '<div class="qs">https://rdstudiohub.github.io/Yasmeen-Al-Dammam/</div>\n'
html += '<div class="fdv"></div>\n'
html += '<div class="ql" style="font-size:10px">\u0645\u0637\u0639\u0645 \u064a\u0627\u0633\u0645\u064a\u0646 \u0627\u0644\u062f\u0645\u0627\u0645 \u00a9 2024</div>\n'
html += '</div>\n'

# JavaScript
html += '''<script>
(function(){
  var tabs = document.querySelectorAll('.ctab');
  var secs = document.querySelectorAll('.sec');
  tabs.forEach(function(tab){
    tab.addEventListener('click', function(){
      var id = this.getAttribute('data-c');
      if (!id) return;
      tabs.forEach(function(t){ t.classList.remove('a'); });
      secs.forEach(function(s){ s.classList.remove('a'); });
      this.classList.add('a');
      var target = document.getElementById(id);
      if (target) target.classList.add('a');
    });
  });
})();
</script>
</div>
</body>
</html>'''

path = '/opt/data/yasmeen-menu/index.html'
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

sz = os.path.getsize(path)
print(f'Written: {sz} bytes OK')

# Verify
import re
sections = re.findall(r'class="sec(?: a)?" id="([^"]+)"', html)
tabs = re.findall(r'data-c="([^"]+)"', html)
print(f'Sections: {len(sections)} IDs: {sections}')
print(f'Tabs: {len(tabs)} targets: {tabs}')
print(f'QR embedded: {"data:image/png;base64" in html}')
