import random

for i in range(3):
    print(random.random())  # 隨機取3個介於0 and 1之間的數
    print(random.randint(10, 20))  # 隨機取3個介於10 and 20之間的數

members = ['Alice', 'Bob', 'Jean']
leader = random.choice(members)
print(leader)
