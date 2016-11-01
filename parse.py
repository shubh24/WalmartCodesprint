import csv
data = []
global_tags = []
with open('train.tsv', 'rb') as csvfile:
    
    reader = csv.reader(csvfile, delimiter='\t')

    for row in reader:
        dict = {}
        
        dict["seller"] = row[1]
        dict["actors"] = list(row[2].split(","))
        dict["color"] = row[3]
        dict["aspect_ratio"] = row[6]
        dict["genre"] = row[7]
        dict["isbn"] = row[8] != ""           
        dict["class_id"] = row[9]
        dict["literary_genre"] = row[10]
        dict["mpaa"] = row[11]
        dict["long_desc"] = row[12]
        dict["name"] = row[13]
        dict["short_desc"] = row[14]
        dict["publisher"] = row[15]
        dict["rec_loc"] = row[16]
        dict["rec_room"] = row[17]
        dict["rec_use"] = row[18]
        dict["synopsis"] = row[20]
        dict["tags"] = list(row[22][1:-1].split(","))

        # For getting the unique tags!
        # local_tags = dict["tags"]
        # for tag in local_tags:
        #     if tag.lstrip() not in global_tags:
        #         global_tags.append(tag.lstrip())

        data.append(dict)

    # print global_tags
