yob = int(input("Xin hãy nhập vào năm sinh của bạn"))
age = 2018 - yob
print(age)

if age < 10 and age > 0:
    print("baby")
elif age < 18:
    print("teenagers")
else:
    print("adult")        