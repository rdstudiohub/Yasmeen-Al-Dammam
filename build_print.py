#!/usr/bin/env python3
"""Yasmeen Al Dammam — Print-Ready A4 Physical Menu Design"""
import os, base64

with open('/tmp/qr_b64.txt') as f:
    qr = f.read().strip()

# ── DATA ──
grills = [('كباب لحم','Kabab Lahm','30','60','120'),('كباب دجاج','Kabab Dajaj','20','40','80'),('أوصال لحم','Osal Lahm','35','70','140'),('أوصال دجاج شيش طاووق','Shish Tawook','25','50','100'),('مشكل مشويات','Mixed Grills','28','55','110'),('مشكل مشويات دجاج','Mixed Grills Chicken','33','65','130'),('مشكل لحم','Mixed Meat','23','45','90'),('كباب بيتي لحم','Kabab Bayti','35','70','140'),('كباب كرز لحم','Kabab Karaz','45','90','180'),('كباب ميرو','Kabab Miru','35','70','140'),('كباب خشخاش','Kabab Khashkhash','35','70','140'),('اسكندر كباب لحم','Iskandar Lahm','35','70','140'),('اسكندر كباب دجاج','Iskandar Dajaj','25','50','100'),('ريش غنم','Lamb Chops','40','80','160'),('دجاج على الفحم نصف','Grilled Chicken Half','20','-','-'),('دجاج على الفحم حبة','Grilled Chicken Full','40','-','-'),('عرايس','Arayis','20','-','-'),('ماريا بالجبن','Maria bil Jibn','25','-','-'),('تكة البحرين 4 أسياخ','Tikkat Bahrain','30','-','-')]
apps = [('حمص','Hummus','7','10'),('متبل','Mutabbal','7','10'),('بابا غنوج','Baba Ghanoush','7','10'),('فتوش','Fattoush','7','10'),('سلطة خضراء','Green Salad','7','10'),('سلطة يوناني','Greek Salad','-','15'),('سلطة سيزر','Caesar Salad','-','15')]
shawarma = [('صحن شاورما عربي مقطع','Arabic Sliced','20','25','30','25','38','42'),('صحن شاورما عربي فرط','Arabic Loose','25','30','35','30','45','60'),('وجبة شاورما اسكندر','Iskandar Meal','25','30','35','25','38','42'),('شاورما ياسمين الدمام','Yasmeen Special','25','-','35','30','-','47'),('وجبة كاساديا','Quesadilla Meal','25','-','35','30','-','47'),('وجبة إكسترا','Extra Meal','25','-','35','-','-','-'),('وجبة بانية','Pane Meal','25','-','35','-','-','-'),('وجبة فرايز','Fries Meal','25','-','35','-','-','-'),('وجبة فرايز بالخضار','Fries & Veg','25','-','35','-','-','-'),('وجبة ديتس','Diet Meal','25','-','35','-','-','-'),('وجبة عائلية اقتصادية','Family Economy','-','-','60','-','-','70')]
fries = [('صحن بطاطس','Fries Plate','5','10','15'),('صحن بطاطس بالجبن','Cheese Fries','10','15','20'),('بطاطس ويدجز','Wedges','15','-','-'),('بطاطس ديبرز','Dippers','15','-','-')]
sand_g = [('ساندويتش كباب لحم','Kabab Lahm','10'),('ساندويتش كباب دجاج','Kabab Dajaj','8'),('ساندويتش أوصال لحم','Osal Lahm','12'),('ساندويتش شيش طاووق','Shish Tawook','9')]
sand_o = [('صاروخ','Sarooh','11','15'),('فطر','Mushroom','9','12'),('شامي','Shami','7','10'),('صامولي','Samooli','7','10'),('إيطالي','Italian','9','14'),('فرنسي','French','11','18'),('مكسيكي','Mexican','15','18'),('صاروخ بانية','Pane Sarooh','15','25'),('بطاطس','Potato','5','7')]
pizzas = [('خضار','Veggie','12','18','24'),('مارغريتا','Margherita','12','18','24'),('مكسيكان','Mexican','12','18','24'),('دجاج','Chicken','15','21','27'),('لحم','Meat','17','23','29'),('مشكل','Mixed','16','21','28'),('رنش','Ranch','15','20','27'),('باربيكيو','BBQ','15','20','27'),('بيبيروني','Pepperoni','15','20','27'),('شاورما دجاج','Chicken Shawarma','15','21','27'),('شاورما لحم','Meat Shawarma','17','23','29'),('تونة','Tuna','15','20','25'),('هواي','Hawaiian','15','20','25'),('فود تندر','Chicken Tenders','15','20','25'),('تورتيلا','Tortilla','15','20','25')]
pstrs = [('نوتيلا','Nutella','10'),('فلافل','Falafel','10'),('بيض بالجبن','Egg & Cheese','12'),('بالبنة والبيض','Labneh & Egg','12'),('سبانخ','Spinach','8'),('محمرة','Mhamra','6'),('محمرة بالجبن','Mhamra & Cheese','7'),('بطاطس','Potato','8'),('بطاطس بالجبن','Potato & Cheese','10'),('جبن سائل','Cream Cheese','7'),('مكس جبن','Mixed Cheese','9'),('لبنة','Labneh','7'),('لبنة بالزعتر','Labneh Zaatar','7'),('لبنة بالعسل','Labneh Honey','8'),('زعتر','Zaatar','6'),('مشكل دجاج','Mixed Chicken','8'),('مشكل لحم','Mixed Meat','10'),('عكاوي','Akkawi','9'),('عش البلبل','Ashp Balbul','9')]
juices = [('كوكتيل','Cocktail','15','22','8','6'),('طبقات','Layered','18','24','10','8'),('مانجو','Mango','15','22','8','6'),('فراولة','Strawberry','15','22','8','6'),('جوافة','Guava','15','22','8','6'),('ليمون نعناع','Lemon Mint','15','22','8','6'),('خربز','Melon','15','22','8','6'),('بطيخ','Watermelon','15','22','8','6'),('موز بالحليب','Banana Milk','15','22','8','6'),('موز حليب عسل','Banana Honey','15','22','8','6'),('أناناس','Pineapple','15','22','8','6'),('رمان','Pomegranate','15','22','8','6'),('كيوي','Kiwi','15','22','8','6'),('عوار القلب','Awar al-Qalb','18','24','10','8'),('أصفهاني','Isfahani','18','24','10','8'),('عصير جي','Juice J','18','24','10','8'),('موهيتو','Mojito','-','-','12','10'),('أفوكادو','Avocado','18','24','10','8'),('برتقال','Orange','18','24','10','8'),('سبيشل ياسمين','Yasmeen Special','20','25','12','10'),('فيتامين C','Vitamin C','18','25','10','8'),('عصير روقان','Rawqan','18','25','10','8'),('عرايسي','Arayisi','18','24','10','8'),('عرايسي ملكي','Arayisi King','18','25','15','12'),('سلطة فواكة كاسة','Fruit Salad Cup','-','-','10','8'),('سلطة فواكة صحن','Fruit Salad Plate','-','-','-','10'),('ميلك شيك أوريو لوتس','Oreo Lotus Shake','18','25','10','8')]
extras = [('قطعة جبن شيدر','Cheddar Cheese','1'),('جبن موزاريلا','Mozzarella','3'),('أي علبة صوص','Sauce Pack','2')]

def h(s):
    return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def print_cat(title, en_title, headers, rows, cols):
    """Print category section HTML."""
    out = f'<div class="cat-section"><div class="cat-head"><span class="ch-ar">{h(title)}</span><span class="ch-en">{h(en_title)}</span></div>\n'
    out += f'<table class="p-table"><tr>'
    for hh in headers:
        out += f'<th>{h(hh)}</th>'
    out += '</tr>\n'
    for row in rows:
        ar, en = row[0], row[1]
        prices = row[2:]
        out += '<tr>'
        out += f'<td class="td-name"><span class="tn-ar">{h(ar)}</span><span class="tn-en">{h(en)}</span></td>'
        for p in prices:
            out += f'<td class="td-price">{h(p) if p!="-" else "<span class=\"na\">–</span>"}</td>'
        out += '</tr>\n'
    out += '</table></div>\n'
    return out

# ── COVER PAGE ──
cover = '''
<div class="page cover">
  <div class="cover-bg"></div>
  <div class="cover-content">
    <div class="cover-line"></div>
    <div class="cover-ar">مطعم ياسمين الدمام</div>
    <div class="cover-en">YASMEEN AL DAMMAM</div>
    <div class="cover-line"></div>
    <div class="cover-tagline">قائمة الطعام</div>
    <div class="cover-tagline-en">MENU</div>
    <div class="cover-div"></div>
    <div class="cover-loc">الدمام، المملكة العربية السعودية</div>
    <div class="cover-contact">📞 0554159831 &nbsp;|&nbsp; 💬 واتساب</div>
  </div>
</div>
'''

# ── INNER PAGES ──
inner = ''
inner += '<div class="page">\n'
inner += '<div class="p-header"><span class="ph-ar">قائمة الطعام</span><span class="ph-en">MENU</span></div>\n'

# Page 1: Grills + Appetizers (2 columns)
inner += '<div class="p-col">\n'
inner += print_cat('المشويات','GRILLS',['الفرد','½ ك','كيلو'],grills,4)
inner += '</div>\n'
inner += '<div class="p-col">\n'
inner += print_cat('مقبلات وسلطات','APPETIZERS & SALADS',['صغير','كبير'],apps,3)
inner += '</div>\n'
inner += '</div>\n'  # close page

# Page 2: Shawarma + Sandwiches
inner += '<div class="page">\n'
inner += '<div class="p-header"><span class="ph-ar">قائمة الطعام</span><span class="ph-en">MENU</span></div>\n'
inner += '<div class="p-col">\n'
inner += '<div class="cat-section"><div class="cat-head"><span class="ch-ar">أطباق الشاورما</span><span class="ch-en">SHAWARMA PLATTERS</span></div>\n'
inner += '<table class="p-table"><tr><th>الصنف</th><th>د S</th><th>د M</th><th>د L</th><th>ل S</th><th>ل M</th><th>ل L</th></tr>\n'
for row in shawarma:
    ar, en = row[0], row[1]
    prices = row[2:]
    inner += '<tr>'
    inner += f'<td class="td-name"><span class="tn-ar">{h(ar)}</span><span class="tn-en">{h(en)}</span></td>'
    for p in prices:
        inner += f'<td class="td-price">{h(p) if p!="-" else "<span class=\"na\">–</span>"}</td>'
    inner += '</tr>\n'
inner += '</table></div>\n'
inner += '<div class="cat-section sub-section"><div class="cat-head" style="background:#b8922f"><span class="ch-ar">🍟 البطاطس المقلية</span><span class="ch-en">FRIES &amp; SIDES</span></div>\n'
inner += '<table class="p-table"><tr><th>الصنف</th><th>صغير</th><th>وسط</th><th>كبير</th></tr>\n'
for row in fries:
    ar, en = row[0], row[1]
    prices = row[2:]
    inner += '<tr>'
    inner += f'<td class="td-name"><span class="tn-ar">{h(ar)}</span><span class="tn-en">{h(en)}</span></td>'
    for p in prices:
        inner += f'<td class="td-price">{h(p) if p!="-" else "<span class=\"na\">–</span>"}</td>'
    inner += '</tr>\n'
inner += '</table></div>\n'
inner += '</div>\n' # close col

inner += '<div class="p-col">\n'
# Sandwiches
inner += '<div class="cat-section"><div class="cat-head"><span class="ch-ar">سندويتشات مشويات</span><span class="ch-en">GRILLED SANDWICHES</span></div>\n'
inner += '<table class="p-table"><tr><th>الصنف</th><th>SR</th></tr>\n'
for row in sand_g:
    ar, en, p = row
    inner += '<tr>'
    inner += f'<td class="td-name"><span class="tn-ar">{h(ar)}</span><span class="tn-en">{h(en)}</span></td>'
    inner += f'<td class="td-price">{p}</td>'
    inner += '</tr>\n'
inner += '</table></div>\n'

inner += '<div class="cat-section"><div class="cat-head" style="background:#b8922f"><span class="ch-ar">🌯 شاورما وسندويتشات</span><span class="ch-en">SHAWARMA &amp; OTHER</span></div>\n'
inner += '<table class="p-table"><tr><th>الصنف</th><th>دجاج</th><th>لحم</th></tr>\n'
for row in sand_o:
    ar, en, c, m = row
    inner += '<tr>'
    inner += f'<td class="td-name"><span class="tn-ar">{h(ar)}</span><span class="tn-en">{h(en)}</span></td>'
    inner += f'<td class="td-price">{c}</td><td class="td-price">{m}</td>'
    inner += '</tr>\n'
inner += '</table></div>\n'
inner += '</div>\n' # close col
inner += '</div>\n' # close page

# Page 3: Pizza + Pastries + Extras
inner += '<div class="page">\n'
inner += '<div class="p-header"><span class="ph-ar">قائمة الطعام</span><span class="ph-en">MENU</span></div>\n'
inner += '<div class="p-col">\n'
inner += print_cat('البيتزا','PIZZA',['صغير','وسط','كبير'],pizzas,4)
inner += '</div>\n'
inner += '<div class="p-col">\n'
inner += print_cat('فطائر ياسمين','YASMEEN PASTRIES',['SR'],pstrs,2)
inner += print_cat('إضافات','EXTRAS',['SR'],extras,2)
inner += '</div>\n'
inner += '</div>\n'

# Page 4: Juices
inner += '<div class="page">\n'
inner += '<div class="p-header"><span class="ph-ar">عصائر ومشروبات</span><span class="ph-en">FRESH JUICES &amp; SMOOTHIES</span></div>\n'
inner += '<div class="p-col" style="width:100%">\n'
inner += '<div class="cat-section"><div class="cat-head"><span class="ch-ar">قائمة العصائر</span><span class="ch-en">BEVERAGES</span></div>\n'
inner += '<table class="p-table"><tr><th>الصنف</th><th>1 لتر</th><th>1.5 لتر</th><th>كبير</th><th>وسط</th></tr>\n'
for row in juices:
    ar, en = row[0], row[1]
    prices = row[2:]
    inner += '<tr>'
    inner += f'<td class="td-name"><span class="tn-ar">{h(ar)}</span><span class="tn-en">{h(en)}</span></td>'
    for p in prices:
        inner += f'<td class="td-price">{h(p) if p!="-" else "<span class=\"na\">–</span>"}</td>'
    inner += '</tr>\n'
inner += '</table></div>\n'
inner += '</div>\n'
inner += '</div>\n'

# ── BACK COVER ──
back = f'''
<div class="page back-cover">
  <div class="back-bg"></div>
  <div class="back-content">
    <div class="back-line"></div>
    <div class="back-ar">مطعم ياسمين الدمام</div>
    <div class="back-en">YASMEEN AL DAMMAM</div>
    <div class="back-line"></div>
    <img class="back-qr" src="data:image/png;base64,{qr}" alt="QR">
    <div class="back-scan">امسح الكود لعرض القائمة الرقمية</div>
    <div class="back-div"></div>
    <div class="back-loc">📍 الدمام، المملكة العربية السعودية</div>
    <div class="back-tel">📞 0554159831</div>
    <div class="back-wa">💬 واتساب: 0554159831</div>
    <div class="back-div"></div>
    <div class="back-foot">تم التصميم بواسطة: مالك رضوان</div>
  </div>
</div>
'''

# ── FULL HTML ──
html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>مطعم ياسمين الدمام | Yasmeen Al Dammam — طباعة</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&family=Playfair+Display:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
@page {{ size: A4 portrait; margin: 0; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'Tajawal', 'Playfair Display', sans-serif; background: #1a1a1a; direction: rtl; color: rgba(255,255,255,.9); }}
.page {{ width: 210mm; min-height: 297mm; background: #0d0d0d; position: relative; overflow: hidden; page-break-after: always; padding: 0; }}
/* ── COVER ── */
.cover {{ display: flex; align-items: center; justify-content: center; }}
.cover-bg {{ position: absolute; inset: 0; background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 40%, #0d0a05 100%); }}
.cover-bg::before {{ content: ''; position: absolute; inset: 20mm; border: 2px solid rgba(212,168,67,.15); border-radius: 8mm; }}
.cover-content {{ position: relative; z-index: 1; text-align: center; padding: 40mm 20mm; }}
.cover-line {{ width: 60mm; height: 0.5mm; background: linear-gradient(90deg, transparent, #D4A843, transparent); margin: 0 auto; }}
.cover-ar {{ font-size: 42pt; font-weight: 900; color: #D4A843; margin: 12mm 0 3mm; letter-spacing: 1px; }}
.cover-en {{ font-family: 'Playfair Display', serif; font-size: 18pt; font-weight: 700; color: rgba(255,255,255,.5); letter-spacing: 6px; text-transform: uppercase; margin-bottom: 8mm; }}
.cover-tagline {{ font-size: 24pt; font-weight: 700; color: rgba(255,255,255,.7); margin-top: 6mm; }}
.cover-tagline-en {{ font-family: 'Playfair Display', serif; font-size: 12pt; font-weight: 400; color: rgba(212,168,67,.6); letter-spacing: 3px; text-transform: uppercase; margin-top: 2mm; }}
.cover-div {{ width: 30mm; height: 0.3mm; background: #D4A843; margin: 8mm auto; }}
.cover-loc {{ font-size: 11pt; color: rgba(255,255,255,.35); letter-spacing: 1px; margin-top: 10mm; }}
.cover-contact {{ font-size: 10pt; color: rgba(255,255,255,.4); margin-top: 3mm; }}

/* ── INNER PAGES ── */
.p-header {{ background: linear-gradient(135deg, #D4A843, #b8922f); text-align: center; padding: 8px 0; }}
.ph-ar {{ font-size: 14pt; font-weight: 800; color: #1a1a1a; display: block; }}
.ph-en {{ font-family: 'Playfair Display', serif; font-size: 8pt; font-weight: 600; color: rgba(26,26,26,.6); letter-spacing: 2px; }}
.p-col {{ width: 50%; display: inline-block; vertical-align: top; padding: 4mm 3mm; }}
.cat-section {{ margin-bottom: 4mm; border: 1px solid rgba(212,168,67,.12); border-radius: 3mm; overflow: hidden; background: linear-gradient(135deg, #161616, #1e1e1e); }}
.cat-head {{ background: linear-gradient(135deg, #D4A843, #c49a35); padding: 3mm 4mm; text-align: center; }}
.ch-ar {{ font-size: 12pt; font-weight: 800; color: #1a1a1a; display: block; }}
.ch-en {{ font-family: 'Playfair Display', serif; font-size: 7pt; font-weight: 600; color: rgba(26,26,26,.65); letter-spacing: 1.5px; display: block; text-transform: uppercase; }}
.sub-section {{ margin-top: -1mm; }}
.p-table {{ width: 100%; border-collapse: collapse; font-size: 8pt; }}
.p-table th {{ background: rgba(212,168,67,.12); color: #D4A843; font-weight: 700; padding: 2mm 1mm; text-align: center; font-size: 7pt; }}
.p-table td {{ padding: 1.5mm 1mm; text-align: center; border-bottom: 1px solid rgba(255,255,255,.03); color: rgba(255,255,255,.85); }}
.p-table tr:last-child td {{ border-bottom: none; }}
.td-name {{ text-align: right !important; }}
.tn-ar {{ font-size: 9pt; font-weight: 700; color: #fff; display: block; line-height: 1.3; }}
.tn-en {{ font-family: 'Playfair Display', serif; font-size: 6.5pt; color: rgba(255,255,255,.35); display: block; }}
.td-price {{ font-size: 8.5pt; font-weight: 700; color: #D4A843; }}
.na {{ color: rgba(255,255,255,.15); }}

/* ── BACK COVER ── */
.back-cover {{ display: flex; align-items: center; justify-content: center; }}
.back-bg {{ position: absolute; inset: 0; background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 40%, #0d0a05 100%); }}
.back-bg::before {{ content: ''; position: absolute; inset: 20mm; border: 2px solid rgba(212,168,67,.15); border-radius: 8mm; }}
.back-content {{ position: relative; z-index: 1; text-align: center; padding: 30mm 20mm; }}
.back-line {{ width: 50mm; height: 0.5mm; background: linear-gradient(90deg, transparent, #D4A843, transparent); margin: 0 auto; }}
.back-ar {{ font-size: 28pt; font-weight: 900; color: #D4A843; margin: 8mm 0 2mm; }}
.back-en {{ font-family: 'Playfair Display', serif; font-size: 14pt; font-weight: 700; color: rgba(255,255,255,.4); letter-spacing: 4px; margin-bottom: 6mm; }}
.back-qr {{ width: 80px; height: 80px; margin: 6mm auto; display: block; }}
.back-scan {{ font-size: 9pt; color: rgba(255,255,255,.35); letter-spacing: 1px; }}
.back-div {{ width: 25mm; height: 0.3mm; background: rgba(212,168,67,.3); margin: 6mm auto; }}
.back-loc {{ font-size: 10pt; color: rgba(255,255,255,.5); margin-top: 4mm; }}
.back-tel, .back-wa {{ font-size: 10pt; color: rgba(255,255,255,.4); margin-top: 2mm; }}
.back-foot {{ font-size: 8pt; color: rgba(255,255,255,.2); margin-top: 8mm; }}

/* ── PRINT ── */
@media print {{
  body {{ background: #0d0d0d; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
}}
</style>
</head>
<body>
{cover}
{inner}
{back}
</body>
</html>'''

path = '/opt/data/yasmeen-menu/print-menu.html'
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

sz = os.path.getsize(path)
print(f'✅ Print menu written: {sz} bytes')
print(f'📄 File: {path}')
