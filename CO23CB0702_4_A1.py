sum = 0
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    if num > 0:
        sum += num
print("The sum of all the positive numbers entered is:", sum)
