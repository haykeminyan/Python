import os
import codecs
import random
from random import shuffle,choice
import re
directory=os.getcwd()+'/data'
arr_names=[]


N=int(input('Напиши сколько у тебя вариантов по каждой теме: '))
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

nested_lists=[[]for i in range(len(categories_without_numbers))]
# print(emty_lists)
result=[]
for i in range(1,N+1):
    for j in range(len(categories_without_numbers)):
        nested_lists[j].append(categories_without_numbers[j]+str(i))

print(nested_lists)

with open('file_result.tex','w') as outfile:
    outfile.write('\\begin{document}\n')
    outfile.write('\n')
for i in range(N):
    with open('file_result.tex','a') as outfile:
        outfile.write('\n')
        outfile.write('\\begin{center}\n')
        outfile.write('\\textbf{MYhyp}\n')
        outfile.write('\\end{center}\n')
        outfile.write('\\begin{enumerate}\n')
        outfile.write('\n')
        outfile.write('\\input '+random.choice(nested_lists[0]))
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\\input '+random.choice(nested_lists[1]))
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\\input '+random.choice(nested_lists[2]))
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\\input '+random.choice(nested_lists[3]))
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\\input '+random.choice(nested_lists[4]))
        outfile.write('\n')
        outfile.write('\n')
        outfile.write('\\input '+random.choice(nested_lists[5]))
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