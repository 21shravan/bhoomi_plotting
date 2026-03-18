import re

# === SCALE FACTORS ===
scale_x = 11858 / 739
scale_y = 8375 / 1600

# === FILES ===
input_file = "index.html"
output_file = "index_scaled.html"

def scale_points(points_str):
    pairs = points_str.strip().split(' ')
    new_pairs = []

    for pair in pairs:
        if not pair.strip():
            continue
        x, y = pair.split(',')
        new_x = float(x) * scale_x
        new_y = float(y) * scale_y
        new_pairs.append(f"{round(new_x,2)},{round(new_y,2)}")

    return " ".join(new_pairs)

# === READ FILE ===
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# === FIND & REPLACE POLYGONS ===
def replace_points(match):
    original_points = match.group(1)
    scaled = scale_points(original_points)
    return f'points="{scaled}"'

new_content = re.sub(r'points="([^"]+)"', replace_points, content)

# === WRITE OUTPUT ===
with open(output_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ Done! Scaled file saved as:", output_file)