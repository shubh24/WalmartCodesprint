import sys
import csv

tabin = csv.reader(open("train_tag.tsv", "rb"), dialect=csv.excel_tab)
commaout = csv.writer(open("train_tag.csv", "wb"), dialect=csv.excel)
for row in tabin:
	commaout.writerow(row)

