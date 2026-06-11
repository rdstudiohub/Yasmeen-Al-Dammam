#!/usr/bin/env python3
"""Yasmeen Al Dammam — Print-Ready A4 PDF Menu (WeasyPrint optimized)"""
import base64

with open('/tmp/qr_b64.txt') as f:
    qr = f.read().strip()

def h(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

# Data
grills = [('كباب لحم','Kabab Lahm','30','60','120'),('كباب دجاج','Kabab Dajaj','20','40','80'),('أوصال لحم','Osal Lahm','35','70','140'),('أوصال دجاج شيش طاووق','Shish Tawook','25','50','100'),('مشكل مشويات','Mixed Grills','28','55','110'),('مشكل مشويات دجاج','Mixed Grills Chicken','33','65','130'),('مشكل لحم','Mixed Meat','23','45','90'),('كباب بيتي لحم','Kabab Bayti','35','70','140'),('كباب كرز لحم','Kabab Karaz','45','90','180'),('كباب ميرو','Kabab Miru','35','70','140'),('كباب خشخاش','Kabab Khashkhash','35','70','140'),('اسكندر كباب لحم','Iskandar Lahm','35','70','140'),('اسكندر كباب دجاج','Iskandar Dajaj','25','50','100'),('ريش غنم','Lamb Chops','40','80','160'),('دجاج على الفحم نصف','Grilled Chicken Half','20','–','–'),('دجاج على الفحم حبة','Grilled Chicken Full','40','–','–'),('عرايس','Arayis','20','–','–'),('ماريا بالجبن','Maria bil Jibn','25','–','–'),('تكة البحرين 4 أسياخ','Tikkat Bahrain','30','–','–')]
apps = [('حمص','Hummus','7','10'),('متبل','Mutabbal','7','10'),('بابا غنوج','Baba Ghanoush','7','10'),('فتوش','Fattoush','7','10'),('سلطة خضراء','Green Salad','7','10'),('سلطة يوناني','Greek Salad','–','15'),('سلطة سيزر','Caesar Salad','–','15')]
sha = [('صحن شاورما عربي مقطع','Arabic Sliced','20','25','30','25','38','42'),('صحن شاورما عربي فرط','Arabic Loose','25','30','35','30','45','60'),('وجبة شاورما اسكندر','Iskandar Meal','25','30','35','25','38','42'),('شاورما ياسمين الدمام','Yasmeen Special','25','–','35','30','–','47'),('وجبة كاساديا','Quesadilla Meal','25','–','35','30','–','47'),('وجبة إكسترا','Extra Meal','25','–','35','–','–','–'),('وجبة بانية','Pane Meal','25','–','35','–','–','–'),('وجبة فرايز','Fries Meal','25','–','35','–','–','–'),('وجبة فرايز بالخضار','Fries & Veg','25','–','35','–','–','–'),('وجبة ديتس','Diet Meal','25','–','35','–','–','–'),('وجبة عائلية اقتصادية','Family Economy','–','–','60','–','–','70')]
frs = [('صحن بطاطس','Fries Plate','5','10','15'),('صحن بطاطس بالجبن','Cheese Fries','10','15','20'),('بطاطس ويدجز','Wedges','15','–','–'),('بطاطس ديبرز','Dippers','15','–','–')]
sg = [('ساندويتش كباب لحم','Kabab Lahm','10'),('ساندويتش كباب دجاج','Kabab Dajaj','8'),('ساندويتش أوصال لحم','Osal Lahm','12'),('ساندويتش شيش طاووق','Shish Tawook','9')]
so = [('صاروخ','Sarooh','11','15'),('فطر','Mushroom','9','12'),('شامي','Shami','7','10'),('صامولي','Samooli','7','10'),('إيطالي','Italian','9','14'),('فرنسي','French','11','18'),('مكسيكي','Mexican','15','18'),('صاروخ بانية','Pane Sarooh','15','25'),('بطاطس','Potato','5','7')]
pz = [('خضار','Veggie','12','18','24'),('مارغريتا','Margherita','12','18','24'),('مكسيكان','Mexican','12','18','24'),('دجاج','Chicken','15','21','27'),('لحم','Meat','17','23','29'),('مشكل','Mixed','16','21','28'),('رنش','Ranch','15','20','27'),('باربيكيو','BBQ','15','20','27'),('بيبيروني','Pepperoni','15','20','27'),('شاورما دجاج','Chicken Shawarma','15','21','27'),('شاورما لحم','Meat Shawarma','17','23','29'),('تونة','Tuna','15','20','25'),('هواي','Hawaiian','15','20','25'),('فود تندر','Chicken Tenders','15','20','25'),('تورتيلا','Tortilla','15','20','25')]
pt = [('نوتيلا','Nutella','10'),('فلافل','Falafel','10'),('بيض بالجبن','Egg & Cheese','12'),('بالبنة والبيض','Labneh & Egg','12'),('سبانخ','Spinach','8'),('محمرة','Mhamra','6'),('محمرة بالجبن','Mhamra & Cheese','7'),('بطاطس','Potato','8'),('بطاطس بالجبن','Potato & Cheese','10'),('جبن سائل','Cream Cheese','7'),('مكس جبن','Mixed Cheese','9'),('لبنة','Labneh','7'),('لبنة بالزعتر','Labneh Zaatar','7'),('لبنة بالعسل','Labneh Honey','8'),('زعتر','Zaatar','6'),('مشكل دجاج','Mixed Chicken','8'),('مشكل لحم','Mixed Meat','10'),('عكاوي','Akkawi','9'),('عش البلبل','Ashp Balbul','9')]
jc = [('كوكتيل','Cocktail','15','22','8','6'),('طبقات','Layered','18','24','10','8'),('مانجو','Mango','15','22','8','6'),('فراولة','Strawberry','15','22','8','6'),('جوافة','Guava','15','22','8','6'),('ليمون نعناع','Lemon Mint','15','22','8','6'),('خربز','Melon','15','22','8','6'),('بطيخ','Watermelon','15','22','8','6'),('موز بالحليب','Banana Milk','15','22','8','6'),('موز حليب عسل','Banana Honey','15','22','8','6'),('أناناس','Pineapple','15','22','8','6'),('رمان','Pomegranate','15','22','8','6'),('كيوي','Kiwi','15','22','8','6'),('عوار القلب','Awar al-Qalb','18','24','10','8'),('أصفهاني','Isfahani','18','24','10','8'),('عصير جي','Juice J','18','24','10','8'),('موهيتو','Mojito','–','–','12','10'),('أفوكادو','Avocado','18','24','10','8'),('برتقال','Orange','18','24','10','8'),('سبيشل ياسمين','Yasmeen Special','20','25','12','10'),('فيتامين C','Vitamin C','18','25','10','8'),('عصير روقان','Rawqan','18','25','10','8'),('عرايسي','Arayisi','18','24','10','8'),('عرايسي ملكي','Arayisi King','18','25','15','12'),('سلطة فواكة كاسة','Fruit Salad Cup','–','–','10','8'),('سلطة فواكة صحن','Fruit Salad Plate','–','–','–','10'),('ميلك شيك أوريو لوتس','Oreo Lotus Shake','18','25','10','8')]
ex = [('قطعة جبن شيدر','Cheddar Cheese','1'),('جبن موزاريلا','Mozzarella','3'),('أي علبة صوص','Sauce Pack','2')]

def tbl_cat(title, en_title, headers, rows):
    out = f'<div class="cat"><div class="chd"><span class="ca">{h(title)}</span><span class="ce">{h(en_title)}</span></div>\n'
    out += '<table><tr>'
    for hh in headers:
        out += f'<th>{h(hh)}</th>'
    out += '</tr>\n'
    for row in rows:
        ar, en = row[0], row[1]
        prices = row[2:]
        out += '<tr>'
        out += f'<td class="nm"><span class="nar">{h(ar)}</span><span class="nen">{h(en)}</span></td>'
        for p in prices:
            cls = ' na' if p == '–' else ''
            out += f'<td class="pr{cls}">{h(p)}</td>'
        out += '</tr>\n'
    out += '</table></div>\n'
    return out

# Build
html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8">
<title>Yasmeen Al Dammam Menu</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;800;900&family=Playfair+Display:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
@page {{ size: A4; margin: 12mm 14mm; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:Tajawal,Playfair Display,sans-serif; direction:rtl; color:#1a1a1a; background:#fff; }}
.page {{ page-break-after:always; }}

/* Cover */
.cvr {{ text-align:center; padding-top:80mm; }}
.cvr-ln {{ width:60mm; height:0.5mm; background:#D4A843; margin:0 auto; }}
.cvr-ar {{ font-size:36pt; font-weight:900; color:#D4A843; margin:10mm 0 3mm; }}
.cvr-en {{ font-family:Playfair Display,serif; font-size:16pt; font-weight:700; color:#999; letter-spacing:5px; text-transform:uppercase; margin-bottom:6mm; }}
.cvr-tg {{ font-size:22pt; font-weight:700; color:#333; margin-top:5mm; }}
.cvr-tge {{ font-family:Playfair Display,serif; font-size:11pt; font-weight:400; color:#D4A843; letter-spacing:3px; text-transform:uppercase; margin-top:2mm; }}
.cvr-dv {{ width:30mm; height:0.3mm; background:#D4A843; margin:6mm auto; }}
.cvr-lc {{ font-size:10pt; color:#999; margin-top:8mm; }}
.cvr-ct {{ font-size:9pt; color:#aaa; margin-top:3mm; }}

/* Header */
.phd {{ background:#D4A843; padding:6px 0; text-align:center; margin-bottom:4mm; }}
.pha {{ font-size:14pt; font-weight:800; color:#1a1a1a; }}
.phe {{ font-family:Playfair Display,serif; font-size:8pt; font-weight:600; color:rgba(26,26,26,.6); letter-spacing:2px; }}

/* Content */
.cat {{ border:1px solid #e0d5c0; border-radius:2mm; margin-bottom:3mm; overflow:hidden; }}
.chd {{ background:#D4A843; padding:2mm 3mm; text-align:center; }}
.ca {{ font-size:11pt; font-weight:800; color:#1a1a1a; display:block; }}
.ce {{ font-family:Playfair Display,serif; font-size:7pt; font-weight:600; color:rgba(26,26,26,.6); letter-spacing:1.5px; display:block; text-transform:uppercase; }}
table {{ width:100%; border-collapse:collapse; font-size:7.5pt; }}
th {{ background:#f5f0e8; color:#333; font-weight:700; padding:1.5mm 1mm; text-align:center; font-size:7pt; }}
td {{ padding:1.2mm 1mm; text-align:center; border-bottom:1px solid #eee; }}
tr:last-child td {{ border-bottom:none; }}
.nm {{ text-align:right; }}
.nar {{ font-size:8.5pt; font-weight:700; color:#1a1a1a; display:block; line-height:1.3; }}
.nen {{ font-family:Playfair Display,serif; font-size:6.5pt; color:#999; display:block; }}
.pr {{ font-size:8pt; font-weight:700; color:#D4A843; }}
.na {{ color:#ddd; }}
.juice-cat table {{ font-size:6.5pt; }}
.juice-cat td {{ padding:1mm 0.7mm; }}
.juice-cat .nar {{ font-size:7pt; }}
.juice-cat .nen {{ font-size:5.5pt; }}
.juice-cat .pr {{ font-size:7pt; }}

/* Flex layout for two cats per page */
.flex {{ display:flex; gap:3mm; }}
.flex .col {{ flex:1; min-width:0; }}
.flex .cat {{ margin-bottom:2mm; }}

/* Back cover */
.bcvr {{ text-align:center; padding-top:50mm; }}
.bcvr-ln {{ width:50mm; height:0.5mm; background:#D4A843; margin:0 auto; }}
.bcvr-ar {{ font-size:24pt; font-weight:900; color:#D4A843; margin:6mm 0 2mm; }}
.bcvr-en {{ font-family:Playfair Display,serif; font-size:12pt; font-weight:700; color:#999; letter-spacing:4px; margin-bottom:5mm; }}
.bcvr-qr {{ width:90px; height:90px; margin:5mm auto; display:block; }}
.bcvr-sc {{ font-size:8pt; color:#aaa; letter-spacing:1px; }}
.bcvr-dv {{ width:25mm; height:0.3mm; background:#ddd; margin:5mm auto; }}
.bcvr-lc {{ font-size:9pt; color:#666; margin-top:3mm; }}
.bcvr-tl {{ font-size:9pt; color:#888; margin-top:1.5mm; }}
.bcvr-ft {{ font-size:7pt; color:#bbb; margin-top:6mm; }}

@media print {{ body {{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }} }}
</style>
</head>
<body>

<!-- ═══ PAGE 1: COVER ═══ -->
<div class="page">
<div class="cvr">
<div class="cvr-ln"></div>
<div class="cvr-ar">مطعم ياسمين الدمام</div>
<div class="cvr-en">YASMEEN AL DAMMAM</div>
<div class="cvr-ln"></div>
<div class="cvr-tg">قائمة الطعام</div>
<div class="cvr-tge">MENU</div>
<div class="cvr-dv"></div>
<div class="cvr-lc">الدمام، المملكة العربية السعودية</div>
<div class="cvr-ct">📞 0535604862 &nbsp;|&nbsp; 💬 واتساب</div>
</div>
</div>

<!-- ═══ PAGE 2: GRILLS + APPETIZERS ═══ -->
<div class="page">
<div class="phd"><span class="pha">قائمة الطعام</span><span class="phe">MENU</span></div>
<div class="flex">
<div class="col">
{tbl_cat('المشويات','GRILLS',['فرد','½ ك','كيلو'],grills)}
</div>
<div class="col">
{tbl_cat('مقبلات وسلطات','APPETIZERS & SALADS',['صغير','كبير'],apps)}
</div>
</div>
</div>

<!-- ═══ PAGE 3: SHAWARMA + SANDWICHES ═══ -->
<div class="page">
<div class="phd"><span class="pha">قائمة الطعام</span><span class="phe">MENU</span></div>
<div class="flex">
<div class="col">
{tbl_cat('أطباق الشاورما','SHAWARMA PLATTERS',['د S','د M','د L','ل S','ل M','ل L'],sha)}
{tbl_cat('🍟 البطاطس المقلية','FRIES & SIDES',['صغير','وسط','كبير'],frs)}
</div>
<div class="col">
{tbl_cat('🥩 سندويتشات مشويات','GRILLED SANDWICHES',['SR'],sg)}
{tbl_cat('🌯 شاورما وسندويتشات','SHAWARMA & OTHER',['دجاج','لحم'],so)}
</div>
</div>
</div>

<!-- ═══ PAGE 4: PIZZA + PASTRIES ═══ -->
<div class="page">
<div class="phd"><span class="pha">قائمة الطعام</span><span class="phe">MENU</span></div>
<div class="flex">
<div class="col">
{tbl_cat('البيتزا','PIZZA',['صغير','وسط','كبير'],pz)}
</div>
<div class="col">
{tbl_cat('فطائر ياسمين','YASMEEN PASTRIES',['SR'],pt)}
{tbl_cat('إضافات','EXTRAS',['SR'],ex)}
</div>
</div>
</div>

<!-- ═══ PAGE 5: JUICES ═══ -->
<div class="page">
<div class="phd"><span class="pha">عصائر ومشروبات</span><span class="phe">FRESH JUICES &amp; SMOOTHIES</span></div>
{tbl_cat('قائمة المشروبات','BEVERAGES',['1 لتر','1.5 لتر','كبير','وسط'],jc).replace('<div class="cat">','<div class="cat juice-cat">')}
</div>

<!-- ═══ PAGE 6: BACK COVER ═══ -->
<div class="page">
<div class="bcvr">
<div class="bcvr-ln"></div>
<div class="bcvr-ar">مطعم ياسمين الدمام</div>
<div class="bcvr-en">YASMEEN AL DAMMAM</div>
<div class="bcvr-ln"></div>
<img class="bcvr-qr" src="data:image/png;base64,{qr}" alt="QR">
<div class="bcvr-sc">امسح الكود لعرض القائمة الرقمية</div>
<div class="bcvr-dv"></div>
<div class="bcvr-lc">📍 الدمام، المملكة العربية السعودية</div>
<div class="bcvr-tl">📞 0535604862</div>
<div class="bcvr-tl">💬 واتساب: 0535604862</div>
<div class="bcvr-dv"></div>
<div class="bcvr-ft">تم التصميم بواسطة: مالك رضوان</div>
</div>
</div>

</body></html>'''

path = '/opt/data/yasmeen-menu/print-menu.html'
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Written: {len(html)} bytes')
