import io, sys, os, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
d = open(os.path.join(os.environ['TEMP'], 'db-dom.html'), encoding='utf-8', errors='ignore').read()
print('count kpi class:', d.count('class="kpi"'))
print('count kpi-ish  :', d.count('kpi'))
m = re.search(r'<section class="kpis[^>]*>([\s\S]{0,900})', d)
print('--- section head ---')
print(m.group(1)[:700] if m else 'NONE')
