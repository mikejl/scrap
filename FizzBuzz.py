
for x in range(1, 101):
    if (x % 3 == 0) and (x % 5 == 0):
        answer = "Fizzbuzz"
    elif (x % 3 == 0):
        answer = "Fizz"
    elif (x % 5 == 0):
        answer = "Buzz"
    else:
        answer = x
    print answer

        