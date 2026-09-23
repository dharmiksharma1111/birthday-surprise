import sys

replacements = {
    'â ¤ï¸ ': '❤️',
    'âœ¨': '✨',
    'ðŸ¥¹': '🥹',
    'ðŸ«‚': '🫂',
    'ðŸ¤ ': '🤍',
    'ðŸŒ¸': '🌸',
    'ðŸ“–': '📖',
    'ðŸŽ‚': '🎂',
    'ðŸ‘€': '👀',
    'â† ': '←',
    'â†’': '→',
    'â™ª': '🎵',
    'Ã—': '×',
    'â€œ': '“',
    'â€ ': '”',
    'â€¢': '•',
    'â€¦': '…'
}

try:
    with open(r'd:\birthday\index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    for bad, good in replacements.items():
        text = text.replace(bad, good)

    with open(r'd:\birthday\index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Success")
except Exception as e:
    print(f"Error: {e}")
