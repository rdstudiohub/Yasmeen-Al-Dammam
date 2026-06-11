#!/usr/bin/env python3
"""Rebuild all menu sections with new items, preserving structure."""
import os

path = '/opt/data/yasmeen-menu/index.html'
with open(path, 'r') as f:
    html = f.read()

# ============ 1. GRILLS ============
grills_new = '''<div class="sec a reveal" id="g"><div class="sh"><h2>مشويات ياسمين الدمام</h2><div class="she">Yasmeen Grills</div></div>
<img class="bimg tilt" src="grills_banner.jpg" alt="مشويات ياسمين الدمام" loading="lazy">
<table class="tbl"><tr><th>الصنف</th><th>فرد</th><th>نصف كيلو</th><th>كيلو</th></tr>
<tr><td>كباب لحم<span class="es">Kabab Lahm</span></td><td>30</td><td>60</td><td>120</td></tr>
<tr><td>كباب دجاج<span class="es">Kabab Dajaj</span></td><td>20</td><td>40</td><td>80</td></tr>
<tr><td>أوصال لحم<span class="es">Osal Lahm</span></td><td>35</td><td>70</td><td>140</td></tr>
<tr><td>أوصال دجاج (شيش طاووق)<span class="es">Shish Tawook</span></td><td>25</td><td>50</td><td>100</td></tr>
<tr><td>مشكل مشويات<span class="es">Mixed Grills</span></td><td>28</td><td>55</td><td>110</td></tr>
<tr><td>مشكل مشويات دجاج<span class="es">Mixed Grills Chicken</span></td><td>33</td><td>65</td><td>130</td></tr>
<tr><td>مشكل لحم<span class="es">Mixed Meat</span></td><td>23</td><td>45</td><td>90</td></tr>
<tr><td>كباب كرز لحم<span class="es">Kabab Karaz</span></td><td>45</td><td>90</td><td>180</td></tr>
<tr><td>كباب ميرو<span class="es">Kabab Miru</span></td><td>35</td><td>70</td><td>140</td></tr>
<tr><td>كباب خشخاش<span class="es">Kabab Khashkhash</span></td><td>35</td><td>70</td><td>140</td></tr>
<tr><td>ريش غنم<span class="es">Lamb Chops</span></td><td>40</td><td>80</td><td>160</td></tr>
<tr><td>دجاج على الفحم (نصف)<span class="es">Grilled Chicken Half</span></td><td>20</td><td>-</td><td>-</td></tr>
<tr><td>دجاج على الفحم (حبة)<span class="es">Grilled Chicken Full</span></td><td>40</td><td>-</td><td>-</td></tr>
<tr><td>عرايس<span class="es">Arayis</span></td><td>20</td><td>-</td><td>-</td></tr>
<tr><td>تكة البحرين (4 أسياخ)<span class="es">Tikkat Bahrain</span></td><td>30</td><td>-</td><td>-</td></tr>
</table>
</div>'''

# ============ 2. APPETIZERS ============
apps_new = '''<div class="sec reveal" id="ap" data-title="Appetizers &amp; Salads">
<div class="sh"><h2>مقبلات ياسمين الدمام</h2><div class="she">Yasmeen Appetizers</div></div>
<img class="bimg tilt" src="appetizers_banner.jpg" alt="مقبلات ياسمين الدمام" loading="lazy">
<table class="tbl"><tr><th>الصنف</th><th>صغير</th><th>كبير</th></tr>
<tr><td>حمص<span class="es">Hummus</span></td><td>7</td><td>10</td></tr>
<tr><td>متبل<span class="es">Mutabbal</span></td><td>7</td><td>10</td></tr>
<tr><td>بابا غنوج<span class="es">Baba Ghanoush</span></td><td>7</td><td>10</td></tr>
<tr><td>فتوش<span class="es">Fattoush</span></td><td>7</td><td>10</td></tr>
<tr><td>سلطة خضراء<span class="es">Green Salad</span></td><td>7</td><td>10</td></tr>
</table>
</div>'''

# ============ 3. SHAWARMA ============
shawarma_new = '''<div class="sec reveal" id="sw">
<div class="sh"><h2>أطباق ياسمين الدمام</h2><div class="she">Yasmeen Shawarma Dishes</div></div>
<img class="bimg tilt" src="shawarma_banner.jpg" alt="أطباق ياسمين الدمام" loading="lazy">
<table class="tbl">
<tr><th>الصنف</th><th>صغير</th><th>وسط</th><th>كبير</th></tr>
<tr style="background:rgba(212,168,67,.06)"><td colspan="4" style="text-align:center;font-weight:800;font-size:16px;color:#D4A843">صحن شاورما عربي مقطع<span class="es">Arabic Sliced Shawarma</span></td></tr>
<tr><td style="padding-right:20px">🐔 دجاج</td><td>20</td><td>25</td><td>30</td></tr>
<tr><td style="padding-right:20px">🥩 لحم</td><td>25</td><td>38</td><td>42</td></tr>
<tr style="background:rgba(212,168,67,.06)"><td colspan="4" style="text-align:center;font-weight:800;font-size:16px;color:#D4A843">صحن شاورما عربي فرط (شرائح)<span class="es">Arabic Loose Slices</span></td></tr>
<tr><td style="padding-right:20px">🐔 دجاج</td><td>25</td><td>30</td><td>35</td></tr>
<tr><td style="padding-right:20px">🥩 لحم</td><td>30</td><td>45</td><td>60</td></tr>
<tr style="background:rgba(212,168,67,.06)"><td colspan="4" style="text-align:center;font-weight:800;font-size:16px;color:#D4A843">صحن شاورما ياسمين الدمام<span class="es">Yasmeen Al Dammam Special</span></td></tr>
<tr><td style="padding-right:20px">🐔 دجاج</td><td>25</td><td>-</td><td>35</td></tr>
<tr><td style="padding-right:20px">🥩 لحم</td><td>30</td><td>-</td><td>47</td></tr>
<tr style="background:rgba(212,168,67,.06)"><td colspan="4" style="text-align:center;font-weight:800;font-size:16px;color:#D4A843">وجبة شاورما كاساديا<span class="es">Shawarma Quesadilla</span></td></tr>
<tr><td style="padding-right:20px">🐔 دجاج</td><td>25</td><td>-</td><td>35</td></tr>
<tr><td style="padding-right:20px">🥩 لحم</td><td>30</td><td>-</td><td>47</td></tr>
<tr style="background:rgba(212,168,67,.06)"><td colspan="4" style="text-align:center;font-weight:800;font-size:16px;color:#D4A843">وجبة شاورما فرايز<span class="es">Fries Shawarma Meal</span></td></tr>
<tr><td style="padding-right:20px">🐔 دجاج</td><td>25</td><td>-</td><td>35</td></tr>
<tr style="background:rgba(212,168,67,.06)"><td colspan="4" style="text-align:center;font-weight:800;font-size:16px;color:#D4A843">وجبة شاورما ديتس<span class="es">Diet Shawarma Meal</span></td></tr>
<tr><td style="padding-right:20px">🐔 دجاج</td><td>25</td><td>-</td><td>35</td></tr>
<tr style="background:rgba(212,168,67,.06)"><td colspan="4" style="text-align:center;font-weight:800;font-size:16px;color:#D4A843">وجبة شاورما عائلية اقتصادية (مع بيبسي)<span class="es">Family Economy w/ Pepsi</span></td></tr>
<tr><td style="padding-right:20px">🐔 دجاج</td><td colspan="3">60</td></tr>
<tr><td style="padding-right:20px">🥩 لحم</td><td colspan="3">70</td></tr>
</table>
<div class="sb">🍟 إضافات <span class="sbe">Sides</span></div>
<table class="tbl"><tr><th>الصنف</th><th>صغير</th><th>وسط</th><th>كبير</th></tr>
<tr><td>صحن بطاطس<span class="es">Fries Plate</span></td><td>5</td><td>10</td><td>15</td></tr>
<tr><td>صحن بطاطس بالجبن<span class="es">Cheese Fries</span></td><td>10</td><td>15</td><td>20</td></tr>
</table>
</div>'''

# ============ 4. SANDWICHES ============
sandwiches_new = '''<div class="sec reveal" id="sd">
<div class="sh"><h2>سندويتشات ياسمين الدمام</h2><div class="she">Yasmeen Sandwiches</div></div>
<img class="bimg tilt" src="sandwiches_banner.jpg" alt="سندويتشات ياسمين الدمام" loading="lazy">
<div class="sb">🥩 سندويتشات المشويات <span class="sbe">Grilled Sandwiches</span></div>
<table class="tbl"><tr><th>الصنف</th><th>السعر</th></tr>
<tr><td>ساندويتش كباب لحم<span class="es">Kabab Lahm</span></td><td>10</td></tr>
<tr><td>ساندويتش كباب دجاج<span class="es">Kabab Dajaj</span></td><td>8</td></tr>
<tr><td>ساندويتش أوصال لحم<span class="es">Osal Lahm</span></td><td>12</td></tr>
<tr><td>ساندويتش شيش طاووق<span class="es">Shish Tawook</span></td><td>9</td></tr>
</table>
<div class="sb">🌯 سندويتشات الشاورما <span class="sbe">Shawarma Sandwiches</span></div>
<table class="tbl"><tr><th>الصنف</th><th>دجاج</th><th>لحم</th></tr>
<tr><td>ساندويتش صاروخ<span class="es">Sarooh</span></td><td>11</td><td>15</td></tr>
<tr><td>ساندويتش فطر<span class="es">Mushroom</span></td><td>9</td><td>12</td></tr>
<tr><td>ساندويتش شامي<span class="es">Shami</span></td><td>7</td><td>10</td></tr>
<tr><td>ساندويتش إيطالي<span class="es">Italian</span></td><td>9</td><td>14</td></tr>
<tr><td>ساندويتش فرنسي<span class="es">French</span></td><td>11</td><td>18</td></tr>
<tr><td>ساندويتش مكسيكي<span class="es">Mexican</span></td><td>15</td><td>18</td></tr>
<tr><td>ساندويتش بطاطس<span class="es">Potato</span></td><td>5</td><td>7</td></tr>
</table>
</div>'''

# ============ 5. PIZZA ============
pizza_new = '''<div class="sec reveal" id="pz" data-title="Yasmeen Pizza">
<div class="sh"><h2>قسم البيتزا</h2><div class="she">Pizza</div></div>
<img class="bimg tilt" src="pizza_banner.jpg" alt="قسم البيتزا" loading="lazy">
<table class="tbl"><tr><th>الصنف</th><th>صغير</th><th>وسط</th><th>كبير</th></tr>
<tr><td>بيتزا خضار<span class="es">Veggie Pizza</span></td><td>12</td><td>18</td><td>24</td></tr>
<tr><td>بيتزا مارغريتا<span class="es">Margherita Pizza</span></td><td>12</td><td>18</td><td>24</td></tr>
<tr><td>بيتزا مكس جبن<span class="es">Mixed Cheese Pizza</span></td><td>14</td><td>20</td><td>26</td></tr>
<tr><td>بيتزا دجاج<span class="es">Chicken Pizza</span></td><td>15</td><td>21</td><td>27</td></tr>
<tr><td>بيتزا لحم<span class="es">Meat Pizza</span></td><td>17</td><td>23</td><td>29</td></tr>
<tr><td>بيتزا مشكل<span class="es">Mixed Pizza</span></td><td>16</td><td>21</td><td>28</td></tr>
<tr><td>بيتزا رنش<span class="es">Ranch Pizza</span></td><td>15</td><td>20</td><td>27</td></tr>
<tr><td>بيتزا باربيكيو<span class="es">BBQ Pizza</span></td><td>15</td><td>20</td><td>27</td></tr>
<tr><td>بيتزا بيبروني<span class="es">Pepperoni Pizza</span></td><td>15</td><td>20</td><td>27</td></tr>
<tr><td>بيتزا شاورما دجاج<span class="es">Chicken Shawarma Pizza</span></td><td>15</td><td>21</td><td>27</td></tr>
<tr><td>بيتزا شاورما لحم<span class="es">Meat Shawarma Pizza</span></td><td>17</td><td>23</td><td>29</td></tr>
<tr><td>بيتزا هواي<span class="es">Hawaiian Pizza</span></td><td>15</td><td>20</td><td>25</td></tr>
<tr><td>بيتزا فور تشيز<span class="es">Four Cheese Pizza</span></td><td>17</td><td>23</td><td>29</td></tr>
</table>
</div>'''

# ============ 6. PASTRIES ============
pastries_new = '''<div class="sec reveal" id="pt" data-title="Yasmeen Pastries">
<div class="sh"><h2>فطائر ياسمين الدمام</h2><div class="she">Yasmeen Pastries</div></div>
<img class="bimg tilt" src="pastries_banner.jpg" alt="فطائر ياسمين الدمام" loading="lazy">
<table class="tbl"><tr><th>الصنف</th><th>السعر</th></tr>
<tr><td>فطيرة فلافل<span class="es">Falafel Pastry</span></td><td>10</td></tr>
<tr><td>فطيرة بيض<span class="es">Egg Pastry</span></td><td>10</td></tr>
<tr><td>فطيرة تونا بالبيض<span class="es">Tuna &amp; Egg Pastry</span></td><td>12</td></tr>
<tr><td>فطيرة محمرة<span class="es">Mhamra Pastry</span></td><td>6</td></tr>
<tr><td>فطيرة محمرة بالجبن<span class="es">Mhamra &amp; Cheese Pastry</span></td><td>7</td></tr>
<tr><td>فطيرة بطاطس<span class="es">Potato Pastry</span></td><td>8</td></tr>
<tr><td>فطيرة بطاطس بالجبن<span class="es">Potato &amp; Cheese Pastry</span></td><td>10</td></tr>
<tr><td>فطيرة جبن سائل<span class="es">Cream Cheese Pastry</span></td><td>7</td></tr>
<tr><td>فطيرة مكس جبن<span class="es">Mixed Cheese Pastry</span></td><td>9</td></tr>
<tr><td>فطيرة لبنة<span class="es">Labneh Pastry</span></td><td>7</td></tr>
<tr><td>فطيرة لبنة بالزعتر<span class="es">Labneh &amp; Zaatar Pastry</span></td><td>7</td></tr>
<tr><td>فطيرة لبنة بالعسل<span class="es">Labneh &amp; Honey Pastry</span></td><td>8</td></tr>
<tr><td>فطيرة زعتر<span class="es">Zaatar Pastry</span></td><td>6</td></tr>
<tr><td>فطيرة مشكل دجاج<span class="es">Mixed Chicken Pastry</span></td><td>8</td></tr>
<tr><td>فطيرة مشكل لحم<span class="es">Mixed Meat Pastry</span></td><td>10</td></tr>
<tr><td>فطيرة عكاوي<span class="es">Akkawi Pastry</span></td><td>9</td></tr>
<tr><td>فطيرة عش البلبل<span class="es">Ashp Balbul Pastry</span></td><td>9</td></tr>
</table>
</div>'''

# ============ 7. JUICES ============
juices_new = '''<div class="sec reveal" id="jc">
<div class="sh"><h2>عصائر ياسمين الدمام</h2><div class="she">Yasmeen Fresh Juices</div></div>
<img class="bimg tilt" src="juices_banner.jpg" alt="عصائر ياسمين الدمام" loading="lazy">
<table class="tbl"><tr><th>الصنف</th><th>1 لتر</th><th>1.5 لتر</th><th>كبير</th><th>وسط</th></tr>
<tr><td>كوكتيل<span class="es">Cocktail</span></td><td>15</td><td>22</td><td>8</td><td>6</td></tr>
<tr><td>طبقات<span class="es">Layered</span></td><td>18</td><td>24</td><td>10</td><td>8</td></tr>
<tr><td>مانجو<span class="es">Mango</span></td><td>15</td><td>22</td><td>8</td><td>6</td></tr>
<tr><td>موز بالحليب<span class="es">Banana Milk</span></td><td>15</td><td>22</td><td>8</td><td>6</td></tr>
<tr><td>رمان<span class="es">Pomegranate</span></td><td>15</td><td>22</td><td>8</td><td>6</td></tr>
<tr><td>كيوي<span class="es">Kiwi</span></td><td>15</td><td>22</td><td>8</td><td>6</td></tr>
<tr><td>عوار القلب<span class="es">Awar al-Qalb</span></td><td>18</td><td>24</td><td>10</td><td>8</td></tr>
<tr><td>اصفهاني<span class="es">Isfahani</span></td><td>18</td><td>24</td><td>10</td><td>8</td></tr>
<tr><td>أفوكادو<span class="es">Avocado</span></td><td>18</td><td>24</td><td>10</td><td>8</td></tr>
<tr><td>برتقال<span class="es">Orange</span></td><td>18</td><td>24</td><td>10</td><td>8</td></tr>
<tr><td>اسبيشل ياسمين الدمام<span class="es">Yasmeen Special</span></td><td>20</td><td>25</td><td>12</td><td>10</td></tr>
<tr><td>عصير روقان<span class="es">Rawqan Juice</span></td><td>18</td><td>25</td><td>10</td><td>8</td></tr>
</table>
</div>'''

# ============ APPLY ALL REPLACEMENTS ============
# Use unique markers to find each section

# 1. Grills
old_start = '<div class="sec a reveal" id="g"><div class="sh"><h2>المشويات</h2>'
new_start = '<div class="sec a reveal" id="g"><div class="sh"><h2>مشويات ياسمين الدمام</h2>'
html = html.replace(old_start, new_start, 1)

# Replace entire grills section (from first <div class="sec a reveal" id="g"> to </div> before next section)
import re

# Use section IDs as markers
sections = {
    'g': grills_new,
    'ap': apps_new,
    'sw': shawarma_new,
    'sd': sandwiches_new,
    'pz': pizza_new,
    'pt': pastries_new,
    'jc': juices_new,
}

for sec_id, new_html in sections.items():
    # Find the section - from <div class="sec ... id="{sec_id}"> to the closing </div> before next section
    pattern = re.compile(
        r'(<div class="sec[^"]*" id="' + re.escape(sec_id) + r'"[^>]*>.*?</div>\s*)',
        re.DOTALL
    )
    match = pattern.search(html)
    if match:
        old_section = match.group(1)
        html = html.replace(old_section, new_html, 1)
        print(f"✅ Replaced section: {sec_id}")
    else:
        print(f"❌ Could not find section: {sec_id}")

with open(path, 'w') as f:
    f.write(html)

print(f"\n✅ All sections updated! File written to {path}")
