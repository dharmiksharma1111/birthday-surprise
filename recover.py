import json
import re

transcript_path = r'C:\Users\Dell\.gemini\antigravity-ide\brain\1cffabe9-b73d-4822-b0df-8f14eff8e85c\.system_generated\logs\transcript_full.jsonl'
original_html = ''

# Find the view_file response that contains the original index.html
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'TOOL_RESPONSE' and 'index.html' in str(data):
            # Look for the view_file output format
            out = data.get('content', '')
            if 'Showing lines 1 to 401' in out or 'Showing lines 1 to 442' in out or 'Showing lines 1 to 443' in out:
                # Need the very first one
                if 'photo1.jpg' in out and not 'Pic_1.jpg' in out:
                    original_html = out
                    break

if original_html:
    # Strip headers and line numbers
    lines = original_html.split('\n')
    cleaned_lines = []
    started = False
    for line in lines:
        if 'The following code has been modified to include a line number' in line:
            started = True
            continue
        if 'The above content shows the entire, complete file contents' in line or 'The above content does NOT show the entire' in line:
            started = False
            break
        if started:
            # line is like '1: <!DOCTYPE html>'
            if ':' in line:
                cleaned_lines.append(line.split(':', 1)[1][1:])
            else:
                cleaned_lines.append(line)
    
    html = '\n'.join(cleaned_lines)
    
    # Do replacements
    html = html.replace('photo1.jpg', 'Pic_1.jpg')
    html = html.replace('photo2.jpg', 'Pic_2.jpg')
    html = html.replace('photo3.jpg', 'Pic_3.jpeg')
    html = html.replace('photo4.jpg', 'Pic_4.jpeg')
    html = html.replace('photo5.jpg', 'Pic_5.jpg')
    html = html.replace('photo6.jpg', 'Pic_6.jpg')
    html = html.replace('photo7.jpg', 'Pic_7.jpeg')
    html = html.replace('photo8.jpg', 'Pic_8.jpeg')
    html = html.replace('photo9.jpg', 'Pic_9.jpeg')
    html = html.replace('photo10.jpg', 'Pic_10.jpg')
    html = html.replace('photo11.jpg', 'Pic_11.jpg')
    html = html.replace('photo12.jpg', 'Pic_12.jpeg')
    
    # Also update age to 21
    html = html.replace('<h1 class="age-number" id="age">24</h1>', '<h1 class="age-number" id="age">21</h1>')
    
    with open(r'd:\birthday\index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Successfully restored from transcript!')
else:
    print('Could not find original HTML in transcript.')
