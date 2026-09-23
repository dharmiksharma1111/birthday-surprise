import re

# 1. Update index.html to add the audio element
with open(r'd:\birthday\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'id="bgMusic"' not in html:
    audio_tag = '''
    <!-- Background Music -->
    <audio id="bgMusic" loop preload="auto">
        <source src="assets/music/music.mp3" type="audio/mpeg">
    </audio>
</body>
'''
    html = html.replace('</body>', audio_tag)
    with open(r'd:\birthday\index.html', 'w', encoding='utf-8') as f:
        f.write(html)

# 2. Update script.js
with open(r'd:\birthday\script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace openBtn click logic
old_open_btn_logic = '''openBtn.addEventListener('click', () => {
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
    });'''

new_open_btn_logic = '''openBtn.addEventListener('click', async () => {
        // Play music
        const bgMusic = document.getElementById("bgMusic");
        const musicBtn = document.getElementById('music-btn');
        if (bgMusic && bgMusic.paused) {
            try {
                bgMusic.volume = 0;
                await bgMusic.play();
                
                // Fade in music smoothly
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
                
                // Update button visual state
                if (musicBtn) {
                    musicBtn.style.background = 'rgba(255, 215, 0, 0.2)';
                    musicBtn.style.borderColor = 'rgba(255, 215, 0, 0.6)';
                    musicBtn.innerHTML = '⏸'; // Change icon to pause
                }
            } catch (error) {
                console.log("Music playback could not start:", error);
            }
        }

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
    });'''
js = js.replace(old_open_btn_logic, new_open_btn_logic)

# Replace musicBtn logic
old_music_btn_logic = '''const musicBtn = document.getElementById('music-btn');
    let isPlaying = false;
    
    musicBtn.addEventListener('click', () => {
        isPlaying = !isPlaying;
        if (isPlaying) {
            musicBtn.style.background = 'rgba(255, 215, 0, 0.2)';
            musicBtn.style.borderColor = 'rgba(255, 215, 0, 0.6)';
            console.log("Music state: PLAYING (Mock)");
        } else {
            musicBtn.style.background = ''; // Reverts to CSS default
            musicBtn.style.borderColor = '';
            console.log("Music state: PAUSED (Mock)");
        }
    });'''

new_music_btn_logic = '''const musicBtn = document.getElementById('music-btn');
    const bgMusic = document.getElementById("bgMusic");
    
    musicBtn.addEventListener('click', () => {
        if (!bgMusic) return;
        
        if (bgMusic.paused) {
            bgMusic.play();
            musicBtn.style.background = 'rgba(255, 215, 0, 0.2)';
            musicBtn.style.borderColor = 'rgba(255, 215, 0, 0.6)';
            musicBtn.innerHTML = '⏸';
        } else {
            bgMusic.pause();
            musicBtn.style.background = ''; // Reverts to CSS default
            musicBtn.style.borderColor = '';
            musicBtn.innerHTML = '🎵';
        }
    });'''
js = js.replace(old_music_btn_logic, new_music_btn_logic)

with open(r'd:\birthday\script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Music logic updated.")
