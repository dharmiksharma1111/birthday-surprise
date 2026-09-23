import re
import random

photos = [
    "Pic_1.jpg", "Pic_2.jpg", "Pic_3.jpeg", "Pic_4.jpeg",
    "Pic_5.jpg", "Pic_6.jpg", "Pic_7.jpeg", "Pic_8.jpeg",
    "Pic_9.jpeg", "Pic_10.jpg", "Pic_11.jpg", "Pic_12.jpeg",
    "Pic_13.jpeg", "Pic_14.jpeg"
]

themes = [
    "", # Original
    "filter: grayscale(100%);", # B/W
    "filter: sepia(60%) contrast(110%);", # Vintage/Paris
    "filter: brightness(110%) saturate(130%) sepia(20%);", # Warm/Paris
    "filter: grayscale(100%) contrast(120%);", # High contrast B/W
]

with open(r'd:\birthday\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to replace all instances of <img src="assets/photos/Pic_..." ...>
# There are 31 of them.
# We will use re.sub with a replacement function

counter = 0

def replace_img(match):
    global counter
    # Don't touch the modal image
    if 'id="modal-img"' in match.group(0):
        return match.group(0)
        
    photo_file = photos[counter % len(photos)]
    
    # Assign a theme. First 14 can be original, next 14 can be themed.
    # Actually, randomizing is fine, or cycle based on counter.
    theme_idx = (counter // len(photos)) % len(themes)
    # But let's add some variety
    if theme_idx == 0 and counter >= len(photos):
        theme_idx = random.randint(1, len(themes)-1)
    
    theme_style = themes[theme_idx]
    
    # The original tag looks like: <img src="assets/photos/Pic_1.jpg" alt="Memory" class="collage-photo p1 gallery-img">
    # We replace the src attribute.
    tag = match.group(0)
    tag = re.sub(r'src="assets/photos/[^"]+"', f'src="assets/photos/{photo_file}"', tag)
    
    # Add style if not empty
    if theme_style:
        # Check if style attribute exists
        if 'style="' in tag:
            tag = re.sub(r'style="([^"]*)"', r'style="\1 ' + theme_style + '"', tag)
        else:
            tag = tag.replace('>', f' style="{theme_style}">')
            
    counter += 1
    return tag

# Replace all images that have src="assets/photos/..."
new_html = re.sub(r'<img [^>]*src="assets/photos/[^>]*>', replace_img, html)

with open(r'd:\birthday\index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Replaced {counter} images.")
