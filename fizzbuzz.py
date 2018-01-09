#FizzBuzz in Python

""" here is one way:

for i in range(1,101):
    str = ""
    if i % 3 == 0:
        str += "Fizz"
        if i % 5 == 0:
            str += "Buzz"
        print(str)
    elif i % 5 == 0:
        str += "Buzz"
        print(str)
    else:
        print(i)
        
"""

# can I come up with another...

for i in range(1,101):
    str = ""
    if i % 3 == 0:
        str += "Fizz"
    if i % 5 == 0:
        str += "Buzz"
    print(str or i)