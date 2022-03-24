#!/usr/bin/env python3
import json
import requests
from bs4 import BeautifulSoup
from os import link
from dotenv import load_dotenv
from urllib.parse import urlunsplit, urlencode
import requests as rq
import json
import dotenv
from urllib.request import urlopen
from datetime import datetime
from lxml import etree
from datetime import datetime
from lxml import etree
from csv import writer
from time import perf_counter
from threading import Thread

"""
configurations
"""

CONFIG = dotenv.dotenv_values()
html = etree.Element("html")

def scrape_site(x, y):
        
        for i in range(x, y):
            if i < 1000:
                i = str(i).zfill(4)        
            try:
                try:
                    url ="https://www.colisprive.com/moncolis/pages/detailColis.aspx?numColis="+CONFIG['SPECIAL']+str(i)+CONFIG['ZIP']
                     
                    page = requests.get(url).text
                except:
                    print("impossible to load the website")
                try:
                    soup = BeautifulSoup(page, 'html.parser')
                    dom = etree.HTML(str(soup))
                    TRACKINGID = dom.xpath('//*[@id="ctl00_ContentDetailColis_pnResultatColis"]/div[1]/div/div[1]/div')[0]
                    ID = TRACKINGID.text
                    data = {
                    "username": CONFIG['EMBEDUSERNAME'],
                    "embeds": [{
                        "title": "TRACKING FOUND : " + str(ID),
                        "color": int(CONFIG['COLOUR']),
                        "footer": {"text": CONFIG['FOOTERTEXT']},
                        "timestamp": str(datetime.utcnow()),
                        "url": url,
                        
                        }]
                    }
                    result = rq.post(CONFIG['WEBHOOK'], data=json.dumps(data), headers={"Content-Type": "application/json"})
                    with open('TRACKINGIDS.csv', 'a', newline='') as inp:
                                                writer_object = writer(inp)
                                                list_data = ["track :", str(ID)]
                                                writer_object.writerow(list_data)  
                                                inp.close()
                except:
                    print(url)
                                  
            except:
                print("Searching ...")
                pass
           
start_time = perf_counter()
threads = []
def main():
        t0 = Thread(target=scrape_site, args=(1000,1500)).start()
        t1 = Thread(target=scrape_site, args=(1500,2000)).start()
        t2 = Thread(target=scrape_site, args=(2000,2500)).start()
        t3 = Thread(target=scrape_site, args=(2500,3000)).start()
        t4 = Thread(target=scrape_site, args=(3000,3500)).start()
        t5 = Thread(target=scrape_site, args=(3500,4000)).start()
        t6 = Thread(target=scrape_site, args=(4000,4500)).start()
        t7 = Thread(target=scrape_site, args=(4500,5000)).start()
        t8 = Thread(target=scrape_site, args=(5000,5500)).start()
        t9 = Thread(target=scrape_site, args=(5500,6000)).start()
        t10 = Thread(target=scrape_site, args=(6000,6500)).start()
        t11 = Thread(target=scrape_site, args=(6500,7000)).start()
        t12 = Thread(target=scrape_site, args=(7000,7500)).start()
        t13 = Thread(target=scrape_site, args=(7500,8000)).start()
        t14 = Thread(target=scrape_site, args=(8000,8500)).start()
        t15 = Thread(target=scrape_site, args=(8500,9000)).start()
        t16 = Thread(target=scrape_site, args=(9000,9500)).start()
        t17 = Thread(target=scrape_site, args=(9500,9999)).start()
        t18 = Thread(target=scrape_site, args=(0,500)).start()
        t19 = Thread(target=scrape_site, args=(500,1000)).start()
    
if __name__ == '__main__':
    main()
