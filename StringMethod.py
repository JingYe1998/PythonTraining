course='Python for Beginners'
print(len(course)) #計算長度
print(course.upper())#不會modify原始course
print(course.find('P'))#尋找inex，如果找不到會回傳-1
print(course.replace('Beginners','Super Beginners'))

# 'in'=======>判斷A是否存在於B元素中
print('p' in course)#判斷是否含有特定字元 #False
print('P' in course) #True