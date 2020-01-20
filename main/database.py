import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup


def get_soup(url):
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(5)
    doc = browser.find_element(id="btnMore")
    doc.click()
    time.sleep(3)
    source = requests.get().text
    soup = BeautifulSoup(source, 'lxml')
    return soup


def get_categories():
    res = ["Office", "Gaming", "Other"]
    return res


def get_types():
    res = ["Monitor", "Speaker", "Keyboards", "Chairs", "Mouse", "Headset", "Printer"]
    return res


def get_peripherals():
    return None


def __get_monitors():
    url = "https://www.pccomponentes.com/monitores-pc"
    datablock = get_soup(url)
    for data in datablock:
        res = []
    return res


def __get_speakers():
    url = "https://www.pccomponentes.com/altavoces"
    datablock = get_soup(url)
    res = []
    return res


def __get_keyboards():
    url = "https://www.pccomponentes.com/teclados"
    datablock = get_soup(url)
    res = []
    return res


def __get_chairs():
    url = "https://www.pccomponentes.com/sillas"
    datablock = get_soup(url)
    res = []
    return res


def __get_mice():
    url = "https://www.pccomponentes.com/ratones"
    datablock = get_soup(url)
    res = []
    return res


def __get_headsets():
    url = "https://www.pccomponentes.com/auriculares"
    datablock = get_soup(url)
    res = []
    return res


def __get_printers():
    url = "https://www.pccomponentes.com/impresoras"
    datablock = get_soup(url)
    res = []
    return res


def get_ratings():
    url = ""
    datablock = get_soup(url)
    res = []
    return res


browser = webdriver.Chrome()
browser.get("https://www.pccomponentes.com/impresoras")
time.sleep(5)
doc = browser.find_element(id="btnMore")
doc.click()
time.sleep(3)
print(browser)
