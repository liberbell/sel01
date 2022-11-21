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