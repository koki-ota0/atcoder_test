A, B = map(int, input().split())
if abs(A-B)==1 and min(A,B)%3!=0:
    print("Yes")
else:
    print("No")