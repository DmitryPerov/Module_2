first = input("Первое число: ")
second = input("Второе число: ")
third = input("Третье число: ")
print (first, second, third)
if first == second == third:
    print ('3')
elif first == second or second == third or third == first:
    print ('2')
else:
    print ('0')