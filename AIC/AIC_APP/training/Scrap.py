from bs4 import BeautifulSoup
import requests
import re

def getData(data):
    page = requests.get(data).text
    soup = BeautifulSoup(page,'lxml')
    # for i in soup.find_all('a'):
    #     if re.search("^https:",i['href'].replace(' ','')) or re.search("^http:",i['href'].replace(' ','')):
    #         try:
    #             link = requests.get(i['href'].replace(' ','')).text
    #             if link is not None:
    #                 tempContent = BeautifulSoup(link,'lxml')
    #                 for j in tempContent.find_all(['h1','h2','h3','h4','h5','h6','h7','p']):
    #                     print(j.text.strip().replace('\n','') if len((j.text.strip()).split(' '))>20 else "")
    #                 with open('scrapped','a',encoding='utf-8') as f:
    #                     f.writelines(j.text if len((j.text.strip().replace('  ','')).split(' '))>20 else "")
    #         except:
    #             pass
    #     else:
    #         print("Extra https://www.aicte-india.org"+i['href'].replace(' ',''))
    #         try:
    #             link = requests.get(i['href'].replace(' ', '')).text
    #             if link is not None:
    #                 tempContent = BeautifulSoup(link, 'lxml')
    #                 for j in tempContent.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'p']):
    #                     print(j.text.strip().replace('\n', '') if len((j.text.strip()).split(' ')) > 20 else "")
    #                 with open('scrapped', 'a', encoding='utf-8') as f:
    #                     f.writelines(j.text if len((j.text.strip().replace('  ', '')).split(' ')) > 20 else "")
    #         except:
    #             pass

    data = ""
    for i in soup.find_all(['h1','h2','h3','h4','h5','h6','h7','p']):
        data += i.text.strip()
    return data
