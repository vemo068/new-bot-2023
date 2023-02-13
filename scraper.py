import requests

from bs4 import BeautifulSoup

def scraptest4():
   url = "http://faculty.univ-eloued.dz/faculty/fse"

   response = requests.get(url)
   soup = BeautifulSoup(response.content, "html.parser")

   for div in soup.find_all("div", {"class": "col-xl-3 col-lg-3 col-md-4 col-sm-6 col-xs-12 px-0"}):
      content = div.find("p", {"class": "mb-1 px-2"}).text
      link = "http://faculty.univ-eloued.dz" + div.find("a")["href"]

      print(content)
     # print(link)


      sub_response = requests.get(link)
      sub_soup = BeautifulSoup(sub_response.content, "html.parser")

      for sub_div in sub_soup.find_all("div", {"class": "col-xl-9 col-lg-9 col-md-9 col-sm-12 px-0 h-100 ms-2"}):
         sub_content = sub_div.find("p").text
         sub_links =  sub_div.find_all("a")
         print("    ", sub_content)
         if len(sub_links)>0:
            for sub_link in sub_links:
               if sub_link["href"].endswith("pdf"):
                  pdfTitle=sub_div.find("span").text
                  print(pdfTitle,"::", sub_link["href"])
               else:
                  print("  ", sub_link["href"])