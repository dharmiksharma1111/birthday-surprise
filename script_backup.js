document.addEventListener("DOMContentLoaded", () => {
    console.log("Birthday cinematic intro initialized.");

    // Add progressive enhancement class to body
    document.body.classList.add('js-enabled');

    initIntro();
    initMusic();
    initFloatElements();
    initPhotoGallery();
    initDiary();
    initLetterAnimations();
    initPoemReveal();
    initFinalSurprise();
    
    // --- 1. Intro Logic ---
    function initIntro() {
        const openBtn = document.getElementById('open-surprise-btn');
        const introContent = document.querySelector('.intro-content');
        const mainSection = document.getElementById('birthday-main');
        const bgMusic = document.getElementById("bgMusic");

        if (openBtn) {
            openBtn.addEventListener('click', async () => {
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

                // Handle Transitions
                if (introContent) {
                    introContent.classList.add('intro-leaving');
                }
                document.body.classList.remove('no-scroll');
                
                setTimeout(() => {
                    if (mainSection) {
                        mainSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    }
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
                    this.speedX = Math.random() * 0.4 - 0.2;
                    this.speedY = Math.random() * 0.4 - 0.2;
                    this.opacity = Math.random() * 0.5 + 0.1;
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
                const numParticles = Math.min(Math.floor(window.innerWidth / 15), 100); 
                for (let i = 0; i < numParticles; i++) { particles.push(new Particle()); }
            }
            function animateParticles() {
                ctx.clearRect(0, 0, width, height);
                particles.forEach(p => { p.update(); p.draw(); });
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
            setInterval(createFloatingElement, 2500);
        }
    }

    // --- 4. Photo Gallery & Modal ---
    function initPhotoGallery() {
        // Polaroid Base Rotations
        document.querySelectorAll('.polaroid').forEach(pol => {
            const rot = (Math.random() * 10 - 5) + 'deg';
            pol.style.transform = `rotate(${rot}) translateY(0)`;
            pol.style.setProperty('--base-rot', rot);
        });

        // Photo Modal Logic
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
                    currentImgIndex = index;
                    modalImg.src = img.src;
                    modal.classList.remove('modal-hidden');
                    document.body.classList.add('no-scroll');
                });
            });

            if (closeModal) {
                closeModal.addEventListener('click', () => {
                    modal.classList.add('modal-hidden');
                    document.body.classList.remove('no-scroll');
                });
            }

            if (prevNav) {
                prevNav.addEventListener('click', () => {
                    currentImgIndex = (currentImgIndex - 1 + galleryArray.length) % galleryArray.length;
                    modalImg.src = galleryArray[currentImgIndex].src;
                });
            }
            if (nextNav) {
                nextNav.addEventListener('click', () => {
                    currentImgIndex = (currentImgIndex + 1) % galleryArray.length;
                    modalImg.src = galleryArray[currentImgIndex].src;
                });
            }

            modal.addEventListener('click', (e) => {
                if (e.target === modal || e.target === document.querySelector('.modal-image-container')) {
                    modal.classList.add('modal-hidden');
                    document.body.classList.remove('no-scroll');
                }
            });

            // Touch Swipe Logic for Modal
            let touchStartX = 0;
            let touchEndX = 0;
            modal.addEventListener('touchstart', e => {
                touchStartX = e.changedTouches[0].screenX;
            }, {passive: true});
            modal.addEventListener('touchend', e => {
                touchEndX = e.changedTouches[0].screenX;
                if (touchStartX - touchEndX > 50) { // swipe left (next)
                    if (nextNav) nextNav.click();
                } else if (touchEndX - touchStartX > 50) { // swipe right (prev)
                    if (prevNav) prevNav.click();
                }
            }, {passive: true});
        }
    }

    // --- 5. Scrapbook Pagination ---
    function initDiary() {
        let currentPage = 1;
        const totalPages = 2; // Fixed to exactly 2 pages as requested
        const pages = document.querySelectorAll('.sb-page');
        const prevSbBtn = document.querySelector('.prev-sb-btn');
        const nextSbBtn = document.querySelector('.next-sb-btn');
        const sbIndicator = document.querySelector('.sb-indicator-text');
        const scrapbookContainer = document.querySelector('.scrapbook-wrapper');

        function updateScrapbook() {
            pages.forEach(page => {
                const pageNum = parseInt(page.getAttribute('data-page'));
                if (pageNum === currentPage) {
                    page.style.display = 'block';
                    setTimeout(() => page.style.opacity = '1', 50);
                } else {
                    page.style.opacity = '0';
                    setTimeout(() => page.style.display = 'none', 300);
                }
            });

            if (sbIndicator) sbIndicator.innerText = `${currentPage} / ${totalPages}`;
            
            if (prevSbBtn) {
                if (currentPage === 1) prevSbBtn.style.opacity = '0.5';
                else prevSbBtn.style.opacity = '1';
            }
            if (nextSbBtn) {
                if (currentPage === totalPages) nextSbBtn.style.opacity = '0.5';
                else nextSbBtn.style.opacity = '1';
            }
        }

        if (prevSbBtn && nextSbBtn) {
            prevSbBtn.addEventListener('click', () => {
                if (currentPage > 1) {
                    currentPage--;
                    updateScrapbook();
                }
            });
            nextSbBtn.addEventListener('click', () => {
                if (currentPage < totalPages) {
                    currentPage++;
                    updateScrapbook();
                }
            });
            updateScrapbook(); // Init on load
        }

        // Swipe logic for Diary
        if (scrapbookContainer) {
            let touchStartX = 0;
            let touchEndX = 0;
            scrapbookContainer.addEventListener('touchstart', e => {
                touchStartX = e.changedTouches[0].screenX;
            }, {passive: true});
            scrapbookContainer.addEventListener('touchend', e => {
                touchEndX = e.changedTouches[0].screenX;
                if (touchStartX - touchEndX > 50 && currentPage < totalPages) { // swipe left (next)
                    if (nextSbBtn) nextSbBtn.click();
                } else if (touchEndX - touchStartX > 50 && currentPage > 1) { // swipe right (prev)
                    if (prevSbBtn) prevSbBtn.click();
                }
            }, {passive: true});
        }
    }

    // --- 6. Letter Animations ---
    function initLetterAnimations() {
        const cinematicObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
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

        document.querySelectorAll('.reveal-p, .scroll-anim, .fade-up, .scale-in, .reveal-blur, .poem-reveal-line').forEach(el => {
            cinematicObserver.observe(el);
        });

        const continueLetterBtn = document.getElementById('continue-to-letter-btn');
        const scrapbookSection = document.getElementById('scrapbook');
        if (continueLetterBtn) {
            continueLetterBtn.addEventListener('click', () => {
                if (scrapbookSection) {
                    scrapbookSection.style.transition = 'opacity 0.5s ease';
                    scrapbookSection.style.opacity = '0.3'; 
                }
                setTimeout(() => {
                    const letterSection = document.getElementById('mr-husband-letter');
                    if (letterSection) letterSection.scrollIntoView({ behavior: 'smooth' });
                    setTimeout(() => {
                        if (scrapbookSection) scrapbookSection.style.opacity = '1';
                    }, 1000);
                }, 300);
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

                readHeartBtn.style.transform = 'scale(0.95)';
                setTimeout(() => readHeartBtn.style.transform = 'scale(1)', 150);

                const overlay = document.createElement('div');
                overlay.style.position = 'fixed';
                overlay.style.top = '0';
                overlay.style.left = '0';
                overlay.style.width = '100%';
                overlay.style.height = '100%';
                overlay.style.backgroundColor = 'rgba(0,0,0,0.5)';
                overlay.style.zIndex = '9999';
                overlay.style.pointerEvents = 'none';
                overlay.style.transition = 'opacity 0.6s ease';
                document.body.appendChild(overlay);

                setTimeout(() => { overlay.style.opacity = '0'; }, 600);
                setTimeout(() => { overlay.remove(); }, 1200);

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
                            
                            if (index === lines.length - 1) {
                                const climaxWrapper = line.closest('.poem-climax-wrapper');
                                if (climaxWrapper) {
                                    climaxWrapper.classList.add('climax-active');
                                    createTinyHearts(climaxWrapper, false);
                                    
                                    const spot = poemSection.querySelector('.poem-spotlight');
                                    if (spot) {
                                        spot.style.background = 'radial-gradient(circle at 50% 50%, rgba(200, 100, 120, 0.18), transparent 60%)';
                                        spot.style.transition = 'background 2s ease';
                                    }
                                }
                            }
                        }, delay);
                    });
                }, 300);
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
                finalTapBtn.style.transform = 'scale(0.9)';
                
                setTimeout(() => {
                    if (finalIntro) {
                        finalIntro.style.opacity = '0';
                        setTimeout(() => finalIntro.classList.add('final-hidden'), 500);
                    }

                    setTimeout(() => {
                        finalMessage.classList.remove('final-hidden');
                        const finalParticles = document.getElementById('final-particles');
                        if (finalParticles) {
                            for(let i=0; i<30; i++) {
                                let p = document.createElement('div');
                                p.classList.add('burst-part');
                                p.style.left = '50%';
                                p.style.top = '50%';
                                p.style.setProperty('--tx', (Math.random() - 0.5) * 200 + 'px');
                                p.style.setProperty('--ty', (Math.random() - 0.5) * 200 + 'px');
                                finalParticles.appendChild(p);
                            }
                        }

                        finalLines.forEach((line, idx) => {
                            setTimeout(() => {
                                line.classList.add('revealed');
                            }, 500 + (idx * 1500));
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

    // --- Helper for Hearts ---
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
