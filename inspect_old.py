import re
from collections import Counter

with open(r'd:\birthday\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check for music button
print('Music/Audio/Sound keywords:')
for t in html.split('<'):
    if 'music' in t.lower() or 'audio' in t.lower() or 'sound' in t.lower():
        print('<' + t.split('\n')[0])

print('---')
# Check for remaining diary pages
pages = re.findall(r'data-page=\"(\d+)\"', html)
print('Diary pages:', pages)

print('---')
# Check for duplicates IDs
ids = re.findall(r'id=\"([^\"]+)\"', html)
counts = Counter(ids)
print('Duplicate IDs:', {k:v for k,v in counts.items() if v > 1})

print('---')
# Check CSS overly generic classes
with open(r'd:\birthday\style.css', 'r', encoding='utf-8') as f:
    css = f.read()
    
if '.hidden ' in css or '.hidden{' in css or '.hidden {' in css:
    print('Generic .hidden found in CSS')
