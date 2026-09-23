import re

# 1. Update HTML
with open(r'd:\birthday\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make tumse-thoda-aur locked initially
html = html.replace('<section id="tumse-thoda-aur" class="poem-section">', '<section id="tumse-thoda-aur" class="poem-section poem-locked">')

# Change reveal-blur to poem-reveal-line inside poem section
def replace_blur(match):
    return match.group(0).replace('reveal-blur', 'poem-reveal-line')

html = re.sub(r'<section id="tumse-thoda-aur".*?</section>', replace_blur, html, flags=re.DOTALL)

with open(r'd:\birthday\index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update CSS
with open(r'd:\birthday\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* Poem Unlock Sequence */
.poem-locked {
    opacity: 0;
    visibility: hidden;
    max-height: 0;
    overflow: hidden;
    pointer-events: none;
    margin: 0 !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}

.poem-unlocked {
    opacity: 1;
    visibility: visible;
    max-height: 3000px;
    pointer-events: auto;
    transition: opacity 1s ease, max-height 1s ease, padding 1s ease;
}

.poem-reveal-line {
    opacity: 0;
    transform: translateY(15px);
    filter: blur(4px);
    transition: opacity 0.8s ease, transform 0.8s ease, filter 0.8s ease;
}

.poem-reveal-line.revealed {
    opacity: 1;
    transform: translateY(0);
    filter: blur(0);
}
'''
if '.poem-locked' not in css:
    css += '\n' + new_css
    with open(r'd:\birthday\style.css', 'w', encoding='utf-8') as f:
        f.write(css)


# 3. Update JS
with open(r'd:\birthday\script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the old readHeartBtn logic
js = re.sub(r'const readHeartBtn\s*=\s*document\.getElementById\(\'read-heart-btn\'\);.*?\}\);', '', js, flags=re.DOTALL)

# Add the new sequenced readHeartBtn logic
new_js = '''
    const readHeartBtn = document.getElementById('read-heart-btn');
    const poemSection = document.getElementById('tumse-thoda-aur');
    let poemUnlocked = false;

    if (readHeartBtn && poemSection) {
        readHeartBtn.addEventListener('click', () => {
            if (poemUnlocked) return;
            poemUnlocked = true;

            // Heart ripple on button
            readHeartBtn.style.transform = 'scale(0.95)';
            setTimeout(() => readHeartBtn.style.transform = 'scale(1)', 150);

            // Darken screen slightly
            const overlay = document.createElement('div');
            overlay.style.position = 'fixed';
            overlay.style.top = '0';
            overlay.style.left = '0';
            overlay.style.width = '100%';
            overlay.style.height = '100%';
            overlay.style.backgroundColor = 'rgba(0,0,0,0.4)';
            overlay.style.zIndex = '9999';
            overlay.style.pointerEvents = 'none';
            overlay.style.transition = 'opacity 0.6s ease';
            document.body.appendChild(overlay);

            setTimeout(() => { overlay.style.opacity = '0'; }, 500);
            setTimeout(() => { overlay.remove(); }, 1200);

            // Unlock section
            poemSection.classList.remove('poem-locked');
            poemSection.classList.add('poem-unlocked');

            // Change button state
            readHeartBtn.innerHTML = 'Opened With Love ❤️';
            readHeartBtn.style.opacity = '0.6';
            readHeartBtn.style.pointerEvents = 'none';

            setTimeout(() => {
                poemSection.scrollIntoView({ behavior: 'smooth', block: 'start' });

                // Start Reveal Sequence
                const title = poemSection.querySelector('.poem-title');
                const subtitle = poemSection.querySelector('.poem-subtitle');
                const lines = poemSection.querySelectorAll('.poem-line');

                setTimeout(() => { if (title) title.classList.add('revealed'); }, 300);
                setTimeout(() => { if (subtitle) subtitle.classList.add('revealed'); }, 600);

                const delays = [1000, 1500, 2000, 2500, 3000, 3500, 4200];
                lines.forEach((line, index) => {
                    const delay = delays[index] || (4200 + (index - 6) * 700);
                    setTimeout(() => {
                        line.classList.add('revealed');
                        
                        // If it's the final climax line
                        if (index === lines.length - 1) {
                            const climaxWrapper = line.closest('.poem-climax-wrapper');
                            if (climaxWrapper) {
                                climaxWrapper.classList.add('climax-active');
                                createTinyHearts(climaxWrapper, false);
                                
                                // Make central spotlight slightly brighter
                                const spot = poemSection.querySelector('.poem-spotlight');
                                if (spot) {
                                    spot.style.background = 'radial-gradient(circle at 50% 50%, rgba(200, 100, 120, 0.18), transparent 60%)';
                                    spot.style.transition = 'background 2s ease';
                                }
                            }
                        }
                    }, delay);
                });
            }, 250);
        });
    }
'''

# The climax logic in the intersection observer shouldn't run anymore for the poem, 
# because I removed poem-climax-wrapper from the intersection observer by changing its classes?
# Wait, the intersection observer checks `if (entry.target.classList.contains('poem-climax-wrapper'))` but it's observing `.reveal-blur, .reveal-p`.
# Since I changed `.reveal-blur` to `.poem-reveal-line`, the climax wrapper won't be observed by intersection observer anymore! Which is perfect!

js = js.replace('// Read my heart btn -> Poem section', new_js)

with open(r'd:\birthday\script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("All updated")
