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
#page_content=''
print 'Launching Chrome..'
#prox = Proxy()
#prox.proxy_type = ProxyType.MANUAL
#prox.http_proxy = "127.0.0.1:9667"
#prox.socks_proxy = "127.0.0.1:9667"
#prox.ssl_proxy = "127.0.0.1:9667"
#capabilities = webdriver.DesiredCapabilities.CHROME
#prox.add_to_capabilities(capabilities)
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--incognito")
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
browser = webdriver.Chrome(executable_path='C:\Users\lenovo\Desktop\python\chromedriver.exe',chrome_options=options,desired_capabilities=capa)
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
                    browser.find_element_by_xpath('//*[@id="pt1:r1:0:cb1"]').click()
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
            try:
                wait = WebDriverWait(browser, 20)
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pt1:r1:0:it1::content"]')))
                test=browser.find_element_by_xpath('//*[@id="pt1:r1:0:r1:0:it1::content"]')
                print 'Clearing Cookies'
                browser.get("about:blank")
                browser.delete_all_cookies()
                time.sleep(3)
                browser.get('https://www.tis.bizfile.gov.sg/ngbtisinternet/faces/oracle/webcenter/portalapp/pages/TransactionMain.jspx?selectedETransId=dirSearch#%40%3FselectedETransId%3DdirSearch%26_adf.ctrl-state%3Dxtehpl541_9')
                captcha()
            except:
                main()
        def main():
            search()
            global old
            #global sheet1 = book.get_sheet(0)
            global count
            global roww
            global coll
            try:
                wait = WebDriverWait(browser, 25)
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[starts-with(@id,"pt1:r1:0:search:")]')))
                time.sleep(3)
        #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pt1:r1:0:search:0:pgl6"]/tbody/tr/td[3]/span')))    
                new=browser.find_element_by_xpath('//*[starts-with(@id,"pt1:r1:0:search:") and contains(@id, ":pgl6")]/tbody/tr/td[3]/span').text
                #print new
                count+=1
                print str(count)+' '+uen
                match_count=0
                while new==old:
                    if match_count<10:
                        time.sleep(2)
                        #print 'Waiting..'
                        match_count+=1
            #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pt1:r1:0:search:0:pgl6"]/tbody/tr/td[3]/span')))
                        try:
                            new=browser.find_element_by_xpath('//*[starts-with(@id,"pt1:r1:0:search:") and contains(@id, ":pgl6")]/tbody/tr/td[3]/span').text
                        except:
                            search()
                    else:
                        break
                #print 'load success'
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
            #pyautogui.hotkey('F5')
            #pyautogui.hotkey('ENTER')   
            except Exception as e:
                #print(e)
                #print 'fetch problem'
                #continue
                search()
        captcha()
        #if checking==1:
            #main()
        #else:
            #browser.close()
            #time.sleep(1)
            #browser = webdriver.Chrome(executable_path='C:\Users\lenovo\Desktop\python\chromedriver.exe',chrome_options=options,desired_capabilities=capa)
            #time.sleep(1)
            #browser.get("about:blank")
            #browser.delete_all_cookies()
            #time.sleep(3)
            #browser.execute_script('window.localStorage.clear();')
            #browser.execute_script('localStorage.clear();')
            #time.sleep(1)
            #browser.get("about:blank")
            #browser.delete_all_cookies()
            #browser.get('https://www.tis.bizfile.gov.sg/ngbtisinternet/faces/oracle/webcenter/portalapp/pages/TransactionMain.jspx?selectedETransId=dirSearch#%40%3FselectedETransId%3DdirSearch%26_adf.ctrl-state%3Dxtehpl541_9')        
            #main()
print 'Closing Chrome..'
browser.close()
