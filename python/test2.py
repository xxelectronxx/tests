
def fibonacci(n):

    x = 1
    oldx = 1
    olderx = 0
    y = 0

    while y < int(n):
        x = oldx + olderx
        olderx = oldx
        oldx = x
        y += 1
    print(olderx)


if __name__=='__main__':
    number = input("How many numbers of the Fibinachi Sequence do you want to print?")
    fibonacci(number)
