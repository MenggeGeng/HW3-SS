from nltk.book import *
import sys
sys.path.append(r'D:\\pycharm\\New project\\FE595HW3\\merge_files.py')
import merge_files as mf
import re

#invoke merge_files.py to get the combined txt
combine = mf.merge_files()

#split all the words with space
com1 = re.split(r'\s+', combine)

#get the 10 most common words
f_comb = FreqDist(com1)
print("The 10 most common words")
print(f_comb.most_common(10))

#replace all "Name" , "Purpose", "for' and "and"
data1 = combine.replace("Name", " ")
data2 = data1.replace("Purpose", " ")
data3 = data2.replace("for", " ")
data4 = data3.replace("and", " ")

#split all the words with space
com2 = re.split(r'\s+', data4)

#get the 10 most common words
f_comb1 = FreqDist(com2)
print("The 10 most common words after noise reduction :")
print(f_comb1.most_common(10))