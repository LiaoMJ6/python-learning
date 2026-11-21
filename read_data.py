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
              'qyt':int(parts[3]),
              'price':float(parts[4]),
              'date':parts[5],

        }
       orders.append(order)
print(orders)
print('一共读入',len(orders),'条订单')




