try:
    age = int(input("Age:"))
    print(age)
    income=20000
    risk=income/age
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age can not be zero")
