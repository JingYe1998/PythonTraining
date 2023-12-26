for item in [1,2,3,4,5,6]: # assign 1~6 to item
    print(item)

for item in range(10):
    print(item) # 0~9

for item in range(5,10): # 5~9
    print(item)

for item in range(5,10,2): # 5,7,9都間隔2
    print(item)

####練習
prices=[10,20,30]
total=0 # 初始化
for price in prices:
    total=total+price
print(f"The total price is {total}")
