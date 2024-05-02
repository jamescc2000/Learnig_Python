# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())
val = True

for i in range(n):
    s = set(map(int, input().split()))
    if not(A.isdisjoint(s)):
        val = False
        
print(val)