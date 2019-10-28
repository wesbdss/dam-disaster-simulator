from bs4 import BeautifulSoup #pip install beautifulsoup4
import requests
import scrapy #pip3 install scrapy
from selenium import webdriver
import urllib

cores = [(255, 255, 255),
(255, 197, 197),
(255, 140, 140),
(255, 82, 82),
(255, 25, 25),
(255, 32, 0),
(255, 89, 0),
(255, 147, 0),
(255, 204, 0),
(249, 255, 0),
(192, 255, 0),
(134, 255, 0),
(76, 255, 0),
(19, 255, 0),
(0, 255, 75),
(0, 255, 191),
(0, 230, 255),
(0, 173, 255),
(0, 115, 255),
(0, 58, 255)]

class pickImage():
    
    def pegarImage(self=' ', link= ''):
        try:
            options = webdriver.ChromeOptions() #drives do chrome
            options.add_argument('headless')
            options.add_argument('windows-size=1920x1080')
            driver = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=options) #uso do drive na pasta main
            driver.get(link)
            imgs = driver.find_elements_by_xpath("//img[contains(@class, 'leaflet-image-layer leaflet-zoom-animated')]")
            for x in imgs:
                urllib.request.urlretrieve(x.get_attribute('src'), "imagens/"+(link.split('/')[5])+".png")
            driver.quit()
            print("Imagem extraida com sucesso")
            return (link.split('/')[5])+".png"
        except Exception :
            print("Ocorreu um erro")
        
        