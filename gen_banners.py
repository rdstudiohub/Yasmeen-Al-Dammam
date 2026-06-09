import os, json, subprocess, time, sys

# Run with: source /opt/data/.env && python3 this_script.py
tok = os.environ.get('REPLICATE_API_TOKEN', '')
if not tok:
    print("ERROR: REPLICATE_API_TOKEN not set")
    sys.exit(1)

auth = "Bearer " + tok
API = "https://api.replicate.com/v1/models/black-forest-labs/flux-schnell/predictions"
OUT = os.path.dirname(os.path.abspath(__file__))

BANNERS = [
  ("pizza_banner","Assorted pizzas on dark wooden table, Margherita, Pepperoni, Four Cheese, melted cheese, fresh basil, warm lighting, black background, premium restaurant food photography, 8k"),
  ("feteer_banner","Traditional feteer pastries, golden brown flaky layers, savory with cheese and sweet with honey, on ornate brass platter, warm ambient lighting, premium restaurant food photography, 8k"),
  ("shawarma_banner","Shawarma wraps on wooden board, chicken and meat, toasted bread, garlic sauce, pickles, fries, warm golden lighting, dark background, professional food photography, 8k"),
  ("saj_banner","Fresh Saj sandwiches on grill, chicken and meat fillings, crispy golden, vegetables, sauces, dark textured surface, steam rising, premium food photography, 8k"),
  ("burgers_banner","Gourmet burger collection on dark board, cheese burger, crispy chicken, double beef, fresh lettuce tomato, sizzling patties, dramatic lighting, dark background, 8k"),
  ("grills_banner","Arabian mixed grill platter, kebabs, shish tawook, grilled vegetables, rice, on ornate tray, charcoal marks, warm golden lighting, premium Arabic restaurant photography, 8k"),
  ("meals_banner","Whole grilled chicken on platter, golden crispy skin, roasted vegetables, rice, Arabic bread, herbs garnish, family style, warm restaurant lighting, 8k"),
  ("salads_banner","Fresh Arabic salads, fattoush, green salad, tabbouleh, colorful, dark wooden table, natural lighting, healthy, premium photography, 8k"),
  ("sides_banner","Crispy french fries, cheese fries, dipping sauces, garlic sauce, on dark slate, steam rising, warm lighting, premium food photography, 8k"),
  ("juices_banner","Fresh juice glasses, avocado, orange, strawberry, mango, pomegranate, fresh fruits, ice cubes, condensation, vibrant colors, sunlight, premium menu photography, 8k"),
  ("cocktails_banner","Colorful cocktails and drinks, layered cocktails, mojito, fresh juices, mint, lime, ice, dark background, vibrant colors, warm lighting, premium beverage photography, 8k"),
]

def gen(key, prompt):
    out = os.path.join(OUT, key + ".jpg")
    if os.path.exists(out) and os.path.getsize(out) > 2000:
        print(f"  SKIP {key}")
        return True
    payload = json.dumps({"input": {"prompt": prompt, "num_outputs": 1, "aspect_ratio": "4:5", "output_format": "jpg", "quality": 85}})
    try:
        r = subprocess.run(["curl", "-s", "-X", "POST", API, "-H", "Authorization: " + auth, "-H", "Content-Type: application/json", "-d", payload], capture_output=True, text=True, timeout=60).stdout.strip()
        d = json.loads(r)
        pid = d.get("id")
        if not pid:
            print(f"  FAIL {key}: {r[:100]}")
            return False
        for _ in range(30):
            time.sleep(3)
            pr = subprocess.run(["curl", "-s", f"https://api.replicate.com/v1/predictions/{pid}", "-H", "Authorization: " + auth], capture_output=True, text=True, timeout=15).stdout.strip()
            sd = json.loads(pr)
            if sd.get("status") == "succeeded":
                url = sd["output"][0] if isinstance(sd["output"], list) else sd["output"]
                subprocess.run(["curl", "-sL", url, "-o", out], timeout=30)
                print(f"  OK {key} ({os.path.getsize(out)}b)")
                return True
            elif sd.get("status") == "failed":
                print(f"  FAIL {key}")
                return False
        print(f"  TIMEOUT {key}")
        return False
    except Exception as e:
        print(f"  ERROR {key}: {e}")
        return False

print(f"Generating {len(BANNERS)} banners...")
ok = 0
for i, (k, p) in enumerate(BANNERS):
    sys.stdout.write(f"[{i+1}/{len(BANNERS)}] {k}... ")
    sys.stdout.flush()
    if gen(k, p): ok += 1
    if i < len(BANNERS) - 1: time.sleep(2)
print(f"\nDone: {ok}/{len(BANNERS)} banners")
