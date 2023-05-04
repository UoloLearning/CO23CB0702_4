string = input("Enter a string: ")
i = 0
while i < len(string):
    if string[i] == " ":
        break
    if string[i] == "":
        i += 1
        continue
    print(string[i])
    i += 1
