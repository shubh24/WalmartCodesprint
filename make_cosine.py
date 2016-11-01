import csv
import math

def get_cosine(v1, v2):
    v1 = [int(i) for i in v1]
    v2 = [int(i) for i in v2]

    sumxx, sumxy, sumyy = 0, 0, 0
    
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    
    if sumxx == 0 or sumyy == 0: 
        return 0
    else:      
        return sumxy/math.sqrt(sumxx*sumyy)

train = open("train_ref.csv", "r")
train_reader = csv.reader(train)


test = open("test_ref.csv", "r")
test_reader = csv.reader(test)

test_arr = {}
for i in test_arr:    
    test_arr.update({i[0]:i[1:]})

train_arr = {}
for i in train_reader:    
    train_arr.update({i[0]:i[1:]})


cos_dict = {i:{} for i in test_arr}
