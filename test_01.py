
def fizzbuzz(j):
    # get number from user input
    fb = []
    fizz = "Fizz"
    buzz = "Buzz"
    fizz_buzz = "Fizz Buzz"

    # a = int(input("please input a number"))
    a = j
    for i in range(1, a+1):
        if i % 15 == 0:
           fb.append(fizz_buzz)
        elif i % 5 == 0:
           fb.append(buzz)
        elif i % 3 == 0:
           fb.append(fizz)
        else:
            fb.append(str(i))
    #print(fb)
    return fb


if __name__ == "__main__":

    fizzbuzz(30)
