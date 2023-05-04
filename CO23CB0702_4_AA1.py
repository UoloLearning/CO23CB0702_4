for i in range(10):
    num = int(input("Enter a number: "))
    if num > 100:
        print("Number greater than 100 entered. Exiting loop.")
        break
    else:
        print(num)
