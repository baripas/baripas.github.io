import sys, json, re
mode = sys.argv[1] if len(sys.argv) > 1 else 'changed'
text = sys.stdin.read()
if mode == 'sitemap':
    urls = re.findall(r'<loc>(.*?)</loc>', text)
else:
    urls = []
    for line in text.splitlines():
        f = line.strip()
        if not f: continue
        if f == 'index.html': urls.append('https://baripas.github.io/')
        elif f.endswith('/index.html'): urls.append('https://baripas.github.io/' + f[:-10])
        else: urls.append('https://baripas.github.io/' + f)
print(json.dumps(urls))