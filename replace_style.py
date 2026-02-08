import re

with open('dist/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <style>...</style> with link tag
new_content = re.sub(r'  <style>.*?  </style>', '  <link href="/styles.css" rel="stylesheet"/>', content, flags=re.DOTALL)

with open('dist/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated index.html with stylesheet link')
