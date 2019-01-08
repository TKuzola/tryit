'''
Created on Apr 19, 2018

@author: Anthony Kuzola
Script that reads a specified column in and excel woorksheet and prints out
the multi-reddit URL composed of each sumbretit listed in that column
'''
import pandas as pd

file_name = 'C:/Users/tkuzo/Documents/DirtBudget.xlsx'
sheet_name = 'subs'
column_name = 'Tech'
DeeDee = 'ok'
xl_workbook = pd.ExcelFile(file_name)  # Load the excel workbook
data_frame = xl_workbook.parse(sheet_name)  # Parse the sheet into a dataframe
# Cast the desired column into a python list
aList = data_frame[column_name].tolist()
cleanedList = [x for x in aList if str(x) != 'nan']  # remove empty entries

url_contcat_subs = 'https://old.reddit.com/r/' + '+'.join(cleanedList)
print(url_contcat_subs)
if __name__ == '__main__':
    pass
