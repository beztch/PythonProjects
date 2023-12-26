import requests
from bs4 import BeautifulSoup
from .sites import url, headers

def Parser(n):
    """searches the information on site
    Args:
        n (int): place in the ranking.
    Returns:
        film (str): name and year of the film.
        img (str): link to the photo.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        film = soup.find('div', attrs={'style':'z-index:' + str(1001 - n) + ';'}).text
        film = film.partition(')')[0] + ')'
        img = soup.find('div', attrs={'style': 'z-index:' + str(1001 - n) + ';'})
        img = img.find('div', attrs={'class': 'pic'})
        img = img.find('img')
        img = img.attrs.get("src")
        film = str(film.lstrip())
        return film, img
    except Exception:
        return "Такого номера у нас в рейтинге нет(", ""
