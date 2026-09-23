import re

# 1. Update HTML
with open(r'd:\birthday\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Match from mr-husband-letter start to final-surprise start
pattern = r'(<section id="mr-husband-letter".*?)(<!-- Final Surprise Section -->)'
match = re.search(pattern, html, re.DOTALL)

if match:
    new_html = '''    <!-- Mr. Husband Letter Section -->
    <section id="mr-husband-letter" class="letter-section enhanced-section">
        <!-- Spotlight -->
        <div class="cinematic-spotlight"></div>

        <div class="letter-header">
            <h2 class="letter-title">For My Mr. Husband ❤️</h2>
            <p class="letter-subtitle fade-in-slow">A few words I never want you to forget... ❤️</p>
        </div>

        <div class="letter-container delayed-reveal">
            <div class="letter-card premium-card">
                <div class="card-pulse-heart">❤️</div>
                
                <div class="letter-body">
                    <p class="reveal-p">Hello my mr.husband ❤️</p>

                    <p class="reveal-p">Aaje khabar che ketlo special day che?<br>Mara birthday ni jetli excitement nathi hoti, aetli tara birthday ni hoy che… 💝</p>

                    <p class="reveal-p">Finally, today’s date — 16/10 🥳🥳🥳🥳<br>Mara ae person no birthday che, jene always mane support karyo che, always mari sathe j ryo che… 🫂<br>Always mane happy rakhvani j try kari che…<br>Mari life j tu cho, Jay. 🫂</p>

                    <p class="reveal-p highlight-line">Because maru world 🌎 j tu cho…</p>

                    <p class="reveal-p">Tane khabar che, bija loko ne eni life ma problem aave to mummy, papa, bhai yaad aave…<br>Pan mari life ma kai pan problem aave, aetle pela tu yaad aav…<br>Mara life ni last 7 minutes pan tu j cho, Jay… 🫂🫂🫂🫂</p>

                    <p class="reveal-p">Tari sathe life ni nani nani moments pan special bani jaay chhe.<br>Tari ek smile maru mood badli shake chhe, ane taro ek word — 'hu chu ne' — mane badhi problems ma strong feel karave chhe. ❤️</p>

                    <p class="reveal-p">Jay, mane life perfect nathi joie…<br>Mane bas badhi situation ma taro support joie che —<br>happiness hoy ke sadness, success hoy ke struggle, hu always tari sathe chu. 🥺❤️</p>

                    <p class="reveal-p heartbeat-line">Jay, ek promise karu...<br>Life hamesha easy nathi hoy, badha days perfect nathi hoy, but ek vaat always same rehse —<br>hu tari sathe rahish. 🥹❤️</p>

                    <p class="reveal-p highlight-line">Jya sudhi life chhe,<br>tya sudhi tari sathe aa journey chhe. ❤️♾️</p>

                    <p class="reveal-p highlight-line">My world is not perfect,<br>but because you are in it,<br>I find it the most beautiful. 🥺❤️</p>

                    <p class="reveal-p">Thank you for being my person, my forever, my husband, my love, my everything. 🎂❤️</p>

                    <p class="reveal-p">Thank you so much mari life ma aavi ne mari life ne complete banava mate. ❤️🥹<br>Thank you for always being there for me, my lifeline… ❤️🫶🏻</p>

                    <p class="reveal-p">Bas aaje aa special day par ae j pray karis ke Hari tane always happy and healthy rakhe… 🥰</p>

                    <p class="reveal-p highlight-line-large">Happy Birthday to the man who makes my life more beautiful every single day. ❤️<br>I love you endlessly, Jayu ❤️♾️🫂🫂🫂🧿🧿</p>
                </div>
                
                <div class="letter-signature reveal-p">
                    <p>Forever yours ❤️</p>
                </div>
            </div>
            
            <div class="next-section-trigger reveal-p">
                <p class="trigger-text">There's something more I want from you... ❤️</p>
                <button id="read-heart-btn" class="glow-btn">Read My Heart →</button>
            </div>
        </div>
    </section>

    <!-- Poem Section -->
    <section id="tumse-thoda-aur" class="poem-section">
        <div class="poem-spotlight"></div>

        <div class="poem-header">
            <h2 class="poem-title reveal-blur">Tumse Bas Thoda Sa Aur... ❤️</h2>
            <p class="poem-subtitle reveal-blur">Kuch baatein sirf dil se maangi jaati hain...</p>
        </div>

        <div class="poem-body">
            <p class="poem-line reveal-blur">Tumse tumhara waqt maangungi… ⏳❤️</p>
            <p class="poem-line reveal-blur">Kab, kahan, kaise ho — iska zikr maangungi… 💭🥹</p>
            <p class="poem-line reveal-blur">Waqt-bewaqt call karne ka haq maangungi… 📞💕</p>
            <p class="poem-line reveal-blur">Bin baat ke mere ladne par tumhara sabr maangungi… 🥺🫂</p>
            <p class="poem-line reveal-blur">Savere uthaa ke tumhari tasveer maangungi… 📸💗</p>
            
            <p class="poem-line reveal-blur special-pause">Main jab bhi maangungi… 🌷</p>
            
            <div class="poem-climax-wrapper reveal-blur">
                <div class="climax-glow-heart"></div>
                <p class="poem-line climax-line">Tumhe tumse thoda aur maangungi… ♾️❤️✨</p>
            </div>
        </div>
    </section>

    '''
    
    html = html.replace(match.group(1), new_html)
    with open(r'd:\birthday\index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("HTML replaced")
else:
    print("Could not find sections to replace")

# 2. Update CSS
with open(r'd:\birthday\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* ==========================================================================
   Enhanced Cinematic Letter Section
   ========================================================================== */
.enhanced-section {
    background-color: #1a0b12 !important; /* deep burgundy/midnight */
    background-image: none !important;
    position: relative;
    padding: 80px 20px 100px;
}

.cinematic-spotlight {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 150vw;
    height: 150vh;
    background: radial-gradient(circle at 50% 45%, rgba(255, 210, 190, 0.24), rgba(255, 170, 180, 0.08) 35%, transparent 65%);
    pointer-events: none;
    z-index: 0;
    animation: slowBreathe 8s ease-in-out infinite alternate;
}

@keyframes slowBreathe {
    0% { transform: translate(-50%, -50%) scale(1); opacity: 0.8; }
    100% { transform: translate(-50%, -50%) scale(1.05); opacity: 1; }
}

.enhanced-section .letter-title {
    color: #f8e5e5;
    text-shadow: 0 0 15px rgba(255,255,255,0.2);
    position: relative;
    z-index: 2;
}

.fade-in-slow {
    opacity: 0;
    animation: slowFadeIn 1.5s 0.8s forwards;
    position: relative;
    z-index: 2;
    color: #e0d0d0;
    font-style: italic;
    font-size: 1.1rem;
    margin-bottom: 30px;
}

@keyframes slowFadeIn {
    to { opacity: 1; }
}

.delayed-reveal {
    opacity: 0;
    transform: translateY(20px) scale(0.97);
    animation: delayedReveal 1.2s 2s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
}

@keyframes delayedReveal {
    to { opacity: 1; transform: translateY(0) scale(1); }
}

.premium-card {
    background: #fdfbf7 !important; /* warm ivory */
    box-shadow: 0 15px 40px rgba(25, 0, 10, 0.4), inset 0 0 0 1px rgba(212, 106, 106, 0.1) !important;
    border-radius: 12px;
    padding: 50px 25px 40px !important;
    position: relative;
    overflow: hidden;
}

.premium-card::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: url('data:image/svg+xml;utf8,<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><filter id="noise"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(%23noise)" opacity="0.04"/></svg>');
    opacity: 0.8;
    pointer-events: none;
    border-radius: 12px;
}

.card-pulse-heart {
    position: absolute;
    top: -15px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 30px;
    background: #fdfbf7;
    border-radius: 50%;
    padding: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    animation: slowHeartbeat 2s infinite ease-in-out;
    z-index: 3;
}

@keyframes slowHeartbeat {
    0%, 100% { transform: translateX(-50%) scale(1); }
    15% { transform: translateX(-50%) scale(1.08); }
    30% { transform: translateX(-50%) scale(1); }
    45% { transform: translateX(-50%) scale(1.08); }
}

.reveal-p {
    opacity: 0;
    transform: translateY(15px);
    transition: opacity 0.8s ease, transform 0.8s ease;
    position: relative;
    z-index: 2;
}

.reveal-p.revealed {
    opacity: 1;
    transform: translateY(0);
}

.highlight-line {
    font-family: 'Playfair Display', serif !important;
    font-size: 18px !important;
    color: #b54a4a !important;
    text-align: center;
    font-style: italic;
    margin: 30px 0 !important;
    position: relative;
}

.highlight-line::after {
    content: '❤️';
    display: block;
    font-size: 12px;
    margin-top: 5px;
    opacity: 0;
    animation: popHeart 0.5s 0.8s forwards;
}

@keyframes popHeart {
    0% { transform: scale(0); opacity: 0; }
    50% { transform: scale(1.2); opacity: 1; }
    100% { transform: scale(1); opacity: 0.6; }
}

.highlight-line-large {
    font-family: 'Playfair Display', serif !important;
    font-size: 21px !important;
    color: #a33b3b !important;
    text-align: center;
    font-style: italic;
    margin: 40px 0 !important;
}

.highlight-line-large::after {
    content: '❤️';
    display: block;
    font-size: 14px;
    margin-top: 8px;
    opacity: 0;
    animation: popHeart 0.5s 1s forwards;
}

.heartbeat-line.revealed {
    animation: bgPulse 2s ease forwards;
    position: relative;
    z-index: 3;
}

@keyframes bgPulse {
    0% { text-shadow: 0 0 0 rgba(212,106,106,0); }
    50% { text-shadow: 0 0 15px rgba(212,106,106,0.6); transform: scale(1.02); }
    100% { text-shadow: 0 0 0 rgba(212,106,106,0); transform: scale(1); }
}

.next-section-trigger {
    text-align: center;
    margin-top: 50px;
    position: relative;
    z-index: 2;
}

.trigger-text {
    font-family: 'Inter', sans-serif;
    color: #e8dada;
    margin-bottom: 20px;
    font-size: 16px;
    font-style: italic;
}

/* ==========================================================================
   Poem Section
   ========================================================================== */
.poem-section {
    background-color: #130a12; /* very dark romantic tone */
    min-height: 100vh;
    padding: 80px 20px;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow: hidden;
}

.poem-spotlight {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 120vw;
    height: 120vh;
    background: radial-gradient(circle at 50% 50%, rgba(200, 100, 120, 0.1), transparent 60%);
    pointer-events: none;
    z-index: 0;
}

.poem-header {
    text-align: center;
    margin-bottom: 60px;
    position: relative;
    z-index: 2;
}

.poem-title {
    font-family: 'Caveat', cursive;
    font-size: clamp(32px, 9vw, 44px);
    color: #e59090;
    margin-bottom: 10px;
}

.poem-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 15px;
    color: #a8949b;
    font-style: italic;
}

.poem-body {
    width: min(92vw, 430px);
    text-align: center;
    position: relative;
    z-index: 2;
}

.reveal-blur {
    opacity: 0;
    transform: translateY(15px);
    filter: blur(4px);
    transition: opacity 0.8s ease, transform 0.8s ease, filter 0.8s ease;
}

.reveal-blur.revealed {
    opacity: 1;
    transform: translateY(0);
    filter: blur(0);
}

.poem-line {
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    line-height: 1.8;
    color: #eadddf;
    margin-bottom: 30px;
}

.special-pause {
    transition: opacity 1s ease;
}

.special-pause.dimmed {
    opacity: 0.6;
}

.poem-climax-wrapper {
    position: relative;
    margin-top: 50px;
    padding: 20px 0;
    cursor: pointer;
}

.climax-glow-heart {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 250px;
    height: 250px;
    background: radial-gradient(circle, rgba(212,106,106,0.15) 0%, transparent 60%);
    opacity: 0;
    transition: opacity 1.5s ease;
    pointer-events: none;
    z-index: -1;
    border-radius: 50%;
}

.poem-climax-wrapper.climax-active .climax-glow-heart {
    opacity: 1;
}

.poem-climax-wrapper.climax-active .climax-line {
    font-size: 20px;
    color: #f4c2c2;
    text-shadow: 0 0 10px rgba(244, 194, 194, 0.4);
    animation: gentleShimmer 2s ease-in-out;
}

@keyframes gentleShimmer {
    0% { filter: brightness(1); }
    50% { filter: brightness(1.3); text-shadow: 0 0 20px rgba(244, 194, 194, 0.8); }
    100% { filter: brightness(1); text-shadow: 0 0 10px rgba(244, 194, 194, 0.4); }
}

@media (prefers-reduced-motion: reduce) {
    .cinematic-spotlight, .poem-spotlight, .card-pulse-heart, .burst-part {
        animation: none !important;
    }
    .reveal-p, .reveal-blur, .fade-in-slow, .delayed-reveal {
        transition: none !important;
        animation: none !important;
        opacity: 1 !important;
        transform: none !important;
        filter: none !important;
    }
}
'''

css += '\n' + new_css
with open(r'd:\birthday\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 3. Update JS
with open(r'd:\birthday\script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the old continueToLetterBtn logic because we want the new cinematic 500ms fade logic
js = js.replace('''
    const continueLetterBtn = document.getElementById('continue-to-letter-btn');
    if (continueLetterBtn) {
        continueLetterBtn.addEventListener('click', () => {
            const letterSection = document.getElementById('mr-husband-letter');
            if (letterSection) {
                letterSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    }
''', '')

new_js = '''
document.addEventListener("DOMContentLoaded", () => {
    // Cinematic Intersection Observer for reveal-p and reveal-blur
    const cinematicObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                
                // Poem climax logic
                if (entry.target.classList.contains('poem-climax-wrapper')) {
                    setTimeout(() => {
                        entry.target.classList.add('climax-active');
                        createTinyHearts(entry.target, false);
                    }, 500);
                }
                cinematicObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });

    document.querySelectorAll('.reveal-p, .reveal-blur').forEach(el => {
        cinematicObserver.observe(el);
    });

    // Continue to letter btn - cinematic transition
    const continueLetterBtn = document.getElementById('continue-to-letter-btn');
    const scrapbookSection = document.getElementById('scrapbook');
    if (continueLetterBtn) {
        continueLetterBtn.addEventListener('click', () => {
            if (scrapbookSection) {
                scrapbookSection.style.transition = 'opacity 0.5s ease';
                scrapbookSection.style.opacity = '0.1'; // darken
            }
            
            // Screen darkens for 500ms, then scrolls
            setTimeout(() => {
                const letterSection = document.getElementById('mr-husband-letter');
                if (letterSection) {
                    letterSection.scrollIntoView({ behavior: 'smooth' });
                }
                
                // Restore opacity after transition just in case user scrolls back
                setTimeout(() => {
                    if (scrapbookSection) scrapbookSection.style.opacity = '1';
                }, 1000);
            }, 500);
        });
    }

    // Read my heart btn -> Poem section
    const readHeartBtn = document.getElementById('read-heart-btn');
    if (readHeartBtn) {
        readHeartBtn.addEventListener('click', () => {
            document.getElementById('tumse-thoda-aur').scrollIntoView({ behavior: 'smooth' });
        });
    }

    // Poem climax tap interaction
    const poemClimax = document.querySelector('.poem-climax-wrapper');
    if (poemClimax) {
        poemClimax.addEventListener('click', () => {
            createTinyHearts(poemClimax, true);
            const heartGlow = poemClimax.querySelector('.climax-glow-heart');
            if (heartGlow) {
                heartGlow.style.opacity = '0.3';
                setTimeout(() => heartGlow.style.opacity = '1', 300);
            }
        });
    }

    function createTinyHearts(parent, interactive = false) {
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
        const num = interactive ? 6 : 10;
        for (let i = 0; i < num; i++) {
            const heart = document.createElement('div');
            heart.innerText = '❤️';
            heart.style.position = 'absolute';
            heart.style.fontSize = (10 + Math.random() * 8) + 'px';
            heart.style.left = (30 + Math.random() * 40) + '%';
            heart.style.top = '50%';
            heart.style.opacity = '0';
            heart.style.pointerEvents = 'none';
            heart.style.zIndex = '5';
            heart.style.animation = `burstUp 2s cubic-bezier(0.25, 1, 0.5, 1) forwards`;
            
            const tx = (Math.random() - 0.5) * 120 + 'px';
            const ty = - (60 + Math.random() * 120) + 'px';
            const rot = (Math.random() - 0.5) * 60 + 'deg';
            
            heart.style.setProperty('--tx', tx);
            heart.style.setProperty('--ty', ty);
            heart.style.setProperty('--rot', rot);
            
            parent.appendChild(heart);
            setTimeout(() => {
                if (heart.parentNode) heart.remove();
            }, 2000);
        }
    }
});
'''

js += '\n' + new_js
with open(r'd:\birthday\script.js', 'w', encoding='utf-8') as f:
    f.write(js)
    
print("CSS/JS updated")
