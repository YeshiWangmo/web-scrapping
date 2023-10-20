#objective of this code is to fetch HTML content of a webpage using the 'requests' & then parse that content using'BeautifulSoup' library
# web scrapping/ to extract content and data from a website instead of screen scraping.
#For auto-fetch of data from particular webpage
# Requests allows you to send HTTP 
# There’s no need to manually add query strings to your URLs 
import requests
from bs4 import BeautifulSoup # HTML web scrapping using tool like bs4(BeautifulSoup)
url= input("Enter your url:")
response = requests.get(url) #step1: get the HTML
                             #using 'requests'library to send an HTTP get request to the specified URL

#step2: parse the HTML(converts it into a structured format)
#'BeautifulSoup' library to parse that HTML content and create a BeautifulSoup object 'soup'

soup = BeautifulSoup(response.content, 'html.parser')


print(soup.get_text) #print code into text /'soup' object to extract the text from the parsed HTML
                     #other way to print the soup - #print(soup.prettify );to print the soup into nicely formatted Unicode string.







 


