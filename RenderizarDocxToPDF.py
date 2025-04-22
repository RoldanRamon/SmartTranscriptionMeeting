import markdown
from weasyprint import HTML

# Read the .txt file with Markdown markup
with open('ata_melhorada_da_reuniao.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Markdown configuration with useful extensions
html_content = markdown.markdown(text, extensions=['extra', 'nl2br', 'sane_lists'])

# More complete and adjusted CSS
css = '''
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 30px;
        line-height: 1.5;
    }
    h1 {
        color: #2E86C1;
        border-bottom: 1px solid #2E86C1;
        padding-bottom: 10px;
    }
    h2, h3 {
        color: #34495E;
        margin-top: 25px;
    }
    ul {
        margin-left: 20px;
    }
    li {
        margin-bottom: 8px;
        text-align: justify;
    }
    strong {
        color: #000;
    }
    hr {
        margin: 25px 0;
    }
</style>
'''

# Combine HTML and CSS
html_final = f"<html><head>{css}</head><body>{html_content}</body></html>"

# Generate the final PDF
HTML(string=html_final).write_pdf('resultado.pdf')
