import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup


def get_soup(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    return soup


def get_peripherals():
    return None


def __get_monitors():
    url = "https://www.vsgamers.es/category/perifericos/monitores/6"
    data_block = get_soup(url).find_all('div', class_='vs-product-card')
    monitors = []
    for data in data_block:
        name = data.find('div', class_='vs-product-card-title').a.text.strip()
        brand = data.find('div', class_='vs-product-card-detail').a.text.strip()
        image = data.find('div', class_='vs-product-card-image').img['src']
        price = data.find('div', class_='vs-product-card-prices-price')
        stars = len(data.find_all('i', class_='vs-icon-star-full'))
        if data.find('i', class_='vs-icon-star-half'):
            stars += 0.5
        if stars == 0:
            stars = None
        type_db = "Monitor"

        monitor = [name, brand, image, price, stars, type_db]
        monitors.append(monitor)
    return monitors


def __get_routers():
    url = "https://www.vsgamers.es/category/perifericos/redes/3"
    data_block = get_soup(url).find_all('div', class_='vs-product-card')
    routers = []
    for data in data_block:
        name = data.find('div', class_='vs-product-card-title').a.text.strip()
        brand = data.find('div', class_='vs-product-card-detail').a.text.strip()
        image = data.find('div', class_='vs-product-card-image').img['src']
        price = data.find('div', class_='vs-product-card-prices-price')
        stars = len(data.find_all('i', class_='vs-icon-star-full'))
        if data.find('i', class_='vs-icon-star-half'):
            stars += 0.5
        if stars == 0:
            stars = None
        type_db = "Router"

        router = [name, brand, image, price, stars, type_db]
        routers.append(router)
    return routers


def __get_keyboards():
    url = "https://www.vsgamers.es/category/perifericos/teclados/4"
    data_block = get_soup(url).find_all('div', class_='vs-product-card')
    keyboards = []
    for data in data_block:
        name = data.find('div', class_='vs-product-card-title').a.text.strip()
        brand = data.find('div', class_='vs-product-card-detail').a.text.strip()
        image = data.find('div', class_='vs-product-card-image').img['src']
        price = data.find('div', class_='vs-product-card-prices-price')
        stars = len(data.find_all('i', class_='vs-icon-star-full'))
        if data.find('i', class_='vs-icon-star-half'):
            stars += 0.5
        if stars == 0:
            stars = None
        type_db = "Keyboard"

        keyboard = [name, brand, image, price, stars, type_db]
        keyboards.append(keyboard)
    return keyboards


def __get_chairs():
    url = "https://www.vsgamers.es/category/sillas/4"
    data_block = get_soup(url).find_all('div', class_='vs-product-card')
    chairs = []
    for data in data_block:
        name = data.find('div', class_='vs-product-card-title').a.text.strip()
        brand = data.find('div', class_='vs-product-card-detail').a.text.strip()
        image = data.find('div', class_='vs-product-card-image').img['src']
        price = data.find('div', class_='vs-product-card-prices-price')
        stars = len(data.find_all('i', class_='vs-icon-star-full'))
        if data.find('i', class_='vs-icon-star-half'):
            stars += 0.5
        if stars == 0:
            stars = None
        type_db = "Chair"

        chair = [name, brand, image, price, stars, type_db]
        chairs.append(chair)
    return chairs


def __get_mice():
    url = "https://www.vsgamers.es/category/perifericos/ratones/4"
    data_block = get_soup(url).find_all('div', class_='vs-product-card')
    mice = []
    for data in data_block:
        name = data.find('div', class_='vs-product-card-title').a.text.strip()
        brand = data.find('div', class_='vs-product-card-detail').a.text.strip()
        image = data.find('div', class_='vs-product-card-image').img['src']
        price = data.find('div', class_='vs-product-card-prices-price')
        stars = len(data.find_all('i', class_='vs-icon-star-full'))
        if data.find('i', class_='vs-icon-star-half'):
            stars += 0.5
        if stars == 0:
            stars = None
        type_db = "Mouse"

        mouse = [name, brand, image, price, stars, type_db]
        mice.append(mouse)
    return mice


def __get_headsets():
    url = "https://www.vsgamers.es/category/perifericos/auriculares/7"
    data_block = get_soup(url).find_all('div', class_='vs-product-card')
    headsets = []
    for data in data_block:
        name = data.find('div', class_='vs-product-card-title').a.text.strip()
        brand = data.find('div', class_='vs-product-card-detail').a.text.strip()
        image = data.find('div', class_='vs-product-card-image').img['src']
        price = data.find('div', class_='vs-product-card-prices-price')
        stars = len(data.find_all('i', class_='vs-icon-star-full'))
        if data.find('i', class_='vs-icon-star-half'):
            stars += 0.5
        if stars == 0:
            stars = None
        type_db = "Mouse"

        headset = [name, brand, image, price, stars, type_db]
        headsets.append(headset)
    return headsets


def __get_mouse_pads():
    url = "https://www.vsgamers.es/category/perifericos/alfombrillas/4"
    data_block = get_soup(url).find_all('div', class_='vs-product-card')
    pads = []
    for data in data_block:
        name = data.find('div', class_='vs-product-card-title').a.text.strip()
        brand = data.find('div', class_='vs-product-card-detail').a.text.strip()
        image = data.find('div', class_='vs-product-card-image').img['src']
        price = data.find('div', class_='vs-product-card-prices-price')
        stars = len(data.find_all('i', class_='vs-icon-star-full'))
        if data.find('i', class_='vs-icon-star-half'):
            stars += 0.5
        if stars == 0:
            stars = None
        type_db = "Mouse Pads"

        pad = [name, brand, image, price, stars, type_db]
        pads.append(pad)
    return pads
