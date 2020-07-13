import requests
from os import getenv, environ
import datetime
import re

from modify import write

if environ.get('TOKEN') is None:
    from dotenv import load_dotenv
    load_dotenv()

user = "filiptronicek"
repo = "filiptronicek.github.io"

url = "https://api.github.com/repos/{}/{}/git/trees/master?recursive=1".format(
    user, repo)
headers = {'Authorization': getenv("TOKEN")}
r = requests.get(url, headers=headers)
res = r.json()

posts = []

for file in res["tree"]:
    if "_posts/" in file["path"]:
        fileNm = file["path"].split("/")[-1]
        dateStr = fileNm[:10]
        date_time_obj = datetime.datetime.strptime(dateStr, "%Y-%m-%d")
        fmtTime = date_time_obj.strftime(r"%B %-d, %Y")
        flUrl = f"https://raw.githubusercontent.com/filiptronicek/filiptronicek.github.io/master/_posts/{fileNm}"
        flReq = requests.get(flUrl).text
        if "title" in flReq.strip().split("\n")[1]:
            title = (flReq.strip().split("\n")[1])[7:]
        elif "title" in flReq.strip().split("\n")[2]:
            title = (flReq.strip().split("\n")[2])[7:]
        else:
            title = fileNm
        blogUrl = f"https://blog.trnck.dev/{fileNm[11:].replace('.md','/')}"
        posts.append({"time": fmtTime, "title": title, "url": blogUrl})
write(posts[-1]["title"], posts[-1]["url"], posts[-1]["time"])
