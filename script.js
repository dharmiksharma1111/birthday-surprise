document.addEventListener("DOMContentLoaded", () => {
    console.log("Birthday cinematic intro initialized.");

    // Add progressive enhancement class to body
    document.body.classList.add('js-enabled');

    // --- ADVANCED FX INJECTION ---
    const addFx = (selector, classes) => {
        document.querySelectorAll(selector).forEach(el => {
            el.classList.add(...classes.split(' '));
        });
    };
    addFx('.intro-age', 'fx-intro-age fx-ready');
    addFx('.happy-bday', 'fx-hb-text fx-ready');
    addFx('.boyfriend-name', 'fx-hb-text fx-ready');
    addFx('.collage-photo', 'fx-heart-photo fx-ready');
    addFx('.film-strip-container', 'fx-film-strip fx-ready');
    addFx('.film-track', 'fx-film-track fx-ready');
    addFx('.polaroid', 'fx-polaroid fx-ready');
    addFx('#memories', 'fx-paper-transition fx-ready');
    addFx('.scrapbook-wrapper', 'fx-diary fx-ready');
    addFx('.letter-card', 'fx-letter-card fx-ready');
    addFx('.letter-card p', 'fx-letter-p fx-ready');
    addFx('.poem-line', 'fx-poem-line fx-ready');
    addFx('.climax-line', 'fx-climax-text fx-ready');
    addFx('#final-surprise', 'fx-final-bg-move');

    // Advanced FX Observer
    const fxObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                if (entry.target.classList.contains('fx-heart-photo')) {
                    const idx = Array.from(document.querySelectorAll('.fx-heart-photo')).indexOf(entry.target);
                    setTimeout(() => {
                        entry.target.classList.add('fx-revealed');
                        if (idx === 6) { // 7 photos total
                            setTimeout(() => {
                                document.querySelector('.heart-collage').classList.add('fx-collage-heartbeat');
                            }, 800);
                        }
                    }, idx * 100);
                } else if (entry.target.classList.contains('fx-polaroid')) {
                    const idx = Array.from(document.querySelectorAll('.fx-polaroid')).indexOf(entry.target);
                    setTimeout(() => entry.target.classList.add('fx-revealed'), (idx % 3) * 150);
                } else if (entry.target.classList.contains('fx-hb-text')) {
                    const idx = Array.from(document.querySelectorAll('.fx-hb-text')).indexOf(entry.target);
                    setTimeout(() => entry.target.classList.add('fx-revealed'), idx * 150);
                } else if (entry.target.classList.contains('fx-film-strip')) {
                    entry.target.classList.add('fx-revealed');
                    setTimeout(() => document.querySelector('.film-track')?.classList.add('fx-revealed'), 100);
                    setTimeout(() => document.querySelector('.film-strip')?.classList.add('fx-film-flash'), 900);
                } else {
                    entry.target.classList.add('fx-revealed');
                }
                fxObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });

    document.querySelectorAll('.fx-ready').forEach(el => fxObserver.observe(el));


    initIntro();
    initMusic();
    initFloatElements();
    initPhotoGallery();
    initDiary();
    initLetterAnimations();
    initPoemReveal();
    initFinalSurprise();
    initParallax();
    
    // --- 1. Intro Logic ---
    function initIntro() {
        const openBtn = document.getElementById('open-surprise-btn');
        const introContent = document.querySelector('.intro-content');
        const mainSection = document.getElementById('birthday-main');
        const bgMusic = document.getElementById("bgMusic");

        if (openBtn) {
            openBtn.addEventListener('click', async () => {
                // Intro Button Animation
                openBtn.classList.add('fx-ripple-active');
                const ripple = document.createElement('div');
                ripple.className = 'fx-btn-ripple';
                ripple.style.width = '100px'; ripple.style.height = '100px';
                ripple.style.left = '50%'; ripple.style.top = '50%';
                ripple.style.transformOrigin = 'center';
                ripple.style.marginLeft = '-50px'; ripple.style.marginTop = '-50px';
                openBtn.appendChild(ripple);
                setTimeout(() => ripple.remove(), 600);

                // Handle Music
                if (bgMusic && bgMusic.paused) {
                    try {
                        bgMusic.volume = 0;
                        await bgMusic.play();
                        
                        const targetVolume = 0.55;
                        const step = 0.03;
                        const fade = setInterval(() => {
                            if (bgMusic.volume < targetVolume - step) {
                                bgMusic.volume += step;
                            } else {
                                bgMusic.volume = targetVolume;
                                clearInterval(fade);
                            }
                        }, 80);
                    } catch (error) {
                        console.log("Music playback could not start:", error);
                    }
                }

                // Cream Reveal Transition
                const creamLayer = document.createElement('div');
                creamLayer.className = 'fx-cream-reveal-layer';
                document.body.appendChild(creamLayer);
                
                setTimeout(() => creamLayer.classList.add('fx-expand'), 50);

                // Handle Transitions
                if (introContent) {
                    introContent.classList.add('intro-leaving');
                }
                document.body.classList.remove('no-scroll');
                
                setTimeout(() => {
                    if (mainSection) {
                        mainSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    }
                    setTimeout(() => {
                        creamLayer.style.opacity = '0';
                        setTimeout(() => creamLayer.remove(), 1000);
                    }, 800);
                }, 500);

                setTimeout(() => {
                    if (introContent) introContent.classList.remove('intro-leaving');
                }, 1200);
            });
        }

        // Restore intro when scrolled to top
        window.addEventListener('scroll', () => {
            if (window.scrollY < window.innerHeight * 0.65 && introContent) {
                introContent.classList.remove('intro-leaving');
            }
        }, { passive: true });

        // Intro Particles Canvas
        const canvas = document.getElementById('particle-canvas');
        if (canvas) {
            const ctx = canvas.getContext('2d');
            let width, height;
            let particles = [];
            
            function initCanvas() {
                width = canvas.width = window.innerWidth;
                height = canvas.height = window.innerHeight;
            }
            window.addEventListener('resize', initCanvas);
            initCanvas();
            
            class Particle {
                constructor() {
                    this.x = Math.random() * width;
                    this.y = Math.random() * height;
                    this.size = Math.random() * 1.5;
                    this.speedX = Math.random() * 0.2 - 0.1;
                    this.speedY = Math.random() * 0.2 - 0.1;
                    this.opacity = Math.random() * 0.5 + 0.1;
                    this.layer = Math.floor(Math.random() * 3); // 0, 1, 2 for depth
                    if (this.layer === 2) { this.speedX *= 2; this.speedY *= 2; this.size *= 1.5; }
                    if (this.layer === 0) { this.speedX *= 0.5; this.speedY *= 0.5; this.opacity *= 0.5; }
                }
                update() {
                    this.x += this.speedX;
                    this.y += this.speedY;
                    if (this.x < 0) this.x = width;
                    if (this.x > width) this.x = 0;
                    if (this.y < 0) this.y = height;
                    if (this.y > height) this.y = 0;
                }
                draw() {
                    ctx.fillStyle = `rgba(255, 255, 255, ${this.opacity})`;
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctx.fill();
                }
            }
            function createParticles() {
                particles = [];
                const numParticles = Math.min(Math.floor(window.innerWidth / 20), 50); // Reduced for mobile
                for (let i = 0; i < numParticles; i++) { particles.push(new Particle()); }
            }
            function animateParticles() {
                if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
                    ctx.clearRect(0, 0, width, height);
                    particles.forEach(p => { p.update(); p.draw(); });
                }
                requestAnimationFrame(animateParticles);
            }
            createParticles();
            animateParticles();
        }
    }

    // --- 2. Music Toggle ---
    function initMusic() {
        const musicBtn = document.getElementById('music-btn');
        const bgMusic = document.getElementById("bgMusic");

        if (musicBtn && bgMusic) {
            musicBtn.addEventListener('click', () => {
                if (bgMusic.paused) {
                    bgMusic.play();
                    musicBtn.style.opacity = '1';
                } else {
                    bgMusic.pause();
                    musicBtn.style.opacity = '0.6';
                }
            });
        }
    }

    // --- 3. Float Elements in Intro ---
    function initFloatElements() {
        const introContainer = document.querySelector('.intro-content');
        if (introContainer) {
            function createFloatingElement() {
                if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
                const el = document.createElement('div');
                el.classList.add('floating-element');
                const types = ['❤️', '🎈', '✨'];
                el.innerText = types[Math.floor(Math.random() * types.length)];
                el.style.left = Math.random() * 100 + 'vw';
                const durations = 10 + Math.random() * 10;
                el.style.animationDuration = `${durations}s`;
                el.style.fontSize = (15 + Math.random() * 15) + 'px';
                introContainer.appendChild(el);
                setTimeout(() => { if (el.parentNode) el.remove(); }, durations * 1000);
            }
            setInterval(createFloatingElement, 3500);
        }
    }

    // --- 4. Photo Gallery & Modal ---
    function initPhotoGallery() {
        document.querySelectorAll('.polaroid').forEach(pol => {
            const rot = (Math.random() * 10 - 5) + 'deg';
            pol.style.transform = `rotate(${rot}) translateY(0)`;
            pol.style.setProperty('--base-rot', rot);
        });

        const modal = document.getElementById('photo-modal');
        const modalImg = document.getElementById('modal-img');
        const closeModal = document.querySelector('.close-modal');
        const galleryImgs = document.querySelectorAll('.gallery-img');
        const prevNav = document.querySelector('.prev-nav');
        const nextNav = document.querySelector('.next-nav');
        let currentImgIndex = 0;
        const galleryArray = Array.from(galleryImgs);

        if (modal && modalImg) {
            galleryArray.forEach((img, index) => {
                img.addEventListener('click', () => {
                    // Mobile Touch Depth Animation
                    img.classList.add('fx-touch-scale');
                    setTimeout(() => {
                        img.classList.remove('fx-touch-scale');
                        currentImgIndex = index;
                        modalImg.src = img.src;
                        modal.classList.remove('modal-hidden');
                        document.body.classList.add('no-scroll');
                    }, 120);
                });
            });

            if (closeModal) closeModal.addEventListener('click', () => { modal.classList.add('modal-hidden'); document.body.classList.remove('no-scroll'); });
            if (prevNav) prevNav.addEventListener('click', () => { currentImgIndex = (currentImgIndex - 1 + galleryArray.length) % galleryArray.length; modalImg.src = galleryArray[currentImgIndex].src; });
            if (nextNav) nextNav.addEventListener('click', () => { currentImgIndex = (currentImgIndex + 1) % galleryArray.length; modalImg.src = galleryArray[currentImgIndex].src; });

            modal.addEventListener('click', (e) => {
                if (e.target === modal || e.target === document.querySelector('.modal-image-container')) {
                    modal.classList.add('modal-hidden');
                    document.body.classList.remove('no-scroll');
                }
            });

            let touchStartX = 0, touchEndX = 0;
            modal.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].screenX; }, {passive: true});
            modal.addEventListener('touchend', e => {
                touchEndX = e.changedTouches[0].screenX;
                if (touchStartX - touchEndX > 50) { if (nextNav) nextNav.click(); }
                else if (touchEndX - touchStartX > 50) { if (prevNav) prevNav.click(); }
            }, {passive: true});
        }
    }

    // --- 5. Scrapbook Pagination & 3D Turn ---
    function initDiary() {
        let currentPage = 1;
        const totalPages = 2; 
        const pages = document.querySelectorAll('.sb-page');
        const prevSbBtn = document.querySelector('.prev-sb-btn');
        const nextSbBtn = document.querySelector('.next-sb-btn');
        const sbIndicator = document.querySelector('.sb-indicator-text');
        const scrapbookContainer = document.querySelector('.scrapbook-wrapper');
        
        // Add diary glow
        const glow = document.createElement('div');
        glow.className = 'fx-diary-glow';
        scrapbookContainer?.appendChild(glow);

        function updateScrapbook(direction) {
            pages.forEach(page => {
                const pageNum = parseInt(page.getAttribute('data-page'));
                if (pageNum === currentPage) {
                    page.style.display = 'block';
                    if (direction === 'next') {
                        page.classList.add('fx-page-turn-in');
                        setTimeout(() => {
                            page.classList.remove('fx-page-turn-in');
                            page.classList.add('fx-page-active');
                        }, 50);
                    } else if (direction === 'prev') {
                        page.classList.add('fx-page-turn-out');
                        setTimeout(() => {
                            page.classList.remove('fx-page-turn-out');
                            page.classList.add('fx-page-active');
                        }, 50);
                    } else {
                        page.style.opacity = '1';
                    }
                } else {
                    if (direction === 'next') {
                        page.classList.remove('fx-page-active');
                        page.classList.add('fx-page-turn-out');
                    } else if (direction === 'prev') {
                        page.classList.remove('fx-page-active');
                        page.classList.add('fx-page-turn-in');
                    } else {
                        page.style.opacity = '0';
                    }
                    setTimeout(() => {
                        page.style.display = 'none';
                        page.classList.remove('fx-page-turn-in', 'fx-page-turn-out', 'fx-page-active');
                    }, 600);
                }
            });

            if (sbIndicator) sbIndicator.innerText = `${currentPage} / ${totalPages}`;
            if (prevSbBtn) prevSbBtn.style.opacity = currentPage === 1 ? '0.5' : '1';
            if (nextSbBtn) nextSbBtn.style.opacity = currentPage === totalPages ? '0.5' : '1';
        }

        if (prevSbBtn && nextSbBtn) {
            prevSbBtn.addEventListener('click', () => { if (currentPage > 1) { currentPage--; updateScrapbook('prev'); } });
            nextSbBtn.addEventListener('click', () => { if (currentPage < totalPages) { currentPage++; updateScrapbook('next'); } });
            updateScrapbook('none');
        }

        if (scrapbookContainer) {
            let touchStartX = 0, touchEndX = 0;
            scrapbookContainer.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].screenX; }, {passive: true});
            scrapbookContainer.addEventListener('touchend', e => {
                touchEndX = e.changedTouches[0].screenX;
                if (touchStartX - touchEndX > 50 && currentPage < totalPages) { if (nextSbBtn) nextSbBtn.click(); }
                else if (touchEndX - touchStartX > 50 && currentPage > 1) { if (prevSbBtn) prevSbBtn.click(); }
            }, {passive: true});
        }
    }

    // --- 6. Letter Animations ---
    function initLetterAnimations() {
        const cinematicObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                    cinematicObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });

        // Maintain old visibility recovery
        document.querySelectorAll('.reveal-p, .scroll-anim, .fade-up, .scale-in, .reveal-blur, .poem-reveal-line').forEach(el => {
            cinematicObserver.observe(el);
        });
        
        // Add rose spotlight
        const letterSection = document.getElementById('mr-husband-letter');
        if (letterSection) {
            const spot = document.createElement('div');
            spot.className = 'fx-rose-spotlight';
            letterSection.appendChild(spot);
        }

        const continueLetterBtn = document.getElementById('continue-to-letter-btn');
        const scrapbookSection = document.getElementById('scrapbook');
        if (continueLetterBtn) {
            continueLetterBtn.addEventListener('click', () => {
                // Sequenced Diary Continue Transition
                continueLetterBtn.classList.add('fx-ripple-active');
                if (scrapbookSection) {
                    scrapbookSection.style.transition = 'opacity 0.7s ease, filter 0.7s ease';
                    scrapbookSection.style.opacity = '0.3'; 
                    scrapbookSection.style.filter = 'brightness(0.5)';
                }
                
                const heartGlow = document.createElement('div');
                heartGlow.innerText = '❤️';
                heartGlow.style.position = 'fixed'; heartGlow.style.top = '50%'; heartGlow.style.left = '50%';
                heartGlow.style.transform = 'translate(-50%, -50%) scale(0)';
                heartGlow.style.fontSize = '50px'; heartGlow.style.transition = 'transform 0.5s ease, opacity 0.5s ease';
                heartGlow.style.zIndex = '9999';
                document.body.appendChild(heartGlow);
                
                setTimeout(() => heartGlow.style.transform = 'translate(-50%, -50%) scale(1)', 100);

                setTimeout(() => {
                    if (letterSection) letterSection.scrollIntoView({ behavior: 'smooth' });
                    heartGlow.style.opacity = '0';
                    setTimeout(() => heartGlow.remove(), 500);
                    setTimeout(() => {
                        if (scrapbookSection) {
                            scrapbookSection.style.opacity = '1';
                            scrapbookSection.style.filter = 'none';
                        }
                    }, 1000);
                }, 700);
            });
        }
    }

    // --- 7. Poem Reveal ---
    function initPoemReveal() {
        const readHeartBtn = document.getElementById('read-heart-btn');
        const poemSection = document.getElementById('tumse-thoda-aur');
        let poemUnlocked = false;

        if (readHeartBtn && poemSection) {
            readHeartBtn.addEventListener('click', () => {
                if (poemUnlocked) return;
                poemUnlocked = true;

                
                readHeartBtn.classList.add('fx-ripple-active');
                const ripple = document.createElement('div');
                ripple.className = 'fx-btn-ripple';
                ripple.style.width = '100px'; ripple.style.height = '100px';
                ripple.style.left = '50%'; ripple.style.top = '50%';
                ripple.style.transformOrigin = 'center';
                ripple.style.marginLeft = '-50px'; ripple.style.marginTop = '-50px';
                readHeartBtn.appendChild(ripple);
                setTimeout(() => ripple.remove(), 600);

                setTimeout(() => readHeartBtn.style.transform = 'scale(1)', 150);

                const overlay = document.createElement('div');
                overlay.style.position = 'fixed'; overlay.style.top = '0'; overlay.style.left = '0';
                overlay.style.width = '100%'; overlay.style.height = '100%';
                overlay.style.backgroundColor = 'rgba(0,0,0,0.5)';
                overlay.style.zIndex = '9999'; overlay.style.pointerEvents = 'none';
                overlay.style.transition = 'opacity 0.6s ease';
                document.body.appendChild(overlay);

                setTimeout(() => overlay.style.opacity = '0', 600);
                setTimeout(() => overlay.remove(), 1200);

                poemSection.classList.remove('poem-locked');
                poemSection.classList.add('poem-unlocked');

                readHeartBtn.innerHTML = 'Opened With Love ❤️';
                readHeartBtn.style.opacity = '0.6';
                readHeartBtn.style.pointerEvents = 'none';

                setTimeout(() => {
                    poemSection.scrollIntoView({ behavior: 'smooth', block: 'start' });

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
                            
                            // Emotional Heartbeat for specific text
                            if (line.innerText.includes('hu tari sathe rahish')) {
                                document.querySelector('.fx-rose-spotlight')?.classList.add('fx-emotional-pulse');
                            }
                            
                            if (index === lines.length - 1) {
                                // Final Poem Line Climax
                                const climaxWrapper = line.closest('.poem-climax-wrapper');
                                if (climaxWrapper) {
                                    climaxWrapper.classList.add('climax-active');
                                    document.body.classList.add('fx-climax-darken');
                                    
                                    const heartLight = document.createElement('div');
                                    heartLight.className = 'fx-climax-heart-light';
                                    climaxWrapper.appendChild(heartLight);
                                    setTimeout(() => heartLight.classList.add('fx-active'), 50);
                                    
                                    for(let i=0; i<8; i++) {
                                        const h = document.createElement('div');
                                        h.className = 'fx-tiny-heart-rise';
                                        h.innerText = '❤️';
                                        h.style.left = (30 + Math.random()*40) + '%';
                                        h.style.animationDelay = (Math.random() * 0.5) + 's';
                                        climaxWrapper.appendChild(h);
                                    }
                                }
                            }
                        }, delay);
                    });
                }, 300);
            });
        }
    }

    // --- 8. Final Surprise ---
    function initFinalSurprise() {
        const finalTapBtn = document.getElementById('final-tap-btn');
        const finalIntro = document.getElementById('final-intro');
        const finalMessage = document.getElementById('final-message');
        const finalLines = document.querySelectorAll('.f-line');
        const replayBtn = document.getElementById('replay-btn');

        if (finalTapBtn && finalMessage) {
            finalTapBtn.addEventListener('click', () => {
                // Button tap animation
                finalTapBtn.classList.add('fx-ripple-active');
                const ripple = document.createElement('div');
                ripple.className = 'fx-btn-ripple';
                ripple.style.width = '100px'; ripple.style.height = '100px';
                ripple.style.left = '50%'; ripple.style.top = '50%';
                ripple.style.transformOrigin = 'center';
                ripple.style.marginLeft = '-50px'; ripple.style.marginTop = '-50px';
                finalTapBtn.appendChild(ripple);
                
                setTimeout(() => {
                    if (finalIntro) {
                        finalIntro.classList.add('fx-final-btn-tapped'); // This fades out the intro
                    }
                    // Darken screen
                    document.body.classList.add('fx-final-screen-darken');

                    setTimeout(() => {
                        finalMessage.classList.remove('final-hidden');
                        const finalParticles = document.getElementById('final-particles');
                        if (finalParticles) {
                            for(let i=0; i<15; i++) { // Restrained burst
                                let p = document.createElement('div');
                                p.className = 'fx-restrained-burst';
                                p.style.left = '50%';
                                p.style.top = '50%';
                                p.style.setProperty('--tx', (Math.random() - 0.5) * 150 + 'px');
                                p.style.setProperty('--ty', (Math.random() - 0.5) * 150 + 'px');
                                finalParticles.appendChild(p);
                            }
                        }

                        finalLines.forEach((line, idx) => {
                            setTimeout(() => {
                                line.classList.add('revealed');
                                
                                // Special Moment Reveal
                                if (line.classList.contains('final-special-line')) {
                                    const glow = line.parentElement.querySelector('.final-special-glow');
                                    if (glow) glow.classList.add('fx-active');
                                    line.classList.add('fx-shimmer-active');
                                    
                                    for(let i=0; i<8; i++) {
                                        const h = document.createElement('div');
                                        h.className = 'fx-tiny-heart-rise';
                                        h.innerText = '❤️';
                                        h.style.left = (30 + Math.random()*40) + '%';
                                        h.style.animationDelay = (Math.random() * 0.5) + 's';
                                        line.parentElement.appendChild(h);
                                    }
                                }
                            }, 500 + (idx * 2000));
                        });
                    }, 600);
                }, 300);
            });
        }

        if (replayBtn) {
            replayBtn.addEventListener('click', () => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }
    }
    
    // --- 9. Parallax ---
    function initParallax() {
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
        
        const memories = document.getElementById('memories');
        if (!memories) return;
        
        // Desktop mouse parallax
        memories.addEventListener('mousemove', (e) => {
            if (window.innerWidth <= 768) return; // Disable on mobile
            const x = (e.clientX / window.innerWidth - 0.5) * 12; // max 6px
            const y = (e.clientY / window.innerHeight - 0.5) * 12; // max 6px
            const polaroids = document.querySelectorAll('.polaroid');
            polaroids.forEach(p => {
                const rot = p.style.getPropertyValue('--base-rot') || '0deg';
                p.style.transform = `translate(${x}px, ${y}px) rotate(${rot})`;
            });
        });
        
        // Mobile autonomous drift
        let driftPhase = 0;
        let lastScrollY = window.scrollY;
        let isScrolling = false;
        
        window.addEventListener('scroll', () => {
            isScrolling = true;
            lastScrollY = window.scrollY;
        }, {passive: true});
        
        setInterval(() => {
            if (Math.abs(window.scrollY - lastScrollY) < 5) isScrolling = false;
            lastScrollY = window.scrollY;
        }, 100);
        
        function drift() {
            if (!isScrolling && window.innerWidth <= 768) {
                driftPhase += 0.01;
                const y = Math.sin(driftPhase) * 3; // max 3px
                const polaroids = document.querySelectorAll('.polaroid');
                polaroids.forEach((p, idx) => {
                    const rot = p.style.getPropertyValue('--base-rot') || '0deg';
                    const offset = (idx % 2 === 0) ? y : -y;
                    p.style.transform = `translate(0, ${offset}px) rotate(${rot})`;
                });
            }
            requestAnimationFrame(drift);
        }
        drift();
    }
});
