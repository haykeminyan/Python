import os
import codecs
import random
from random import shuffle,choice
directory=os.getcwd()+'/data'
arr_names=[]
with os.scandir(directory) as files:
    for i in files:
        arr_names.append(i)

dict_1={}
random_numbers=[i for i in range(len(arr_names))]
shuffle(random_numbers)
print(random_numbers)
for i in range(len(arr_names)):
    c=arr_names[i]
    dict_1[c]=random_numbers[i]
print(dict_1)

for i in range(12):
    with open('file_'+str(i)+'.tex','w') as outfile:
        shuffle(arr_names)
        for names in arr_names[:1]:
            with codecs.open(names,encoding='ISO-8859-1') as infile:
                outfile.write('\n')
                outfile.write('\\documentclass[a4paper,12pt]{scrartcl}\n')
                outfile.write('\\usepackage{mathtext}\n')
                outfile.write('\\usepackage[cp1251]{inputenc}\n')
                outfile.write('\\usepackage[english, russian]{babel} \n')
                outfile.write('\\usepackage[left=1cm,right=1cm,top=1cm,bottom=2cm]{geometry}\n')
                outfile.write('\\usepackage{amssymb, amsmath}\n')
                outfile.write('\n')
                outfile.close()
for i in range(12):
    with open('file_'+str(i)+'.tex','a') as outfile:
        shuffle(arr_names)
        for names in arr_names[:1]:    
                outfile.write('\\begin{document}\n')
                outfile.close()

for i in range(12):
    with open('file_'+str(i)+'.tex','a') as outfile:
        shuffle(arr_names)
        for names in arr_names[:2]:
            with codecs.open(names,encoding='ISO-8859-1') as infile:
                outfile.write(infile.read())
                outfile.write('--------------------------')
for i in range(12):
    with open('file_'+str(i)+'.tex','a') as outfile:
        shuffle(arr_names)
        for names in arr_names[:1]:
            outfile.write('\n')
            outfile.write('\\end{document}\n')
 
