# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

numbers = input()
list_num = list()
for k, g in groupby(numbers):
    list_num.append(f'({len(list(g))}, {k})')
    
print(' '.join(map(str, list_num)))