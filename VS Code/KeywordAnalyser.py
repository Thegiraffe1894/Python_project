import pandas as pd # type: ignore
#import json

doc = pd.read_csv('condition autocase.csv')
print(doc.head())
print(len(doc))

X = doc.Condition
print(X.shape)
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(stop_words='english')

vect.fit(X)


voc = vect.vocabulary_
#voc1 = eval(voc)
#voc1 =json.dumps(voc)
for row in list(voc):
    #if 'short_description' in row:
       # voc1.pop(row)
    if len(row) != 32 or 'short_description' in row:
        voc.pop(row)

for row in voc:
    print(row)

#print(voc1)
import csv
header = ["keywords","itr"]
with open('KeyWord.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    for row in voc:
        writer.writerow(row)
#print(voc)
#first_col = list(voc.keys())
#sec_col = [sum(voc[key]) for key in voc.keys()]
#arr = list(zip(first_col,sec_col))
#print(voc)
#df=pd.DataFrame() 
#df["TimeTook"] = voc
#writer = pd.ExcelWriter("result.xlsx",engine='xlsxwriter')
#df.to_excel(writer,sheet_name='sheetname')
#writer.save()

#import xlsxwriter

#workbook = xlsxwriter.Workbook('hello.xlsx')
#worksheet = workbook.add_worksheet()

#worksheet.write(voc)
#workbook.close()
