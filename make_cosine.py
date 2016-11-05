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
for i in test_reader:    
    val = i[1:]
    val_int = [int(j) for j in val]
    test_arr.update({int(i[0]):val_int})

train_arr = {}
for i in train_reader:    
    val = i[1:]
    val_int = [int(j) for j in val]
    train_arr.update({int(i[0]):val_int})


cos_dict = {i:{} for i in test_arr}
c = 0
for test_case in test_arr:
    print c
    c+=1
    test_case_cos_arr = {}

    for train_case in train_arr:
        test_case_cos_arr.update({train_case:get_cosine(train_arr[train_case], test_arr[test_case])})
    
    cos_dict[test_case] = sorted(test_case_cos_arr, key = lambda x : test_case_cos_arr[x], reverse = True)[:50]

with open('cos_dict.pickle', 'wb') as handle:
    pickle.dump(cos_dict, handle)
