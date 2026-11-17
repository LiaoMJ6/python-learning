from idlelib.editor import keynames

money=500000
name=input("Enter your name:")
# 定义查询函数
def query():
    print("-------余额查询---------")
    print(f"您好,{name},你的余额剩余{money}")
# 定义存款函数
def saving(num):
    global money
    money+=num
    print("-------存款---------")
    print(f"您好{name}，你存款{num}成功,账户余额{money}")
# 定义取款函数
def get_money(num):
    global money
    money-=num
    print("-------取款---------")
    print(f"您好{name},你成功取款{num},账户余额{money}")
# 定义主菜单函数
def main():
    print("-------主菜单---------")
    print(f"您好{name},欢迎来到xxxATM")
    print('余额查询\t[输入1]')
    print('取款\t\t[输入2]')
    print('存款\t\t[输入3]')
    print('退出\t\t[输入4]')
    return input("请选择")
# 设置无限循环，确保程序不退出
while True:
    keyboard=main()
    if keyboard == "1":
        query()
        continue
    elif keyboard == "2":
        num=int(input("你想要取多少钱"))
        get_money(num)
        continue
    elif keyboard == "3":
        num=int(input("你想要存多少钱"))
        saving(num)
        continue
    else:
        print("程序退出了")
        break





