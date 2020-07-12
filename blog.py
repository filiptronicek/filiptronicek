import requests
from os import getenv
import datetime
from dotenv import load_dotenv
load_dotenv()

user = "filiptronicek"
repo = "filiptronicek.github.io"

url = "https://api.github.com/repos/{}/{}/git/trees/master?recursive=1".format(user, repo)
headers = {'Authorization': getenv("TOKEN")}
r = requests.get(url, headers=headers)
res = r.json()

for file in res["tree"]:
    if "_posts/" in file["path"]:
        fileNm = file["path"].split("/")[1]
        dateStr = fileNm[:10]
        date_time_obj = datetime.datetime.strptime(dateStr, "%Y-%M-%d")
        print(date_time_obj.strftime("%B %d, %Y"))
