# -----------------  功能1，读文件，把文件装进列表   -------------------
def load_orders():
    with open('orders.csv', 'r', encoding='utf-8') as f:
        x = f.read()
        lines = x.split("\n")
        orders = []
        for line in lines[1:]:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            order = {'id': parts[0],
                     'user': parts[1],
                     'product': parts[2],
                     'qyt': int(parts[3]),
                     'price': float(parts[4]),
                     'date': parts[5],

                     }
            orders.append(order)
        return orders
# -------------------- 功能2，显示全部菜单  --------------------
def show_all_orders(orders):
    for order in orders:
        print(order['id'], order['user'], order['product'], order['qyt'])

# -------------------- 功能3，算总金额  --------------------
def show_total(orders):
    total = 0
    for order in orders:
        total += order['qyt'] * order['price']
    print('总金额：', total)

# -------------------- 功能4，按用户统计单数  --------------------
def count_by_user(orders):
    by_user = {}
    for order in orders:
        u = order['user']
        if u not in by_user:             # 新用户：开张记1
            by_user[u] = 1
        else:                            # 老用户：加1
            by_user[u] += 1
    print(by_user)

# -------------------- 功能5，按商品统计单数  --------------------
def count_by_product(orders):
    by_product = {}
    for order in orders:
        p = order['product']
        if p not in by_product:          # 新商品：开张记1
            by_product[p] = 1
        else:                            # 老商品：加1
            by_product[p] += 1
    print(by_product)

# -------------------- 主菜单  --------------------
def main():
    orders = load_orders()               # 先把数据读好，只读一次
    while True:                          # 无限循环，直到用户选退出
        print('=' * 30)
        print('    订单分析系统')
        print('1. 显示全部订单')
        print('2. 查看总金额')
        print('3. 按用户统计单数')
        print('4. 按商品统计单数')
        print('5. 退出')
        print('=' * 30)
        choice = input('请输入选择：')    # 接收输入（是字符串，所以下面都带引号）

        if choice == '1':
            show_all_orders(orders)
        elif choice == '2':
            show_total(orders)
        elif choice == '3':
            count_by_user(orders)
        elif choice == '4':
            count_by_product(orders)
        elif choice == '5':
            print('再见！')
            break                        # 跳出while循环，程序结束
        else:
            print('输入有误，请重新输入')

main()                                   # 程序入口：调用main函数





