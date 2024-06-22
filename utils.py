import requests
from bs4 import BeautifulSoup

def get_instagram_caption(url)->str:
    html = requests.get(url).text
    soup = BeautifulSoup(html,features="html.parser")
    mydivs = soup.find_all("meta", attrs={"property": "og:title"})
    ans = mydivs[0].get('content')
    return ans
