with open('orders.csv','r',encoding='utf-8') as f:
   x=f.read()
   lines = x.split("\n")
   orders = []
   for line in lines[1:]:
       line=line.strip()
       if line=="":
           continue
       parts = line.split(",")
       order={'id':parts[0],
              'user':parts[1],
              'product':parts[2],
              'qty':int(parts[3]),
              'price':float(parts[4]),
              'date':parts[5],

        }
       orders.append(order)

print('一共读入',len(orders),'条订单')

total=0
for i in orders:
    total+= i['qty'] * i['price']
print(f'总金额是：{total}')
by_user=dict()
for name in orders:
    name=name['user']
    if name not in by_user:
        by_user[name]=1
    else:
        by_user[name]+=1
print(by_user)

by_money = dict()
for o in orders:
    u = o['user']
    m = o['qty'] * o['price']
    if u not in by_money:
        by_money[u] = m
    else:
        by_money[u] += m
print(by_money)

# 按商品统计单数
by_product = dict()
for o in orders:
    p = o['product']
    if p not in by_product:
        by_product[p] = 1
    else:
        by_product[p] += 1
print(by_product)

# 按商品统计金额
by_product_money = dict()
for o in orders:
    p = o['product']
    m = o['qty'] * o['price']
    if p not in by_product_money:
        by_product_money[p] = m
    else:
        by_product_money[p] += m
print(by_product_money)



