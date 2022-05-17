# target file
file = open("koko.txt", "rt")
# read file
data = file.read()
# split words
words = data.split()
# print result
print('Number of words in text file :', len(words))