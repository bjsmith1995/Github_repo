#open excel file that has images stored in cells as comments
#save the document as a web page
#this will download all the images to a folder title: yourexcelfile"_files"
#this program will then look at the html document for anchor points that point to each image
#note only works with single worksheets at a time
#break up the sheets into seperate workbooks and repeat

import os
from bs4 import BeautifulSoup

#location of saved web page
#please note!!! this is the location of the file 'Sheet001.htm' and the location of the images
url_path = 'C:/Users/bjsmith/Desktop/lincoln steel testing/MUP_skus_files/'
with open(url_path+'sheet001.htm', 'r') as f:
	page = f.read()
soup = BeautifulSoup(page, 'html.parser')

def sku_find_and_rename(i):
	#this is a function that find the cell directly to the left of the image
	current_anchor = '_anchor_'+str(i)
	anchor_lookup = soup.find('span', id=current_anchor)
	#for the above. Like to add a check to see if there was none as a find
	#if type(anchor_lookup) = None:
	#	do nothing
	#else:
	#	do everything below this	
	current_sku = anchor_lookup.parent.parent.previous.previous
	#remove the leading zero once you have figured it out
	if 1<=i<10:
		current_image = '00'+ str(i)
	elif 10<=i<100:
		current_image = '0'+ str(i)
	else:
		current_image = str(i)
	os.rename((url_path+'image'+current_image+'.jpg'), (url_path+current_sku+'.jpg'))

#need to look for num of anchors
#replace the number in the range with the correct number of anchors

for i in range(1, 1584+1):
	sku_find_and_rename(i)