#1.終極密碼
#2.自訂數字
#3.計算次數

import random

start = input('請輸入開始數字')
end = input('請輸入結束數字')
start = int(start)
end = int(end)
num_ran = random.randint(start, end)
count = 0

while True:
    count = count + 1
    num = input('終極密碼，請猜一個數字：')
    num = int(num)
    if num == num_ran:
	    print('恭喜中獎')
	    print('你已經猜了幾', count,'次')
	    break
    elif num > num_ran:
	    print('數字太大了，再小一點')
    elif num < num_ran:
	    print('數字太小了，再大一點')
    print('你已經猜了幾', count,'次')
