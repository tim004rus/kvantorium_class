# №1
typeofyear = int(input("Введите любое натуральное число, которое больше нуля: "))
if typeofyear % 4 != 0:
    print("Самый обычный год")
elif typeofyear % 100 == 0:
    if typeofyear % 400 == 0:
        print("Этот год не обычный")
    else:
        print("Этот год нормальный")
else:
    print("Этот год не совсем обычный")

#№2
n = int(input("Введите любое число для поиска факториала: "))
 
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
 
print(factorial)

# №3
sentense = input("введите предложение: ")
s = sentense.replace('а', '')
print(s)

