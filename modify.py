import re

filename = "README.md"
patt = r'<a.*class="post".*>.*</a>'

def write(rank, url, date):
    with open(filename) as f:
        content = f.readlines()
    content = [x for x in content] 
    replaced = ""
    for c in content:
        if re.search(patt, c):
            splitToModify = (c.split(re.split(patt, c)[0])[1])
            splitToModify = splitToModify.replace('href="https://blog.trnck.dev/"', f'href="{url}"')
            modify = re.sub(r">[\d]+?<",f">{str(rank)}<", splitToModify)
            replaced += c.split(splitToModify)[0] + modify + c.split(splitToModify)[1]
        else:
            replaced += c
    with open(filename, "w") as f:
        f.write(replaced)