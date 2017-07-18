import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import openpyxl
import time

#read excel file with list of skus
#create a list from the excel file


def ebay_price_lookup(ebay_url):
	ebay_List = []
	r = requests.get(ebay_url)
	ebay_page_soup = BeautifulSoup(r.text, 'html.parser')
	price_list = ebay_page_soup.find_all('span', class_= "bold")
	for i in price_list:
		ebay_List.append(i.text.replace('\n', '').replace('\t', ''))
	return (ebay_List)


excel_workbook = openpyxl.load_workbook('testtest.xlsx')
excel_sheet = excel_workbook.active
url_list = excel_sheet['A']
excel_write_to_sheet = excel_workbook.create_sheet("Price_Sheet", 0)

for current_col in range(len(url_list)):
	#call download function and store the price for current skus in a list
	current_sku_price = ebay_price_lookup(url_list[current_col].value)
	#insert the sku back in front of the prices to see which prices go to which skus
	current_sku_price.insert(0, url_list[current_col].value)
	excel_write_to_sheet.append(current_sku_price)
	time.sleep(1)

excel_workbook.save(filename='samplesample.xlsx')