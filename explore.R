train = read.csv("train.tsv", stringsAsFactors = TRUE, sep = "\t")
test = read.csv("test.tsv", stringsAsFactors = TRUE, sep = "\t")

train$train = 1
test$train = 0
test$tag = -1
items = rbind(train, test)

# items$Actors = strsplit(as.character(items$Actors), ",")
items$Actors = NULL #try and separate the actors into one-hot encoded factor variables!
items$Artist.ID = NULL

items$Genre.ID = as.factor(items$Genre.ID)
items$ISBN = as.factor(is.na(items$ISBN))
items$movie = as.factor(items$MPAA.Rating != "")

items$text = paste(as.character(items$Product.Name), as.character(items$Product.Long.Description), as.character(items$Product.Short.Description), as.character(items$Short.Description), as.character(items$Synopsis), sep = " ")
items$Product.Name = NULL
items$Product.Long.Description = NULL
items$Product.Short.Description = NULL
items$Short.Description = NULL
items$Synopsis = NULL
items$text = NULL #Use later for tfidf

#tags = c('4483', '581514', '4537', '1229817', '1229821', '3304195', '1180168', '447913', '522484', '1070524', '95987', '127175', '529295', '106546', '1229825', '1229820', '5065', '4538', '650659', '4536', '1225174', '1071165', '1229819', '62056', '1084835', '1229818', '648819', '4457', '1085065', '133270', '645319', '1229823')
# items[, tags] = NA

#Getting tag values in itags for future reference
items$tag = as.character(items$tag)
items$tag = substr(items$tag, 2, nchar(items$tag) - 1)
items$tag = strsplit(items$tag, ",")
itags = items$tag
items$tag = NULL

library(caret)
dmy = data.frame(predict(dummyVars("~.", data=items), newdata = items))
# items_vectors = with(items, data.frame(item_id, model.matrix(~.-1, items)))

train_ref = subset(dmy, dmy$train == 1)
test_ref = subset(dmy, dmy$train == 0)

train_ref$train = NULL
test_ref$train = NULL
write.table(train_ref, "train_ref.csv", sep = ",", row.names = F, col.names = FALSE)
write.table(test_ref, "train_ref.csv", sep = ",", row.names = F, col.names = FALSE)

