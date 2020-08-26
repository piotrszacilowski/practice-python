def is_primary(number):
    # if number == 2:
    #     print("2 is a prime number")
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
            else:
                print(number, " is a prime number")


num = int(input("Give a number: "))
is_primary(num)
