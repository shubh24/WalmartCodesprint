import pickle
import csv

with open('cos_dict.pickle', 'r') as handle:
    cos_dict = pickle.load(handle)

train = open("train_tag.csv", "r")
train_reader = csv.reader(train)

train_arr = {}
for row in train_reader:    

    if row[0] == "item_id":
        continue
    
    item = int(row[0])
    
    shelf = list(row[1][1:-1].split(","))
    shelf_ref = [int(j) for j in shelf]
    
    train_arr.update({item : shelf})


