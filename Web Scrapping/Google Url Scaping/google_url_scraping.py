from bs4 import BeautifulSoup
import requests
import os 

#taking search key from user
print("What do you want to search in google: ", end="")
search_key = input()

#google parameters that we are not robot
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"
}

parameter= {
    "q": search_key, 
    "hl": "en"  # only shows english results
}

#taking html file
html_file = requests.get("https://www.google.com/search", params = parameter, headers= headers )
soup = BeautifulSoup(html_file.text, "lxml")

#finding all files 
main_div = soup.find_all("div", class_="yuRUbf")

print(os.path.abspath("."))
#opening file for 
with open(                os.path.join(  os.path.abspath(".")+"\\Web Scrapping\\Google Url Scaping","url_found.txt")      ,"a"           ) as save_File:
    #finding all links
    for elements in main_div:
        url_finder = elements.find("a").get("href")
        save_File.write(url_finder + str("\n"))
    #seperator for every search
    save_File.write("-"*20)
