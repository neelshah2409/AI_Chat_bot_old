import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests as r


# News Scarap
#############################################################
# html_page = r.get("https://www.aicte-india.org/news?date_value%5Bvalue%5D=").text

# scrap = BeautifulSoup(html_page, "lxml")
# multi_news = scrap.find("div",class_="item-list")
#
# for news in multi_news.ul.find_all("li"):
#     print(news.find("div",class_='content-group views-fieldset').div.div.span.text)
#     print(news.find("div",class_='content-group views-fieldset').find("div",class_="views-field views-field-nothing").span.a['href'])
#     print(news.find("div",class_='content-group views-fieldset').find("div",class_="views-field views-field-nothing").span.a.text)
#     print(news.find("div",class_='content-group views-fieldset').find("div",class_="views-field views-field-field-news-overview-text").div.text)
#
#
# for i in range(1,8):
#     html_page = r.get(f'https://www.aicte-india.org/news?date_value%5Bvalue%5D=&page={i}', "lxml").text
#     print(html_page)

# scrap = BeautifulSoup(html_page)
# multi_news = scrap.find("div", class_="item-list")
#
# for news in multi_news.ul.find_all("li"):
#     print("\n\n")
#     print(news.find("div", class_='content-group views-fieldset').div.div.span.text)
#     print(news.find("div", class_='content-group views-fieldset').find("div",class_="views-field views-field-nothing").span.a['href'])
#     print(news.find("div", class_='content-group views-fieldset').find("div",class_="views-field views-field-nothing").span.a.text)
#     print(news.find("div", class_='content-group views-fieldset').find("div",class_="views-field views-field-field-news-overview-text").div.text)




# Student Development Scheme
##########################################################
# html_page = requests.get("https://www.aicte-india.org/schemes/students-development-schemes").text
#
# scrap = BeautifulSoup(html_page,"lxml")
#
# student_schemes = scrap.find("div",class_="schemes_html lzt_html")
#
# temp = ""
# queAns = []
i = 0
# for schemes in student_schemes.find_all("div"):
#     # print("\n\n")
#
#     # print(f"What is {schemes.h5.text.strip()}?")
#     if temp != "":
#         temp = temp+f", {schemes.h5.text.strip()}"
#     else:
#         temp = temp + f"{schemes.h5.text.strip()}"
#     if schemes.ul is not None:
#         tempDict = {"tag": f"Data-{i}", "patterns": [
#             f"What is {schemes.h5.text.strip()}?"
#         ], "responses": f"{schemes.h5.text.strip()} {schemes.p.text.strip()} For More Information : <a href = '{schemes.ul.li.a['href'].replace(' ','')}'>{schemes.ul.li.a.text.strip()}</a>" }
#     else:
#         tempDict = {"tag": f"Data-{i}", "patterns": [
#             f"What is {schemes.h5.text.strip()}?"
#         ], "responses": f"{schemes.h5.text.strip()} {schemes.p.text.strip()}"}

#     i += 1
#     queAns.append(tempDict)
#
# tempDict = {"tag": f"Data-{i}", "patterns": [
#             f"What are the available schemes for student ?"
#         ], "responses": f"Available Schemes Are : {temp}"}
#
# i += 1
# queAns.append(tempDict)
#
# print(queAns)
#



# Faculty Development Scheme
##########################################################
html_page = requests.get("https://internship.aicte-india.org").text

scrap = BeautifulSoup(html_page,"lxml")

student_schemes = scrap.find("div",class_="state")
temp=""
queans=[]
que=[]
ans=[]
# i=0
for schemes in student_schemes.find_all("div"):
    with open('scrap.txt','a') as f:
        f.writelines(f"What is {schemes.h5.text.strip()} SCHEME?\n")
        if temp != "":
            temp = temp+f", {schemes.h5.text.strip()}"
        else:
            temp = temp + f"{schemes.h5.text.strip()}"

        text = temp = schemes.p.text.strip().replace('\n',' ')
        if schemes.ul is not None:
            # tempDict = {"tag": f"Data-{i}", "patterns": [
            #     f"What is {schemes.h5.text.strip()}?"
            # ],
            #             "responses": f"{schemes.h5.text.strip()}\n{temp}\nFor More Information : <a href = '{schemes.ul.li.a['href'].replace(' ', '')}'>{schemes.ul.li.a.text.strip()}</a>"}
            # f.writelines(f"{schemes.h5.text.strip()}\n{temp}\nFor More Information : {schemes.ul.li.a['href'].replace(' ','')}\n")
            que.append(f"What is {schemes.h5.text.strip()}?") #NEW
            ans.append(f"{schemes.h5.text.strip()}\n{temp}\nFor More Information : <a href = '{schemes.ul.li.a['href'].replace(' ', '')}'>{schemes.ul.li.a.text.strip()}</a>") #NEW

        else:
            # tempDict = {"tag": f"Data-{i}", "patterns": [
            #     f"What is {schemes.h5.text.strip()}?"
            # ], "responses": f"{schemes.h5.text.strip()} {schemes.p.text.strip()}"}
            # f.writelines(f"{schemes.h5.text.strip()}\n{temp}\nFor More Information : {schemes.ul.li.a['href'].replace(' ', '')}\n")
            que.append(f"What is {schemes.h5.text.strip()}?") #NEW
            ans.append(f"{schemes.h5.text.strip()}\n{temp}\nFor More Information : {schemes.ul.li.a['href'].replace(' ', '')}\n") #NEW
        i += 1
        f.writelines("\n")
        # queans.append(tempDict)


# with open('scrap.txt','a') as f:
#     f.writelines(f"What are the available schemes for student ?\n")
#     f.writelines(f"Available Schemes Are : {temp}")
#     # tempDict = {"tag": f"Data-{i}", "patterns": [
#     #             f"What are the available schemes for student ?"
#     #         ], "responses": f"Available Schemes Are : {temp}"}
#     f.writelines("\n")

i += 1
# queans.append(tempDict)

# print(queans)


csvData = {"que" : que, "ans" : ans}

df = pd.DataFrame(csvData)

print(df.to_csv("events.csv",index=False))




# Institutional Development Scheme
##########################################################
# html_page = requests.get("https://www.aicte-india.org/schemes/institutional-development-schemes").text
#
# scrap = BeautifulSoup(html_page,"lxml")
#
# student_schemes = scrap.find("div",class_="schemes_html lzt_html")
#
# for schemes in student_schemes.find_all("div"):
#     print(schemes.h5.text.strip())
#     print(schemes.p.text.strip())
#     for sub in schemes.ul.find_all("li"):
#         print(sub.a.text)
#         print(sub.a['href'].replace(" ", ""))




# Research & Innovations Development Schemes
##########################################################
# html_page = requests.get("https://www.aicte-india.org/schemes/research-innovations-development-schemes").text
#
# scrap = BeautifulSoup(html_page,"lxml")
#
# student_schemes = scrap.find("div",class_="schemes_html lzt_html")
#
# for schemes in student_schemes.find_all("div"):
#     print(schemes.h5.text.strip())
#     print(schemes.p.text.strip())
#     for sub in schemes.ul.find_all("li"):
#         print(sub.a.text)
#         print(sub.a['href'].replace(" ", ""))





# General Schemes
##########################################################
# html_page = requests.get("https://www.aicte-india.org/schemes/other-schemes").text
#
# scrap = BeautifulSoup(html_page,"lxml")
#
# student_schemes = scrap.find("div",class_="schemes_html lzt_html")
#
# for schemes in student_schemes.find_all("div"):
#     print(schemes.h5.text.strip())
#     print(schemes.p.text.strip())
#     for sub in schemes.ul.find_all("li"):
#         print(sub.a.text)
#         print(sub.a['href'].replace(" ", ""))




# Oppertunities for students
######################################################################################################
# html_page = requests.get("https://www.aicte-india.org/opportunities/students/overview").text
#
# scrap = BeautifulSoup(html_page, "lxml")
#
# student_opp = scrap.find('section', id = "col_nats")
#
#
# for opps in student_opp.find_all("div"):
#     for subopp in opps.find_all("article"):
#         print(subopp.h3.text)
#         if subopp.find("p") is not None:
#             print(subopp.p.text)
#         # print(opps.p.text)
#         print(subopp.a['href'].replace(" ",""))
#         print(subopp.a.text)




# library services
#####################################################################################################
# html_page = requests.get("https://www.aicte-india.org/education/library-services").text
# scrap = BeautifulSoup(html_page, "lxml")
#
# library_service = scrap.find('div', class_="collaboration_html library_html lzt_html")
#
# for lists in library_service.ul.find_all("li"):
#     print(lists.a.text)
#     print(lists.a['href'])
#


# bulletins/circulars
#####################################################################################################
#
# html_page = requests.get("https://www.aicte-india.org/bulletins/circulars").text
# scrap = BeautifulSoup(html_page, "lxml")
# circular = scrap.find('table', class_="views-table cols-4")
#
# for rows in circular.tbody.find_all("tr"):
#     for alltd in rows.find_all('td'):
#         if(alltd.span is not None):
#             print(alltd.span.text)
#     title=rows.find('td',class_="views-field views-field-title")
#     print(title.text)
#     for alltd in rows.find_all('td'):
#         if(alltd.a is not None):
#             print(alltd.a.text)
#             print(alltd.a['href'])



# Startup contest
####################################################################################################

# html_page = requests.get("https://www.aicte-india.org/Initiatives/startup-contest-2017").text
# scrap = BeautifulSoup(html_page, "lxml")
# sc = scrap.find('div', class_="contest_html lzt_html keep_space")
#
# for items in sc.find_all("p"):
#     print(items.text)
#
# for dots in sc.section.ul.find_all("li"):
#     print(dots.text)


