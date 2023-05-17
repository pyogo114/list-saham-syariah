#############################################################
# Membuat list saham syariah dari JII (Jakarta Islamic Index)
# Input membutuhkan data emiten dari JII 
# https://www.idx.co.id/id/data-pasar/data-saham/indeks-saham
# Output berupa csv data dari masing masing emiten.
# CSV data dapat dibuka spreadsheet utk diurutkan berdasarkan
# parameter yang diinginkan. 
# 
# Created by : Priambodo Yoga Sudarsono
# Semarang (2023-05-17)
#############################################################


from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time
from list_saham_syariah import l_saham_syariah

today = datetime.date.today()

for xsaham in l_saham_syariah:
    
    driver = webdriver.Chrome()

    nama_saham = xsaham

    driver.get("https://finance.yahoo.com/quote/" + nama_saham + ".JK/")

    # ambil data dari yahoo finance
    saham_nama = driver.find_elements(By.XPATH,'//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1')
    saham_previous_close = driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[2]')
    saham_open = driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[2]')
    saham_bid = driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[1]/table/tbody/tr[3]/td[2]')
    saham_ask_now =  driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[1]/table/tbody/tr[4]/td[2]')
    saham_52_week = driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[1]/table/tbody/tr[6]/td[2]')
    saham_volume = driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]/fin-streamer')
    saham_avg_volume = driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[2]')
    saham_market_cap = driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[1]/table/tbody/tr[6]/td[2]')
    saham_pe = driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[2]/table/tbody/tr[3]/td[2]')
    saham_eps = driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[2]/table/tbody/tr[4]/td[2]')
    saham_earning_date = driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[2]/table/tbody/tr[5]/td[2]/span')
    saham_forward_devidend = driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[2]/table/tbody/tr[6]/td[2]')
    saham_ex_devidend_date = driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[2]/table/tbody/tr[7]/td[2]/span')
    saham_1y_target = driver.find_elements(By.XPATH,'//*[@id="quote-summary"]/div[2]/table/tbody/tr[8]/td[2]')

    
    time.sleep(3)
    

    data_saham = [
        saham_nama[0].text,
        saham_previous_close[0].text,
        saham_open[0].text,
        saham_bid[0].text,
        saham_ask_now[0].text,
        saham_52_week[0].text,
        saham_volume[0].text,
        saham_avg_volume[0].text,
        saham_market_cap[0].text,
        saham_pe[0].text,
        saham_eps[0].text,
        #saham_earning_date[0].text,
        #saham_forward_devidend[0].text,
        #saham_ex_devidend_date[0].text,
        #saham_1y_target[0].text
        ]
 
    
    driver.close()
    

    with open('data_saham_syariah-' + str(today) + '.csv', 'a') as file:
        for x in data_saham:
            file.write(x + "; ")
        
        file.writelines('\n')
