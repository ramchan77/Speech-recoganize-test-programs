from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.common.proxy import Proxy,ProxyType
import time
import cookielib
import requests
import csv
import xlsxwriter
from xlutils.copy import copy
from xlrd import open_workbook
import pyautogui
import re
from pytesseract import *
from PIL import Image
from StringIO import StringIO
from six.moves import urllib
import os
import PyBaiduYuyin as sr
from wit import Wit
import json
import string


print 'Launching Chrome..'
#prox = Proxy()
#prox.proxy_type = ProxyType.MANUAL
#prox.http_proxy = "127.0.0.1:9667"
#prox.socks_proxy = "127.0.0.1:9667"
#prox.ssl_proxy = "127.0.0.1:9667"
#capabilities = webdriver.DesiredCapabilities.CHROME
#prox.add_to_capabilities(capabilities)
##options = webdriver.ChromeOptions()
##options.add_argument('--ignore-certificate-errors')
##options.add_argument('--ignore-ssl-errors')
##capa = DesiredCapabilities.CHROME
##capa["pageLoadStrategy"] = "none"
##download_dir = "C:\Users\lenovo\Desktop\python\Acra"
##preferences = {"download.default_directory": download_dir ,
##               "directory_upgrade": True,
##               "safebrowsing.enabled": True }
##options.add_experimental_option("prefs", preferences)
#browser = webdriver.Chrome(executable_path='C:\Users\lenovo\Desktop\python\chromedriver.exe',chrome_options=options,desired_capabilities=capa)
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", 'C:\Users\lenovo\Desktop\python\Acra')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/wav")
browser = webdriver.Firefox(executable_path='C:\Users\lenovo\Desktop\python\geckodriver.exe',firefox_profile=profile)
