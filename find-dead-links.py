import requests
from sys import argv
from bs4 import BeautifulSoup

def bad_url(url,depth):
    try:
        r = requests.get(url)
        if r.status_code not in [200, 303]:
            print("Bad link: {}".format(url))
            return
        except:
            print("Bad link: {}".format(url))
            return
        if depth  > 0:
            newUrls = []
            r = requests.get(url)
            soup = BeautifulSoup(r.text, features="html.parser")
            for a in soup.find_all("a", href=True):
                newUrl = a["href"]
                if not newUrl.startwith("http"):
                    if newUrl.startswith("/" and url.endswith("/"):
                            newUrl = url + newUrl[1:]
                    else:
                        newUrl = url + newUrl
                bad_url(newUrl, depth-1)

																				 
																				 
if len(argv) == 3:
    depth = argv[1]
    url = argv[2]
    if depth.startswith("-"):
        try:
            depth = int(depth[1:]
            bad_url(url,depth)
        except:
            print("Usage: find-dead-links <url>")
            print("Usage: find-dead-links -<depth> <url>")
    else:
        print("Usage: find-dead-links <url>")
        print("Usage: find-dead-lnks -<depth> <url>")
elif len(argv) == 2:
    url = argv[1]
    bad_url(url,1)
else:
    print("Usage: find-dead-links <url>")
    print("Usage: find-dead-links -<depth> <url>")
																			 
