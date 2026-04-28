import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make changes
content = content.replace('Bapusaheb Patil', 'sunil yogi')
content = content.replace('David Gumpel', 'sunil yogi')
content = content.replace('BUILT BY · BAPSPATIL.COM', 'BUILT BY · SUNIL YOGI')
content = content.replace('https://www.bapspatil.com', '#')
content = content.replace('AI Design Engineer', 'ui/ux designer and developer')
content = content.replace('Frontend performance advocate. Former div auditor. Currently unreachable. On sabbatical writing raw HTML.', 'ui/ux designer and developer.')

# Fix 'Donate'
content = content.replace('>Donate<', '>Refactor<')
content = content.replace('data-donate-label="Donate"', 'data-donate-label="Audit Project"')

# Fix donation text
content = content.replace('Thank you for your donation!', 'Thank you for your audit!')
content = content.replace('Close donation receipt', 'Close audit receipt')
content = content.replace('<span>Donation</span>', '<span>Audit</span>')
content = content.replace('>Donation<', '>Audit<')
content = content.replace('>1 cookie<', '>1 cpu cycle<')
content = content.replace('Elf morale tax', 'Tech debt penalty')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Replacements done.')
