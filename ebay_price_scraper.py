import requests
from bs4 import BeautifulSoup
import openpyxl
import time
import random


#create a list from the excel file
#function to download prices from ebay by being passed a keyword to search
#if there are a limited number of results the scraper is not smart enought to distinguish between results and other suggested items 
#it is important to pass UPC as the keyword to prevent other results from showing

def ebay_price_lookup(ebay_url):
	#used to 
	ebay_List = []
	#sets the ebay url with query selectors
	#&LH_BIN=1  requires buy it now items
	#LH_FS=1    requires free shipping (workaround:couldn't figure out how to scrape shipping price)
	#&_sop=15   price + shipping: set as priority
	ebay_url_prepend = 'https://www.ebay.com/sch/i.html?LH_BIN=1&LH_FS=1&_sop=15&_nkw='
	#pulls the html page using the url prepend and passed keywords
	r = requests.get(str(ebay_url_prepend + str(ebay_url))
	ebay_page_soup = BeautifulSoup(r.text, 'html.parser')
	#search for all bold tags (only price has a span w/ class "bold")
	price_list = ebay_page_soup.find_all('span', class_= 'bold')
	for i in price_list:
		#replace filler html
		ebay_List.append(i.text.replace('\n', '').replace('\t', ''))
	return (ebay_List)

#read excel file with list of SKU UPC's in column A of the Active Sheet
excel_workbook = openpyxl.load_workbook('Mozenda.xlsx')
excel_sheet = excel_workbook.active
#Keywords should be placed in Column A
url_list = excel_sheet['A']
#pricing will be saved to a new sheet titled: Price Sheet
excel_write_to_sheet = excel_workbook.create_sheet("Price_Sheet", 0)

for current_col in range(len(url_list)):
	#call download function and store the price for current skus in a list, checking to see if the cell is blank
	if url_list[current_col] != None
		current_sku_price = ebay_price_lookup(url_list[current_col].value)
	else:
		current_sku_price = 'error in url'
	#insert the sku back in front of the prices to see which prices go to which skus
	current_sku_price.insert(0, url_list[current_col].value)
	#write current row to excel sheet
	excel_write_to_sheet.append(current_sku_price)
	#delay for random interval (.5 to 2 seconds) to simulate human clicking
	time.sleep(random.randint(5,20)/10)

#save to new workbook titled 'filename'
excel_workbook.save(filename='scrapetest.xlsx')