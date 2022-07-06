import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from threading import Thread
from pathlib import Path
import urllib.request
import os
from socket import setdefaulttimeout

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

setdefaulttimeout(30)

LOCAL_PATH = Path().resolve()
PATH_TO_IMG = str(LOCAL_PATH) + "/tmp/"
WIKI_PATH = "https://en.wikipedia.org/"
DIRECTORY = "/tmp/"
HTML_FILE = "output1.html"

IGNORED_LIST = ["[d]", "(male)", "(female)", "(young)", "[45]", "", "[81]"]


def printer(url):
    try:
        os.mkdir(PATH_TO_IMG)
    except FileExistsError:
        print("The file already exist, keep going")
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = find_table(soup)
    create_basic_html_file()
    success = output_animals_and_pic(table)
    close_html_file()
    if success:
        return "You can calm down, we got it!"
    else:
        "Oh shit! something went wrong"


def find_table(soup):
    tables = soup.find_all("table", {"class": "wikitable sortable"})
    animal_table = None
    for table in tables:
        if "Animal" in table.find('tbody').find("tr").find("th"):
            animal_table = table
            break
    if animal_table is None:
        raise Exception("The desired table doesnt exist in this page, please check you provide a valid page")
    else:
        return animal_table


def output_animals_and_pic(table):
    rows = table.find_all("tr")
    threads = []
    for row in rows:
        try:
            items = row.find_all('td')
            img_url = items[0].find("a")["href"]
            download_to = PATH_TO_IMG.replace('\\', '/') + img_url.split("/")[2] + ".png"
            threads.append(Thread(target=download_pic, args=(img_url, download_to)))

            diff_of_the_same_adjective = items[5].get_text(separator=" ").strip().split(" ")

            for collateral_adjective in diff_of_the_same_adjective:

                if collateral_adjective in IGNORED_LIST:
                    continue

                animal_name = items[0].text.strip().replace("(list)", "").replace("[c]", "").replace("[12]", "")
                threads.append(Thread(target=output_into_html, args=(animal_name, collateral_adjective, download_to)))


        except (IndexError, AttributeError, TypeError):
            continue
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return True


def download_pic(img_url, download_to):
    try:
        response = session.get(WIKI_PATH + img_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_src = soup.select("table.infobox a.image img[src]")[0]['src'].replace('\\', '/')
        urllib.request.urlretrieve("https:" + img_src, download_to)

        print("Downloading the img - %s" % img_src)
    except IndexError:
        return


def output_into_html(animal_name, collateral_adjective, local_path_to_img):
    with open(HTML_FILE, "a", encoding='utf-8') as file:
        text = f"""<tr><td>{animal_name}</td><td>{collateral_adjective}</td><td>{local_path_to_img}</td></tr>\n"""
        file.write(text)


def create_basic_html_file():
    with open(HTML_FILE, "w", encoding='utf-8') as file:
        text = """<html>
        <head></head>
        <body><table><tbody><tr><th>Animal</th><th>Collateral adjective</th><th>Local Path</th></tr>\n"""
        file.write(text)


def close_html_file():
    with open(HTML_FILE, "a") as file:
        text = """</tbody></table></body>
</html>"""
        file.write(text)
