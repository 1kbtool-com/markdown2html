from markdown import markdown
import pandas as pd
extensions = [  # 根据不同教程加上的扩展
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',  # 代码高亮扩展
    'markdown.extensions.toc',
    'markdown.extensions.tables',
    'markdown.extensions.fenced_code',
]

# 读取

with open('README.md', 'r', encoding='utf-8') as f:
    file = f.read()

with open('template.html', 'r', encoding='utf-8') as f:
    template = f.read()

html = markdown(file, extensions=extensions)

html = template.replace(r'{{content}}', html)

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html)
