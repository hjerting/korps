def start(digit):
    array = []
    while digit > 0:
        array.append(digit % 10)
        digit //= 10
    newDigit = 0
    for i in range(len(array) - 1, -1, -1):
        newDigit *= 10
        if array[i] == 4:
            newDigit += array[i] - 1
        else:
            newDigit += array[i]

    return(newDigit)

def containsDigit(number, digit):
    while number > 0:
        if number % 10 == digit:
            return True
        number //= 10
    return False

def containsFour(number):
    return containsDigit(number, 4)

def makeCheque(number):
    
    cheque1 = start(number)
    
    while True:
        cheque2 = number - cheque1
        if not (containsFour(cheque1) or containsFour(cheque2)):
            break
        cheque1 -= 1
    return cheque1, cheque2

cases = int(input())
for i in range(1, cases + 1):
    case = int(input())
    x, y = makeCheque(case)
    output = "Case #{}: {} {}".format(i, y, x)
    print(output)

