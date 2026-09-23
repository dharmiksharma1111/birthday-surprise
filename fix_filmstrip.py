import re

# FIX HTML
with open(r'd:\birthday\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the film strip contents
film_strip_match = re.search(r'<div class="film-strip">(.*?)</div>', html, re.DOTALL)
if film_strip_match:
    inner = film_strip_match.group(1).strip()
    # The inner content is 4 img tags
    # Wrap each one in <div class="film-photo">...</div>
    new_inner = re.sub(r'(<img [^>]+>)', r'<div class="film-photo">\1</div>', inner)
    
    # Wrap everything in film-track
    new_strip = f'<div class="film-strip">\n                    <div class="film-track">\n                        {new_inner}\n                    </div>\n                </div>'
    
    html = html.replace(film_strip_match.group(0), new_strip)
    
    with open(r'd:\birthday\index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
# FIX CSS
with open(r'd:\birthday\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove old film-strip, film-img blocks safely
css = re.sub(r'\.film-strip \{[^}]+\}', '', css, count=1)
css = re.sub(r'\.film-img \{[^}]+\}', '', css, count=1)

new_film_css = '''
.film-strip {
    width: 100%;
    max-width: 620px;
    box-sizing: border-box;
    overflow: hidden;
    position: relative;
    background-color: #1a1a1a;
    border-radius: 4px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    background-image: 
        radial-gradient(circle, #fdfbf7 3px, transparent 4px),
        radial-gradient(circle, #fdfbf7 3px, transparent 4px);
    background-size: 20px 10px, 20px 10px;
    background-position: 5px 2px, 5px calc(100% - 2px);
    background-repeat: repeat-x;
    transition: transform 0.4s ease;
}

.film-track {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 8px;
    box-sizing: border-box;
    padding: 14px 12px;
}

.film-photo {
    width: 100%;
    min-width: 0;
    overflow: hidden;
    box-sizing: border-box;
}

.film-photo img, .film-img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    background-color: #ddd;
    cursor: pointer;
    transition: filter 0.3s ease;
    aspect-ratio: 4 / 3;
}
'''

# Insert it around where it was
css = css.replace('.film-strip:hover {', new_film_css + '\n.film-strip:hover {')

# Adjust mobile layout
mobile_film_css = '''
    .film-strip {
        width: min(92vw, 390px);
        margin-inline: auto;
    }
    .film-track {
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 4px;
        padding: 10px 8px;
    }
'''

# Append mobile CSS to the @media (max-width: 768px) block. 
# We'll just put it at the very end.
if '@media (max-width: 768px)' in css:
    css = css[:-1] + mobile_film_css + '\n}\n'
else:
    css += '\n@media (max-width: 768px) {\n' + mobile_film_css + '\n}\n'


with open(r'd:\birthday\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Film strip layout updated.")
