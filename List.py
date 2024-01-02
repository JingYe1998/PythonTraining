names=['John','Smith','Jean']
print(names)
names[0]='Apple' # 取代功能
print(names)

# Exercise
numbers=[1,4,2,7,5]
max=numbers[0]
for number in numbers: # 類似java for(int i : List)
    if number>max:
        max=number
print(max)