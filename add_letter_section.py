import re

with open(r'd:\birthday\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_section = '''
    <!-- Mr. Husband Letter Section -->
    <section id="mr-husband-letter" class="letter-section">
        <div class="letter-header scroll-anim fade-up">
            <h2 class="letter-title">For My Mr. Husband ❤️</h2>
            <p class="letter-subtitle">A little letter straight from my heart...</p>
        </div>

        <div class="letter-container scroll-anim fade-up">
            <div class="letter-card">
                <p>Hello my Mr. Husband ❤️</p>

                <p>Aaje khabar che ketlo special day che?<br>Mara birthday ni jetli excitement nathi hoti, aetli tara birthday ni hoy che… 💝</p>

                <p>Finally, today’s date — 16/10 🥳🥳🥳🥳<br>Mara ae person no birthday che, jene always mane support karyo che, always mari sathe j ryo che… 🫂<br>Always mane happy rakhvani j try kari che…<br>Mari life j tu cho, Jay. 🫂</p>

                <p>Tane khabar che, bija loko ne eni life ma problem aave to mummy, papa, bhai yaad aave…<br>Pan mari life ma kai pan problem aave, aetle pela tu yaad aav…<br>Because maru world 🌎 j tu cho…<br>Mara life ni last 7 minutes pan tu j cho, Jay… 🫂🫂🫂🫂</p>

                <p>Tari sathe life ni nani nani moments pan special bani jaay chhe.<br>Tari ek smile maru mood badli shake chhe, ane taro ek word — 'hu chu ne' — mane badhi problems ma strong feel karave chhe. ❤️</p>

                <p>Jay, mane life perfect nathi joie…<br>Mane bas badhi situation ma taro support joie che —<br>happiness hoy ke sadness,<br>success hoy ke struggle,<br>hu always tari sathe chu. 🥺❤️</p>

                <p>Jay, ek promise karu...<br>Life hamesha easy nathi hoy,<br>badha days perfect nathi hoy,<br>but ek vaat always same rehse —<br>hu tari sathe rahish. 🥹❤️</p>

                <p>Bas ek j wish chhe…<br>Jya sudhi life chhe,<br>tya sudhi tari sathe aa journey chhe. ❤️♾️</p>

                <p class="letter-highlight">My world is not perfect,<br>but because you are in it,<br>I find it the most beautiful. 🥺❤️</p>

                <p class="letter-highlight">Thank you for being my person,<br>my forever,<br>my husband,<br>my love,<br>my everything. 🎂❤️</p>

                <p>Thank you so much mari life ma aavi ne mari life ne complete banava mate. ❤️🥹<br>Thank you for always being there for me, my lifeline… ❤️🫶🏻</p>

                <p>Bas aaje aa special day par ae j pray karis ke Hari tane always happy and healthy rakhe… 🥰</p>

                <p class="letter-highlight">Happy Birthday to the man who makes my life more beautiful every single day. ❤️<br>I love you endlessly, Jayu ❤️♾️🫂🫂🫂🧿🧿</p>
                
                <div class="letter-signature">
                    <p>Forever yours ❤️</p>
                </div>
            </div>
            <!-- Decorative elements inside container -->
            <div class="letter-sparkle s1">✨</div>
            <div class="letter-sparkle s2">✨</div>
            <div class="letter-heart h1">❤️</div>
            <div class="letter-heart h2">❤️</div>
        </div>
    </section>
'''

html = html.replace('    </section>\n\n    <!-- Fullscreen Modal -->', '    </section>\n' + new_section + '\n    <!-- Fullscreen Modal -->')

with open(r'd:\birthday\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open(r'd:\birthday\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* Mr. Husband Letter Section */
.letter-section {
    padding: 80px 20px;
    background-color: #fdfaf8; /* warm cream / soft blush */
    background-image: radial-gradient(rgba(212, 106, 106, 0.1) 1.5px, transparent 1.5px);
    background-size: 30px 30px;
    position: relative;
    overflow: hidden;
}

.letter-header {
    text-align: center;
    margin-bottom: 40px;
}

.letter-title {
    font-family: 'Caveat', cursive;
    font-size: clamp(2.8rem, 9vw, 4rem);
    color: #d46a6a;
    margin-bottom: 8px;
    line-height: 1.1;
}

.letter-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 1.1rem;
    color: #8c7e73;
    font-style: italic;
}

.letter-container {
    max-width: 430px;
    width: min(92vw, 430px);
    margin: 0 auto;
    position: relative;
}

.letter-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 45px 25px 35px;
    box-shadow: 0 12px 35px rgba(212, 106, 106, 0.08);
    position: relative;
    z-index: 2;
}

.letter-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    border-radius: 16px;
    background-image: url('data:image/svg+xml;utf8,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><filter id="noise"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="4" stitchTiles="stitch"/></filter><rect width="100" height="100" filter="url(%23noise)" opacity="0.05"/></svg>');
    pointer-events: none;
    z-index: -1;
}

.letter-card p {
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    line-height: 1.7;
    color: #4a413d;
    margin-bottom: 22px;
}

.letter-highlight {
    text-align: center;
    font-family: 'Playfair Display', serif !important;
    font-size: 19px !important;
    color: #d46a6a !important;
    font-style: italic;
    margin: 35px 0 25px 0 !important;
    line-height: 1.5 !important;
}

.letter-signature {
    margin-top: 45px;
    text-align: right;
}

.letter-signature p {
    font-family: 'Caveat', cursive !important;
    font-size: 2.2rem !important;
    color: #d46a6a !important;
    margin: 0 !important;
}

.letter-sparkle, .letter-heart {
    position: absolute;
    z-index: 1;
    animation: floatAnim 4s ease-in-out infinite alternate;
}

.letter-sparkle.s1 { top: -20px; left: -10px; font-size: 26px; }
.letter-sparkle.s2 { bottom: 40px; right: -15px; font-size: 22px; animation-delay: 1s; }
.letter-heart.h1 { top: 35%; right: -25px; font-size: 32px; animation-delay: 0.5s; opacity: 0.8; }
.letter-heart.h2 { bottom: -15px; left: 5px; font-size: 28px; animation-delay: 1.5s; opacity: 0.8; }

@keyframes floatAnim {
    0% { transform: translateY(0) rotate(0deg); }
    100% { transform: translateY(-15px) rotate(8deg); }
}
'''

css += '\n' + new_css

with open(r'd:\birthday\style.css', 'w', encoding='utf-8') as f:
    f.write(css)
    
print("New section built successfully.")
