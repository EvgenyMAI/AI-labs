import os
import json

with open('lab1/KIDBOOK/concepts.json', 'r', encoding='utf-8') as f:
    concepts = json.load(f)['concepts']

for term in concepts:
    filename = f"lab1/KIDBOOK/{term}.md"
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# {term}\n\n(Описание пока отсутствует.)\n")
    
    with open(filename, 'r+', encoding='utf-8') as f:
        content = f.read()
        for linked_term in concepts:
            if linked_term != term and linked_term in content:
                link = f"[{linked_term}](./{linked_term}.md)"
                if link not in content:
                    f.write(f"\n\n**Связанные понятия:** {link}")