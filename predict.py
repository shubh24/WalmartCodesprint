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
    shelf = [int(j) for j in shelf]
    
    train_arr.update({item : shelf})

result = {}
for test_case in cos_dict:
    
    counter_dict = {}
    
    for train_case in cos_dict[test_case]:

        for shelf in train_arr[train_case]:
    
            if shelf not in counter_dict:
                counter_dict[shelf] = 1
            else:
                counter_dict[shelf] += 1

    max_shelf_val = counter_dict[max(counter_dict, key = lambda x:counter_dict[x])]
    top_shelves = [shelf for shelf, count  in counter_dict.items() if count == max_shelf_val]

    result.update({str(test_case):str(top_shelves)})

f = open("result.csv", "wb")
f_writer = csv.writer(f, delimiter = "\t", dialect = "excel")

for r_row, r_val in result.items():
    f_writer.writerow([r_row, r_val])

f.close()