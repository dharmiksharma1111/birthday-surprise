
document.addEventListener("DOMContentLoaded", () => {

    // --- 1. Float Elements in Intro ---
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

    // --- 2. Polaroid Rotations ---
    document.querySelectorAll('.polaroid').forEach(pol => {
        const rot = (Math.random() * 10 - 5) + 'deg';
        pol.style.transform = `rotate(${rot}) translateY(0)`;
        pol.style.setProperty('--base-rot', rot);
    });

    // --- 3. Photo Modal Logic ---
    const modal = document.getElementById('photo-modal');
    const modalImg = document.getElementById('modal-img');
    const closeModal = document.querySelector('.close-modal');
    const galleryImgs = document.querySelectorAll('.gallery-img');
    let currentImgIndex = 0;
    const galleryArray = Array.from(galleryImgs);

    if (modal && modalImg) {
        galleryArray.forEach((img, index) => {
            img.addEventListener('click', () => {
                currentImgIndex = index;
                modalImg.src = img.src;
                modal.classList.remove('hidden');
                document.body.classList.add('no-scroll');
            });
        });

        if (closeModal) {
            closeModal.addEventListener('click', () => {
                modal.classList.add('hidden');
                document.body.classList.remove('no-scroll');
            });
        }

        const prevNav = document.querySelector('.prev-nav');
        const nextNav = document.querySelector('.next-nav');
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
            if (e.target === modal) {
                modal.classList.add('hidden');
                document.body.classList.remove('no-scroll');
            }
        });
    }

    // --- 4. Scrapbook Pagination ---
    let currentPage = 1;
    const totalPages = 2;
    const pages = document.querySelectorAll('.sb-page');
    const prevSbBtn = document.querySelector('.prev-sb-btn');
    const nextSbBtn = document.querySelector('.next-sb-btn');
    const sbIndicator = document.querySelector('.sb-indicator-text');

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
        updateScrapbook();
    }

    // --- 5. Final Surprise Logic ---
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
                    setTimeout(() => finalIntro.classList.add('hidden'), 500);
                }

                setTimeout(() => {
                    finalMessage.classList.remove('hidden');
                    // Create particles for final
                    const finalParticles = document.getElementById('final-particles');
                    if (finalParticles) {
                        for (let i = 0; i < 30; i++) {
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

});
