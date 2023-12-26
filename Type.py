print("I am Jean")
print('*'*10)

price=10
price=20 #會取代上面的price=10
rating=4.9
name='Jean'
is_published=False
print(price)

# 讓user輸入
name=input('What is your name? ')
print("Hi "+ name)
favorite_color=input('What is your favorite_color?')
print(name+' likes '+favorite_color)

# Input的東西always is String not Integer
# so...以下會報錯，因為birthyear是input值，一定是String，而String不能做運算
'''
birth_year=input("Birth Year: ")
age=2023-birth_year
print(age)
'''
# 所以需要先轉型：
birth_year=input("Birth Year: ")
age=2023-int(birth_year)
print(age)

# check 類型的方法：
print(type(birth_year))

