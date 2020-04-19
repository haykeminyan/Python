import os
import codecs
import random
from random import shuffle,choice
import re
directory=os.getcwd()+'/data'
arr_names=[]

class GetNamesFiles:
    def __init__(self,dirname):
        self.dirname=dirname
    def __iter__(self):
        for i in os.listdir(self.dirname):
            yield i
for i in GetNamesFiles(directory):
    arr_names.append(i)

shuffle(arr_names)
categories_with_numbers=[]
for i in arr_names:
    categories_with_numbers.append(i.split('.')[0])
categories_without_numbers=[]
for i in categories_with_numbers:
    output = re.sub(r'\d+', '', i)
    categories_without_numbers.append(output)

categories_without_numbers=list(set(categories_without_numbers))

print(len(categories_without_numbers))
print(len(categories_with_numbers))
print(categories_without_numbers)


# names_categories=[]

# for i in range(len(arr_names)):
#     for j in result:
#         a=re.search('lra'+str(i),j)
#         if k:
#             names_category_of_A.append(a[0])
#         if l:
#             names_category_of_B.append(b[0])

with open('file_result.tex','w') as outfile:
    outfile.write('\\begin{document}\n')
    outfile.write('\n')
for i in range(131):            
    with open('file_result.tex','a') as outfile:
        outfile.write('\n')
        outfile.write('\\begin{center}\n')
        outfile.write('\\textbf{MYhyp}\n')
        outfile.write('\\end{center}\n')
        outfile.write('\\begin{enumerate}\n')
        outfile.write('\n')
        outfile.write('\\input '+random.choice(categories_with_numbers))
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\\input '+random.choice(categories_with_numbers))
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\\input '+random.choice(categories_with_numbers))
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\\input '+random.choice(categories_with_numbers))
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\\input '+random.choice(categories_with_numbers))
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\\input '+random.choice(categories_with_numbers))
        outfile.write('\n')
        # outfile.write(infile_1.read())
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\\end{enumerate}\n')
        outfile.write('\\newpage\n')


with open('file_result.tex','a') as outfile:
    outfile.write('\\end{document}')