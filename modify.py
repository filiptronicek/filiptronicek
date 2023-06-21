import re

filename = "README.md"
patt = r'<a class="post" href="https:\/\/blog.trnck.dev\/.*\/">.*<\/a>'


def write(title, url, date):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    replaced = re.sub(
        patt, f'<a class="post" href="{url}">{title} (published on {date})</a>', content
    )

    with open(filename, "w", encoding="utf-8") as f:
        f.write(replaced)
