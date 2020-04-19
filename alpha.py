import os
import codecs
import random
from random import shuffle,choice
directory=os.getcwd()+'/data'
arr_names=[]
with os.scandir(directory) as files:
    for i in files:
        arr_names.append(i)
        # with codecs.open(i,encoding='ISO-8859-1') as j:
        #     for k in j.read().splitlines():
        #         arr_names.append(k)
dict_1={}
random_numbers=[i for i in range(len(arr_names))]
shuffle(random_numbers)
print(random_numbers)
for i in range(len(arr_names)):
    c=arr_names[i]
    dict_1[c]=random_numbers[i]
print(dict_1)

# for i in range(len(arr_names)):
for i in range(12):
# for i in list(dict_1.values()):
    with open('file_'+str(i)+'.tex','w') as outfile:
        # for names in arr_names:
        # names=choice(arr_names)
        shuffle(arr_names)
        for names in arr_names[:2]:
            with codecs.open(names,encoding='ISO-8859-1') as infile:
                outfile.write('\n')
                outfile.write('--------------------------')
                outfile.write('\n')
                outfile.write(infile.read())
                outfile.write('\n')
                outfile.write('--------------------------')