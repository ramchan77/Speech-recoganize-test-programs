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


input_file_name = raw_input("Enter The Input file Name (with csv Extention ): ")
output_file_name = raw_input("Enter The file Name (with xls Extention ) : ")
#print output_file_name
workbook = xlsxwriter.Workbook(output_file_name)
worksheet = workbook.add_worksheet()
workbook.close()
book_ro = open_workbook(output_file_name)
book = copy(book_ro)
sheet1 = book.get_sheet(0)
count=0
#count_l=0
roww=0
coll=0
old=''
old_captcha=''
#page_content=''
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
#print 'Waiting for 2 mins...'
#time.sleep(90)
print 'Entering to website...'
browser.get('https://www.tis.bizfile.gov.sg/ngbtisinternet/faces/oracle/webcenter/portalapp/pages/TransactionMain.jspx?selectedETransId=dirSearch#%40%3FselectedETransId%3DdirSearch%26_adf.ctrl-state%3Dxtehpl541_9')
with open(input_file_name, "r") as f:
    reader=csv.reader(f)
    for row in reader:
        uen = row[0]
        count_l=0
        def search():
            global count_l
            if count_l<25:
                try:
                    wait = WebDriverWait(browser, 20)
                    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pt1:r1:0:it1::content"]')))
                    editor=browser.find_element_by_xpath('//*[@id="pt1:r1:0:it1::content"]')
            #editor.click()
                    editor.clear()
                    editor.send_keys(uen)
            #wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pt1:r1:0:cb1"]')))
                    #browser.find_element_by_xpath('//*[@id="pt1:r1:0:cb1"]').click()
                    #print 'Search success'
                except Exception as e:
                #print(e)
                #print 'Retrying'
                    count_l+=1
                    search()
            else:
                browser.get('https://www.tis.bizfile.gov.sg/ngbtisinternet/faces/oracle/webcenter/portalapp/pages/TransactionMain.jspx?selectedETransId=dirSearch#%40%3FselectedETransId%3DdirSearch%26_adf.ctrl-state%3Dxtehpl541_9')
                count_l=0
                search()
        def captcha():
            #global pytesseract
            global Keys
            global old_captcha
            try:
                wait = WebDriverWait(browser, 20)
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pt1:r1:0:r1:0:it1::content"]')))
                test=browser.find_element_by_xpath('//*[@id="pt1:r1:0:r1:0:it1::content"]')
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pt1:r1:0:r1:0:i1"]')))
                captcha_elem=browser.find_element_by_xpath('//*[@id="pt1:r1:0:r1:0:i1"]')
                old_captcha=captcha_elem.get_attribute("src")
                print 'old captcha  : '+old_captcha
##                location = captcha_elem.location
##                size = captcha_elem.size
##                img = browser.get_screenshot_as_png()
##                img = Image.open(StringIO(img))
##                left = location['x']
##                top = location['y']
##                right = location['x'] + size['width']
##                bottom = location['y'] + size['height']
##                img = img.crop((int(left), int(top), int(right), int(bottom)))
##                img.save('screenshot.png')
##                #img1 = Image.open('capcha_image.png')
##                captcha_text = image_to_string(Image.open('screenshot.png'))
##                #im=Image.open('screenshot-2.png')
##                #r,g,b,a = im.split()
##                #im = Image.merge('RGB',(r,g,b))
##                #print pytesseract.image_to_string(im)
##                #print pytesseract.image_to_string(im, config=config)
##                print 'method 1'
##                print captcha_text
##                print 'method 2'
##                captcha()
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pt1:r1:0:r1:0:cb21"]')))
                browser.find_element_by_xpath('//*[@id="pt1:r1:0:r1:0:cb21"]').click()
                time.sleep(5)
##                try:
##                    new_captcha=browser.find_element_by_xpath('//*[@id="pt1:r1:0:r1:0:i1"]').get_attribute("src")
##                except:
##                    new_captcha=old_captcha
##                match_count1=0
##                while old_captcha==new_captcha:
##                    if match_count1<15:
##                        time.sleep(3)
##                        match_count1+=1
##                        try:
##                            new_captcha=browser.find_element_by_xpath('//*[@id="pt1:r1:0:r1:0:i1"]').get_attribute("src")
##                        except Exception as e:
##                            print(e)
##                            new_captcha=old_captcha
##                        print 'new captcha  : '+new_captcha
##                    else:
##                        captcha()
                time.sleep(2)
                browser.execute_script('''window.open("https://www.tis.bizfile.gov.sg/ngbtisinternet/audioservlet","_blank");''')
                while not os.path.exists('C:\\Users\\lenovo\\Desktop\\python\\Acra\\audioservlet'):
                    time.sleep(2)
                time.sleep(3)
                #cmd="ffmpeg -y -i audioservlet -acodec pcm_s16le -ac 1 -ar 16000 myfile.wav"
                cmd='ffmpeg -y -i audioservlet -filter:a "atempo=0.85" -vn myfile.wav'
                #cmd2='ffmpeg -y -i myfile.wav -filter:a loudnorm myfile.wav'
                cmd1="del audioservlet"
                os.system(cmd)
                time.sleep(1)
                os.system(cmd1)
                #os.system(cmd2)
                r = sr.Recognizer()
                # captcha_a = sr.AudioFile('myfile.wav')
                # with captcha_a as source:
                #     audio = r.record(source)
                with open('myfile.wav','rb') as source:
                    audio = r.record(source)
                try:
                    # captcha_text=r.recognize_bing(audio,key='4782f102dcf4453d939624cdda8d8e63')
                    captcha_text=r.recognize(audio)
                    print(captcha_text)
                #except sr.UnknownValueError:
                #except:
                    #print("Could not understand audio")
                #except sr.RequestError as e:
                    #print("Could not request results; {0}".format(e))
                except Exception as e:
                    print(e)
                editor_captcha=browser.find_element_by_xpath('//*[@id="pt1:r1:0:r1:0:it1::content"]')
                editor_captcha.send_keys(captcha_text)
                browser.find_element_by_xpath('//*[@id="pt1:r1:0:cb1"]').click()
            except Exception as e:
                print(e)
                print "Error captcha Reading"
                #main()
        def main():
            result_status=0
            #search()
            global old
            #global sheet1 = book.get_sheet(0)
            global count
            global roww
            global coll
            global old_captcha
            try:
               new_captcha=browser.find_element_by_xpath('//*[@id="pt1:r1:0:r1:0:i1"]').get_attribute("src")
            except:
                new_captcha=old_captcha
            match_count1=0
            while old_captcha==new_captcha:
                if match_count1<15:
                    time.sleep(3)
                    match_count1+=1
                    try:
                        new_captcha=browser.find_element_by_xpath('//*[@id="pt1:r1:0:r1:0:i1"]').get_attribute("src")
                    except Exception as e:
                        print(e)
                        new_captcha=old_captcha
                    print 'new captcha  : '+new_captcha
                else:
                    captcha()
            try:
                wait = WebDriverWait(browser, 25)
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[starts-with(@id,"pt1:r1:0:search:")]')))
                
                time.sleep(3)
        #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pt1:r1:0:search:0:pgl6"]/tbody/tr/td[3]/span')))
                new=browser.find_element_by_xpath('//*[starts-with(@id,"pt1:r1:0:search:") and contains(@id, ":pgl6")]/tbody/tr/td[3]/span').text
                print new
                match_count=0
                print(match_count)
                while new==old:
                    if match_count<15:
                        time.sleep(3)
                        print 'Waiting..'
                        print(match_count)
                        if match_count==4:
                            try:
                                test_result=browser.find_element_by_xpath('/html/body/div[2]/div/form/span[1]/div[5]/table/tbody/tr[2]/td/table/tbody/tr/td/div[2]/div[2]/div[1]/div[3]/div/div[3]/div/div[2]/div/table/tbody/tr/td[2]').text
                                print test_result
                                if test_result=='You have entered an invalid CAPTCHA keyword. Please try again.':
                                    print 'Wrong Captch'
                                    match_count=0
                                    captcha()
                                if test_result=='No record(s) found.':
                                    result_status=1
                                    print 'No Records Found'
                                    break
                            except:
                                print 'wrong captcha ram'
                        match_count+=1
            #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pt1:r1:0:search:0:pgl6"]/tbody/tr/td[3]/span')))
                        try:
                            new=browser.find_element_by_xpath('//*[starts-with(@id,"pt1:r1:0:search:") and contains(@id, ":pgl6")]/tbody/tr/td[3]/span').text
                        except:
                            #test_result=browser.find_element_by_xpath('/html/body/div[2]/div/form/span[1]/div[5]/table/tbody/tr[2]/td/table/tbody/tr/td/div[2]/div[1]/div/table/tbody/tr/td/table/tbody/tr/td[2]/div').text
                            #print "Result Error  "+test_result
                            result_status=1
                            print 'Result Status Condition Not Satisfied'
                            break
                    else:
                        result_status=1
                        print 'Result Status Condition Not Satisfied'
                        break
                #print 'load success'
                if result_status!=1:
                    count+=1
                    print str(count)+' '+uen
                    sheet1.write(roww,coll,uen)
                    sheet1.write(roww,coll+1,browser.find_element_by_xpath('//*[starts-with(@id,"pt1:r1:0:search:") and contains(@id, ":pgl4")]/tbody/tr/td[2]').text)
        #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pt1:r1:0:search:0:pgl6"]/tbody/tr/td[3]/span')))
                    sheet1.write(roww,coll+2,browser.find_element_by_xpath('//*[starts-with(@id,"pt1:r1:0:search:") and contains(@id, ":pgl6")]/tbody/tr/td[3]/span').text)
                    sheet1.write(roww,coll+3,browser.find_element_by_xpath('//*[starts-with(@id,"pt1:r1:0:search:") and contains(@id, ":pgl9")]/tbody/tr/td[2]/span').text)
                    sheet1.write(roww,coll+4,browser.find_element_by_xpath('//*[starts-with(@id,"pt1:r1:0:search:") and contains(@id, ":pgl23")]/tbody/tr/td[3]').text)
                    address=browser.find_element_by_xpath('//*[starts-with(@id,"pt1:r1:0:search:") and contains(@id, ":pgl23")]/tbody/tr/td[3]').text
                    try:
                        block_number=re.split('\s.*', address)
                        sheet1.write(roww,coll+5,block_number[0])
                    except:
                        pass
                    if '#' in address:
                        try:
                            road_name=re.split('.*?\s(.*)\s#.*', address)
                            sheet1.write(roww,coll+6,road_name[1])
                        except:
                            pass
                        try:
                            unit_no=re.split('.*(#.*?)\s.*', address)
                            sheet1.write(roww,coll+7,unit_no[1])
                        except:
                            pass
                        try:
                            building_name=re.split('.*#.*?\s(.*?)\sSINGAPORE.*', address)
                            sheet1.write(roww,coll+8,building_name[1])
                        except:
                            pass
                    else:
                        try:
                            road_name=re.split('.*?\s(.*)\sSINGAPORE.*', address)
                            sheet1.write(roww,coll+6,road_name[1])
                        except:
                            pass
                    try:
                        postal_code=re.split('.*SINGAPORE\s(\d+)', address)
                        sheet1.write(roww,coll+9,postal_code[1])
                    except:
                        pass
                    sheet1.write(roww,coll+10,'SINGAPORE')
                    sheet1.write(roww,coll+11,browser.find_element_by_xpath('//*[starts-with(@id,"pt1:r1:0:search:") and contains(@id, "pgl36")]/tbody/tr/td[2]/span').text)
                    sheet1.write(roww,coll+12,browser.find_element_by_xpath('//*[starts-with(@id,"pt1:r1:0:search:")]').get_attribute("outerHTML"))
                    old=new
                    roww+=1
                    book.save(output_file_name)
            except Exception as e:
                pass
        search()
        captcha()
        main()
print 'Closing Chrome..'
browser.close()
