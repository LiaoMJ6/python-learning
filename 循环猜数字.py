#while循环猜数字
import random
num=random.randint(1,10)
flag=True
count=0
while flag:
    guess_num=int(input("请输入你猜测的数字"))
    if guess_num==num:
        print("恭喜，你猜对了")
        flag=False
    else:
        if guess_num>num:
            print("你猜大了")
        else:
            print("你猜小了")

    count+=1
print(f"你猜了{count}次")

