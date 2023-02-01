def converter(a, b, c=10):
    hex = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
           '9': '9', 'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}

    dictforhex1 = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    length = len(a)
    result = 0

    for i in range(length):
        if a[i] in hex.keys():
            result += int(hex[a[i]]) * b ** (length - 1)
        length -= 1
    rem = ''
    while result > 0:
        asd = result % c
        if asd > 9:
            asd = dictforhex1[asd]
            result //= c
            rem += str(asd)
        else:
            result //= c
            rem += str(asd)
    return rem[::-1]


a = str(input("შეიყვანეთ ციფრი: "))
b = int(input("რომელ პოზიციურ სისტემაშია მოცემული რიცხვი? "))
c = int(input("რომელ პოზიციურ სისტემაში გსურთ გადაიყვანოთ ეს რიცხვი? "))

print(converter(a, b, c))

