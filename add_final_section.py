import re

# 1. Update index.html
with open(r'd:\birthday\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_section_html = '''
    <!-- Final Surprise Section -->
    <section id="final-surprise" class="final-section">
        <!-- Background Effects -->
        <div class="final-stars"></div>
        <div id="final-particles" class="final-particles"></div>

        <div class="final-container">
            <div id="final-intro" class="final-step scroll-anim fade-up">
                <h2 class="final-heading">One Last Thing... ❤️</h2>
                <p class="final-sub">Before this little surprise ends,<br>there's something I still want to say...</p>
                <button id="final-tap-btn" class="glow-btn pulse-btn mt-4">Tap Here, Jayu ❤️</button>
            </div>
            
            <div id="final-message" class="final-step hidden">
                <div class="final-heart-reveal">
                    <svg class="pulsing-heart" viewBox="0 0 32 29.6">
                        <path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2
                        c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z" fill="none" stroke="#d46a6a" stroke-width="1.5"/>
                        <text x="50%" y="55%" dominant-baseline="middle" text-anchor="middle" class="heart-text">J + ❤️</text>
                    </svg>
                </div>
                <div class="final-lines">
                    <p class="f-line f-l1">Happy Birthday, Jayu ❤️</p>
                    <p class="f-line f-l2 mt-3">You are not just a part of my life...</p>
                    <p class="f-line f-l3 mt-3">You are my comfort,<br>my happiness,<br>my safe place,<br>and my favourite person. 🫂❤️</p>
                    <p class="f-line f-l4 mt-3">Thank you for every little moment,<br>every smile,<br>every 'hu chu ne',<br>and every time you stayed beside me.</p>
                    <p class="f-line f-l5 mt-3">I don't know what every tomorrow will look like...</p>
                    <p class="f-line f-l6 mt-3">But I know one thing —</p>
                    <p class="f-line f-l7 mt-3">I want you in all of them. ❤️♾️</p>
                    <p class="f-line f-l8 f-large mt-4">Happy Birthday to my Husband,<br>My Love,<br>My Everything. 🎂❤️</p>
                    <p class="f-line f-l9 f-huge mt-4">I Love You Endlessly, Jayu ❤️♾️</p>
                </div>
                
                <div class="final-footer f-line f-l10">
                    <p class="f-made-with">Made with all my love, just for you. ❤️</p>
                    <p class="f-date">16 October ✨</p>
                    <button id="replay-btn" class="replay-btn mt-4">Relive Our Memories ↟</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Fullscreen Modal -->'''

html = html.replace('    <!-- Fullscreen Modal -->', new_section_html)

with open(r'd:\birthday\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css
with open(r'd:\birthday\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_section_css = '''
/* ==========================================================================
   Final Surprise Section
   ========================================================================== */
.final-section {
    min-height: 100vh;
    background-color: #0b1021;
    background-image: radial-gradient(circle at center, #1a223f 0%, #0b1021 70%);
    position: relative;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 80px 20px;
    color: #fff;
    text-align: center;
}

.final-stars {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: 
        radial-gradient(1px 1px at 20px 30px, #ffffff, rgba(0,0,0,0)),
        radial-gradient(1px 1px at 40px 70px, #ffffff, rgba(0,0,0,0)),
        radial-gradient(1.5px 1.5px at 90px 40px, #ffffff, rgba(0,0,0,0));
    background-size: 150px 150px;
    opacity: 0.4;
    animation: twinkle 4s infinite alternate;
    pointer-events: none;
    z-index: 0;
}

.final-container {
    position: relative;
    z-index: 2;
    width: min(90vw, 410px);
    max-width: 100%;
}

.final-step {
    transition: opacity 0.8s ease, transform 0.8s ease;
}

.final-step.hidden {
    opacity: 0;
    visibility: hidden;
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%) scale(0.95);
    width: 100%;
}

.final-step.active {
    opacity: 1;
    visibility: visible;
    position: relative;
    top: auto; left: auto;
    transform: translate(0, 0) scale(1);
}

.final-heading {
    font-family: 'Playfair Display', serif;
    font-size: clamp(30px, 9vw, 46px);
    color: #fdfaf8;
    margin-bottom: 20px;
    text-shadow: 0 0 20px rgba(255,255,255,0.1);
}

.final-sub {
    font-family: 'Inter', sans-serif;
    font-size: 18px;
    line-height: 1.6;
    color: #d8d4d1;
    margin-bottom: 50px;
}

.pulse-btn {
    animation: softPulse 2.5s infinite;
    padding: 16px 36px;
    font-size: 18px;
    border-radius: 50px;
    min-height: 50px;
    box-shadow: 0 4px 15px rgba(212, 106, 106, 0.3);
}

@keyframes softPulse {
    0% { box-shadow: 0 0 0 0 rgba(212, 106, 106, 0.4); }
    70% { box-shadow: 0 0 0 15px rgba(212, 106, 106, 0); }
    100% { box-shadow: 0 0 0 0 rgba(212, 106, 106, 0); }
}

.final-heart-reveal {
    width: 100px;
    margin: 0 auto 30px;
    opacity: 0;
    transform: scale(0.8);
    transition: opacity 1s ease, transform 1s ease;
}

.final-heart-reveal.show {
    opacity: 1;
    transform: scale(1);
}

.pulsing-heart {
    width: 100%;
    overflow: visible;
    animation: gentlePulse 3.5s infinite ease-in-out;
}

.heart-text {
    font-family: 'Caveat', cursive;
    font-size: 9px;
    fill: #d46a6a;
}

@keyframes gentlePulse {
    0%, 100% { transform: scale(1); filter: drop-shadow(0 0 5px rgba(212, 106, 106, 0.2)); }
    50% { transform: scale(1.05); filter: drop-shadow(0 0 15px rgba(212, 106, 106, 0.5)); }
}

.final-lines p {
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    line-height: 1.65;
    color: #fdfaf8;
    opacity: 0;
    transform: translateY(15px);
    transition: opacity 0.8s ease, transform 0.8s ease;
}

.final-lines p.show {
    opacity: 1;
    transform: translateY(0);
}

.f-large {
    font-family: 'Playfair Display', serif !important;
    font-size: 22px !important;
    color: #f3a8a8 !important;
    font-style: italic;
    line-height: 1.4 !important;
}

.f-huge {
    font-family: 'Caveat', cursive !important;
    font-size: 34px !important;
    color: #d46a6a !important;
}

.final-footer {
    opacity: 0;
    transform: translateY(15px);
    transition: opacity 0.8s ease, transform 0.8s ease;
    margin-top: 60px;
}

.final-footer.show {
    opacity: 1;
    transform: translateY(0);
}

.f-made-with {
    font-family: 'Caveat', cursive;
    font-size: 22px;
    color: #d46a6a;
    margin-bottom: 5px;
}

.f-date {
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    color: #8c93a8;
    letter-spacing: 1px;
}

.replay-btn {
    background: transparent;
    border: 1px solid rgba(255,255,255,0.2);
    color: #fff;
    padding: 12px 24px;
    border-radius: 30px;
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.3s ease;
}
.replay-btn:hover {
    background: rgba(255,255,255,0.1);
    border-color: rgba(255,255,255,0.5);
}

.final-particles {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    pointer-events: none;
    z-index: 3;
    overflow: hidden;
}

.burst-part {
    position: absolute;
    bottom: -30px;
    font-size: 22px;
    opacity: 0;
    animation: burstUp 4s cubic-bezier(0.25, 1, 0.5, 1) forwards;
}

@keyframes burstUp {
    0% { transform: translate(0, 0) scale(0); opacity: 0; }
    10% { opacity: 1; transform: scale(1); }
    90% { opacity: 0.8; }
    100% { transform: translate(var(--tx), var(--ty)) scale(1.2) rotate(var(--rot)); opacity: 0; }
}

@media (prefers-reduced-motion: reduce) {
    .final-step, .final-heart-reveal, .final-lines p, .final-footer {
        transition: none !important;
    }
    .burst-part, .pulse-btn, .pulsing-heart, .final-stars {
        animation: none !important;
    }
}
'''
css += '\n' + new_section_css

with open(r'd:\birthday\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 3. Update script.js
with open(r'd:\birthday\script.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_section_js = '''
document.addEventListener("DOMContentLoaded", () => {
    // Final Surprise Logic
    const finalTapBtn = document.getElementById('final-tap-btn');
    const finalIntro = document.getElementById('final-intro');
    const finalMessage = document.getElementById('final-message');
    const heartReveal = document.querySelector('.final-heart-reveal');
    const finalLines = document.querySelectorAll('.f-line');
    const replayBtn = document.getElementById('replay-btn');
    const finalParticles = document.getElementById('final-particles');

    if (finalTapBtn) {
        finalTapBtn.addEventListener('click', () => {
            // Fade out intro
            finalIntro.classList.remove('is-visible');
            finalIntro.style.opacity = '0';
            finalIntro.style.transform = 'scale(0.95)';

            setTimeout(() => {
                finalIntro.style.display = 'none'; // Fully remove from layout flow
                
                finalMessage.classList.remove('hidden');
                // Force reflow
                void finalMessage.offsetWidth;
                finalMessage.classList.add('active');

                // Reveal heart at 400ms
                setTimeout(() => {
                    heartReveal.classList.add('show');
                }, 400);

                // Reveal text lines starting at 800ms
                let delay = 800;
                finalLines.forEach((line, index) => {
                    setTimeout(() => {
                        line.classList.add('show');
                        
                        // Fire particle burst when reaching the last text line (before footer)
                        if (index === finalLines.length - 2) {
                             setTimeout(createBurst, 1000);
                        }
                    }, delay);
                    // Dynamically space out the reveal
                    delay += (line.classList.contains('f-large') || line.classList.contains('f-huge')) ? 1000 : 700;
                });
            }, 800);
        });
    }

    if (replayBtn) {
        replayBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    function createBurst() {
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
        
        const emojis = ['❤️', '✨', '🌷', '💗'];
        const numParticles = 18;
        
        for (let i = 0; i < numParticles; i++) {
            const p = document.createElement('div');
            p.classList.add('burst-part');
            p.innerText = emojis[Math.floor(Math.random() * emojis.length)];
            
            // Randomize position across width
            const startX = 10 + Math.random() * 80; // 10vw to 90vw
            p.style.left = startX + 'vw';
            
            // Randomize trajectory
            const tx = (Math.random() - 0.5) * 200 + 'px';
            const ty = - (300 + Math.random() * 400) + 'px';
            const rot = (Math.random() - 0.5) * 180 + 'deg';
            
            p.style.setProperty('--tx', tx);
            p.style.setProperty('--ty', ty);
            p.style.setProperty('--rot', rot);
            
            finalParticles.appendChild(p);
            
            // Cleanup
            setTimeout(() => {
                if (p.parentNode) p.remove();
            }, 4000);
        }
    }
});
'''
js += '\n' + new_section_js

with open(r'd:\birthday\script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Final Surprise section created successfully.")
