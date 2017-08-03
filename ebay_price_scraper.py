import requests
from bs4 import BeautifulSoup
import openpyxl
import time
import random


#create a list from the excel file
#function to download prices from ebay by being passed a keyword to search
#if there are a limited number of results the scraper is not smart enought to distinguish between results and other suggested items 
#it is important to pass UPC as the keyword to prevent other results from showing

#this should probably be read from an excel sheet
ship_cost_dictionary = {1:4.16,2:4.54,3:4.82,4:5.12,5:5.3,	6:5.37,7:5.52,8:5.69,9:5.81,10:8.55,11:7.2,12:7.2,13:7.3,14:7.56,15:7.86,16:8.03,17:8.35,18:8.65,19:8.77,20:9.08,21:9.38,22:9.69,23:9.99,24:10.39,25:10.6,26:10.94,27:11.23,28:11.78,29:12.06,30:12.23,31:12.45,32:12.65,33:13.05,34:13.26,35:13.55,36:13.84,37:14.1,38:14.38,39:14.71,40:14.97,41:15.27,42:15.59,43:16.06,44:16.19,45:16.43,46:16.68,47:16.88,48:17.11,49:17.3,50:17.35,51:17.37,52:17.38,53:17.4,54:17.41,55:17.43,56:17.45,57:17.46,58:17.51,59:17.66,60:17.8,61:17.94,62:18.05,63:18.16,64:18.4,65:18.5,66:18.6,67:18.7,68:18.8,69:18.9,70:19.2,71:19.5,72:19.6,73:19.8,74:20.1,75:20.5,76:20.7,77:20.8,78:20.9,79:21.35,80:21.7,81:21.9,82:21.99,83:22.24,84:22.53,85:22.76,86:23.04,87:23.28,88:23.53,89:23.76,90:23.83,91:23.86,92:24.15,93:24.33,94:24.59,95:24.74,96:24.87,97:25.15,98:25.42,99:25.69,100:25.95,101:25.97,102:26.2,103:26.66,104:26.67,105:26.89,106:27.12,107:27.36,108:27.59,109:27.82,110:28.07,111:28.3,112:28.52,113:28.76,114:28.99,115:29.22,116:29.41,117:29.63,118:29.86,119:30.1,120:30.33,121:30.51,122:30.74,}




def ebay_price_lookup(ebay_url):
#used to 
	ebay_List = []
	#sets the ebay url with query selectors
	#&LH_BIN=1  requires buy it now items
	#LH_FS=1    requires free shipping (workaround:couldn't figure out how to scrape shipping price)
	#&_sop=15   price + shipping: set as priority
	ebay_url_prepend = 'https://www.ebay.com/sch/i.html?LH_BIN=1&LH_FS=1&_sop=15&_nkw='
	#pulls the html page using the url prepend and passed keywords
	r = requests.get(ebay_url_prepend + str(ebay_url))
	ebay_page_soup = BeautifulSoup(r.text, 'html.parser')
	#search for all bold tags (only price has a span w/ class "bold")
	price_list = ebay_page_soup.find_all('span', class_= 'bold')
	for i in price_list:
		#replace filler html
		ebay_List.append(i.text.replace('\n', '').replace('\t', ''))
	return (ebay_List)

#read excel file with list of SKU UPC's in column A of the Active Sheet
excel_workbook = openpyxl.load_workbook('testtest.xlsx')
excel_sheet = excel_workbook.active

#Keywords (UPCs) should be placed in Column A; current prices in Column B; 
#the following will pull the data from excel and query ebay for the provided UPCs
price_lookup=[]
excel_columns = tuple(excel_sheet.columns)
for i in range(len(excel_columns[0])):
    time.sleep(random.randit(5,20)/10)
    if excel_columns[0][i].value is not None:
        price_lookup.append(ebay_price_lookup(excel_columns[0][i].value))
    else:
        price_lookup.append(['error in url'])

#need to calculate dimensional weight from dimensions
#lookup shipping price by dim_weight
#do some calculations to figure out a zone where we still make x amount of profit
#profit should be different based on the cost of the item (eg make more money on running boards than ventvisors)
ship_cost = []
purchase_cost = []

for i in range(len(excel_columns[0])):
    dimensions = sorted([excel_columns[3][i].value, excel_columns[4][i].value, excel_columns[5][i].value])
    package_weight = excel_columns[6][i].value
    package_volume = dimensions[0]*dimensions[1]*dimensions[2]
    
    if package_volume >= 1728:
        dimensional_weight_denomenator = 166
    else:
        dimensional_weight_denomenator = 139
    dimensional_weight = package_volume/dimensional_weight_denomenator
    large_package_check = 2*dimensions[0]+2*dimensions[1]*2 + dimensions[2]
    if large_package_check > dimensional_weight:
        dimensional_weight = 90
    billable_weight = max(dimensional_weight, package_weight)
    ship_cost.append(ship_cost_dictionary[billable_weight ])
    purchase_cost.append(excel_columns[2][i].value)
    
 
#this is the old lookup function
#it was changed becauase of requiring additional excel columns
"""
url_list = excel_sheet['A']
#pricing will be saved to a new sheet titled: Price Sheet
excel_write_to_sheet = excel_workbook.create_sheet("Price_Sheet", 0)

for current_col in range(len(url_list)):
	#call download function and store the price for current skus in a list, checking to see if the cell is blank
	#insert the sku back in front of the prices to see which prices go to which skus
	if url_list[current_col].value is not None:
		current_sku_price = ebay_price_lookup(url_list[current_col].value)
		current_sku_price.insert(0, url_list[current_col].value)
	else:
		current_sku_price = ['error in url']
	#write current row to excel sheet
	excel_write_to_sheet.append(current_sku_price)
	#delay for random interval (.5 to 2 seconds) to simulate human clicking
	time.sleep(random.randint(5,20)/10)

#save to new workbook titled 'filename'
excel_workbook.save(filename='scrapetest.xlsx')
"""