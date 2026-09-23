import re

with open(r'd:\birthday\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .intro-content styles to be explicitly visible
css = re.sub(
    r'\.intro-content \{[^}]+\}',
    '''.intro-content {
    text-align: center;
    z-index: 10;
    padding: 0 1.5rem;
    max-width: 800px;
    opacity: 1;
    visibility: visible;
    transform: none;
    transition: opacity 0.5s ease, transform 0.5s ease;
}''', css, count=1)

# Replace fade-out with intro-leaving
css = re.sub(
    r'\.intro-content\.fade-out \{[^}]+\}',
    '''.intro-content.intro-leaving {
    opacity: 0;
    transform: translateY(-20px) scale(.98);
    transition: opacity 0.5s ease, transform 0.5s ease;
    pointer-events: none;
}''', css, count=1)

with open(r'd:\birthday\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open(r'd:\birthday\script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the click logic for openBtn
old_logic = '''openBtn.addEventListener('click', () => {
        // Fade out intro content
        introContent.classList.add('fade-out');
        
        // Unlock scroll on body
        document.body.classList.remove('no-scroll');
        
        // Wait a short moment for fade-out to begin, then smooth scroll down
        setTimeout(() => {
            mainSection.scrollIntoView({ behavior: 'smooth' });
        }, 600);
    });'''

new_logic = '''openBtn.addEventListener('click', () => {
        // Fade out intro content temporarily
        introContent.classList.add('intro-leaving');
        
        // Unlock scroll on body
        document.body.classList.remove('no-scroll');
        
        // Wait a short moment for fade-out to begin, then smooth scroll down
        setTimeout(() => {
            mainSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 500);

        // Restore it after scrolled past so it's there when they scroll back up
        setTimeout(() => {
            introContent.classList.remove('intro-leaving');
        }, 1200);
    });

    // Safety restore when user scrolls back to the very top
    window.addEventListener('scroll', () => {
        if (window.scrollY < window.innerHeight * 0.65) {
            introContent.classList.remove('intro-leaving', 'fade-out', 'hidden');
            introContent.style.removeProperty('opacity');
            introContent.style.removeProperty('visibility');
            introContent.style.removeProperty('transform');
        }
    }, { passive: true });'''

js = js.replace(old_logic, new_logic)

with open(r'd:\birthday\script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Bug fixed.")
