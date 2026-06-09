#!/usr/bin/env python3
"""Generate banner images for Yasmeen Al Dammam menu categories."""
import os, subprocess, json, time, sys

TOKEN = os.environ.get("REPLICATE_API_TOKEN") or os.environ.get("REPLICATE_TOKEN")
if not TOKEN:
    print("ERROR: No Replicate token found")
    sys.exit(1)

AUTH = "Bearer " + TOKEN
API = "https://api.replicate.com/v1/models/black-forest-labs/flux-schnell/predictions"
OUT = "/opt/data/yasmeen-menu"

banners = [
    ("hero", "Premium restaurant food banner: grilled meat platter with kebabs, shawarma wraps, fresh salads, pizza, and colorful juices arranged on a dark wooden table. Professional food photography, birds eye view overhead shot, gold and black theme, luxury Arabic restaurant style, warm ambient lighting, shallow depth of field, rich textures, vibrant colors, cinematic quality, 8k, restaurant menu cover design"),
    
    ("grills", "Premium grilled meat platter: mixed kebabs, shish tawook skewers, lamb chops, grilled chicken, sizzling on a hot cast iron grill, smoke and steam rising. Professional food photography, close up shot, dark background, warm amber lighting, rich textures, charred edges, fresh herbs garnish, lemon wedges, cinematic lighting, 8k quality, restaurant menu banner"),
    
    ("appetizers", "Arabic mezze spread: bowls of hummus drizzled with olive oil, mutabbal, baba ghanoush, fattoush salad with crispy bread, fresh green salad, arranged on a rustic wooden table. Professional food photography, overhead flat lay, natural daylight style, vibrant colors, fresh herbs garnish, pomegranate seeds, tahini drizzle, 8k quality, restaurant menu banner"),
    
    ("shawarma", "Delicious chicken shawarma platter: sliced shawarma meat on a tray, grilled tomatoes and peppers, fresh parsley, pickles, garlic sauce and tahini, served with warm Arabic bread. Professional food photography, close up angled shot, warm golden lighting, juicy meat textures, steam rising, dark elegant background, cinematic quality, 8k, restaurant menu banner"),
    
    ("sandwiches", "Assorted gourmet sandwiches: grilled chicken sandwich, shawarma wrap cut in half showing layers, Italian sub, Mexican style sandwich, on a wooden board with fresh lettuce and tomatoes. Professional food photography, side angle, crispy bread textures, melted cheese visible, warm lighting, rustic wooden surface, shallow depth of field, 8k quality"),
    
    ("pizza", "Fresh baked gourmet pizzas: margherita with melted mozzarella and basil, pepperoni with crispy edges, BBQ chicken pizza, cheese pull stretching. Professional food photography, close up shot, wood fired oven style, charred crust, vibrant sauce colors, melted cheese textures, warm ambient lighting, cinematic quality, 8k, restaurant menu banner"),
    
    ("pastries", "Arabic pastries and cheese pastries: golden baked fatayer with spinach, cheese pastries, zaatar manakeesh, meat pastries, labneh rolls, arranged on an elegant serving tray. Professional food photography, overhead flat lay, warm golden brown colors, sesame seeds garnish, olive oil drizzle, natural lighting, 8k quality, restaurant menu banner"),
    
    ("juices", "Colorful fresh juice glasses: tall glasses of mango, pomegranate, orange, cocktail, avocado smoothie, with fresh fruits around, mint leaves garnish, ice cubes, condensation drops on glasses. Professional beverage photography, dark wooden table, warm backlighting through glasses, vibrant colors, fresh fruit slices, premium bar style, cinematic lighting, 8k quality"),
]

def gen(key, prompt):
    out_path = os.path.join(OUT, f"{key}_banner.jpg")
    payload = json.dumps({
        "input": {
            "prompt": prompt,
            "num_outputs": 1,
            "aspect_ratio": "4:5",
            "output_format": "jpg",
            "quality": 90
        }
    })
    
    # Submit
    r = subprocess.run(["curl", "-s", "-X", "POST", API,
        "-H", "Authorization: " + AUTH,
        "-H", "Content-Type: application/json",
        "-d", payload], capture_output=True, text=True, timeout=60)
    data = json.loads(r.stdout)
    pid = data.get("id")
    if not pid:
        print(f"  ERROR: No prediction ID for {key}")
        return False
    
    # Poll
    for i in range(30):
        time.sleep(3)
        pr = subprocess.run(["curl", "-s",
            f"https://api.replicate.com/v1/predictions/{pid}",
            "-H", "Authorization: " + AUTH],
            capture_output=True, text=True, timeout=30)
        sd = json.loads(pr.stdout)
        st = sd.get("status")
        if st == "succeeded":
            url = sd["output"]
            if isinstance(url, list):
                url = url[0]
            subprocess.run(["curl", "-sL", url, "-o", out_path], timeout=30)
            sz = os.path.getsize(out_path)
            print(f"  ✅ {key}: {sz} bytes")
            return True
        elif st == "failed":
            print(f"  ❌ {key}: failed")
            return False
        # still processing
    print(f"  ⏰ {key}: timeout")
    return False

print(f"🎯 Generating {len(banners)} banners...\n")

for i in range(0, len(banners), 2):
    batch = banners[i:i+2]
    print(f"Batch {i//2 + 1}: {', '.join(b[0] for b in batch)}")
    for key, prompt in batch:
        if os.path.exists(os.path.join(OUT, f"{key}_banner.jpg")):
            sz = os.path.getsize(os.path.join(OUT, f"{key}_banner.jpg"))
            print(f"  ⏭️ {key}: already exists ({sz} bytes)")
            continue
        if not gen(key, prompt):
            print(f"  ⚠️ Failed to generate {key}")
    if i+2 < len(banners):
        time.sleep(3)

print("\n✅ Banner generation complete!")
print(f"\nGenerated files:")
for key, _ in banners:
    path = os.path.join(OUT, f"{key}_banner.jpg")
    if os.path.exists(path):
        print(f"  {key}: {os.path.getsize(path)} bytes")
    else:
        print(f"  {key}: MISSING")
