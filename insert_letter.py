import re

with open(r'd:\birthday\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Page 8
old_page_8_match = re.search(r'<!-- Page 8 -->\s*<div class="sb-page page-8".*?</div>\s*</div>\s*</div>', html, re.DOTALL)
if old_page_8_match:
    old_page_8 = old_page_8_match.group(0)
    
    new_page_8 = '''<!-- Page 8 -->
                    <div class="sb-page page-8" data-page="8">
                        <div class="page-content sb-letter" style="display: flex; flex-direction: column; height: 100%;">
                            <h3 class="page-title-clean">To My Mr. Husband ❤️</h3>
                            <div class="sb-letter-body mt-3" style="flex: 1; overflow-y: auto; padding-right: 8px; scrollbar-width: thin;">
                                <p>Aaje khabar che ketlo special day che?<br>Mara birthday ni jetli excitement nathi hoti, aetli tara birthday ni hoy che… 💝</p>
                                <p>Finally, today’s date — 16/10 🥳🥳🥳🥳<br>Mara ae person no birthday che, jene always mane support karyo che, always mari sathe j ryo che… 🫂<br>Always mane happy rakhvani j try kari che…<br>Mari life j tu cho, Jay. 🫂</p>
                                <p>Tane khabar che, bija loko ne eni life ma problem aave to mummy, papa, bhai yaad aave…<br>Pan mari life ma kai pan problem aave, aetle pela tu yaad aav…<br>Because maru world 🌎 j tu cho…<br>Mara life ni last 7 minutes pan tu j cho, Jay… 🫂🫂🫂🫂</p>
                                <p>Tari sathe life ni nani nani moments pan special bani jaay chhe.<br>Tari ek smile maru mood badli shake chhe, ane taro ek word — “hu chu ne” — mane badhi problems ma strong feel karave chhe. ❤️</p>
                                <p>Jay, mane life perfect nathi joie…<br>Mane bas badhi situation ma taro support joie che —<br>happiness hoy ke sadness, success hoy ke struggle, hu always tari sathe chu. 🥺❤️</p>
                                <p>Jay, ek promise karu...<br>Life hamesha easy nathi hoy, badha days perfect nathi hoy, but ek vaat always same rehse — hu tari sathe rahish. 🥹❤️</p>
                                <p>Bas ek j wish chhe…<br>Jya sudhi life chhe, tya sudhi tari sathe aa journey chhe. ❤️♾️</p>
                                <p>My world is not perfect, but because you are in it, I find it the most beautiful. 🥺❤️</p>
                                <p>Thank you for being my person, my forever, my husband, my love, my everything. 🎂❤️</p>
                                <p>Thank you so much mari life ma aavi ne mari life ne complete banava mate. ❤️🥹<br>Thank you for always being there for me, my lifeline… ❤️🫶🏻</p>
                                <p>Bas aaje aa special day par ae j pray karis ke Hari tane always happy and healthy rakhe… 🥰</p>
                                <p>Happy Birthday to the man who makes my life more beautiful every single day. ❤️<br>I love you endlessly, Jayu ❤️♾️🫂🫂🫂🧿🧿</p>
                            </div>
                            <div class="sb-letter-footer mt-2 text-right">
                                <p style="font-family: 'Playfair Display', serif; font-style: italic; margin-bottom: 0;">With all my love,</p>
                                <p class="sb-signature" style="margin-top: 5px;">Tari Wife ❤️</p>
                            </div>
                        </div>
                    </div>'''

    html = html.replace(old_page_8, new_page_8)
    
    with open(r'd:\birthday\index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Letter updated successfully.")
else:
    print("Could not find Page 8 to replace.")
