#from siraj ravels example: https://github.com/llSourcell/How_to_use_Tensorflow_for_classification-LIVE
#tensorflow/anyother classifier to predict 0/1 (dropship/instock)
#based on kevin larkins past history
#he has been doing all the decisions; i assume that he has been
#doing a good job
#from siraj's code:
#we should convert dropship and instock to boolean values
#eg dropship = 0; instock = 1
#use classifier to classify if sku is 0/1


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

#loading dataset as a dataframe using pandas
#dataframe = pd.read_csv('datafilename.csv')
#						  ^^^^^^^^^^^^^^^^^ update filename!!!!!!!!!!!!!!!!!!!!!!!


#also need to severly clean the data
#convert dropship/instock to boolean
#determine which indices(columns) whould be included (maybe all of them?)
#find empty cells; delete/fill them
#are outliers important to get rid of?
#need to consider more
#his code included below: used to remove nonimportant columns
#dataframe = dataframe.drop(['index', 'price', 'sq_price'], axis=1)

#seperate input matrix from labels matrix
#here input are various things: eg size, quant. sold, price, etc
#output matrix is 1/0 values from dropship/instock

#input matrix is somewhat simple; just include interesting columns
#input_matrix = dataframe.loc[:, ['size', 'quant_sold', 'etc']].as_matrix()

#output matrix has 
#label_matrix = dataframe.loc[:, ['']]





