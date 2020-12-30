for index in range(1, 101):
    result = str(index) + " "
    if index % 3 == 0:
        result += "Fizz"
    if index % 5 == 0:
        result += "Buzz"
    print(result)
