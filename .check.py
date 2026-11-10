import io, sys, os, re, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
edge = None
for p in [r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
          r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"]:
    if os.path.exists(p): edge = p; break
url = "file:///c:/Users/11643/Desktop/dashboard/index.html"
out = os.path.join(os.environ['TEMP'], "db-dom.html")
subprocess.run([edge, "--headless", "--disable-gpu", "--virtual-time-budget=4000",
                "--dump-dom", url], stdout=open(out,"wb"), stderr=subprocess.DEVNULL, timeout=60)
full = open(out, encoding='utf-8', errors='ignore').read()

r = []
r.append(('title',        '销售转化看板' in full))
r.append(('KPI cards',    full.count('class="kpi"') == 4))
r.append(('KPI numbers',  '访客' in full and '线索' in full and '成交' in full))
r.append(('funnel canvas','id="funnel"' in full))
r.append(('trend canvas', 'id="trend"' in full))
r.append(('chan canvas',  'id="chan"' in full))
r.append(('table rows',   full.count('<tr>') >= 7))
r.append(('6 channels',   all(c in full for c in ['自然搜索','付费广告','社交媒体','邮件营销','转介绍','线下活动'])))
r.append(('rates shown',  '%</td>' in full or re.search(r'\d+\.\d\d%', full)))
r.append(('no JS errors', 'ReferenceError' not in full and 'TypeError' not in full))
for k,v in r: print(('PASS' if v else 'FAIL'),'-',k)
