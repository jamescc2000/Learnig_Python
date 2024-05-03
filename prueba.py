from itertools import combinations

n = 6
text = 'a b c d e a'.split()
k = 2
index = list()
index_a = list()

for i, char in enumerate(text):
    index.append(i+1)
    if char == 'a':
        index_a.append(i+1)

perm = list(combinations(index,k))
bool = False
cont = 0

for tuple in perm:
    for j in tuple:
        if j in index_a:
            bool = True
    
    if bool:
        cont +=1
    bool = False
        
print(cont/len(perm))
        

