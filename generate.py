content = ""

with open("repo.rift", "r") as f:
    entries = f.readlines()

with open("template.html", "r") as f:
    template = f.read()

for entry in entries:
    entryinfo = entry.split(";")
    content = content + f'''<div class="box"><h2>{entryinfo[0]}</h2>\n\n<p>{entryinfo[2]}</p><button onclick="window.location.href='{entryinfo[1]}'">Download</button></div>\n\n'''

with open("index.html", "w") as f:
    template = template.replace("$RIFT.TITLE", "PLACEHOLDER")
    template = template.replace("$RIFT.VERSION", "24.11")
    template = template.replace("$RIFT.CONTENT", content)
    f.write(template)