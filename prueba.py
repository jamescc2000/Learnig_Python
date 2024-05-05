# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
import math as m



K, M = input().split()
list_lists = list()
a = m.sqrt(int(M)/3)
sum_tot = 0

for i in range(int(K)):
    lista = list(map(int, input().split()))
    list_num = lista[1:]
    list_num.sort()
    ith = 0
    if max(list_num) < a:
        sum_tot += max(list_num)*max(list_num)
    elif min(list_num) > a:
        sum_tot += min(list_num)*min(list_num)
    else:
        for j in range(2,len(list_num)-3):
            if list_num[j] <= a and list_num[j+1] > a:
                sum_tot += list_num[j]*list_num[j]
        
        
print(sum_tot)
    