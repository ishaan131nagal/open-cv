import math
A = [40,30,130,40]
N = len(A)
result = 0;
for i in range(0,N):
    for j in range(0,N):
        if(A[i] == A[j]):
            result = max(result,abs(i-j))
print(result)

A = [40,30,130,40]
N = len(A)
result = 0;
for i in range(0,N):
    for j in range(0,N):
        if(A[i] == A[j]):
            result = max(result,abs(i-j))
print(result)