import re

with open(r'd:\birthday\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove Page 2
html = re.sub(r'<!-- Page 2 -->.*?<!-- Page 3 -->', '<!-- Page 3 -->', html, flags=re.DOTALL)

# 2. Rename Page 3 to Page 2
html = html.replace('<!-- Page 3 -->', '<!-- Page 2 -->')
html = html.replace('<div class="sb-page page-3" data-page="3">', '<div class="sb-page page-2" data-page="2">')

# 3. Add continue button to new Page 2 and remove Page 4 through Page 9 (or Secret Page)
# We find where Page 2 ends (before <!-- Page 4 -->)
btn_html = '''
                            <button id="continue-to-letter-btn" class="glow-btn sb-continue-btn mt-4" style="font-size: 16px; padding: 12px 24px;" aria-label="Continue">Continue ❤️</button>
                        </div>
                    </div>'''

# Replace the closing tags of Page 2 with the button + closing tags
html = html.replace('                        </div>\n                    </div>\n\n                    <!-- Page 4 -->', btn_html + '\n\n                    <!-- Page 4 -->')

# 4. Remove everything from <!-- Page 4 --> up to the end of .sb-pages-container
# The end of pages container is marked by '                </div>\n            </div>\n\n            <!-- Scrapbook Controls -->'
html = re.sub(r'<!-- Page 4 -->.*?</div>\n\n                </div>\n            </div>\n\n            <!-- Scrapbook Controls -->', '</div>\n            </div>\n\n            <!-- Scrapbook Controls -->', html, flags=re.DOTALL)

# 5. Update indicator text to "1 / 2"
html = html.replace('<span class="sb-indicator-text">1 / 8</span>', '<span class="sb-indicator-text">1 / 2</span>')

with open(r'd:\birthday\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('HTML updated.')
