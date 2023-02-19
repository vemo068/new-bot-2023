import requests
from faculty import Faculty
from telegramee import send_message_with_photo_pdfs
import telegram_env as televars
import asyncio
from bs4 import BeautifulSoup
import sheet

async def telenews_scraping(faculty:Faculty):
   url = faculty.website

   response = requests.get(url)
   soup = BeautifulSoup(response.content, "html.parser")
   all_divs=soup.find_all("div", {"class": "col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12 px-0"})
   ten_divs=all_divs[0:8]
   for div in ten_divs:
      content = div.find("p", {"class": "mb-1 px-2"}).text
      if sheet.checkNews(faculty.sheetName,content):
         link = "http://faculty.univ-eloued.dz" + div.find("a")["href"]
         photo_url="http://faculty.univ-eloued.dz"+div.find("img")["src"]
         


         sub_response = requests.get(link)
         sub_soup = BeautifulSoup(sub_response.content, "html.parser")

         for sub_div in sub_soup.find_all("div", {"class": "body px-2 mt-2 row mx-0"}):
            spans = []
            links=[]
            description=""
            sub_content = sub_div.find_all("p")
            for des in sub_content:
               description=description+des.text+"\n"
            
   #         sub_links =  sub_div.find_all("a")['href']
            divs = sub_soup.find_all('div', {'class': 'col-6 py-2 col-sm-6 col-md-4 col-xl-3 col-lg-4'})
            for div in divs:
               link = div.find('a')
            
               if link:
                  links.append(link['href'])
               else:
                  links.append(None)
               span = div.find('span').text.strip()
               spans.append(span)
            try: 
               sent_message= await send_message_with_photo_pdfs(televars.api_key,faculty.chat_id,photo_url,content,description,link,links,spans)
               if sent_message is not None:
                  sheet.insert_news(content,faculty.sheetName)
               else :
                  print("not sent")
            except Exception as e:
               print(e)
      print('finished'+faculty.sheetName)

