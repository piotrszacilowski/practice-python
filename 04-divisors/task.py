number = int(input('Give me a number: '))
inputList = range(1, number + 1)
divisors = []

for elem in inputList:
    if number % elem == 0:
        divisors.append(elem)

print('The divisors of ' + str(number) + ":  " + str(divisors))


