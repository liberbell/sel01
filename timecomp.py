def addition(num1, num2):
    total = num1 + num2

    print("The sum of %d and %d is %d"% (num1, num2, total))


addition(10, 15)

def addition(num1, num2):
    num_iterations = 0
    total = num1 + num2

    num_iterations += 1
    print("The sum of %d and %d is %d \nTotal number of iterations = %d"
            % (num1, num2, total, num_iterations))

addition(20, 25)

def check_oddeven(number):
    count = 0
    num_iterations = 0

    if (number % 2 == 0):
        num_iterations += 1
        print("%d is an even number" % number)

    else:
        num_iterations += 1
        print("%d is an odd number" % number)

    print("Total number of iteration = %d" % num_iterations)

check_oddeven(12)

def find_square(number):
    num_iterations = 0
    square = number ** 2

    num_iterations += 1

    print("Square of %d is %d \nTotal number of iteration = %d" % (number, square, num_iterations))

find_square(11)

def check_prime(number):
    num_iterations = 0

    for i in range(2, number):
        num_iterations += 1

        if number % i == 0:
            print("%d is not a prime number\nTotal number of iteration is %d" % (number, num_iterations))
            return

    print("%d is a prime number\nTotal number of iteration is %d" % (number, num_iterations))

check_prime(1847)

def check_prime2(number):
    num_iterations = 0
    mid_point = int(number / 2)

    for i in range(2, mid_point):
        num_iterations += 1

        if number % i == 0:
            print("%d is not a prime number\nTotal number of iterations = %d" % (number, num_iterations))
            return

    print("%d is a prime number\nTotal number of iteration is %d" % (number, num_iterations))

check_prime2(1847)

def find_maxval(num_list):
    maxval = num_list[0]
    num_iterations = 0

    for i in range(len(num_list)):
        num_iterations += 1

        if maxval < num_list[i]:
            maxval = num_list[i]
    
    print("Max value of the list = %d\nTotal number of iteration = %d" % (maxval, num_iterations))

lists = [1, 2, 5, 3, 10, -10, 9]
find_maxval(lists)

def find_factorial(number:int):
    fact = 1
    num_iteratins = 0

    if (number < 0 or type(number) != int):
        print("Invalid number")
        return
    
    for i in range(1, number + 1):
        fact = fact + i