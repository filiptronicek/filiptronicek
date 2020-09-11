import re

filename = "README.md"
patt = r'<a class="post" href="https:\/\/blog.trnck.dev\/.*\/">.*<\/a>'


def write(title, url, date):
    with open(filename, encoding="utf-8") as f:
        content = f.readlines()
    content = [x for x in content]
    replaced = ""
    for c in content:
        if re.search(patt, c):
            print("found")
            splitToModify = c.split(re.split(patt, c)[0])[1]
            splitToModify = re.sub(r'href="https://blog.trnck.dev/[.*]?"',
                                   f'href="{url}"', splitToModify)
            modify = re.sub(r">.*<", f">{str(title)} (published on {date})<",
                            splitToModify)
            replaced += (c.split(splitToModify)[0]).split("<")[0] + modify
            replaced = re.sub(r'\"https://blog.trnck.dev/.*\"', f"\"{url}\"", replaced)
        else:
            replaced += c
    with open(filename, "w", encoding="utf-8") as f:
        f.write(replaced)
