import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://www.fake-plants.co.uk/"
HOST2 = "https://doramy.club/strana/yaponiya"
HOST3 = "https://doramy.club/strana/yuzhnaya-koreya"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
}


@csrf_exempt
def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("li", class_="product-category product")
    plants = []

    for item in items:
        plants.append(
            {
                "link": item.find("a").get("href"),
                "title": item.find(
                    "h2", class_="woocommerce-loop-category__title"
                ).get_text(strip=True),
                "image": item.find("a").find("img").get("src"),
            }
        )
    return plants


@csrf_exempt
def parser_func():
    html = get_html(HOST)
    if html.status_code == 200:
        plants = []
        for i in range(0, 1):
            plants.extend(get_data(html.text))
        return plants
    else:
        raise Exception("Error in parser function")


@csrf_exempt
def get_data_dorama(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="post-home")
    dorama = []
    for item in items:
        dorama.append(
            {
                "link": item.find("a").get("href"),
                "title": item.find("a").find("span").get_text(),
                "image": item.find("a").find("img").get("src"),
            }
        )
    return dorama


@csrf_exempt
def parser_func_dorama():
    html = get_html(HOST3)
    if html.status_code == 200:
        dorama = []
        for i in range(1, 183):
            html = get_html(f"https://doramy.club/strana/yuzhnaya-koreya/page/{i}")
            dorama.extend(get_data_dorama(html.text))
        return dorama
    else:
        raise Exception("Error in parser function dorama")
