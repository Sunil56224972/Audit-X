import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<figcaption class=\"mt-auto pt-4 border-t-2 border-dashed border-\[var\(--color-moss\)\]\">.*?</figcaption>'

new_content = re.sub(pattern, '', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
