def decimaltobinary(decimal_num):
    binary_rev = []

    while decimal_num > 0:
        remainding = decimal_num % 2
        print(remainding)
        binary_rev.append(remainding)
        decimal_num = decimal_num // 2


    return binary_rev



decimal_num = int(input("enter a denary number:"))

binary_rev = decimaltobinary(decimal_num)

print("binary digit in reverse: ")
for bit in binary_rev:
    print(bit,end=",")
print()