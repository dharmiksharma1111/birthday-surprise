import re

with open(r'd:\birthday\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .polaroid
css = re.sub(
    r'\.polaroid \{[^}]+\}',
    '''.polaroid {
    background: #fff;
    padding: 12px 12px 0 12px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.15);
    position: relative;
    width: 260px;
    cursor: pointer;
    z-index: 5;
    background-image: linear-gradient(to right, rgba(255,255,255,0.9), rgba(245,245,245,0.9));
    transform: translate(var(--tx, 0), var(--ty, 0)) rotate(var(--rot, 0deg)) scale(var(--sc, 1));
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease, z-index 0s, opacity 0.6s ease;
    overflow: visible;
}''', css, count=1)

# 2. Update .polaroid-grid
css = re.sub(
    r'\.polaroid-grid \{[^}]+\}',
    '''.polaroid-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    column-gap: 45px;
    row-gap: 55px;
    padding: 20px;
    width: 100%;
}''', css, count=1)

# 3. Update .polaroid-img-container -> .polaroid-image
css = css.replace('.polaroid-img-container {', '.polaroid-image {')
css = css.replace('.polaroid-img-container img {', '.polaroid-image img {')

css = re.sub(
    r'\.polaroid-image \{[^}]+\}',
    '''.polaroid-image {
    width: 100%;
    aspect-ratio: 4 / 5;
    overflow: hidden;
    position: relative;
    background: #eee;
}''', css, count=1)

css = re.sub(
    r'\.polaroid-image img \{[^}]+\}',
    '''.polaroid-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    pointer-events: auto;
}''', css, count=1)

# 4. Update .polaroid-caption
css = re.sub(
    r'\.polaroid-caption \{[^}]+\}',
    '''.polaroid-caption {
    width: 100%;
    min-height: 52px;
    padding: 9px 10px 11px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-family: 'Caveat', cursive;
    font-size: clamp(15px, 1.2vw, 20px);
    line-height: 1.2;
    color: #292321;
    white-space: normal;
    overflow-wrap: break-word;
    word-break: normal;
}''', css, count=1)

# 5. Remove top/left absolute positions from .pol-1 to .pol-8
for i, rot in enumerate([-4, 5, -3, 6, 3, -5, 4, -4], 1):
    css = re.sub(
        fr'\.pol-{i} {{[^}}]+}}',
        fr'.pol-{i} {{ --rot: {rot}deg; }}',
        css
    )

# 6. Mobile Media Query Additions
mobile_css = '''
@media (max-width: 768px) {
    .polaroid-grid {
        gap: 45px;
        flex-direction: column;
        align-items: center;
    }
    .polaroid {
        width: min(82vw, 300px);
    }
    .polaroid-caption {
        font-size: clamp(15px, 4.3vw, 18px);
        min-height: 48px;
        padding: 8px 10px 10px;
    }
    .pol-1 { --rot: -2deg; }
    .pol-2 { --rot: 3deg; }
    .pol-3 { --rot: -3deg; }
    .pol-4 { --rot: 2deg; }
    .pol-5 { --rot: -2deg; }
    .pol-6 { --rot: 3deg; }
    .pol-7 { --rot: -3deg; }
    .pol-8 { --rot: 2deg; }
}
'''
if '@media (max-width: 768px)' not in css:
    css += mobile_css

with open(r'd:\birthday\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# NOW FIX HTML
with open(r'd:\birthday\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Margin bottom for heading
html = html.replace('<div class="memories-header scroll-anim fade-up">', '<div class="memories-header scroll-anim fade-up" style="margin-bottom: 45px;">')

# Remove notes
html = re.sub(r'<div class="scrapbook-note note-\d+[^>]+>.*?</div>', '', html)
html = re.sub(r'<div class="doodle doodle-\d+[^>]+>.*?</div>', '', html)

# Fix Polaroid HTML
html = html.replace('polaroid-img-container', 'polaroid-image')
html = html.replace('<p class="polaroid-caption">', '<div class="polaroid-caption">')
html = html.replace('</p>\n                </div>', '</div>\n                </div>')

# Replace exact captions
captions_old = [
    "My favourite person ❤️",
    "That smile >>>",
    "A little moment, a big memory",
    "My safe place 🫂",
    "Us being us 🤍",
    "One of my favourite days",
    "Forever favourite ✨",
    "You make everything better ❤️"
]
captions_new = [
    "My Favourite Person ❤️",
    "That Smile >>>",
    "One Little Moment ❤️",
    "My Safe Place 🫂",
    "Us Being Us 🤍",
    "Favourite Day ✨",
    "Forever Favourite ✨",
    "You Make Me Smile ❤️"
]
for o, n in zip(captions_old, captions_new):
    html = html.replace(f'<div class="polaroid-caption">{o}</div>', f'<div class="polaroid-caption">{n}</div>')

with open(r'd:\birthday\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updates completed successfully.")
