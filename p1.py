for i in range(5):
    for i in range(i):
        print(i, end=' ')
    print()

for i in range(5) :
    print(str(i)*i)
for num in range(5):
    for i in range(num):
        print(num, end="")
    print()

b=0 
for i in range(5, 0, -1):
    b+=1
    for num in range(1, i+1):
        print(b,end="")
    print()
# open a flutter project if 