#open excel file that has images stored in cells as comments
#save the document as a web page
#this will download all the images to a folder title: yourexcelfile"_files"
#this program will then look at the html document for anchor points that point to each image
import os
from lxml import html
from bs4 import BeautifulSoup

with open('C:/Users/bjsmith/Desktop/trash delete later/testtest image comments_files/sheet001.htm', 'r') as f:
	page = f.read()
soup = BeautifulSoup(page, 'html.parser')
url_path = 'C:/Users/bjsmith/Desktop/trash delete later/testtest image comments_files/'

#need to look for num of anchors
#replace the number 4 with the correct number of anchors


def sku_find_and_rename(i):
	#this will be a function that is called for each number of anchors
	current_anchor = '_anchor_'+i
	anchor_lookup = soup.find('span', id='current_anchor')
	current_sku = anchor_lookup.parent.parent.previous.previous
	#!!!!!need to figure out what to do with leading zeros
	#remove the leading zero once you have figured it out
	current_image = '00'+ i
	os.rename((url_path+'image'+current_image+'.jpg'), (url_path+current_sku+'.jpg'))

for i in range(4):
	sku_find_and_rename(str(i+1))