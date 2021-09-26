a,b = map(int,input().split())
c = list(map(int, input().split()))

for i in range(a):
    if c[i] < b:
        print(c[i], end = " ") # end = " " 개행을 없애준다 " "이걸로 띄어쓰기로