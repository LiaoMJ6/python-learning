# while循环
i=1
while i<=9:
    x=1
    while x<=i:
        print(f"{x}*{i}={i*x}",end="\t")
        x=x+1
    print()
    i=i+1



# for循环
x=1
for x in range(1,10):
    i=1
    for i in range(1,x+1):
        print(f"{i}*{x}={i*x}",end="\t")
    print()