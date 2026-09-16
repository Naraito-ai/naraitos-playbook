import re

with open(r'D:\us-remote-engineering-playbook\app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

with open(r'D:\us-remote-engineering-playbook\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all getElementById calls
id_matches = re.findall(r'document\.getElementById\([\'"]([^\'"]+)[\'"]\)', app_js)
unique_ids = sorted(list(set(id_matches)))

print(f"Found {len(unique_ids)} unique element IDs referenced in app.js:")
missing_ids = []
for el_id in unique_ids:
    # Check if id exists in html
    pattern = f'id=[\'"]{re.escape(el_id)}[\'"]'
    if not re.search(pattern, html):
        missing_ids.append(el_id)

print(f"\nMissing IDs ({len(missing_ids)}):")
for m in missing_ids:
    print(f"  - {m}")
