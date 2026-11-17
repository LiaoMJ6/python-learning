import random
num=random.randint(1,10)
num_1=int(input("第一次请输入数字"))
if num==num_1:
    print("恭喜，猜对了")
else:
    if num>num_1:
        print("猜小了")
    else:
        print("猜大了")
    num_2=int(input("第二次请输入数字"))
    if num==num_2:
        print("恭喜，猜对了")
    else:
        if num_2>num:
            print("猜大了")
        else:
            print("猜小了")
        num_3=int(input("第三次请输入数字"))
        if num_3==num:
            print("恭喜，你赢了")
        else:
            print("sorry,你输了")



